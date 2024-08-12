import pandas as pd


# fmt: off
def model(dbt, fal):
    df_municipios_raw: pd.DataFrame = dbt.ref("info_municipios")
    df_fct_matriculas_ept = dbt.source("staging",
                                       "FCT_MATRICULAS_EPT")

    list_indicador = ['11A','11B']
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

    df_11a = \
        (df_fct_matriculas_ept
            .assign(EPT_TOTAL=lambda x: x.EPT_PRIVADO + x.EPT_PUBLICO,
                    ATENDIMENTO_IND = lambda x: x.EPT_TOTAL)
            .assign(INDICADOR='11A')
            .reindex(columns=['ANO', 'INDICADOR', 'FK_MUNICIPIO_CODIGO',
                            'EPT_TOTAL', 'ATENDIMENTO_IND'])
            .loc[lambda x:x.ANO>2013, :]
        )

    df_11b = \
        (df_fct_matriculas_ept
            .assign(EPT_TOTAL=lambda x:x.EPT_PRIVADO+x.EPT_PUBLICO)
            .reindex(['ANO', 'FK_MUNICIPIO_CODIGO',
                    'EPT_PUBLICO', 'EPT_TOTAL'], axis=1)
            .loc[lambda x:x.ANO>2013,:]
            .merge(
                (df_fct_matriculas_ept
                .loc[lambda y: y.ANO==2013,
                        ['FK_MUNICIPIO_CODIGO', 'EPT_PRIVADO', 'EPT_PUBLICO']]
                .rename(columns={'EPT_PRIVADO': 'EPT_PRIVADO_2013',
                                    'EPT_PUBLICO': 'EPT_PUBLICO_2013'})
                .assign(EPT_TOTAL_2013=lambda x:
                        x.EPT_PRIVADO_2013+x.EPT_PUBLICO_2013)
                .reindex(['FK_MUNICIPIO_CODIGO', 'EPT_PUBLICO_2013',
                            'EPT_TOTAL_2013'], axis=1)),
                on='FK_MUNICIPIO_CODIGO', how='left')
            .assign(INDICADOR='11B')
            .assign(EXPANSAO_EPT_PUBLICA=lambda x:
                (x.EPT_PUBLICO-x.EPT_PUBLICO_2013))
            .loc[lambda x:x.EXPANSAO_EPT_PUBLICA>0,:]
            .assign(EXPANSAO_EPT_TOTAL=lambda x:(x.EPT_TOTAL-x.EPT_TOTAL_2013))
            .assign(ATENDIMENTO_IND=lambda x:
                round((x.EXPANSAO_EPT_PUBLICA)/(x.EXPANSAO_EPT_TOTAL),4))
            .loc[lambda x:x.ATENDIMENTO_IND>=0, :]
            .reindex(['ANO', 'FK_MUNICIPIO_CODIGO', 'INDICADOR',
                    'EPT_PUBLICO', 'EPT_PUBLICO_2013', 'EPT_TOTAL',
                    'EPT_TOTAL_2013', 'EXPANSAO_EPT_PUBLICA',
                    'EXPANSAO_EPT_TOTAL', 'ATENDIMENTO_IND'], axis=1)
        )

    df_11_raw = (pd.concat([df_11a, df_11b]).reset_index(drop=True))

    df_11 = (pd
        .merge(df_11_raw,
            df_ano_munic[['ANO', 'FK_MUNICIPIO_CODIGO',
                          'FK_ESTADO_CODIGO', 'INDICADOR']],
            on=('ANO', 'FK_MUNICIPIO_CODIGO', 'INDICADOR'),
            how='right')
        .assign(
            EPT_PUBLICO = lambda x: x['EPT_PUBLICO'].fillna(0).astype('int'),
            EPT_PUBLICO_2013 = lambda x: x['EPT_PUBLICO_2013'].fillna(0).astype('int'),
            EPT_TOTAL = lambda x: x['EPT_TOTAL'].fillna(0).astype('int'),
            EPT_TOTAL_2013 = lambda x: x['EPT_TOTAL_2013'].fillna(0).astype('int'))
        .reindex(columns=["ANO", "FK_ESTADO_CODIGO", "FK_MUNICIPIO_CODIGO",
                          "INDICADOR", "EPT_PUBLICO", "EPT_PUBLICO_2013",
                          "EPT_TOTAL", "EPT_TOTAL_2013", "ATENDIMENTO_IND"])
    )
    return df_11


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
    sources = {"staging.FCT_MATRICULAS_EPT": "\"postgres\".\"staging\".\"FCT_MATRICULAS_EPT\""}
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
    identifier = "fct_meta_onze"
    
    def __repr__(self):
        return '"postgres"."dbt_serving"."fct_meta_onze"'


class dbtObj:
    def __init__(self, load_df_function) -> None:
        self.source = lambda *args: source(*args, dbt_load_df_function=load_df_function)
        self.ref = lambda *args, **kwargs: ref(*args, **kwargs, dbt_load_df_function=load_df_function)
        self.config = config
        self.this = this()
        self.is_incremental = False

# COMMAND ----------


