import pandas as pd


# fmt: off
def model(dbt, fal):
    # load
    df_dim_estadic_educ_2014 = dbt.source("raw", "DIM_ESTADIC_2014")
    df_dim_estadic_educ_2018 = dbt.source("raw", "DIM_ESTADIC_2018")
    df_dim_estadic_educ_2021 = dbt.source("raw", "DIM_ESTADIC_2021")

    cols_2014=["A1", "A208", "A225", "A228"]
    cols_2018=["COD_UF", "EEDU15", "EEDU22", "EEDU30", "EEDU35", "EEDU27",
               "EEDU261", "EEDU262", "EEDU34", "EEDU331", "EEDU332", "EEDU40",
               "EEDU391", "EEDU392", "EEDU16", "EEDU18", "EEDU20", "EEDU21"]
    cols_2021=["COD_UF", "EEDU15", "EEDU22", "EEDU30", "EEDU35", "EEDU27",
               "EEDU261", "EEDU262", "EEDU34", "EEDU331", "EEDU332", "EEDU40",
               "EEDU391", "EEDU392", "EEDU16", "EEDU18", "EEDU20", "EEDU21"]

    df_estadic_educ = (
        pd.concat(
            [(df_dim_estadic_educ_2014[cols_2014]
            .rename(columns={'A1': 'FK_ESTADO_CODIGO',
                             'A208': 'EEDU22',
                             'A225': 'EEDU30',
                             'A228': 'EEDU35',
                             'A206': 'EEDU16'})
            .assign(ANO=2014)),
            (df_dim_estadic_educ_2018[cols_2018]
            .rename(columns={'COD_UF': 'FK_ESTADO_CODIGO'})
            .assign(ANO=2018)),
            (df_dim_estadic_educ_2021[cols_2021]
            .rename(columns={'COD_UF': 'FK_ESTADO_CODIGO'})
            .assign(ANO=2021))])
        .sort_values(['ANO','FK_ESTADO_CODIGO'])
        .reset_index(drop=True)
        .reindex(['ANO', 'FK_ESTADO_CODIGO', "EEDU15", "EEDU22", "EEDU30",
                  "EEDU35", "EEDU27", "EEDU261", "EEDU262", "EEDU34",
                  "EEDU331", "EEDU332", "EEDU40", "EEDU391", "EEDU392",
                  "EEDU16", "EEDU18", "EEDU20", "EEDU21"], axis=1)
    )

    return df_estadic_educ


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
    sources = {"raw.DIM_ESTADIC_2014": "\"postgres\".\"raw\".\"DIM_ESTADIC_2014\"", "raw.DIM_ESTADIC_2018": "\"postgres\".\"raw\".\"DIM_ESTADIC_2018\"", "raw.DIM_ESTADIC_2021": "\"postgres\".\"raw\".\"DIM_ESTADIC_2021\""}
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
    identifier = "dim_estadic_educ"
    
    def __repr__(self):
        return '"postgres"."dbt_staging"."dim_estadic_educ"'


class dbtObj:
    def __init__(self, load_df_function) -> None:
        self.source = lambda *args: source(*args, dbt_load_df_function=load_df_function)
        self.ref = lambda *args, **kwargs: ref(*args, **kwargs, dbt_load_df_function=load_df_function)
        self.config = config
        self.this = this()
        self.is_incremental = False

# COMMAND ----------


