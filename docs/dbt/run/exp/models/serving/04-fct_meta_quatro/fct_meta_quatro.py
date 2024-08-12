import numpy as np
import pandas as pd


# fmt: off
def model(dbt, fal):
    # load
    df_municipios_raw: pd.DataFrame = dbt.ref("info_municipios")
    df_dim_censo_educ_basica_desagregado_matricula_4 = dbt.ref("dim_censo_educ_basica_desagregado_matricula_4")

    # template
    list_indicador = ['4B', '4C']

    df_ano_munic = pd.DataFrame()
    for indicador in list_indicador:
        for ano in range(2014,2020+1):
            df_temp = (df_municipios_raw[['MUNICIPIO_CODIGO', 'ESTADO_CODIGO']].copy()
                    .rename(columns={'MUNICIPIO_CODIGO':'FK_MUNICIPIO_CODIGO', 'ESTADO_CODIGO':'FK_ESTADO_CODIGO'})
                    )
            df_temp['ANO']=ano
            df_temp['INDICADOR']=indicador
            if df_ano_munic.shape != (0,0):
                df_ano_munic = pd.concat([df_ano_munic, df_temp]).reset_index(drop=True)
            else:
                df_ano_munic = df_temp.copy()

    # ind b
    df_4b = \
        (df_dim_censo_educ_basica_desagregado_matricula_4
        .reindex(columns=['ANO', 'FK_MUNICIPIO_CODIGO',
                        'IN_NECESSIDADE_ESPECIAL', 'IN_ESPECIAL_EXCLUSIVA',
                        'TP_ETAPA_ENSINO','COUNT_MATRICULA'])
        .assign(ANO=lambda x:x['ANO'].astype(int))
        .drop(columns=['IN_NECESSIDADE_ESPECIAL','TP_ETAPA_ENSINO'])
        .assign(IN_ESPECIAL_EXCLUSIVA=lambda x:
                (x['IN_ESPECIAL_EXCLUSIVA'].replace({0:'MAT_ESPECIAL_TURMA_COMUM',
                                                    1:'MAT_TURMA_ESPECIAL_EXCLUSIVA'})))
        .pivot_table(index=["ANO", "FK_MUNICIPIO_CODIGO"],
                    columns="IN_ESPECIAL_EXCLUSIVA",
                    aggfunc=np.sum)
        .reset_index(col_level=1)
        .droplevel(level=0, axis=1)
        .rename_axis(None, axis=1)
        .fillna(0)
        .assign(MAT_ESPECIAL_TOTAL=lambda x:
                x['MAT_ESPECIAL_TURMA_COMUM']+x['MAT_TURMA_ESPECIAL_EXCLUSIVA'])
        .drop(columns=['MAT_TURMA_ESPECIAL_EXCLUSIVA'])
        .assign(ATENDIMENTO_IND=lambda x:(
                round(x['MAT_ESPECIAL_TURMA_COMUM']/x['MAT_ESPECIAL_TOTAL']*100,2)))
        .assign(INDICADOR=list_indicador[0])
        .reindex(columns=['ANO', 'FK_MUNICIPIO_CODIGO','INDICADOR',
                        'MAT_ESPECIAL_TURMA_COMUM', 'MAT_ESPECIAL_TOTAL',
                        'ATENDIMENTO_IND'])
        )

    # ind c
    df_4c = \
        (df_dim_censo_educ_basica_desagregado_matricula_4
        .reindex(columns=['ANO', 'FK_MUNICIPIO_CODIGO',
                          'IN_NECESSIDADE_ESPECIAL', 'IN_ESPECIAL_EXCLUSIVA',
                          'TP_ETAPA_ENSINO', 'TP_TIPO_TURMA', 'COUNT_MATRICULA'])
        .assign(ANO=lambda x:x['ANO'].astype(int))
        .rename(columns={'TP_TIPO_TURMA':'TP_TIPO_TURMA_2019_APOS'})
        .assign(TP_TIPO_TURMA_2019_ANTES=lambda x:
                x['TP_TIPO_TURMA_2019_APOS'].replace({5:4}))
        .assign(TP_TIPO_TURMA=lambda x:
                x['TP_TIPO_TURMA_2019_APOS'].where(x['ANO']>=2019,
                                                   x['TP_TIPO_TURMA_2019_ANTES']))
        .drop(columns=['IN_NECESSIDADE_ESPECIAL','TP_ETAPA_ENSINO',
                       'TP_TIPO_TURMA_2019_ANTES','TP_TIPO_TURMA_2019_APOS'])
        .assign(ESPECIAL=1)
        .assign(ESPECIAL = lambda x:
                x['ESPECIAL'].where((x['IN_ESPECIAL_EXCLUSIVA'].isin([1])) |
                                    (x['TP_TIPO_TURMA'].isin([4])), 0))
        .assign(ESPECIAL=lambda x:(
            x['ESPECIAL'].replace({0:'MAT_ESPECIAL_ATENDIMENTO_COMUM',
                                   1:'MAT_ESPECIAL_ATENDIMENTO_ESPECIALIZADO'})))
        .drop(columns=['TP_TIPO_TURMA','IN_ESPECIAL_EXCLUSIVA'])
        .pivot_table(index=["ANO", "FK_MUNICIPIO_CODIGO"],
                     columns="ESPECIAL",
                     aggfunc=np.sum)
        .reset_index(col_level=1)
        .droplevel(level=0, axis=1)
        .rename_axis(None, axis=1)
        .fillna(0)
        .assign(MAT_ESPECIAL_TOTAL=lambda x:
                (x['MAT_ESPECIAL_ATENDIMENTO_COMUM']+
                 x['MAT_ESPECIAL_ATENDIMENTO_ESPECIALIZADO']))
        .drop(columns=['MAT_ESPECIAL_ATENDIMENTO_COMUM'])
        .assign(ATENDIMENTO_IND=lambda x:(
                round(x['MAT_ESPECIAL_ATENDIMENTO_ESPECIALIZADO']/
                      x['MAT_ESPECIAL_TOTAL']*100,2)))
        .assign(INDICADOR=list_indicador[1])
        .reindex(columns=['ANO', 'FK_MUNICIPIO_CODIGO','INDICADOR',
                          'MAT_ESPECIAL_ATENDIMENTO_ESPECIALIZADO',
                          'MAT_ESPECIAL_TOTAL', 'ATENDIMENTO_IND'])
        )

    # meta concat
    df_4_raw = pd.concat([df_4b, df_4c]).reset_index(drop=True)

    # meta transform
    df_4 = \
        (df_4_raw
            .reset_index(drop=True)
            .merge(
                df_ano_munic[['ANO', 'FK_MUNICIPIO_CODIGO', 'INDICADOR',
                              'FK_ESTADO_CODIGO']],
                on=('ANO', 'FK_MUNICIPIO_CODIGO', 'INDICADOR'),
                how='right')
            .fillna(0)
            .reindex(['ANO', 'FK_ESTADO_CODIGO',
                      'FK_MUNICIPIO_CODIGO', 'INDICADOR',
                      'MAT_ESPECIAL_TURMA_COMUM',
                      'MAT_ESPECIAL_ATENDIMENTO_ESPECIALIZADO',
                      'MAT_ESPECIAL_TOTAL','ATENDIMENTO_IND'],
                    axis=1)
            .astype({col: 'uint32' for col in ['FK_MUNICIPIO_CODIGO',
                                            'FK_ESTADO_CODIGO']})
            .astype({'ANO':'uint16'})
            .astype({'ATENDIMENTO_IND':float})
            .sort_values(by=['ANO', 'INDICADOR', 'FK_MUNICIPIO_CODIGO'])
            .reset_index(drop=True)
        )
    return df_4


# This part is user provided model code
# you will need to copy the next section to run the code
# COMMAND ----------
# this part is dbt logic for get ref work, do not modify

def ref(*args, **kwargs):
    refs = {"dim_censo_educ_basica_desagregado_matricula_4": "\"postgres\".\"dbt_staging\".\"dim_censo_educ_basica_desagregado_matricula_4\"", "info_municipios": "\"postgres\".\"dbt_staging\".\"info_municipios\""}
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
    identifier = "fct_meta_quatro"
    
    def __repr__(self):
        return '"postgres"."dbt_serving"."fct_meta_quatro"'


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
      'postgres.dbt_serving.fct_meta_quatro',
      df
  )