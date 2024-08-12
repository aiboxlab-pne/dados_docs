import pandas as pd


# fmt: off
def model(dbt, fal):
    df_matriculas_raw: pd.DataFrame = dbt.ref("dim_matricula_faixa_idade")
    df_pop_raw: pd.DataFrame = dbt.ref("fct_projecao_populacional")

    df_matriculas = \
        (df_matriculas_raw
         .dropna()
         .assign(QT_MAT_IND=lambda x:x['QT_MAT_6_10']+x['QT_MAT_11_14'])
         .reindex(['ANO','FK_MUNICIPIO_CODIGO','QT_MAT_IND'], axis=1)
         .assign(INDICADOR='2A')
         )
    df_pop = (df_pop_raw
                .query("FK_FAIXAS_ETARIAS_ID in [3,4]")
                .rename(columns={'FK_FAIXAS_ETARIAS_ID':'INDICADOR',
                                 'QUANTIDADE_ESTIMADA':'POP_ESTIMADA_IND'})
                .groupby(["ANO",
                          "FK_ESTADO_CODIGO",
                          "FK_MUNICIPIO_CODIGO"])['POP_ESTIMADA_IND'].sum()
                .reset_index()
                .assign(INDICADOR='2A')
              )

    df_meta = (df_pop
               .merge(df_matriculas,
            left_on = ['ANO', 'FK_MUNICIPIO_CODIGO', 'INDICADOR'],
            right_on = ['ANO', 'FK_MUNICIPIO_CODIGO', 'INDICADOR'],
            how='left')
    .astype({'POP_ESTIMADA_IND':'Int64', 'QT_MAT_IND':'Int64'})
    .assign(POP_ESTIMADA_IND_ORIGINAL=lambda x:x['POP_ESTIMADA_IND'])
    .rename(columns={'POP_ESTIMADA_IND': 'POP_ESTIMADA_IND_AJUSTADA'})
    .assign(FLAG_SUBESTIMADA=1)
    .assign(FLAG_SUBESTIMADA=lambda x:x['FLAG_SUBESTIMADA'].where((x['POP_ESTIMADA_IND_ORIGINAL']>0) &
                       (x['POP_ESTIMADA_IND_ORIGINAL']<x['QT_MAT_IND']) &
                       (x['QT_MAT_IND']>0),
                       0))
    .assign(FLAG_MUNIC_NOVO=1)
    .assign(FLAG_MUNIC_NOVO=lambda x:x['FLAG_MUNIC_NOVO'].where(x['POP_ESTIMADA_IND_ORIGINAL']==0,0))
    .assign(POP_ESTIMADA_IND_AJUSTADA=lambda x:x['QT_MAT_IND'].where(
        (x['FLAG_MUNIC_NOVO']==1) | (x['FLAG_SUBESTIMADA']==1),
        x['POP_ESTIMADA_IND_ORIGINAL']))
    .assign(PP_ATENDIMENTO_IND=\
        lambda x:round(x['QT_MAT_IND']/x['POP_ESTIMADA_IND_AJUSTADA']*100,2))
    .reindex(columns=['ANO', 'FK_ESTADO_CODIGO', 'FK_MUNICIPIO_CODIGO',
                      'INDICADOR','QT_MAT_IND', 'POP_ESTIMADA_IND_ORIGINAL',
                      'POP_ESTIMADA_IND_AJUSTADA', 'FLAG_SUBESTIMADA',
                      'FLAG_MUNIC_NOVO', 'PP_ATENDIMENTO_IND']
             )
    )
    return df_meta


# This part is user provided model code
# you will need to copy the next section to run the code
# COMMAND ----------
# this part is dbt logic for get ref work, do not modify

def ref(*args, **kwargs):
    refs = {"dim_matricula_faixa_idade": "\"postgres\".\"dbt_staging\".\"dim_matricula_faixa_idade\"", "fct_projecao_populacional": "\"postgres\".\"dbt_staging\".\"fct_projecao_populacional\""}
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
    identifier = "fct_meta_dois"
    
    def __repr__(self):
        return '"postgres"."dbt_serving"."fct_meta_dois"'


class dbtObj:
    def __init__(self, load_df_function) -> None:
        self.source = lambda *args: source(*args, dbt_load_df_function=load_df_function)
        self.ref = lambda *args, **kwargs: ref(*args, **kwargs, dbt_load_df_function=load_df_function)
        self.config = config
        self.this = this()
        self.is_incremental = False

# COMMAND ----------


