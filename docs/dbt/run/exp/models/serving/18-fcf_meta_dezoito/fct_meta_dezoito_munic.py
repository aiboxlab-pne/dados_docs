import numpy as np
import pandas as pd


# fmt: off
def model(dbt, fal):
    # load
    df_dim_munic_educ = dbt.ref("dim_munic_educ")
    df_municipios_raw: pd.DataFrame = dbt.ref("info_municipios")

    # template
    list_indicador_munic = ['18E','18F','18G','18H']

    # ind e
    df_18e = \
    (df_dim_munic_educ
        .reindex(columns=['ANO','FK_MUNICIPIO_CODIGO','MEDU16'])
        .assign(INDICADOR=list_indicador_munic[0])
        .rename(columns={'MEDU16':'ATENDIMENTO_IND'})
        .assign(ATENDIMENTO_IND=lambda x:
            x['ATENDIMENTO_IND'].replace({'Sim':1, np.nan:-1,'Não':0,
                                          'Não informado':-1,'Recusa':-1,
                                          'Não informou':-1}))
        .astype({'ATENDIMENTO_IND':np.int8})
        .reindex(columns=['ANO', 'FK_MUNICIPIO_CODIGO','INDICADOR',
                          'ATENDIMENTO_IND'])
        )

    # ind f
    df_18f = \
    (df_dim_munic_educ
        .reindex(columns=['ANO','FK_MUNICIPIO_CODIGO','MEDU18'])
        .assign(INDICADOR=list_indicador_munic[1])
        .rename(columns={'MEDU18':'ATENDIMENTO_IND'})
        .assign(ATENDIMENTO_IND=lambda x:
            x['ATENDIMENTO_IND'].replace({'Sim':1, np.nan:-1,'Não':0,
                                          '(*) Não soube informar':-1,
                                          'Recusa':-1,'Não informou':-1,
                                          '-':-1}))
        .astype({'ATENDIMENTO_IND':np.int8})
        .reindex(columns=['ANO', 'FK_MUNICIPIO_CODIGO','INDICADOR',
                          'ATENDIMENTO_IND'])
        )

    # ind g
    df_18g = \
    (df_dim_munic_educ
        .reindex(columns=['ANO','FK_MUNICIPIO_CODIGO','MEDU20A'])
        .assign(INDICADOR=list_indicador_munic[2])
        .rename(columns={'MEDU20A':'ATENDIMENTO_IND'})
        .assign(ATENDIMENTO_IND=lambda x: x['ATENDIMENTO_IND'].replace(
            {np.nan:0, 'Sim':1, 'Não':0,
             'Não há professores com jornada de 40 horas semanais':-2,
             'Recusa':-1, 'Não informou':-1}))
        .astype({'ATENDIMENTO_IND':np.int8})
        .reindex(columns=['ANO', 'FK_MUNICIPIO_CODIGO','INDICADOR',
                          'ATENDIMENTO_IND'])
        )

    # ind h
    df_18h = \
    (df_dim_munic_educ
        .reindex(columns=['ANO','FK_MUNICIPIO_CODIGO','MEDU21'])
        .assign(INDICADOR=list_indicador_munic[3])
        .rename(columns={'MEDU21':'ATENDIMENTO_IND'})
        .assign(ATENDIMENTO_IND=lambda x:
            x['ATENDIMENTO_IND'].replace({np.nan:-1, 'Não':0, 'Sim':1,
                                          'Recusa':-1, 'Não informou':-1}))
        .astype({'ATENDIMENTO_IND':np.int8})
        .reindex(columns=['ANO', 'FK_MUNICIPIO_CODIGO','INDICADOR',
                          'ATENDIMENTO_IND'])
        )

    # meta concat
    df_18_munic_raw = pd.concat([df_18e, df_18f,
                                 df_18g, df_18h]).reset_index(drop=True)

    # meta transform
    df_18_munic = \
        (df_18_munic_raw
            .reset_index(drop=True)
            .merge(
                (df_municipios_raw.rename(
                    columns={'MUNICIPIO_CODIGO':'FK_MUNICIPIO_CODIGO',
                            'ESTADO_CODIGO':'FK_ESTADO_CODIGO'})
                .reindex(columns=['FK_MUNICIPIO_CODIGO','FK_ESTADO_CODIGO'])),
                on=('FK_MUNICIPIO_CODIGO'),
                how='left')
            .reindex(['ANO', 'FK_ESTADO_CODIGO',
                    'FK_MUNICIPIO_CODIGO', 'INDICADOR',
                    'ATENDIMENTO_IND'],
                    axis=1)
            .fillna(0)
            .astype({col: 'uint32' for col in ['FK_MUNICIPIO_CODIGO', 'FK_ESTADO_CODIGO']})
            .astype({'ANO':'uint16'})
            .sort_values(by=['ANO', 'INDICADOR', 'FK_MUNICIPIO_CODIGO'])
            .reset_index(drop=True)
        )
    return df_18_munic


# This part is user provided model code
# you will need to copy the next section to run the code
# COMMAND ----------
# this part is dbt logic for get ref work, do not modify

def ref(*args, **kwargs):
    refs = {"dim_munic_educ": "\"postgres\".\"dbt_staging\".\"dim_munic_educ\"", "info_municipios": "\"postgres\".\"dbt_staging\".\"info_municipios\""}
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
    identifier = "fct_meta_dezoito_munic"
    
    def __repr__(self):
        return '"postgres"."dbt_serving"."fct_meta_dezoito_munic"'


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
      'postgres.dbt_serving.fct_meta_dezoito_munic',
      df
  )