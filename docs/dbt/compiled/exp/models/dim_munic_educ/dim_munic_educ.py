import pandas as pd


# fmt: off
def model(dbt, fal):
    # load
    df_dim_munic_educ_2014 = dbt.source("raw","DIM_MUNIC_EDUC_2014")
    df_dim_munic_educ_2018 = dbt.source("raw","DIM_MUNIC_EDUC_2018")
    df_dim_munic_educ_2021 = dbt.source("raw","DIM_MUNIC_EDUC_2021")

    cols_2014=["A1","A205", "A245", "A246", "A247", "A248","A207", "A224", "A227", "A235"]
    cols_2018=["COD_MUNICIPIO","MEDU16", "MEDU18", "MEDU21", "MEDU491",
               "MEDU49211", "MEDU492", "MEDU49214", "MEDU49212", "MEDU49213",
               "MEDU117","MEDU27", "MEDU261", "MEDU262", "MEDU34", "MEDU331", "MEDU332", "MEDU40", "MEDU391", "MEDU392", "MEDU22", "MEDU30", "MEDU35", "MEDU41"]
    cols_2021=["CODMUN","MEDU16", "MEDU18", "MEDU21", "MEDU491", "MEDU49211",
               "MEDU492", "MEDU49214", "MEDU49212", "MEDU49213", "MEDU117","MEDU27", "MEDU261", "MEDU262", "MEDU34", "MEDU331", "MEDU332", "MEDU40", "MEDU391", "MEDU392", "MEDU22", "MEDU30", "MEDU35", "MEDU41","MEDU20A"]

    df_munic_educ = (
        pd.concat(
            [(df_dim_munic_educ_2014[cols_2014]
              .rename(columns={'A1':'FK_MUNICIPIO_CODIGO',
                               'A205':'MEDU16',
                               'A245':'MEDU491',
                               'A246':'MEDU49211',
                               'A247':'MEDU492',
                               'A248':'MEDU49214',
                               'A207':'MEDU22',
                               'A224':'MEDU30',
                               'A227':'MEDU35',
                               'A235':'MEDU41'})
              .assign(ANO=2014)),
             (df_dim_munic_educ_2018[cols_2018]
              .rename(columns={'COD_MUNICIPIO':'FK_MUNICIPIO_CODIGO'})
              .assign(ANO=2018)),
             (df_dim_munic_educ_2021[cols_2021]
              .rename(columns={'CODMUN':'FK_MUNICIPIO_CODIGO'})
              .assign(ANO=2021))])
        .sort_values(['ANO','FK_MUNICIPIO_CODIGO'])
        .reindex(['ANO', 'FK_MUNICIPIO_CODIGO', 'MEDU16', 'MEDU18', 'MEDU21',
                'MEDU491', 'MEDU49211', 'MEDU492', 'MEDU49214',
                'MEDU49212', 'MEDU49213', 'MEDU117', 'MEDU27', 'MEDU261',
                'MEDU262', 'MEDU34', 'MEDU331', 'MEDU332', 'MEDU40', 'MEDU391',
                'MEDU392', 'MEDU20A', 'MEDU22', 'MEDU30', 'MEDU35', 'MEDU41'], axis=1)
        )

    return df_munic_educ


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
    sources = {"raw.DIM_MUNIC_EDUC_2014": "\"postgres\".\"raw\".\"DIM_MUNIC_EDUC_2014\"", "raw.DIM_MUNIC_EDUC_2018": "\"postgres\".\"raw\".\"DIM_MUNIC_EDUC_2018\"", "raw.DIM_MUNIC_EDUC_2021": "\"postgres\".\"raw\".\"DIM_MUNIC_EDUC_2021\""}
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
    identifier = "dim_munic_educ"
    
    def __repr__(self):
        return '"postgres"."dbt_staging"."dim_munic_educ"'


class dbtObj:
    def __init__(self, load_df_function) -> None:
        self.source = lambda *args: source(*args, dbt_load_df_function=load_df_function)
        self.ref = lambda *args, **kwargs: ref(*args, **kwargs, dbt_load_df_function=load_df_function)
        self.config = config
        self.this = this()
        self.is_incremental = False

# COMMAND ----------


