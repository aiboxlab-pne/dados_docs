import numpy as np
import pandas as pd


# fmt: off
def model(dbt, fal):
    # load
    df_municipios_raw: pd.DataFrame = dbt.ref("info_municipios")
    df_dim_ideb = dbt.ref("dim_ideb_municipal")

    # template
    list_indicador = ['7A', '7B', '7C']

    list_indicador = ['7A', '7B', '7C']
    df_ano_munic = pd.DataFrame()
    for indicador in list_indicador:
        for ano in [2015, 2017, 2019, 2021]:
            for rede in ['MUNICIPAL','PUBLICA']:
                df_temp = (df_municipios_raw[['MUNICIPIO_CODIGO', 'ESTADO_CODIGO']].copy()
                        .rename(columns={'MUNICIPIO_CODIGO':'FK_MUNICIPIO_CODIGO', 'ESTADO_CODIGO':'FK_ESTADO_CODIGO'})
                        )
                df_temp['ANO']=ano
                df_temp['INDICADOR']=indicador
                df_temp['REDE']=rede
                if df_ano_munic.shape != (0,0):
                    df_ano_munic = pd.concat([df_ano_munic, df_temp]).reset_index(drop=True)
                else:
                    df_ano_munic = df_temp.copy()
    # ind a
    df_7a = \
        (df_dim_ideb
        .reindex(columns=['ANO', 'FK_MUNICIPIO_CODIGO', 'ORIGEM', 'MUNICIPAL',
                          'PUBLICA'])
        .assign(ANO=lambda x:x['ANO'].astype(int))
        .query('ORIGEM=="anos_iniciais"')
        .melt(id_vars=['ANO', 'FK_MUNICIPIO_CODIGO', 'ORIGEM'],
              value_vars=['MUNICIPAL','PUBLICA'],
              var_name='REDE',
              value_name='ATENDIMENTO_IND')
        .assign(ATENDIMENTO_IND=lambda x:
            x['ATENDIMENTO_IND'].replace({'-':np.nan,None:np.nan}))
        .query('ATENDIMENTO_IND==ATENDIMENTO_IND')
        .assign(INDICADOR=list_indicador[0])
        .reindex(columns=['ANO', 'FK_MUNICIPIO_CODIGO','INDICADOR',
                          'REDE', 'ATENDIMENTO_IND'])
        )

    # ind b
    df_7b = \
        (df_dim_ideb
        .reindex(columns=['ANO', 'FK_MUNICIPIO_CODIGO', 'ORIGEM', 'MUNICIPAL',
                          'PUBLICA'])
        .assign(ANO=lambda x:x['ANO'].astype(int))
        .query('ORIGEM=="anos_finais"')
        .melt(id_vars=['ANO', 'FK_MUNICIPIO_CODIGO', 'ORIGEM'],
              value_vars=['MUNICIPAL','PUBLICA'],
              var_name='REDE',
              value_name='ATENDIMENTO_IND')
        .assign(ATENDIMENTO_IND=lambda x:
            x['ATENDIMENTO_IND'].replace({'-':np.nan,None:np.nan}))
        .query('ATENDIMENTO_IND==ATENDIMENTO_IND')
        .assign(INDICADOR=list_indicador[1])
        .reindex(columns=['ANO', 'FK_MUNICIPIO_CODIGO','INDICADOR',
                          'REDE', 'ATENDIMENTO_IND'])
        )

    # ind c
    df_7c = \
        (df_dim_ideb
        .reindex(columns=['ANO', 'FK_MUNICIPIO_CODIGO', 'ORIGEM', 'MUNICIPAL',
                        'PUBLICA'])
        .assign(ANO=lambda x:x['ANO'].astype(int))
        .query('ORIGEM=="ensino_medio"')
        .melt(id_vars=['ANO', 'FK_MUNICIPIO_CODIGO', 'ORIGEM'],
              value_vars=['MUNICIPAL','PUBLICA'],
              var_name='REDE',
              value_name='ATENDIMENTO_IND')
        .assign(ATENDIMENTO_IND=lambda x:
                x['ATENDIMENTO_IND'].replace({'-':np.nan,None:np.nan}))
        .query('ATENDIMENTO_IND==ATENDIMENTO_IND')
        .assign(INDICADOR=list_indicador[2])
        .reindex(columns=['ANO', 'FK_MUNICIPIO_CODIGO','INDICADOR',
                          'REDE', 'ATENDIMENTO_IND'])
        )
    # meta concat
    df_7_raw = pd.concat([df_7a, df_7b, df_7c]).reset_index(drop=True)

    # meta transform
    df_7 = \
        (df_7_raw
            .reset_index(drop=True)
            .merge(
                df_ano_munic[['ANO', 'FK_MUNICIPIO_CODIGO', 'INDICADOR',
                              'FK_ESTADO_CODIGO','REDE']],
                on=('ANO', 'FK_MUNICIPIO_CODIGO', 'INDICADOR','REDE'),
                how='right')
            .fillna(0)
            .assign(INFORME_INDICADOR=lambda x:
                (x['ATENDIMENTO_IND']!=0).astype(int))
            .reindex(['ANO', 'FK_ESTADO_CODIGO',
                      'FK_MUNICIPIO_CODIGO', 'INDICADOR','INFORME_INDICADOR',
                      'REDE', 'ATENDIMENTO_IND'],
                    axis=1)
            .astype({col: 'uint32' for col in ['FK_MUNICIPIO_CODIGO',
                                               'FK_ESTADO_CODIGO']})
            .astype({'ANO':'uint16'})
            .astype({'ATENDIMENTO_IND':float})
            .sort_values(by=['ANO', 'INDICADOR', 'FK_MUNICIPIO_CODIGO','REDE'])
            .reset_index(drop=True)
        )
    return df_7


# This part is user provided model code
# you will need to copy the next section to run the code
# COMMAND ----------
# this part is dbt logic for get ref work, do not modify

def ref(*args, **kwargs):
    refs = {"dim_ideb_municipal": "\"postgres\".\"dbt_staging\".\"dim_ideb_municipal\"", "info_municipios": "\"postgres\".\"dbt_staging\".\"info_municipios\""}
    key = '.'.join(args)
    version = kwargs.get("v") or kwargs.get("version")
    if version:
        key += f".v{version}"
    dbt_load_df_function = kwargs.get("dbt_load_df_function")
    return dbt_load_df_function(refs[key])


def source(*args, dbt_load_df_function):
    sources = {}
    key = '.'.join(args)
    return dbt_load_df_function(sources[key])


config_dict = {}


class config:
    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def get(key, default=None):
        return config_dict.get(key, default)

class this:
    """dbt.this() or dbt.this.identifier"""
    database = "postgres"
    schema = "dbt_serving"
    identifier = "fct_meta_sete_municipal"
    
    def __repr__(self):
        return '"postgres"."dbt_serving"."fct_meta_sete_municipal"'


class dbtObj:
    def __init__(self, load_df_function) -> None:
        self.source = lambda *args: source(*args, dbt_load_df_function=load_df_function)
        self.ref = lambda *args, **kwargs: ref(*args, **kwargs, dbt_load_df_function=load_df_function)
        self.config = config
        self.this = this()
        self.is_incremental = False

# COMMAND ----------


