import pandas as pd

dict_columns_replace = {
    "Acre": 12,
    "Alagoas": 27,
    "Amapá": 16,
    "Amazonas": 13,
    "Bahia": 29,
    "Ceará": 23,
    "Distrito Federal": 53,
    "Espírito Santo": 32,
    "Goiás": 52,
    "M. G. do Sul": 21,
    "Maranhão": 51,
    "Mato Grosso": 50,
    "Minas Gerais": 31,
    "Pará": 15,
    "Paraíba": 25,
    "Paraná": 41,
    "Pernambuco": 26,
    "Piauí": 22,
    "R. G. do Norte": 24,
    "R. G. do Sul": 43,
    "Rio de Janeiro": 33,
    "Rondônia": 11,
    "Roraima": 14,
    "Santa Catarina": 42,
    "São Paulo": 35,
    "Sergipe": 28,
    "Tocantins": 17,
}

# fmt: off
def transform_ideb_2019(df_init, origem):
    return (df_init
     .reindex(['REDE','REGIAO','IDEB_2015_N_X_P','IDEB_2017_N_X_P', 'IDEB_2019_N_X_P'],axis=1)
     .query("['Sudeste','Norte','Centro-Oeste','Nordeste','Sul'] not in REGIAO")
     .query("['Total (3)(4)','Total (4)'] not in REDE")
     .assign(REDE=lambda x:x['REDE'].replace({'Pública (4)':'Pública', 'Privada (2)':'Privada'}))
     .assign(CO_UF=lambda x:x['REGIAO'].replace(dict_columns_replace))
     .drop(columns=['REGIAO'])
     .rename(columns=lambda x: x.replace('IDEB_', ''))
     .rename(columns=lambda x: x.replace('_N_X_P', ''))
     .melt(id_vars=['CO_UF','REDE'], var_name='ANO', value_name='IDEB')
     .pivot_table(
        index=["CO_UF","ANO"],
        columns=["REDE"],
        values=["IDEB"],
        aggfunc=sum)
     .reset_index(col_level=1)
     .droplevel(level=0, axis=1)
     .assign(origem=origem)
     .rename(columns=lambda x:x.upper())
     .rename(columns={'CO_UF': 'FK_ESTADO_CODIGO','PÚBLICA':'PUBLICA'})
    )

def transform_ideb_2021(df_init, origem):
    return (df_init
         .reindex(['REDE','REGIAO','VL_OBSERVADO_2021'],axis=1)
         .query("['Sudeste','Norte','Centro-Oeste','Nordeste','Sul'] not in REGIAO")
         .query("['Total (3)(4)','Total (4)','Total'] not in REDE")
         .assign(REDE=lambda x:x['REDE'].replace({'Pública (4)':'Pública', 'Privada (2)':'Privada'}))
         .assign(CO_UF=lambda x:x['REGIAO'].replace(dict_columns_replace))
         .drop(columns=['REGIAO'])
         .rename(columns=lambda x: x.replace('VL_OBSERVADO_', ''))
         .melt(id_vars=['CO_UF','REDE'], var_name='ANO', value_name='IDEB')
         .pivot_table(
            index=["CO_UF","ANO"],
            columns=["REDE"],
            values=["IDEB"],
            aggfunc=sum)
         .reset_index(col_level=1)
         .droplevel(level=0, axis=1)
         .assign(origem=origem)
         .rename(columns=lambda x:x.upper())
         .rename(columns={'CO_UF': 'FK_ESTADO_CODIGO','PÚBLICA':'PUBLICA'})
        )


