import pandas as pd


# fmt: off
def transform_ideb(df_init, cols_years, origem):
    return (
        df_init[["CO_MUNICIPIO", "REDE"] + cols_years]
        .rename(columns=lambda x: x.replace("VL_OBSERVADO_", ""))
        .melt(id_vars=["CO_MUNICIPIO", "REDE"],
              var_name="ANO",
              value_name="IDEB")
        .pivot_table(
            index=["CO_MUNICIPIO", "ANO"],
            columns=["REDE"],
            values=["IDEB"],
            aggfunc=sum)
        .reset_index(col_level=1)
        .droplevel(level=0, axis=1)
        .assign(origem=origem)
        .rename(columns=lambda x: x.upper())
        .rename(columns={"CO_MUNICIPIO": "FK_MUNICIPIO_CODIGO",
                         "PÚBLICA": "PUBLICA"})
    )


# fmt: off
def model(dbt, fal):
    # load
    df_dim_ideb_anos_iniciais_2019 = dbt.source("raw","DIM_IDEB_MUNICIPAL_ANOS_INICIAIS_2019")
    df_dim_ideb_anos_iniciais_2021 = dbt.source("raw","DIM_IDEB_MUNICIPAL_ANOS_INICIAIS_2021")

    df_dim_ideb_anos_finais_2019 = dbt.source("raw","DIM_IDEB_MUNICIPAL_ANOS_FINAIS_2019")
    df_dim_ideb_anos_finais_2021 = dbt.source("raw","DIM_IDEB_MUNICIPAL_ANOS_FINAIS_2021")

    df_dim_ideb_ensino_medio_2019 = dbt.source("raw","DIM_IDEB_MUNICIPAL_ENSINO_MEDIO_2019")
    df_dim_ideb_ensino_medio_2021 = dbt.source("raw","DIM_IDEB_MUNICIPAL_ENSINO_MEDIO_2021")

    df_ideb = (pd
            .concat([
                transform_ideb(df_dim_ideb_anos_iniciais_2019,
                                ["VL_OBSERVADO_2015",
                                 "VL_OBSERVADO_2017",
                                 "VL_OBSERVADO_2019"],
                                'anos_iniciais'),
                transform_ideb(df_dim_ideb_anos_iniciais_2021,
                                ["VL_OBSERVADO_2021"],
                                'anos_iniciais'),
                transform_ideb(df_dim_ideb_anos_finais_2019,
                                ["VL_OBSERVADO_2015",
                                 "VL_OBSERVADO_2017",
                                 "VL_OBSERVADO_2019"],
                                'anos_finais'),
                transform_ideb(df_dim_ideb_anos_finais_2021,
                                ["VL_OBSERVADO_2021"],
                                'anos_finais'),
                transform_ideb(df_dim_ideb_ensino_medio_2019,
                                ["VL_OBSERVADO_2017",
                                 "VL_OBSERVADO_2019"],
                                'ensino_medio'),
                transform_ideb(df_dim_ideb_ensino_medio_2021,
                                ["VL_OBSERVADO_2021"],
                                'ensino_medio')
                    ])
            .reset_index(drop=True)
            .reindex(['ANO', 'FK_MUNICIPIO_CODIGO', 'ORIGEM', 'MUNICIPAL',
                      'ESTADUAL', 'FEDERAL', 'PUBLICA'], axis=1)
            .sort_values(by=['ANO', 'ORIGEM', 'FK_MUNICIPIO_CODIGO'])
            .astype({col: 'uint32' for col in ['FK_MUNICIPIO_CODIGO']})
            )

    return df_ideb


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
    sources = {"raw.DIM_IDEB_MUNICIPAL_ANOS_FINAIS_2019": "\"postgres\".\"raw\".\"DIM_IDEB_MUNICIPAL_ANOS_FINAIS_2019\"", "raw.DIM_IDEB_MUNICIPAL_ANOS_FINAIS_2021": "\"postgres\".\"raw\".\"DIM_IDEB_MUNICIPAL_ANOS_FINAIS_2021\"", "raw.DIM_IDEB_MUNICIPAL_ANOS_INICIAIS_2019": "\"postgres\".\"raw\".\"DIM_IDEB_MUNICIPAL_ANOS_INICIAIS_2019\"", "raw.DIM_IDEB_MUNICIPAL_ANOS_INICIAIS_2021": "\"postgres\".\"raw\".\"DIM_IDEB_MUNICIPAL_ANOS_INICIAIS_2021\"", "raw.DIM_IDEB_MUNICIPAL_ENSINO_MEDIO_2019": "\"postgres\".\"raw\".\"DIM_IDEB_MUNICIPAL_ENSINO_MEDIO_2019\"", "raw.DIM_IDEB_MUNICIPAL_ENSINO_MEDIO_2021": "\"postgres\".\"raw\".\"DIM_IDEB_MUNICIPAL_ENSINO_MEDIO_2021\""}
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
    identifier = "dim_ideb_municipal"
    
    def __repr__(self):
        return '"postgres"."dbt_staging"."dim_ideb_municipal"'


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
      'postgres.dbt_staging.dim_ideb_municipal',
      df
  )