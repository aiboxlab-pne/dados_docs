import numpy as np
import pandas as pd


# fmt: off
def model(dbt, fal):
    # load
    df_municipios_raw: pd.DataFrame = dbt.ref("info_municipios")
    df_dim_munic_educ = dbt.ref("dim_munic_educ")
    df_dim_educ_bas_escola_19 = dbt.ref("dim_educ_bas_escola_19")
    df_dim_educ_bas_gestor_19 = dbt.ref("dim_educ_bas_gestor_19")

    # template
    list_indicador_munic = ['19A','19B','19E','19F']

    df_ano_munic = pd.DataFrame()
    for indicador in list_indicador_munic:
        for ano in range(2014,2021+1):
            df_temp = (df_municipios_raw[['MUNICIPIO_CODIGO',
                                          'ESTADO_CODIGO']].copy()
                    .rename(columns={'MUNICIPIO_CODIGO':'FK_MUNICIPIO_CODIGO',
                                     'ESTADO_CODIGO':'FK_ESTADO_CODIGO'}))
            df_temp['ANO']=ano
            df_temp['INDICADOR']=indicador
            if df_ano_munic.shape != (0,0):
                df_ano_munic = pd.concat([df_ano_munic, df_temp]).reset_index(drop=True)
            else:
                df_ano_munic = df_temp.copy()

    # ind a
    df_19a = \
    (df_dim_educ_bas_gestor_19
        .reindex(columns=['NU_ANO_CENSO', 'CO_MUNICIPIO', 'TP_DEPENDENCIA',
                          'TP_CARGO_GESTOR', 'TP_TIPO_ACESSO_CARGO'])
        .query('TP_DEPENDENCIA!=4 and TP_CARGO_GESTOR==1')
        .assign(INDICADOR=list_indicador_munic[0])
        .rename(columns={'NU_ANO_CENSO':'ANO',
                         'CO_MUNICIPIO':'FK_MUNICIPIO_CODIGO'})
        .assign(QTD_DIRETORES=1)
        .assign(QTD_DIRETORES_ELEITOS=1)
        .assign(QTD_DIRETORES_ELEITOS=\
                lambda x:x['QTD_DIRETORES_ELEITOS']
                .where(x['TP_TIPO_ACESSO_CARGO'].isin([6]), 0))
        .reindex(columns=['ANO', 'FK_MUNICIPIO_CODIGO', 'INDICADOR',
                          'QTD_DIRETORES', 'QTD_DIRETORES_ELEITOS'])
        .groupby(['ANO', 'FK_MUNICIPIO_CODIGO', 'INDICADOR']).sum().reset_index()
        .assign(ATENDIMENTO_IND=lambda x:round(x['QTD_DIRETORES_ELEITOS']/x['QTD_DIRETORES'],4)*100)
        .reindex(columns=['ANO', 'FK_MUNICIPIO_CODIGO','INDICADOR', 'QTD_DIRETORES_ELEITOS',
                          'QTD_DIRETORES', 'ATENDIMENTO_IND'])
        )

    # ind b
    df_19b = \
    (df_dim_educ_bas_escola_19
        .rename(columns={'NU_ANO_CENSO':'ANO', 'CO_MUNICIPIO':'FK_MUNICIPIO_CODIGO'})
        .query('TP_DEPENDENCIA!=4 and TP_SITUACAO_FUNCIONAMENTO==1')
        .drop(columns=['TP_DEPENDENCIA','TP_SITUACAO_FUNCIONAMENTO'])
        .replace({9:0})
        .assign(QTD_COLEGIADOS_POR_ESCOLA=lambda x:
                x[['IN_ORGAO_ASS_PAIS', 'IN_ORGAO_ASS_PAIS_MESTRES',
                   'IN_ORGAO_CONSELHO_ESCOLAR',
                   'IN_ORGAO_GREMIO_ESTUDANTIL']].sum(axis=1))
        .assign(QTD_COLEGIADOS_POR_ESCOLA=lambda x:
                x['QTD_COLEGIADOS_POR_ESCOLA'].where(
                    x['QTD_COLEGIADOS_POR_ESCOLA']<=3,3))
        .assign(QTD_COLEGIADOS_POSSIVEL_POR_ESCOLA=3)
        .reindex(columns=["ANO","FK_MUNICIPIO_CODIGO",
                          "QTD_COLEGIADOS_POR_ESCOLA",
                          "QTD_COLEGIADOS_POSSIVEL_POR_ESCOLA"])
        .groupby(['ANO','FK_MUNICIPIO_CODIGO']).sum().reset_index()
        .assign(ATENDIMENTO_IND=lambda x:
                round(x['QTD_COLEGIADOS_POR_ESCOLA']/
                      x['QTD_COLEGIADOS_POSSIVEL_POR_ESCOLA'],4)*100)
        .assign(INDICADOR=list_indicador_munic[1])
        .reindex(columns=['ANO', 'FK_MUNICIPIO_CODIGO','INDICADOR',
                          'QTD_COLEGIADOS_POR_ESCOLA', 'QTD_COLEGIADOS_POSSIVEL_POR_ESCOLA',
                          'ATENDIMENTO_IND'])
        )

    # ind c
    df_19e = \
    (df_dim_munic_educ
        .reindex(columns=['ANO', 'FK_MUNICIPIO_CODIGO','MEDU41','MEDU22','MEDU30','MEDU35'])
        .replace({'Não':0, np.nan:0, 'Sim':1,'Não informado':0,
                  'Recusa':0, 'Não informou':0})
        .assign(QTD_CONSELHOS=lambda x:
                x[['MEDU41', 'MEDU22', 'MEDU30', 'MEDU35']].sum(axis=1))
        .assign(QTD_CONSELHOS_MAX=4)
        .assign(ATENDIMENTO_IND=lambda x:
                round(x['QTD_CONSELHOS']/
                    x['QTD_CONSELHOS_MAX'],4)*100)
        .assign(INDICADOR=list_indicador_munic[2])
        .reindex(columns=['ANO', 'FK_MUNICIPIO_CODIGO','INDICADOR',
                          'QTD_CONSELHOS', 'QTD_CONSELHOS_MAX',
                          'ATENDIMENTO_IND'])
        )

    # ind d
    df_19f = \
    (df_dim_munic_educ
        .reindex(columns=['ANO', 'FK_MUNICIPIO_CODIGO','MEDU27','MEDU261',
                          'MEDU262','MEDU34','MEDU331','MEDU332','MEDU40',
                          'MEDU391','MEDU392'])
        .replace({'Não':0,np.nan:0,'Sim':1,'Não informado':0, 'Recusa':0,
                  'Não informou':0,'-':0,'(*) Não soube informar':0})
        .assign(QTD_ESTRUTURA_DISPONIBILIZADA=lambda x:
                x[['MEDU27','MEDU261','MEDU262','MEDU34','MEDU331',
                   'MEDU332','MEDU40', 'MEDU391','MEDU392']].sum(axis=1))
        .assign(QTD_ESTRUTURA_MAX=9)
        .assign(ATENDIMENTO_IND=lambda x:
                round(x['QTD_ESTRUTURA_DISPONIBILIZADA']/
                      x['QTD_ESTRUTURA_MAX'],4)*100)
        .assign(INDICADOR=list_indicador_munic[3])
        .reindex(columns=['ANO', 'FK_MUNICIPIO_CODIGO','INDICADOR',
                          'QTD_ESTRUTURA_DISPONIBILIZADA', 'QTD_ESTRUTURA_MAX',
                          'ATENDIMENTO_IND'])
        )


    # meta concat
    df_19_munic_raw = pd.concat([df_19a, df_19b,
                                 df_19e, df_19f]).reset_index(drop=True)

    # meta transform
    df_19_munic = \
        (df_19_munic_raw
            .reset_index(drop=True)
            .merge(
                df_ano_munic[['ANO', 'FK_MUNICIPIO_CODIGO', 'INDICADOR',
                              'FK_ESTADO_CODIGO']],
                on=('ANO', 'FK_MUNICIPIO_CODIGO', 'INDICADOR'),
                how='right')
            .reindex(['ANO', 'FK_ESTADO_CODIGO', 'FK_MUNICIPIO_CODIGO',
                      'INDICADOR', 'QTD_DIRETORES_ELEITOS', 'QTD_DIRETORES',
                      'QTD_COLEGIADOS_POR_ESCOLA',
                      'QTD_COLEGIADOS_POSSIVEL_POR_ESCOLA', 'QTD_CONSELHOS',
                      'QTD_CONSELHOS_MAX', 'QTD_ESTRUTURA_DISPONIBILIZADA',
                      'QTD_ESTRUTURA_MAX', 'ATENDIMENTO_IND'],
                    axis=1)
            .fillna(0)
            .astype({col: 'uint32' for col in ['FK_MUNICIPIO_CODIGO',
                                               'FK_ESTADO_CODIGO']})
            .astype({'ANO':'uint16'})
            .sort_values(by=['ANO', 'INDICADOR', 'FK_MUNICIPIO_CODIGO'])
            .reset_index(drop=True)
        )
    return df_19_munic


# This part is user provided model code
# you will need to copy the next section to run the code
# COMMAND ----------
# this part is dbt logic for get ref work, do not modify

def ref(*args, **kwargs):
    refs = {"dim_educ_bas_escola_19": "\"postgres\".\"dbt_staging\".\"dim_educ_bas_escola_19\"", "dim_educ_bas_gestor_19": "\"postgres\".\"dbt_staging\".\"dim_educ_bas_gestor_19\"", "dim_munic_educ": "\"postgres\".\"dbt_staging\".\"dim_munic_educ\"", "info_municipios": "\"postgres\".\"dbt_staging\".\"info_municipios\""}
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
    identifier = "fct_meta_dezenove_munic"
    
    def __repr__(self):
        return '"postgres"."dbt_serving"."fct_meta_dezenove_munic"'


class dbtObj:
    def __init__(self, load_df_function) -> None:
        self.source = lambda *args: source(*args, dbt_load_df_function=load_df_function)
        self.ref = lambda *args, **kwargs: ref(*args, **kwargs, dbt_load_df_function=load_df_function)
        self.config = config
        self.this = this()
        self.is_incremental = False

# COMMAND ----------