def model(dbt, fal):
    # load
    df_dim_ideb_estadual_anos_iniciais_2019 = dbt.source("raw","DIM_IDEB_ESTADUAL_ANOS_INICIAIS_2019")
    df_dim_ideb_estadual_anos_iniciais_2021 = dbt.source("raw","DIM_IDEB_ESTADUAL_ANOS_INICIAIS_2021")

    df_dim_ideb_estadual_anos_finais_2019 = dbt.source("raw","DIM_IDEB_ESTADUAL_ANOS_FINAIS_2019")
    df_dim_ideb_estadual_anos_finais_2021 = dbt.source("raw","DIM_IDEB_ESTADUAL_ANOS_FINAIS_2021")

    df_dim_ideb_estadual_ensino_medio_2019 = dbt.source("raw","DIM_IDEB_ESTADUAL_ENSINO_MEDIO_2019")
    df_dim_ideb_estadual_ensino_medio_2021 = dbt.source("raw","DIM_IDEB_ESTADUAL_ENSINO_MEDIO_2021")

    df_ideb_estadual = (pd
           .concat([
               transform_ideb_2019(df_dim_ideb_estadual_anos_iniciais_2019,'anos_iniciais'),
               transform_ideb_2021(df_dim_ideb_estadual_anos_iniciais_2021,'anos_iniciais'),
               transform_ideb_2019(df_dim_ideb_estadual_anos_finais_2019,'anos_finais'),
               transform_ideb_2021(df_dim_ideb_estadual_anos_finais_2021,'anos_finais'),
               transform_ideb_2019(df_dim_ideb_estadual_ensino_medio_2019,'ensino_medio'),
               transform_ideb_2021(df_dim_ideb_estadual_ensino_medio_2021,'ensino_medio')
                   ])
           .reset_index(drop=True)
           .reindex(['ANO', 'FK_ESTADO_CODIGO', 'ORIGEM', 'ESTADUAL', 'PRIVADA', 'PUBLICA'], axis=1)
           .sort_values(by=['ANO', 'ORIGEM', 'FK_ESTADO_CODIGO'])
           .astype({col: 'uint8' for col in ['FK_ESTADO_CODIGO']})
          )
    return df_ideb_estadual


# This part is user provided model code
# you will need to copy the next section to run the code
# COMMAND ----------
# this part is dbt logic for get ref work, do not modify

def ref(*args, **kwargs):
    refs = {}
    key = '.'.join(args)
    version = kwargs.get("v") or kwargs.get("version")
    if version:
        key += f".v{version}"
    dbt_load_df_function = kwargs.get("dbt_load_df_function")
    return dbt_load_df_function(refs[key])


def source(*args, dbt_load_df_function):
    sources = {"raw.DIM_IDEB_ESTADUAL_ANOS_FINAIS_2019": "\"postgres\".\"raw\".\"DIM_IDEB_ESTADUAL_ANOS_FINAIS_2019\"", "raw.DIM_IDEB_ESTADUAL_ANOS_FINAIS_2021": "\"postgres\".\"raw\".\"DIM_IDEB_ESTADUAL_ANOS_FINAIS_2021\"", "raw.DIM_IDEB_ESTADUAL_ANOS_INICIAIS_2019": "\"postgres\".\"raw\".\"DIM_IDEB_ESTADUAL_ANOS_INICIAIS_2019\"", "raw.DIM_IDEB_ESTADUAL_ANOS_INICIAIS_2021": "\"postgres\".\"raw\".\"DIM_IDEB_ESTADUAL_ANOS_INICIAIS_2021\"", "raw.DIM_IDEB_ESTADUAL_ENSINO_MEDIO_2019": "\"postgres\".\"raw\".\"DIM_IDEB_ESTADUAL_ENSINO_MEDIO_2019\"", "raw.DIM_IDEB_ESTADUAL_ENSINO_MEDIO_2021": "\"postgres\".\"raw\".\"DIM_IDEB_ESTADUAL_ENSINO_MEDIO_2021\""}
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
    identifier = "dim_ideb_estadual"
    
    def __repr__(self):
        return '"postgres"."dbt_staging"."dim_ideb_estadual"'


class dbtObj:
    def __init__(self, load_df_function) -> None:
        self.source = lambda *args: source(*args, dbt_load_df_function=load_df_function)
        self.ref = lambda *args, **kwargs: ref(*args, **kwargs, dbt_load_df_function=load_df_function)
        self.config = config
        self.this = this()
        self.is_incremental = False

# COMMAND ----------


