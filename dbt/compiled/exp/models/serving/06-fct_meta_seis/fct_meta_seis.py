import pandas as pd


# fmt: off
def model(dbt, fal):
    df_matriculas_raw: pd.DataFrame = dbt.ref("dim_matricula_6a")
    df_municipios_raw: pd.DataFrame = dbt.ref("info_municipios")
    df_matricula_integral = dbt.source("staging",
                                       "FCT_ESCOLAS_PUBLICAS_INTEGRAL_6B")

    list_indicador = ['6A','6B']
    df_ano_munic = pd.DataFrame()
    for indicador in list_indicador:
        for ano in range(2014, 2021+1):
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

    df_serving_6a = (df_matriculas_raw
        .dropna()
        .assign(QT_MAT_INT_TOTAL=lambda x: (
            x['QT_MAT_INF_INT'] +
            x['QT_MAT_FUND_INT'] +
            x['QT_MAT_MED_INT']))
        .assign(QT_MAT_TOTAL=lambda x: (
            x['QT_MAT_INF'] +
            x['QT_MAT_FUND'] +
            x['QT_MAT_MED']))
        .assign(ATENDIMENTO_IND=lambda x:(
            round(x['QT_MAT_INT_TOTAL']/x['QT_MAT_TOTAL']*100,2)))
        .pipe(lambda x:x.merge(df_ano_munic,
                               on=['ANO', 'FK_MUNICIPIO_CODIGO'],
                               how='right'))
        .reindex(columns=['ANO', 'FK_MUNICIPIO_CODIGO',
                          'INDICADOR','QT_MAT_INT_TOTAL', 'QT_MAT_TOTAL',
                          'ATENDIMENTO_IND'])
        )

    df_serving_6b = (df_matricula_integral
        .query("ETI_1_QT>0")  # Remove entidades sem alunos em regime ETI
        .assign(ETI_percent=lambda x: (x.ETI_1_QT / (x.ETI_0_QT + x.ETI_1_QT)))
        .assign(ETI_goal=1)
        .assign(
            ETI_goal=lambda x: x.ETI_goal.where((x.ETI_percent > 0.25), 0)
        )  # Atinge, entidade com mínimo de 25% dos alunos em ETI
        .groupby(["ANO", "FK_MUNICIPIO_ID"])["ETI_goal"]
        .value_counts()
        .unstack()
        .rename({0: "N_ESCOLAS_ETI_NAO_ATINGIDO", 1: "N_ESCOLAS_ETI"}, axis=1)
        .reset_index()
        .fillna(0)
        .assign(N_ESCOLAS_TOTAL=lambda x:
            (x.N_ESCOLAS_ETI + x.N_ESCOLAS_ETI_NAO_ATINGIDO))
        .drop(columns=["N_ESCOLAS_ETI_NAO_ATINGIDO"], axis=1)
        .assign(
            ATENDIMENTO_IND=lambda x: round(
                (x.N_ESCOLAS_ETI / (x.N_ESCOLAS_TOTAL))*100, 2),
            INDICADOR='6B'
        )
        .rename({'FK_MUNICIPIO_ID':'FK_MUNICIPIO_CODIGO' }, axis=1)
        .reindex(columns=['ANO', 'INDICADOR', 'FK_MUNICIPIO_CODIGO',
                          'N_ESCOLAS_ETI', 'N_ESCOLAS_TOTAL',
                          'QT_MAT_INT_TOTAL', 'QT_MAT_TOTAL',
                          'ATENDIMENTO_IND'])
    )

    df_serving_6_raw = (pd.concat([df_serving_6a, df_serving_6b])
                        .reset_index(drop=True))

    df_serving_6 = (pd
            .merge(df_serving_6_raw,
                   df_ano_munic[['ANO', 'FK_MUNICIPIO_CODIGO',
                                 'FK_ESTADO_CODIGO', 'INDICADOR']],
            on=('ANO', 'FK_MUNICIPIO_CODIGO', 'INDICADOR'),
            how='right')
            .reindex(columns=['ANO', 'FK_ESTADO_CODIGO', 'FK_MUNICIPIO_CODIGO',
                              'INDICADOR', 'N_ESCOLAS_ETI', 'N_ESCOLAS_TOTAL',
                              'QT_MAT_INT_TOTAL', 'QT_MAT_TOTAL',
                              'ATENDIMENTO_IND'])
    )
    return df_serving_6


# This part is user provided model code
# you will need to copy the next section to run the code
# COMMAND ----------
# this part is dbt logic for get ref work, do not modify

def ref(*args, **kwargs):
    refs = {"dim_matricula_6a": "\"postgres\".\"dbt_staging\".\"dim_matricula_6a\"", "info_municipios": "\"postgres\".\"dbt_staging\".\"info_municipios\""}
    key = '.'.join(args)
    version = kwargs.get("v") or kwargs.get("version")
    if version:
        key += f".v{version}"
    dbt_load_df_function = kwargs.get("dbt_load_df_function")
    return dbt_load_df_function(refs[key])


def source(*args, dbt_load_df_function):
    sources = {"staging.FCT_ESCOLAS_PUBLICAS_INTEGRAL_6B": "\"postgres\".\"staging\".\"FCT_ESCOLAS_PUBLICAS_INTEGRAL_6B\""}
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
    identifier = "fct_meta_seis"
    
    def __repr__(self):
        return '"postgres"."dbt_serving"."fct_meta_seis"'


class dbtObj:
    def __init__(self, load_df_function) -> None:
        self.source = lambda *args: source(*args, dbt_load_df_function=load_df_function)
        self.ref = lambda *args, **kwargs: ref(*args, **kwargs, dbt_load_df_function=load_df_function)
        self.config = config
        self.this = this()
        self.is_incremental = False

# COMMAND ----------


