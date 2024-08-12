import pandas as pd


# fmt: off
def model(dbt, fal):
    # load
    df_municipios_raw: pd.DataFrame = dbt.ref("info_municipios")
    df_dim_educ_sup_13 = dbt.ref("dim_educ_sup_13")

    # template
    list_indicador = ['13A', '13B']
    df_ano_munic = pd.DataFrame()
    for indicador in list_indicador:
        for ano in range(2014,2022+1):
            df_temp = (df_municipios_raw[['MUNICIPIO_CODIGO', 'ESTADO_CODIGO']]
                .copy()
                .rename(columns={'MUNICIPIO_CODIGO':'FK_MUNICIPIO_CODIGO',
                                 'ESTADO_CODIGO':'FK_ESTADO_CODIGO'}))
            df_temp['ANO']=ano
            df_temp['INDICADOR']=indicador
            if df_ano_munic.shape != (0,0):
                df_ano_munic = (pd.concat([df_ano_munic, df_temp])
                                  .reset_index(drop=True))
            else:
                df_ano_munic = df_temp.copy()

    # ind a
    df_13a = (df_dim_educ_sup_13
    .rename({'CO_MUNICIPIO_IES': 'FK_MUNICIPIO_CODIGO'}, axis=1)
    .assign(INDICADOR=list_indicador[0])
    .assign(ATENDIMENTO_IND=lambda x:round((x.QT_DOC_EX_MEST+x.QT_DOC_EX_DOUT)/x.QT_DOC_EXE,4)*100)
    .reindex(columns=['ANO', 'FK_MUNICIPIO_CODIGO','INDICADOR',
                      'QT_DOC_EX_MEST', 'QT_DOC_EX_DOUT', 'QT_DOC_EXE',
                      'ATENDIMENTO_IND'])
    )

    # ind b
    df_13b = \
        (df_dim_educ_sup_13
        .rename({'CO_MUNICIPIO_IES': 'FK_MUNICIPIO_CODIGO'}, axis=1)
        .assign(INDICADOR=list_indicador[1])
        .assign(ATENDIMENTO_IND=lambda x:round((x.QT_DOC_EX_DOUT)/x.QT_DOC_EXE, 4)*100)
        .reindex(columns=['ANO', 'FK_MUNICIPIO_CODIGO','INDICADOR',
                          'QT_DOC_EX_MEST', 'QT_DOC_EX_DOUT',
                          'QT_DOC_EXE', 'ATENDIMENTO_IND'])
        )


    # meta concat
    df_13_raw = pd.concat([df_13a, df_13b]).reset_index(drop=True)

    # meta transform
    df_13 = \
    (df_13_raw
        .reset_index(drop=True)
        .merge(
            df_ano_munic[['ANO', 'FK_MUNICIPIO_CODIGO', 'INDICADOR',
                          'FK_ESTADO_CODIGO']],
            on=('ANO', 'FK_MUNICIPIO_CODIGO', 'INDICADOR'),
            how='right')
        .reindex(['ANO', 'FK_ESTADO_CODIGO',
                  'FK_MUNICIPIO_CODIGO', 'INDICADOR',
                  'QT_DOC_EXE', 'QT_DOC_EX_MEST',
                  'QT_DOC_EX_DOUT', 'ATENDIMENTO_IND'],
                 axis=1)
        .fillna(0)
        .astype({col: 'uint32' for col in ['FK_MUNICIPIO_CODIGO',
                                           'FK_ESTADO_CODIGO',
                                           'QT_DOC_EXE', 'QT_DOC_EX_MEST',
                                           'QT_DOC_EX_DOUT', ]})
        .astype({'ANO':'uint16'})
        .sort_values(by=['ANO', 'INDICADOR','FK_MUNICIPIO_CODIGO'])
        .reset_index(drop=True)
    )
    return df_13


# This part is user provided model code
# you will need to copy the next section to run the code
# COMMAND ----------
# this part is dbt logic for get ref work, do not modify

def ref(*args, **kwargs):
    refs = {"dim_educ_sup_13": "\"postgres\".\"dbt_staging\".\"dim_educ_sup_13\"", "info_municipios": "\"postgres\".\"dbt_staging\".\"info_municipios\""}
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
    identifier = "fct_meta_treze"
    
    def __repr__(self):
        return '"postgres"."dbt_serving"."fct_meta_treze"'


class dbtObj:
    def __init__(self, load_df_function) -> None:
        self.source = lambda *args: source(*args, dbt_load_df_function=load_df_function)
        self.ref = lambda *args, **kwargs: ref(*args, **kwargs, dbt_load_df_function=load_df_function)
        self.config = config
        self.this = this()
        self.is_incremental = False

# COMMAND ----------


