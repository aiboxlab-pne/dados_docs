import pandas as pd


# fmt: off
def model(dbt, fal):
    df_municipios_raw: pd.DataFrame = dbt.ref("info_municipios")
    df_matriculas_raw = dbt.source("staging", "FCT_MATRICULAS_EJA_10A")

    list_indicador = ['10A']
    df_ano_munic = pd.DataFrame()
    for indicador in list_indicador:
        for ano in range(2014, 2020+1):
            df_temp = (
                df_municipios_raw[['MUNICIPIO_CODIGO', 'ESTADO_CODIGO']].copy()
                .rename(columns={'MUNICIPIO_CODIGO':'FK_MUNICIPIO_CODIGO',
                                 'ESTADO_CODIGO':'FK_ESTADO_CODIGO'})
                )
            df_temp['ANO']=ano
            df_temp['INDICADOR']=indicador
            if df_ano_munic.shape != (0,0):
                df_ano_munic = (pd.concat([df_ano_munic, df_temp])
                                .reset_index(drop=True))
            else:
                df_ano_munic = df_temp.copy()

    df_10a = (df_matriculas_raw
    .dropna()
    .rename(columns={'NU_ANO_CENSO':"ANO"})
    .assign(STATUS='INTEGRADA_SIM')
    .assign(STATUS=lambda x:x['STATUS']
            .where(x['TP_ETAPA_ENSINO'].isin([67,73,74]), 'INTEGRADA_NAO'))
    .groupby(['ANO', 'FK_MUNICIPIO_CODIGO', 'STATUS']
             )['QTD_MAT_ETAPA_EJA'].sum()
    .unstack(level=-1).reset_index().rename_axis(None, axis=1)
    .fillna(0)
    .astype({'INTEGRADA_NAO':int, 'INTEGRADA_SIM':int})
    .assign(QTD_MAT_EJA_TOTAL=lambda x:x['INTEGRADA_NAO']+x['INTEGRADA_SIM'])
    .drop('INTEGRADA_NAO',axis=1)
    .rename(columns={'INTEGRADA_SIM': 'QTD_MAT_EJA_INTEGRADO'})
    .assign(INDICADOR='10A')
    .assign(ATENDIMENTO_IND = lambda x:
            round((x['QTD_MAT_EJA_INTEGRADO']/x['QTD_MAT_EJA_TOTAL'])*100,2))
    .reset_index(drop=True)
    )

    df_10 = (pd
    .merge(df_10a, df_ano_munic[['ANO', 'FK_MUNICIPIO_CODIGO',
                                 'FK_ESTADO_CODIGO', 'INDICADOR']],
            on=('ANO', 'FK_MUNICIPIO_CODIGO', 'INDICADOR'),
            how='right')
    .reindex(columns=['ANO', 'FK_ESTADO_CODIGO', 'FK_MUNICIPIO_CODIGO',
                      'INDICADOR', 'QTD_MAT_EJA_INTEGRADO',
                      'QTD_MAT_EJA_TOTAL', 'ATENDIMENTO_IND'])
    .assign(
        QTD_MAT_EJA_INTEGRADO= lambda x: x['QTD_MAT_EJA_INTEGRADO'].fillna(0),
        QTD_MAT_EJA_TOTAL= lambda x: x['QTD_MAT_EJA_TOTAL'].fillna(0))
    .astype({'QTD_MAT_EJA_INTEGRADO':'int',
             'QTD_MAT_EJA_TOTAL':'int'})
    )

    return df_10


# This part is user provided model code
# you will need to copy the next section to run the code
# COMMAND ----------
# this part is dbt logic for get ref work, do not modify

def ref(*args, **kwargs):
    refs = {"info_municipios": "\"postgres\".\"dbt_staging\".\"info_municipios\""}
    key = '.'.join(args)
    version = kwargs.get("v") or kwargs.get("version")
    if version:
        key += f".v{version}"
    dbt_load_df_function = kwargs.get("dbt_load_df_function")
    return dbt_load_df_function(refs[key])


def source(*args, dbt_load_df_function):
    sources = {"staging.FCT_MATRICULAS_EJA_10A": "\"postgres\".\"staging\".\"FCT_MATRICULAS_EJA_10A\""}
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
    identifier = "fct_meta_dez"
    
    def __repr__(self):
        return '"postgres"."dbt_serving"."fct_meta_dez"'


class dbtObj:
    def __init__(self, load_df_function) -> None:
        self.source = lambda *args: source(*args, dbt_load_df_function=load_df_function)
        self.ref = lambda *args, **kwargs: ref(*args, **kwargs, dbt_load_df_function=load_df_function)
        self.config = config
        self.this = this()
        self.is_incremental = False

# COMMAND ----------


