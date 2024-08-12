import pandas as pd


# fmt: off
def model(dbt, fal):
    # load
    df_municipios_raw: pd.DataFrame = dbt.ref("info_municipios")
    df_dim_municipios_pib = dbt.source("raw", "DIM_MUNICIPIOS_PIB")
    df_dim_siconfi_20 = dbt.ref("dim_siconfi_20")
    df_dim_tce_pe_educacao = dbt.ref("dim_tce_pe_educacao")
    df_dim_tce_sp_educacao = dbt.ref("dim_tce_sp_educacao")
    df_dim_tce_mg_educacao = dbt.ref("dim_tce_mg_educacao")
    df_dim_tce_es_educacao = dbt.ref("dim_tce_es_educacao")

    # template
    list_indicador = ['20A', '20B']
    df_ano_munic = pd.DataFrame()
    for indicador in list_indicador:
        for ano in range(2014, 2020+1):
            df_temp = (
                df_municipios_raw[['MUNICIPIO_CODIGO', 'ESTADO_CODIGO']]
                .copy()
                .rename(columns={'MUNICIPIO_CODIGO': 'FK_MUNICIPIO_CODIGO',
                                 'ESTADO_CODIGO': 'FK_ESTADO_CODIGO'}))
            df_temp['ANO']=ano
            df_temp['INDICADOR']=indicador
            if df_ano_munic.shape != (0,0):
                df_ano_munic = (pd.concat([df_ano_munic, df_temp])
                                  .reset_index(drop=True))
            else:
                df_ano_munic = df_temp.copy()

    # ind a
    df_20a = \
        (df_dim_siconfi_20
         .query('ANO>=2014 & ANO<=2020')
         .groupby(by=['ANO', 'FK_MUNICIPIO_CODIGO', 'CONTA']).sum(numeric_only=False)
         .reset_index()
         .pivot(index=['ANO', 'FK_MUNICIPIO_CODIGO'], columns='CONTA', values='VALOR')
         .reset_index()
         .rename(columns={"12 - Educação": 'GASTOS_EDUCACAO',
                          "28.847 - Transferências para a Educação Básica": 'TRANSFERENCIAS_EDUC_BASICA'})
         .assign(TRANSFERENCIAS_EDUC_BASICA=lambda x:x['TRANSFERENCIAS_EDUC_BASICA'].fillna(0))
         .assign(GASTOS_EDUCACAO_PUBLICA=lambda x:x['GASTOS_EDUCACAO'].fillna(0))
         .merge(df_dim_municipios_pib[["ANO", "CODIGO_DO_MUNICIPIO",
                                       "PRODUTO_INTERNO_BRUTO_A_PRECOS_CORRENTES_R_1_000"]],
                left_on=['ANO','FK_MUNICIPIO_CODIGO'],
                right_on=['ANO','CODIGO_DO_MUNICIPIO'], how='left')

         .rename(columns={'PRODUTO_INTERNO_BRUTO_A_PRECOS_CORRENTES_R_1_000': 'PIB'})
         .assign(PIB=lambda x:x['PIB']*1000)
         .assign(INDICADOR=list_indicador[0])
         .assign(ATENDIMENTO_IND =\
             lambda x:round((x['GASTOS_EDUCACAO_PUBLICA']+x['TRANSFERENCIAS_EDUC_BASICA'])/x['PIB'],4) * 100)
         .reindex(columns=['ANO', 'FK_MUNICIPIO_CODIGO','INDICADOR',
                           'GASTOS_EDUCACAO_PUBLICA', 'TRANSFERENCIAS_EDUC_BASICA', 'PIB',
                           'ATENDIMENTO_IND'])
        )

    df_20b = \
        (pd.concat([df_dim_tce_pe_educacao[['ANO', 'FK_MUNICIPIO_CODIGO','VALOR_PAGO']],
                    df_dim_tce_sp_educacao[['ANO', 'FK_MUNICIPIO_CODIGO','VALOR_PAGO']],
                    df_dim_tce_mg_educacao[['ANO', 'FK_MUNICIPIO_CODIGO','VALOR_PAGO']],
                    df_dim_tce_es_educacao[['ANO', 'FK_MUNICIPIO_CODIGO','VALOR_PAGO']]]
                )
        .groupby(by=['ANO', 'FK_MUNICIPIO_CODIGO'])['VALOR_PAGO'].sum().reset_index()
        .rename(columns={'VALOR_PAGO':'GASTOS_EDUCACAO'})
        .query('ANO >= 2014 and ANO <= 2020')
        .merge((df_dim_municipios_pib
                .reindex(columns=['ANO', 'CODIGO_DO_MUNICIPIO',
                                  'PRODUTO_INTERNO_BRUTO_A_PRECOS_CORRENTES_R_1_000'])
                .query('ANO >= 2014')
                .rename(columns={'PRODUTO_INTERNO_BRUTO_A_PRECOS_CORRENTES_R_1_000':'PIB',
                                 'CODIGO_DO_MUNICIPIO':'FK_MUNICIPIO_CODIGO'})
                .assign(PIB=lambda x:x['PIB']*1000)
                ),
                on=['ANO','FK_MUNICIPIO_CODIGO'],how='left')
        .assign(INDICADOR=list_indicador[1])
        .assign(ATENDIMENTO_IND = \
                lambda x:round(x['GASTOS_EDUCACAO']/x['PIB'], 4) * 100)
        .reindex(columns=['ANO', 'FK_MUNICIPIO_CODIGO','INDICADOR',
                          'GASTOS_EDUCACAO', 'PIB',
                          'ATENDIMENTO_IND'])
        )
    # meta concat
    df_20_raw = pd.concat([df_20a, df_20b]).reset_index(drop=True)

    # meta transform
    df_20 = \
        (df_20_raw
            .reset_index(drop=True)
            .merge(
                df_ano_munic[['ANO', 'FK_MUNICIPIO_CODIGO', 'INDICADOR',
                              'FK_ESTADO_CODIGO']],
                on=('ANO', 'FK_MUNICIPIO_CODIGO', 'INDICADOR'),
                how='right')
            .reindex(['ANO', 'FK_ESTADO_CODIGO',
                      'FK_MUNICIPIO_CODIGO', 'INDICADOR',
                      'GASTOS_EDUCACAO', 'GASTOS_EDUCACAO_PUBLICA', 'TRANSFERENCIAS_EDUC_BASICA', 'PIB',
                      'ATENDIMENTO_IND'],
                     axis=1)
            .fillna(0)
            .astype({col: 'uint32' for col in ['FK_MUNICIPIO_CODIGO', 'FK_ESTADO_CODIGO',]})
            .astype({'ANO':'uint16'})
            .sort_values(by=['ANO', 'INDICADOR', 'FK_MUNICIPIO_CODIGO'])
            .reset_index(drop=True)
        )
    return df_20


