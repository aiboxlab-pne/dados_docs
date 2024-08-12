import numpy as np
import pandas as pd


# fmt: off
def model(dbt, fal):
    # load
    df_dim_estadic_educ = dbt.ref("dim_estadic_educ")

    # template
    list_indicador_estadic = ['19C','19D']

    # ind c
    df_19c = \
    (df_dim_estadic_educ
        .reindex(columns=['ANO','FK_ESTADO_CODIGO','EEDU15','EEDU22','EEDU30','EEDU35'])
        .replace({'Não':0,np.nan:0,'Sim':1,
                  'Não informado':0, 'Recusa':0, 'Não informou':0})
        .assign(QTD_CONSELHOS=lambda x:
                x[['EEDU15','EEDU22','EEDU30','EEDU35']].sum(axis=1))
        .assign(QTD_CONSELHOS_MAX=4)
        .assign(ATENDIMENTO_IND=lambda x:
                round(x['QTD_CONSELHOS']/
                      x['QTD_CONSELHOS_MAX'],4)*100)
        .assign(INDICADOR=list_indicador_estadic[0])
        .reindex(columns=['ANO', 'FK_ESTADO_CODIGO','INDICADOR',
                          'QTD_CONSELHOS', 'QTD_CONSELHOS_MAX',
                          'ATENDIMENTO_IND'])
        )

    # ind d
    df_19d = \
    (df_dim_estadic_educ
        .reindex(columns=['ANO','FK_ESTADO_CODIGO','EEDU27','EEDU261','EEDU262','EEDU34',
                          'EEDU331','EEDU332','EEDU40','EEDU391','EEDU392'])
        .replace({'Não':0,np.nan:0,'Sim':1,'Não informado':0, 'Recusa':0,
                  'Não informou':0,'-':0,'(*) Não soube informar':0})
        .assign(QTD_ESTRUTURA_DISPONIBILIZADA=lambda x:
                x[['EEDU27','EEDU261','EEDU262','EEDU34','EEDU331','EEDU332','EEDU40',
                   'EEDU391','EEDU392']].sum(axis=1))
        .assign(QTD_MAX_ESTRUTURA_DISPONIBILIZADA=9)
        .assign(ATENDIMENTO_IND=lambda x:
                round(x['QTD_ESTRUTURA_DISPONIBILIZADA']/
                      x['QTD_MAX_ESTRUTURA_DISPONIBILIZADA'],4)*100)
        .assign(INDICADOR=list_indicador_estadic[1])
        .reindex(columns=['ANO', 'FK_ESTADO_CODIGO','INDICADOR',
                          'QTD_ESTRUTURA_DISPONIBILIZADA', 'QTD_MAX_ESTRUTURA_DISPONIBILIZADA',
                          'ATENDIMENTO_IND'])
        )

    # meta concat
    df_19_estadic_raw = pd.concat([df_19c, df_19d]).reset_index(drop=True)

    # meta transform
    df_19_estadic = \
        (df_19_estadic_raw
            .reset_index(drop=True)
            .reindex(['ANO', 'FK_ESTADO_CODIGO', 'FK_MUNICIPIO_CODIGO', 'INDICADOR',
                      'QTD_CONSELHOS', 'QTD_CONSELHOS_MAX', 'QTD_ESTRUTURA_DISPONIBILIZADA',
                      'QTD_MAX_ESTRUTURA_DISPONIBILIZADA', 'ATENDIMENTO_IND'],
                    axis=1)
            .fillna(0)
            .astype({col: 'uint32' for col in ['FK_ESTADO_CODIGO']})
            .astype({col: 'uint16' for col in ['QTD_CONSELHOS', 'QTD_CONSELHOS_MAX',
                                               'QTD_ESTRUTURA_DISPONIBILIZADA',
                                               'QTD_MAX_ESTRUTURA_DISPONIBILIZADA']})
            .astype({'ANO':'uint16'})
            .sort_values(by=['ANO', 'INDICADOR', 'FK_ESTADO_CODIGO'])
            .reset_index(drop=True)
        )
    return df_19_estadic


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
    identifier = "fct_meta_dezenove_estadic"
    
    def __repr__(self):
        return '"postgres"."dbt_serving"."fct_meta_dezenove_estadic"'


class dbtObj:
    def __init__(self, load_df_function) -> None:
        self.source = lambda *args: source(*args, dbt_load_df_function=load_df_function)
        self.ref = lambda *args, **kwargs: ref(*args, **kwargs, dbt_load_df_function=load_df_function)
        self.config = config
        self.this = this()
        self.is_incremental = False

# COMMAND ----------


