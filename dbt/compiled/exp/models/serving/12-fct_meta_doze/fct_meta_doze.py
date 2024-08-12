import pandas as pd


# fmt: off
def model(dbt, fal):
    # load
    df_municipios_raw: pd.DataFrame = dbt.ref("info_municipios")
    df_dim_educ_sup_12 = dbt.ref("dim_educ_sup_12")
    df_populacao: pd.DataFrame = dbt.ref("fct_projecao_populacional")

    # template
    list_indicador = ['12A', '12B', '12C']
    df_ano_munic = pd.DataFrame()
    for indicador in list_indicador:
        for ano in range(2014,2022+1):
            df_temp = (df_municipios_raw[['MUNICIPIO_CODIGO', 'ESTADO_CODIGO']]
                .copy()
                .rename(columns={'MUNICIPIO_CODIGO':'FK_MUNICIPIO_CODIGO',
                                 'ESTADO_CODIGO':'FK_ESTADO_CODIGO'}))
            df_temp['ANO']=ano
            df_temp['INDICADOR']=indicador
            if df_ano_munic.shape != (0,0):
                df_ano_munic = (pd.concat([df_ano_munic, df_temp])
                                  .reset_index(drop=True))
            else:
                df_ano_munic = df_temp.copy()
    # pop etl
    df_populacao_18_a_24 = (df_populacao
    .query('FK_FAIXAS_ETARIAS_ID==6')
    .reindex(columns=['ANO','FK_MUNICIPIO_CODIGO', 'QUANTIDADE_ESTIMADA'])
    .reset_index(drop=True)
    )

    # ind a
    df_12a = \
    (df_dim_educ_sup_12
        .reindex(columns=['ANO', 'FK_MUNICIPIO_CODIGO',
                        'TP_NIVEL_ACADEMICO','QT_MAT'])
        .query('TP_NIVEL_ACADEMICO==1')
        .dropna(subset=['FK_MUNICIPIO_CODIGO'], axis=0)
        .assign(QT_MAT=lambda x:x['QT_MAT'].fillna(0))
        .astype({'ANO':'uint16',
                'FK_MUNICIPIO_CODIGO':'uint32',
                'TP_NIVEL_ACADEMICO':'uint8',
                'QT_MAT':'uint16'})
        .groupby(by=['ANO', 'FK_MUNICIPIO_CODIGO'])[['QT_MAT']]
        .sum().reset_index()
        .merge(df_populacao_18_a_24, left_on=['ANO','FK_MUNICIPIO_CODIGO'],
                right_on=['ANO', 'FK_MUNICIPIO_CODIGO'], how='left')
        .query('ANO>=2014')
        .assign(QUANTIDADE_ESTIMADA=lambda x:x['QUANTIDADE_ESTIMADA'].fillna(0))
        .rename(columns={'QUANTIDADE_ESTIMADA':'POP_ESTIMADA_18_24'})
        .astype({'POP_ESTIMADA_18_24':'uint32'})
        .assign(ATENDIMENTO_IND = lambda x:
            round(((x['QT_MAT']/x['POP_ESTIMADA_18_24'])*100),2))
        .assign(INDICADOR=list_indicador[0])
        .reindex(columns=['ANO','FK_MUNICIPIO_CODIGO','INDICADOR','QT_MAT',
                          'POP_ESTIMADA_18_24','ATENDIMENTO_IND'])
        .reset_index(drop=True)
    )

    # ind b
    df_12b = \
    (df_dim_educ_sup_12[['ANO', 'FK_MUNICIPIO_CODIGO', 'TP_NIVEL_ACADEMICO',
                         'QT_MAT_18_24', 'QT_CONC_18_24']]
        .dropna(subset='FK_MUNICIPIO_CODIGO', axis=0)
        .query('TP_NIVEL_ACADEMICO==1')
        .reset_index(drop=True)
        .assign(QT_CONC=lambda x:x['QT_CONC_18_24'].fillna(0).astype('uint16'))
        .astype({'ANO':'uint16',
                'QT_MAT_18_24':'uint16',
                'FK_MUNICIPIO_CODIGO':'uint32',
                'TP_NIVEL_ACADEMICO':'uint8'})
        .assign(QT_MAT_18_24_E_CONC=lambda x:x['QT_MAT_18_24']+x['QT_CONC'])
        .drop(columns=['QT_MAT_18_24'])
        .groupby(by=['ANO', 'FK_MUNICIPIO_CODIGO'])[['QT_MAT_18_24_E_CONC']]
        .sum().reset_index()
        .merge(df_populacao_18_a_24,
                on=['ANO','FK_MUNICIPIO_CODIGO'],
                how='left')
        .query('ANO>=2014')
        .assign(QUANTIDADE_ESTIMADA=lambda x:x['QUANTIDADE_ESTIMADA'].fillna(0))
        .rename(columns={'QUANTIDADE_ESTIMADA': 'POP_ESTIMADA_18_24'})
        .astype({'POP_ESTIMADA_18_24':'uint32'})
        .assign(ATENDIMENTO_IND = lambda x:
            round((x['QT_MAT_18_24_E_CONC']/x['POP_ESTIMADA_18_24'])*100,2))
        .assign(ATENDIMENTO_IND = lambda x:(round(x['ATENDIMENTO_IND'], 2)))
        .assign(INDICADOR=list_indicador[1])
        .reindex(columns=['ANO','FK_MUNICIPIO_CODIGO','INDICADOR',
                        'QT_MAT_18_24_E_CONC','POP_ESTIMADA_18_24',
                        'ATENDIMENTO_IND'])
        .reset_index(drop=True)
    )

    # ind c
    df_12c = \
    (df_dim_educ_sup_12[['ANO', 'FK_MUNICIPIO_CODIGO', 'TP_NIVEL_ACADEMICO',
                         'TP_CATEGORIA_ADMINISTRATIVA', 'QT_MAT']]
        .dropna(subset='FK_MUNICIPIO_CODIGO', axis=0)
        .query('TP_NIVEL_ACADEMICO==1 and ANO>=2013')
        .assign(QT_MAT=lambda x:x['QT_MAT'].fillna(0))
        .astype({'ANO':'uint16',
                'QT_MAT':'uint16',
                'FK_MUNICIPIO_CODIGO':'uint32',
                'TP_NIVEL_ACADEMICO':'uint8'})
        .assign(PUBLICA="PUBLICA_SIM")
        .assign(PUBLICA=lambda x: (x['PUBLICA']
                                .where(x['TP_CATEGORIA_ADMINISTRATIVA']
                                       .isin([1,2,3,7]), "PUBLICA_NAO")))
        .drop(columns=['TP_NIVEL_ACADEMICO', 'TP_CATEGORIA_ADMINISTRATIVA'])
        .groupby(["ANO", "FK_MUNICIPIO_CODIGO","PUBLICA"])["QT_MAT"]
        .sum().unstack().reset_index().rename_axis(None, axis=1)
        .assign(PUBLICA_SIM=lambda x:x['PUBLICA_SIM'].fillna(0),
                PUBLICA_NAO=lambda x:x['PUBLICA_NAO'].fillna(0),
                QT_TOTAL=lambda x:x['PUBLICA_SIM']+x['PUBLICA_NAO'])
        # # 2013 cols
        .pipe(lambda w:(
        w.merge(w.loc[lambda y: y['ANO'].isin([2013]),
                        ['FK_MUNICIPIO_CODIGO', 'PUBLICA_NAO', 'PUBLICA_SIM']]
                    .rename(columns={'PUBLICA_SIM': 'QT_PUBLICA_2013'})
                    .assign(QT_TOTAL_2013=lambda x:
                        x['QT_PUBLICA_2013'] + x['PUBLICA_NAO'])
                    .reindex(['FK_MUNICIPIO_CODIGO',
                              'QT_TOTAL_2013',
                              'QT_PUBLICA_2013'],
                            axis=1),
                on='FK_MUNICIPIO_CODIGO', how='left')))
        .query('ANO>=2014')
        .rename(columns={'PUBLICA_SIM': 'QT_PUBLICA'})
        .drop(columns=['PUBLICA_NAO'])
        .fillna(0)
        .astype({'QT_PUBLICA':'uint16',
                'QT_TOTAL':'uint16',
                'QT_PUBLICA_2013':'uint16',
                'QT_TOTAL_2013':'uint16'})
        .assign(ATENDIMENTO_IND = lambda x:(
            ((x['QT_PUBLICA']-x['QT_PUBLICA_2013']) /
            (x['QT_TOTAL']-x['QT_TOTAL_2013'])
            )*100).round(2))
        .assign(INDICADOR=list_indicador[2])
        .reindex(columns=['ANO','FK_MUNICIPIO_CODIGO','INDICADOR',
                          'QT_PUBLICA','QT_TOTAL','QT_PUBLICA_2013',
                          'QT_TOTAL_2013','ATENDIMENTO_IND'])
        .reset_index(drop=True)
    )

    # meta concat
    df_12_raw = pd.concat([df_12a, df_12b, df_12c]).reset_index(drop=True)

    # meta transform
    df_12 = \
    (df_12_raw
        .reset_index(drop=True)
        .merge(
            df_ano_munic[['ANO', 'FK_MUNICIPIO_CODIGO', 'INDICADOR',
                          'FK_ESTADO_CODIGO']],
            on=('ANO', 'FK_MUNICIPIO_CODIGO', 'INDICADOR'),
            how='right')
        .reindex(['ANO', 'FK_ESTADO_CODIGO', 'FK_MUNICIPIO_CODIGO',
                  'INDICADOR', 'QT_MAT',
                  'QT_MAT_18_24_E_CONC', 'POP_ESTIMADA_18_24', 'QT_PUBLICA',
                  'QT_TOTAL', 'QT_PUBLICA_2013', 'QT_TOTAL_2013',
                  'ATENDIMENTO_IND'],
                axis=1)
        .fillna(0)
        .astype({col: 'uint32' for col in ['FK_MUNICIPIO_CODIGO', 'QT_MAT',
                                           'QT_MAT_18_24_E_CONC',
                                           "POP_ESTIMADA_18_24", "QT_PUBLICA",
                                           "QT_TOTAL", "QT_PUBLICA_2013",
                                           "QT_TOTAL_2013"]})
        .astype({'ANO':'uint16'})
        .sort_values(by=['ANO', 'INDICADOR','FK_MUNICIPIO_CODIGO'])
        .reset_index(drop=True)
    )
    return df_12


# This part is user provided model code
# you will need to copy the next section to run the code
# COMMAND ----------
# this part is dbt logic for get ref work, do not modify

def ref(*args, **kwargs):
    refs = {"dim_educ_sup_12": "\"postgres\".\"dbt_staging\".\"dim_educ_sup_12\"", "fct_projecao_populacional": "\"postgres\".\"dbt_staging\".\"fct_projecao_populacional\"", "info_municipios": "\"postgres\".\"dbt_staging\".\"info_municipios\""}
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
    identifier = "fct_meta_doze"
    
    def __repr__(self):
        return '"postgres"."dbt_serving"."fct_meta_doze"'


class dbtObj:
    def __init__(self, load_df_function) -> None:
        self.source = lambda *args: source(*args, dbt_load_df_function=load_df_function)
        self.ref = lambda *args, **kwargs: ref(*args, **kwargs, dbt_load_df_function=load_df_function)
        self.config = config
        self.this = this()
        self.is_incremental = False

# COMMAND ----------