# This part is user provided model code
# you will need to copy the next section to run the code
# COMMAND ----------
# this part is dbt logic for get ref work, do not modify

def ref(*args, **kwargs):
    refs = {"dim_siconfi_20": "\"postgres\".\"dbt_staging\".\"dim_siconfi_20\"", "dim_tce_es_educacao": "\"postgres\".\"dbt_staging\".\"dim_tce_es_educacao\"", "dim_tce_mg_educacao": "\"postgres\".\"dbt_staging\".\"dim_tce_mg_educacao\"", "dim_tce_pe_educacao": "\"postgres\".\"dbt_staging\".\"dim_tce_pe_educacao\"", "dim_tce_sp_educacao": "\"postgres\".\"dbt_staging\".\"dim_tce_sp_educacao\"", "info_municipios": "\"postgres\".\"dbt_staging\".\"info_municipios\""}
    key = '.'.join(args)
    version = kwargs.get("v") or kwargs.get("version")
    if version:
        key += f".v{version}"
    dbt_load_df_function = kwargs.get("dbt_load_df_function")
    return dbt_load_df_function(refs[key])


def source(*args, dbt_load_df_function):
    sources = {"raw.DIM_MUNICIPIOS_PIB": "\"postgres\".\"raw\".\"DIM_MUNICIPIOS_PIB\""}
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
    identifier = "fct_meta_vinte"
    
    def __repr__(self):
        return '"postgres"."dbt_serving"."fct_meta_vinte"'


class dbtObj:
    def __init__(self, load_df_function) -> None:
        self.source = lambda *args: source(*args, dbt_load_df_function=load_df_function)
        self.ref = lambda *args, **kwargs: ref(*args, **kwargs, dbt_load_df_function=load_df_function)
        self.config = config
        self.this = this()
        self.is_incremental = False

# COMMAND ----------


# Generated by dbt-fal

def main(read_df, write_df, fal_context=None):
  dbt_context = dbtObj(read_df)
  df = model(dbt_context, fal_context)
  return write_df(
      'postgres.dbt_serving.fct_meta_vinte',
      df
  )