import numpy as np
import pandas as pd


# fmt: off
def model(dbt, fal):
    # load
    df_dim_ideb = dbt.ref("dim_ideb_estadual")

    # template
    list_indicador = ['7A', '7B', '7C']

    # ind a
    df_7a = \
        (df_dim_ideb
        .reindex(columns=['ANO', 'FK_ESTADO_CODIGO', 'ORIGEM', 'ESTADUAL',
                        'PUBLICA'])
        .assign(ANO=lambda x:x['ANO'].astype(int))
        .query('ORIGEM=="anos_iniciais"')
        .melt(id_vars=['ANO', 'FK_ESTADO_CODIGO', 'ORIGEM'],
            value_vars=['ESTADUAL','PUBLICA'],
            var_name='REDE',
            value_name='ATENDIMENTO_IND')
        .assign(ATENDIMENTO_IND=lambda x:
            x['ATENDIMENTO_IND'].replace({'-':np.nan,None:np.nan}))
        .query('ATENDIMENTO_IND==ATENDIMENTO_IND')
        .assign(INDICADOR=list_indicador[0])
        .reindex(columns=['ANO', 'FK_ESTADO_CODIGO','INDICADOR',
                        'REDE', 'ATENDIMENTO_IND'])
        )

    # ind b
    df_7b = \
        (df_dim_ideb
        .reindex(columns=['ANO', 'FK_ESTADO_CODIGO', 'ORIGEM', 'ESTADUAL',
                        'PUBLICA'])
        .assign(ANO=lambda x:x['ANO'].astype(int))
        .query('ORIGEM=="anos_finais"')
        .melt(id_vars=['ANO', 'FK_ESTADO_CODIGO', 'ORIGEM'],
            value_vars=['ESTADUAL','PUBLICA'],
            var_name='REDE',
            value_name='ATENDIMENTO_IND')
        .assign(ATENDIMENTO_IND=lambda x:
            x['ATENDIMENTO_IND'].replace({'-':np.nan,None:np.nan}))
        .query('ATENDIMENTO_IND==ATENDIMENTO_IND')
        .assign(INDICADOR=list_indicador[1])
        .reindex(columns=['ANO', 'FK_ESTADO_CODIGO','INDICADOR',
                        'REDE', 'ATENDIMENTO_IND'])
        )

    # ind c
    df_7c = \
        (df_dim_ideb
        .reindex(columns=['ANO', 'FK_ESTADO_CODIGO', 'ORIGEM', 'ESTADUAL',
                        'PUBLICA'])
        .assign(ANO=lambda x:x['ANO'].astype(int))
        .query('ORIGEM=="ensino_medio"')
        .melt(id_vars=['ANO', 'FK_ESTADO_CODIGO', 'ORIGEM'],
            value_vars=['ESTADUAL','PUBLICA'],
            var_name='REDE',
            value_name='ATENDIMENTO_IND')
        .assign(ATENDIMENTO_IND=lambda x:
            x['ATENDIMENTO_IND'].replace({'-':np.nan,None:np.nan}))
        .query('ATENDIMENTO_IND==ATENDIMENTO_IND')
        .assign(INDICADOR=list_indicador[2])
        .reindex(columns=['ANO', 'FK_ESTADO_CODIGO','INDICADOR',
                        'REDE', 'ATENDIMENTO_IND'])
        )
    # meta concat
    df_7_raw = pd.concat([df_7a, df_7b, df_7c]).reset_index(drop=True)

    # meta transform
    df_7 = \
        (df_7_raw
            .reset_index(drop=True)
            .assign(INFORME_INDICADOR=lambda x:
                (x['ATENDIMENTO_IND']!=0).astype(int))
            .reindex(['ANO', 'FK_ESTADO_CODIGO',
                    'INDICADOR','INFORME_INDICADOR',
                    'REDE', 'ATENDIMENTO_IND'],
                    axis=1)
            .astype({col: 'uint32' for col in ['FK_ESTADO_CODIGO']})
            .astype({'ANO':'uint16'})
            .astype({'ATENDIMENTO_IND':float})
            .sort_values(by=['ANO', 'INDICADOR', 'REDE'])
            .reset_index(drop=True)
        )
    return df_7


# This part is user provided model code
# you will need to copy the next section to run the code
# COMMAND ----------
# this part is dbt logic for get ref work, do not modify

def ref(*args, **kwargs):
    refs = {"dim_ideb_estadual": "\"postgres\".\"dbt_staging\".\"dim_ideb_estadual\""}
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
    identifier = "fct_meta_sete_estadual"
    
    def __repr__(self):
        return '"postgres"."dbt_serving"."fct_meta_sete_estadual"'


class dbtObj:
    def __init__(self, load_df_function) -> None:
        self.source = lambda *args: source(*args, dbt_load_df_function=load_df_function)
        self.ref = lambda *args, **kwargs: ref(*args, **kwargs, dbt_load_df_function=load_df_function)
        self.config = config
        self.this = this()
        self.is_incremental = False

# COMMAND ----------


