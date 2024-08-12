import pandas as pd


# fmt: off
def model(dbt, fal):
    # load
    df_municipios_raw: pd.DataFrame = dbt.ref("info_municipios")
    df_dim_geocapes_titulacao_2022 = dbt.source("raw", "DIM_GEOCAPES_TITULACAO_2022")

    # template
    list_indicador = ['14A', '14B']
    df_ano_munic = pd.DataFrame()
    for indicador in list_indicador:
        for ano in range(2014,2022+1):
            df_temp = (df_municipios_raw[['MUNICIPIO_CODIGO',
                                          'ESTADO_CODIGO']].copy()
                    .rename(columns={'MUNICIPIO_CODIGO':'FK_MUNICIPIO_CODIGO',
                                     'ESTADO_CODIGO':'FK_ESTADO_CODIGO'})
                    )
            df_temp['ANO']=ano
            df_temp['INDICADOR']=indicador
            if indicador=='14A':
                df_temp['GRAU_ACADEMICO']='MESTRADO'
            else:
                df_temp['GRAU_ACADEMICO']='DOUTORADO'
            if df_ano_munic.shape != (0,0):
                df_ano_munic = (pd.concat([df_ano_munic, df_temp])
                                  .reset_index(drop=True))
            else:
                df_ano_munic = df_temp.copy()

    # ind a
    df_14a = (df_dim_geocapes_titulacao_2022
        [['MUNICIPIO', 'UF', 'ANO', 'MESTRADO_TITULADO',
        "MESTRADO_PROFISSIONAL_TITULADO"]]
        # .query("ANO==2022")
        # [['MUNICIPIO', 'UF', 'ANO', 'IES']]
        .assign(MUNICIPIO=lambda x:\
                x['MUNICIPIO'].replace({"SANTA BÁRBARA D´OESTE":"SANTA BÁRBARA D'OESTE",
                                        'SANT´ANA DO LIVRAMENTO':"SANT'ANA DO LIVRAMENTO"}))
        # corrigir erros de uf_munic da base raw
        .assign(UF=lambda x:x['UF'].where(~((x['MUNICIPIO']=='PETROLINA') & (x['UF']=='BA')), 'PE'))
        .assign(UF=lambda x:x['UF'].where(~((x['MUNICIPIO']=='JOÃO PESSOA') & (x['UF']=='PE')), 'PB'))
        .assign(UF=lambda x:x['UF'].where(~((x['MUNICIPIO']=='RIO DE JANEIRO') & (x['UF']=='BA')), 'RJ'))
        # fazer merge com nome_munic e nome_estado
        .merge(df_municipios_raw
                    .applymap(lambda x: x.upper() if isinstance(x, str) else x)
                    .loc[:,['MUNICIPIO_NOME', 'ESTADO_SIGLA', 'MUNICIPIO_CODIGO']],
                left_on=['MUNICIPIO', 'UF'],
                right_on = ['MUNICIPIO_NOME', 'ESTADO_SIGLA'],
                how='left')
        .drop(columns=['MUNICIPIO', 'UF', 'MUNICIPIO_NOME', 'ESTADO_SIGLA'])
        .fillna(0)
        .assign(ATENDIMENTO_IND=lambda x:x['MESTRADO_TITULADO']+x["MESTRADO_PROFISSIONAL_TITULADO"])
        .drop(columns=['MESTRADO_TITULADO', 'MESTRADO_PROFISSIONAL_TITULADO'])
        .groupby(['ANO', 'MUNICIPIO_CODIGO']).sum('ATENDIMENTO_IND').reset_index()
        .assign(GRAU_ACADEMICO='MESTRADO')
        .assign(INDICADOR=list_indicador[0])
        .rename(columns={'MUNICIPIO_CODIGO':'FK_MUNICIPIO_CODIGO'})
        # .loc[lambda x:x['MUNICIPIO_CODIGO'].isna(), :]
        .reindex(columns=['ANO', 'FK_MUNICIPIO_CODIGO', 'INDICADOR',
                          'GRAU_ACADEMICO', 'ATENDIMENTO_IND'])
    )

    # ind b
    df_14b = \
        (df_dim_geocapes_titulacao_2022
         [['MUNICIPIO', 'UF', 'ANO', 'DOUTORADO_TITULADO',
           "DOUTORADO_PROFISSIONAL_TITULADO"]]
        .assign(MUNICIPIO=lambda x:\
                x['MUNICIPIO'].replace({"SANTA BÁRBARA D´OESTE":"SANTA BÁRBARA D'OESTE",
                                        'SANT´ANA DO LIVRAMENTO':"SANT'ANA DO LIVRAMENTO"}))
        # corrigir erros de uf_munic da base raw
        .assign(UF=lambda x:x['UF'].where(~((x['MUNICIPIO']=='PETROLINA') & (x['UF']=='BA')), 'PE'))
        .assign(UF=lambda x:x['UF'].where(~((x['MUNICIPIO']=='JOÃO PESSOA') & (x['UF']=='PE')), 'PB'))
        .assign(UF=lambda x:x['UF'].where(~((x['MUNICIPIO']=='RIO DE JANEIRO') & (x['UF']=='BA')), 'RJ'))
        # fazer merge com nome_munic e nome_estado
        .merge(df_municipios_raw
                    .applymap(lambda x: x.upper() if isinstance(x, str) else x)
                    .loc[:,['MUNICIPIO_NOME', 'ESTADO_SIGLA', 'MUNICIPIO_CODIGO']],
                left_on=['MUNICIPIO', 'UF'],
                right_on = ['MUNICIPIO_NOME', 'ESTADO_SIGLA'],
                how='left')
        .drop(columns=['MUNICIPIO', 'UF', 'MUNICIPIO_NOME', 'ESTADO_SIGLA'])
        .fillna(0)
        .assign(ATENDIMENTO_IND=lambda x:x['DOUTORADO_TITULADO']+x["DOUTORADO_PROFISSIONAL_TITULADO"])
        .drop(columns=['DOUTORADO_TITULADO', 'DOUTORADO_PROFISSIONAL_TITULADO'])
        .groupby(['ANO', 'MUNICIPIO_CODIGO']).sum('ATENDIMENTO_IND').reset_index()
        .assign(GRAU_ACADEMICO='DOUTORADO')
        .assign(INDICADOR=list_indicador[1])
        .rename(columns={'MUNICIPIO_CODIGO':'FK_MUNICIPIO_CODIGO'})
        .reindex(columns=['ANO', 'FK_MUNICIPIO_CODIGO', 'INDICADOR',
                          'GRAU_ACADEMICO', 'ATENDIMENTO_IND'])
)

    # meta concat
    df_14_raw = pd.concat([df_14a, df_14b]).reset_index(drop=True)

    # meta transform
    df_14 = \
    (df_14_raw
        .reset_index(drop=True)
        .merge(
            df_ano_munic[['ANO', 'FK_MUNICIPIO_CODIGO', 'INDICADOR',
                          'FK_ESTADO_CODIGO', 'GRAU_ACADEMICO']],
            on=('ANO', 'FK_MUNICIPIO_CODIGO', 'INDICADOR', 'GRAU_ACADEMICO'),
            how='right')
        .reindex(['ANO', 'FK_ESTADO_CODIGO',
                  'FK_MUNICIPIO_CODIGO', 'INDICADOR',
                  'GRAU_ACADEMICO', 'ATENDIMENTO_IND'],
                 axis=1)
        .fillna(0)
        .astype({col: 'uint32' for col in ['FK_MUNICIPIO_CODIGO',
                                           'FK_ESTADO_CODIGO']})
        .astype({col: 'uint16' for col in ['ANO', 'ATENDIMENTO_IND']})
        .sort_values(by=['ANO', 'INDICADOR', 'FK_MUNICIPIO_CODIGO'])
        .reset_index(drop=True)
    )
    return df_14


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
    sources = {"raw.DIM_GEOCAPES_TITULACAO_2022": "\"postgres\".\"raw\".\"DIM_GEOCAPES_TITULACAO_2022\""}
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
    identifier = "fct_meta_quatorze"
    
    def __repr__(self):
        return '"postgres"."dbt_serving"."fct_meta_quatorze"'


class dbtObj:
    def __init__(self, load_df_function) -> None:
        self.source = lambda *args: source(*args, dbt_load_df_function=load_df_function)
        self.ref = lambda *args, **kwargs: ref(*args, **kwargs, dbt_load_df_function=load_df_function)
        self.config = config
        self.this = this()
        self.is_incremental = False

# COMMAND ----------


