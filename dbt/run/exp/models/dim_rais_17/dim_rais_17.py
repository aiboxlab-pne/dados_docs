import numpy as np
import pandas as pd
import unidecode


# fmt: off
def model(dbt, fal):

    # load
    df_municipios_staging: pd.DataFrame = dbt.ref("info_municipios")
    df_dim_rais_professores_publicos_graduados_2014_2022: pd.DataFrame = dbt.source("raw", "DIM_RAIS_PROFESSORES_PUBLICOS_GRADUADOS_2014_2022")
    df_dim_rais_profissionais_graduados_2014_2022: pd.DataFrame = dbt.source("raw", "DIM_RAIS_PROFISSIONAIS_GRADUADOS_2014_2022")

    dict_replace={
        "AL-OLHO D AGUA DAS FLORES": "AL-OLHO D'AGUA DAS FLORES",
        "AL-OLHO D AGUA DO CASADO": "AL-OLHO D'AGUA DO CASADO",
        "AL-OLHO D AGUA GRANDE": "AL-OLHO D'AGUA GRANDE",
        "AL-TANQUE D ARCA": "AL-TANQUE D'ARCA",
        "BA-DIAS D AVILA": "BA-DIAS D'AVILA",
        "BA-MUQUEM DE SAO FRANCISCO": "BA-MUQUEM DO SAO FRANCISCO",
        "BA-SANTA TERESINHA": "BA-SANTA TEREZINHA",
        "GO-SAO JOAO D ALIANCA": "GO-SAO JOAO D'ALIANCA",
        "GO-SITIO D ABADIA": "GO-SITIO D'ABADIA",
        "MA-OLHO D AGUA DAS CUNHAS": "MA-OLHO D'AGUA DAS CUNHAS",
        "MG-DONA EUSEBIA": "MG-DONA EUZEBIA",
        "MG-OLHOS-D AGUA": "MG-OLHOS-D'AGUA",
        "MG-PASSA-VINTE": "MG-PASSA VINTE",
        "MG-PINGO-D AGUA": "MG-PINGO-D'AGUA",
        "MG-SAO THOME DAS LETRAS": "MG-SAO TOME DAS LETRAS",
        "MT-CONQUISTA D OESTE": "MT-CONQUISTA D'OESTE",
        "MT-FIGUEIROPOLIS D OESTE": "MT-FIGUEIROPOLIS D'OESTE",
        "MT-GLORIA D OESTE": "MT-GLORIA D'OESTE",
        "MT-LAMBARI D OESTE": "MT-LAMBARI D'OESTE",
        "MT-MIRASSOL D OESTE": "MT-MIRASSOL D'OESTE",
        "MT-POXOREO": "MT-POXOREU",
        "MT-SANTO ANTONIO DO LEVERGER": "MT-SANTO ANTONIO DE LEVERGER",
        "PA-PAU D ARCO": "PA-PAU D'ARCO",
        "PB-MAE D AGUA": "PB-MAE D'AGUA",
        "PB-OLHO D AGUA": "PB-OLHO D'AGUA",
        "PE-BELEM DE SAO FRANCISCO": "PE-BELEM DO SAO FRANCISCO",
        "PE-LAGOA DO ITAENGA": "PE-LAGOA DE ITAENGA",
        "PI-BARRA D ALCANTARA": "PI-BARRA D'ALCANTARA",
        "PI-OLHO D AGUA DO PIAUI": "PI-OLHO D'AGUA DO PIAUI",
        "PI-PAU D ARCO DO PIAUI": "PI-PAU D'ARCO DO PIAUI",
        "PR-DIAMANTE D OESTE": "PR-DIAMANTE D'OESTE",
        "PR-ITAPEJARA D OESTE": "PR-ITAPEJARA D'OESTE",
        "PR-PEROLA D OESTE": "PR-PEROLA D'OESTE",
        "PR-RANCHO ALEGRE D OESTE": "PR-RANCHO ALEGRE D'OESTE",
        "PR-SAO JORGE D OESTE": "PR-SAO JORGE D'OESTE",
        "RN-AUGUSTO SEVERO": "RN-CAMPO GRANDE",
        "RN-LAGOA D ANTA": "RN-LAGOA D'ANTA",
        "RN-OLHO-D AGUA DO BORGES": "RN-OLHO D'AGUA DO BORGES",
        "RO-ALTA FLORESTA D OESTE": "RO-ALTA FLORESTA D'OESTE",
        "RO-ALVORADA D OESTE": "RO-ALVORADA D'OESTE",
        "RO-ESPIGAO D OESTE": "RO-ESPIGAO D'OESTE",
        "RO-MACHADINHO D OESTE": "RO-MACHADINHO D'OESTE",
        "RO-NOVA BRASILANDIA D OESTE": "RO-NOVA BRASILANDIA D'OESTE",
        "RO-SANTA LUZIA D OESTE": "RO-SANTA LUZIA D'OESTE",
        "RO-SAO FELIPE D OESTE": "RO-SAO FELIPE D'OESTE",
        "RS - PINTO BANDEIRA": "RS-PINTO BANDEIRA",
        "RS-SANT ANA DO LIVRAMENTO": "RS-SANT'ANA DO LIVRAMENTO",
        "SC-GRAO PARA": "SC-GRAO-PARA",
        "SC-HERVAL D OESTE": "SC-HERVAL D'OESTE",
        "SE-AMPARO DE SAO FRANCISCO": "SE-AMPARO DO SAO FRANCISCO",
        "SE-ITAPORANGA D AJUDA": "SE-ITAPORANGA D'AJUDA",
        "SP-APARECIDA D OESTE": "SP-APARECIDA D'OESTE",
        "SP-BIRITIBA-MIRIM": "SP-BIRITIBA MIRIM",
        "SP-ESTRELA D OESTE": "SP-ESTRELA D'OESTE",
        "SP-FLORINIA": "SP-FLORINEA",
        "SP-GUARANI D OESTE": "SP-GUARANI D'OESTE",
        "SP-PALMEIRA D OESTE": "SP-PALMEIRA D'OESTE",
        "SP-SANTA BARBARA D OESTE": "SP-SANTA BARBARA D'OESTE",
        "SP-SANTA CLARA D OESTE": "SP-SANTA CLARA D'OESTE",
        "SP-SANTA RITA D OESTE": "SP-SANTA RITA D'OESTE",
        "SP-SAO JOAO DO PAU D ALHO": "SP-SAO JOAO DO PAU D'ALHO",
        "SP-SAO LUIS DO PARAITINGA": "SP-SAO LUIZ DO PARAITINGA",
        "TO-FORTALEZA DO TABOCAO": "TO-TABOCAO",
        "TO-PAU D ARCO": "TO-PAU D'ARCO"
    }

    df_staging_17 = \
        (df_dim_rais_profissionais_graduados_2014_2022
         .iloc[:, 1:]
         .query('MUNICIPIO!="Total" and MUNICIPIO!="{ñ class}"')
         .melt(id_vars=['MUNICIPIO'],
               value_vars=['2022', '2021', '2020', '2019', '2018', '2017',
                           '2016', '2015', '2014'],
               var_name='ANO',
               value_name='RENDIMENTO_GRADUADOS')
         .assign(RENDIMENTO_GRADUADOS=
                 lambda x: x['RENDIMENTO_GRADUADOS'].str.replace(',', '.').astype(np.float64))
         .merge((df_dim_rais_professores_publicos_graduados_2014_2022
                 .iloc[:, 1:]
                 .query('MUNICIPIO!="Total" and MUNICIPIO!="{ñ class}"')
                 .melt(id_vars=['MUNICIPIO'],
                       value_vars=['2022', '2021', '2020', '2019', '2018',
                                   '2017', '2016', '2015', '2014'],
                       var_name='ANO',
                       value_name='RENDIMENTO_PROF_PUBLICOS_GRADUADOS')
                 .assign(RENDIMENTO_PROF_PUBLICOS_GRADUADOS=
                         lambda x: x['RENDIMENTO_PROF_PUBLICOS_GRADUADOS'].str.replace(',', '.').astype(np.float64))),
                on=['MUNICIPIO', 'ANO'], how='left')
         .rename(columns={"MUNICIPIO": 'MUNICIPIO_NOME'})
         .assign(MUNICIPIO_NOME=lambda x: x['MUNICIPIO_NOME'].replace(dict_replace))
         .merge((df_municipios_staging[['MUNICIPIO_CODIGO', 'MUNICIPIO_NOME', 'ESTADO_SIGLA']]
                 .assign(MUNICIPIO_NOME=
                         lambda x: x['ESTADO_SIGLA'] + "-" + x['MUNICIPIO_NOME'].str.upper())
                 .reindex(columns=['MUNICIPIO_CODIGO', 'MUNICIPIO_NOME'])
                 .assign(MUNICIPIO_NOME=
                         lambda x: x['MUNICIPIO_NOME'].apply(unidecode.unidecode))),
                on=['MUNICIPIO_NOME'],
                how='left')
         .assign(**{col: lambda x, col=col:
                 x[col].round(2) for col in ['RENDIMENTO_PROF_PUBLICOS_GRADUADOS',
                                             'RENDIMENTO_GRADUADOS']})
         .rename(columns={"MUNICIPIO_CODIGO": 'FK_MUNICIPIO_CODIGO'})
         .reindex(columns=['ANO', 'FK_MUNICIPIO_CODIGO',
                           'RENDIMENTO_PROF_PUBLICOS_GRADUADOS',
                           'RENDIMENTO_GRADUADOS'])
         )
    return df_staging_17


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
    sources = {"raw.DIM_RAIS_PROFESSORES_PUBLICOS_GRADUADOS_2014_2022": "\"postgres\".\"raw\".\"DIM_RAIS_PROFESSORES_PUBLICOS_GRADUADOS_2014_2022\"", "raw.DIM_RAIS_PROFISSIONAIS_GRADUADOS_2014_2022": "\"postgres\".\"raw\".\"DIM_RAIS_PROFISSIONAIS_GRADUADOS_2014_2022\""}
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
    schema = "dbt_staging"
    identifier = "dim_rais_17"
    
    def __repr__(self):
        return '"postgres"."dbt_staging"."dim_rais_17"'


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
      'postgres.dbt_staging.dim_rais_17',
      df
  )