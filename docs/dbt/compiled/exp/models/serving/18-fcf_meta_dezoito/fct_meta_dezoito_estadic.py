import numpy as np
import pandas as pd


# fmt: off
def model(dbt, fal):
    # load
    df_dim_estadic_educ = dbt.ref("dim_estadic_educ")

    # template
    list_indicador_estadic = ['18A','18B','18C','18D']

    # ind a
    df_18a = \
    (df_dim_estadic_educ
        .reindex(columns=['ANO','FK_ESTADO_CODIGO','EEDU16'])
        .assign(INDICADOR=list_indicador_estadic[0])
        .rename(columns={'EEDU16':'ATENDIMENTO_IND'})
        .assign(ATENDIMENTO_IND=lambda x:
            x['ATENDIMENTO_IND'].replace({'Sim':1, np.nan:-1,'Não':0}))
        .astype({'ATENDIMENTO_IND':np.int8})
        .reindex(columns=['ANO', 'FK_ESTADO_CODIGO',
                          'INDICADOR','ATENDIMENTO_IND'])
        )

    # ind b
    df_18b = \
    (df_dim_estadic_educ
        .reindex(columns=['ANO','FK_ESTADO_CODIGO',
                          'EEDU18'])
        .assign(INDICADOR=list_indicador_estadic[1])
        .rename(columns={'EEDU18':'ATENDIMENTO_IND'})
        .assign(ATENDIMENTO_IND=lambda x:
            x['ATENDIMENTO_IND'].replace({'Sim':1, np.nan:-1,'Não':0}))
        .astype({'ATENDIMENTO_IND':np.int8})
        .reindex(columns=['ANO', 'FK_ESTADO_CODIGO',
                          'INDICADOR', 'ATENDIMENTO_IND'])
        )

    # ind c
    df_18c = \
    (df_dim_estadic_educ
        .reindex(columns=['ANO','FK_ESTADO_CODIGO',
                          'EEDU20'])
        .assign(INDICADOR=list_indicador_estadic[2])
        .rename(columns={'EEDU20':'ATENDIMENTO_IND'})
        .assign(ATENDIMENTO_IND=lambda x:
            x['ATENDIMENTO_IND'].replace({'Sim':1, np.nan:-1,'Não':0}))
        .astype({'ATENDIMENTO_IND':np.int8})
        .reindex(columns=['ANO', 'FK_ESTADO_CODIGO',
                          'INDICADOR', 'ATENDIMENTO_IND'])
        )

    # ind d
    df_18d = \
    (df_dim_estadic_educ
        .reindex(columns=['ANO','FK_ESTADO_CODIGO',
                          'EEDU21'])
        .assign(INDICADOR=list_indicador_estadic[3])
        .rename(columns={'EEDU21':'ATENDIMENTO_IND'})
        .assign(ATENDIMENTO_IND=lambda x:
            x['ATENDIMENTO_IND'].replace({'Sim':1, np.nan:-1,'Não':0}))
        .astype({'ATENDIMENTO_IND':np.int8})
        .reindex(columns=['ANO', 'FK_ESTADO_CODIGO',
                          'INDICADOR','ATENDIMENTO_IND'])
        )

    # meta concat
    df_18_estadic_raw = pd.concat([df_18a, df_18b,
                                   df_18c, df_18d]).reset_index(drop=True)

    # meta transform
    df_18_estadic = \
        (df_18_estadic_raw
            .reset_index(drop=True)
            .reindex(['ANO', 'FK_ESTADO_CODIGO', 'INDICADOR',
                      'ATENDIMENTO_IND'],
                    axis=1)
            .fillna(0)
            .astype({col: 'uint32' for col in ['FK_ESTADO_CODIGO']})
            .astype({'ANO':'uint16'})
            .sort_values(by=['ANO', 'INDICADOR', 'FK_ESTADO_CODIGO'])
            .reset_index(drop=True))
    return df_18_estadic


# This part is user provided model code
# you will need to copy the next section to run the code
# COMMAND ----------
# this part is dbt logic for get ref work, do not modify

def ref(*args, **kwargs):
    refs = {"dim_estadic_educ": "\"postgres\".\"dbt_staging\".\"dim_estadic_educ\""}
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
    identifier = "fct_meta_dezoito_estadic"
    
    def __repr__(self):
        return '"postgres"."dbt_serving"."fct_meta_dezoito_estadic"'


class dbtObj:
    def __init__(self, load_df_function) -> None:
        self.source = lambda *args: source(*args, dbt_load_df_function=load_df_function)
        self.ref = lambda *args, **kwargs: ref(*args, **kwargs, dbt_load_df_function=load_df_function)
        self.config = config
        self.this = this()
        self.is_incremental = False

# COMMAND ----------


