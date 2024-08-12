import pandas as pd


# fmt: off
def model(dbt, fal):
    # load
    df_dim_analfabetismo_funcional = dbt.ref("dim_analfabetismo_funcional")

    # template
    list_indicador = ['9A', '9B']

    # ind a
    df_9a = \
        (df_dim_analfabetismo_funcional
         .reindex(columns=['ANO', 'REGIOES', 'FAIXA', 'CATEGORIA', 'QUANTIDADE'])
         .query('FAIXA!="geral"')
         .astype({'ANO':'uint16','QUANTIDADE':'uint16'})
         .assign(SITUACAO='NAO_ALFABETIZADOS')
         .assign(SITUACAO=lambda x: x['SITUACAO'].where(
                     x['CATEGORIA'].isin(["ANALFABETO","ANALFABETOS_FUNCIONAIS"]),
                     'ALFABETIZADOS'))
         .drop(columns=['FAIXA','CATEGORIA'])
         .pivot_table(index=['ANO', 'REGIOES'],
                      columns=['SITUACAO'],
                      values=['QUANTIDADE'],
                      aggfunc=sum)
         .reset_index(col_level=1)
         .droplevel(level=0, axis=1)
         .rename_axis(None, axis=1)
         .assign(TOTAL=lambda x:x['ALFABETIZADOS']+x['NAO_ALFABETIZADOS'])
         .assign(ATENDIMENTO_IND=lambda x:(
                 round(x['ALFABETIZADOS']/x['TOTAL']*100,2)))
         .assign(INDICADOR=list_indicador[0])
         .reindex(columns=['ANO', "REGIOES", 'INDICADOR',
                           'ALFABETIZADOS','NAO_ALFABETIZADOS', 'TOTAL',
                           'ATENDIMENTO_IND'])
        )

    # ind c
    df_9b = \
        (df_dim_analfabetismo_funcional
         .reindex(columns=['ANO', 'REGIOES', 'FAIXA', 'CATEGORIA', 'QUANTIDADE'])
         .query('FAIXA!="geral"')
         .astype({'ANO':'uint16','QUANTIDADE':'uint16'})
         .assign(SITUACAO='NAO_ALFABETIZADOS')
         .assign(SITUACAO=lambda x: x['SITUACAO'].where(
                     x['CATEGORIA'].isin(["ANALFABETO","ANALFABETOS_FUNCIONAIS"]),
                     'ALFABETIZADOS'))
         .drop(columns=['FAIXA','CATEGORIA'])
         .pivot_table(index=['ANO', 'REGIOES'],
                      columns=['SITUACAO'],
                      values=['QUANTIDADE'],
                      aggfunc=sum)
         .reset_index(col_level=1)
         .droplevel(level=0, axis=1)
         .rename_axis(None, axis=1)
         .assign(TOTAL=lambda x:x['ALFABETIZADOS']+x['NAO_ALFABETIZADOS'])
         .assign(ATENDIMENTO_IND=lambda x:(
                 round(x['NAO_ALFABETIZADOS']/x['TOTAL']*100,2)))
         .assign(INDICADOR=list_indicador[1])
         .reindex(columns=['ANO', "REGIOES", 'INDICADOR',
                           'ALFABETIZADOS','NAO_ALFABETIZADOS', 'TOTAL',
                           'ATENDIMENTO_IND'])
        )

    # meta concat
    df_9_raw = pd.concat([df_9a, df_9b]).reset_index(drop=True)

    # meta transform
    df_9 = \
        (df_9_raw
            .reset_index(drop=True)
            .fillna(0)
            .reindex(['ANO', 'REGIOES', 'INDICADOR',
                      'ALFABETIZADOS','NAO_ALFABETIZADOS',
                      'TOTAL','ATENDIMENTO_IND'],
                    axis=1)
            .astype({'ANO':'uint16'})
            .astype({'ATENDIMENTO_IND':float})
            .sort_values(by=['ANO', 'INDICADOR','REGIOES'])
            .reset_index(drop=True)
        )
    return df_9


# This part is user provided model code
# you will need to copy the next section to run the code
# COMMAND ----------
# this part is dbt logic for get ref work, do not modify

def ref(*args, **kwargs):
    refs = {"dim_analfabetismo_funcional": "\"postgres\".\"dbt_staging\".\"dim_analfabetismo_funcional\""}
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
    identifier = "fct_meta_nove"
    
    def __repr__(self):
        return '"postgres"."dbt_serving"."fct_meta_nove"'


class dbtObj:
    def __init__(self, load_df_function) -> None:
        self.source = lambda *args: source(*args, dbt_load_df_function=load_df_function)
        self.ref = lambda *args, **kwargs: ref(*args, **kwargs, dbt_load_df_function=load_df_function)
        self.config = config
        self.this = this()
        self.is_incremental = False

# COMMAND ----------


