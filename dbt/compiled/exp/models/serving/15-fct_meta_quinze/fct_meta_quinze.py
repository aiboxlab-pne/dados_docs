import pandas as pd


# fmt: off
def model(dbt, fal):
    # load
    df_municipios_raw: pd.DataFrame = dbt.ref("info_municipios")
    df_dim_educ_bas_docentes_15 = dbt.ref("dim_educ_bas_docentes_15_group")

    # template
    list_indicador = ['15A', '15B','15C','15D']
    df_ano_munic = pd.DataFrame()
    for indicador in list_indicador:
        for ano in range(2014,2020+1):
            df_temp = (df_municipios_raw[['MUNICIPIO_CODIGO', 'ESTADO_CODIGO']].copy()
                       .rename(columns={'MUNICIPIO_CODIGO':'FK_MUNICIPIO_CODIGO',
                                        'ESTADO_CODIGO':'FK_ESTADO_CODIGO'}))
            df_temp['ANO']=ano
            df_temp['INDICADOR']=indicador
            if df_ano_munic.shape != (0,0):
                df_ano_munic = pd.concat([df_ano_munic, df_temp]).reset_index(drop=True)
            else:
                df_ano_munic = df_temp.copy()

    # ind a
    df_15a = \
        (df_dim_educ_bas_docentes_15
            .assign(INDICADOR=list_indicador[0])
            .query('ETAPA=="1_ENSINO_INFANTIL"')
            .assign(ATENDIMENTO_IND=\
                lambda x:round((x["FORMACAO_ADEQUADA"])/x["DOCENCIA_TOTAL"],4) * 100)
            .reindex(columns=['ANO', 'FK_MUNICIPIO_CODIGO','INDICADOR',
                              'FORMACAO_ADEQUADA', 'DOCENCIA_TOTAL',
                              'ATENDIMENTO_IND'])
        )

    # ind b
    df_15b = \
        (df_dim_educ_bas_docentes_15
            .assign(INDICADOR=list_indicador[1])
            .query('ETAPA=="2_FUND_ANOS_INICIAIS"')
            .assign(ATENDIMENTO_IND=\
                lambda x:round((x["FORMACAO_ADEQUADA"])/x["DOCENCIA_TOTAL"],4) * 100)
            .reindex(columns=['ANO', 'FK_MUNICIPIO_CODIGO','INDICADOR',
                              'FORMACAO_ADEQUADA', 'DOCENCIA_TOTAL',
                              'ATENDIMENTO_IND'])
        )

    # ind c
    df_15c = \
        (df_dim_educ_bas_docentes_15
            .assign(INDICADOR=list_indicador[2])
            .query('ETAPA=="3_FUND_ANOS_FINAIS"')
            .assign(ATENDIMENTO_IND=\
                lambda x:round((x["FORMACAO_ADEQUADA"])/x["DOCENCIA_TOTAL"],4) * 100)
            .reindex(columns=['ANO', 'FK_MUNICIPIO_CODIGO','INDICADOR',
                              'FORMACAO_ADEQUADA', 'DOCENCIA_TOTAL',
                              'ATENDIMENTO_IND'])
        )

    # ind d
    df_15d = \
        (df_dim_educ_bas_docentes_15
            .assign(INDICADOR=list_indicador[3])
            .query('ETAPA=="4_ENSINO_MEDIO"')
            .assign(ATENDIMENTO_IND=\
                lambda x:round((x["FORMACAO_ADEQUADA"])/x["DOCENCIA_TOTAL"],4) * 100)
            .reindex(columns=['ANO', 'FK_MUNICIPIO_CODIGO','INDICADOR',
                              'FORMACAO_ADEQUADA', 'DOCENCIA_TOTAL',
                              'ATENDIMENTO_IND'])
        )

    # meta concat
    df_15_raw = pd.concat([df_15a, df_15b, df_15c, df_15d]).reset_index(drop=True)

    # meta transform
    df_15 = \
        (df_15_raw
            .reset_index(drop=True)
            .merge(
                df_ano_munic[['ANO', 'FK_MUNICIPIO_CODIGO', 'INDICADOR',
                              'FK_ESTADO_CODIGO']],
                on=('ANO', 'FK_MUNICIPIO_CODIGO', 'INDICADOR'),
                how='right')
            .reindex(['ANO', 'FK_ESTADO_CODIGO', 'FK_MUNICIPIO_CODIGO',
                      'INDICADOR', 'FORMACAO_ADEQUADA', 'DOCENCIA_TOTAL',
                      'ATENDIMENTO_IND'],
                    axis=1)
            .fillna(0)
            .astype({col: 'uint32' for col in ['FK_MUNICIPIO_CODIGO',
                                               'FK_ESTADO_CODIGO',
                                               'FORMACAO_ADEQUADA',
                                               'DOCENCIA_TOTAL']})
            .astype({'ANO':'uint16'})
            .sort_values(by=['ANO', 'INDICADOR', 'FK_MUNICIPIO_CODIGO'])
            .reset_index(drop=True)
        )
    return df_15


# This part is user provided model code
# you will need to copy the next section to run the code
# COMMAND ----------
# this part is dbt logic for get ref work, do not modify

def ref(*args, **kwargs):
    refs = {"dim_educ_bas_docentes_15_group": "\"postgres\".\"dbt_staging\".\"dim_educ_bas_docentes_15_group\"", "info_municipios": "\"postgres\".\"dbt_staging\".\"info_municipios\""}
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
    identifier = "fct_meta_quinze"
    
    def __repr__(self):
        return '"postgres"."dbt_serving"."fct_meta_quinze"'


class dbtObj:
    def __init__(self, load_df_function) -> None:
        self.source = lambda *args: source(*args, dbt_load_df_function=load_df_function)
        self.ref = lambda *args, **kwargs: ref(*args, **kwargs, dbt_load_df_function=load_df_function)
        self.config = config
        self.this = this()
        self.is_incremental = False

# COMMAND ----------


