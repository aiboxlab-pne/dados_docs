import numpy as np
import pandas as pd

cols_disciplinas = [
    "IN_DISC_LINGUA_PORTUGUESA",
    "IN_DISC_LINGUA_INGLES",
    "IN_DISC_LINGUA_ESPANHOL",
    "IN_DISC_LINGUA_FRANCES",
    "IN_DISC_LINGUA_OUTRA",
    "IN_DISC_ARTES",
    "IN_DISC_EDUCACAO_FISICA",
    "IN_DISC_MATEMATICA",
    "IN_DISC_CIENCIAS",
    "IN_DISC_QUIMICA",
    "IN_DISC_FISICA",
    "IN_DISC_BIOLOGIA",
    "IN_DISC_ESTUDOS_SOCIAIS",
    "IN_DISC_HISTORIA",
    "IN_DISC_GEOGRAFIA",
    "IN_DISC_SOCIOLOGIA",
    "IN_DISC_FILOSOFIA",
    "IN_DISC_ENSINO_RELIGIOSO",
]

stringa_disc = """IN_DISC_LINGUA_PORTUGUESA,145F15,0
IN_DISC_LINGUA_PORTUGUESA,145F17,0
IN_DISC_LINGUA_PORTUGUESA,223L01,1
IN_DISC_LINGUA_PORTUGUESA,220L03,1
IN_DISC_LINGUA_ESTRANGEIRA,145F14,0
IN_DISC_LINGUA_ESTRANGEIRA,145F17,1
IN_DISC_LINGUA_ESTRANGEIRA,222L01,0
IN_DISC_LINGUA_ESTRANGEIRA,220L03,1
IN_DISC_ARTES,146F02,0
IN_DISC_ARTES,146F04,0
IN_DISC_ARTES,146F07,0
IN_DISC_ARTES,146F20,0
IN_DISC_ARTES,146F22,0
IN_DISC_ARTES,210A01,0
IN_DISC_ARTES,211A02,1
IN_DISC_ARTES,212D01,1
IN_DISC_ARTES,212M02,1
IN_DISC_ARTES,212T01,1
IN_DISC_EDUCACAO_FISICA,146F15,0
IN_DISC_EDUCACAO_FISICA,720E01,1
IN_DISC_MATEMATICA,145F18,0
IN_DISC_MATEMATICA,461M01,1
IN_DISC_CIENCIAS,145F01,0
IN_DISC_CIENCIAS,145F02,0
IN_DISC_CIENCIAS,145F09,0
IN_DISC_CIENCIAS,145F21,0
IN_DISC_CIENCIAS,442Q01,1
IN_DISC_CIENCIAS,441F01,1
IN_DISC_CIENCIAS,421C01,1
IN_DISC_CIENCIAS,440C01,1
IN_DISC_QUIMICA,145F02,0
IN_DISC_QUIMICA,145F21,0
IN_DISC_QUIMICA,442Q01,1
IN_DISC_FISICA,145F02,0
IN_DISC_FISICA,145F09,0
IN_DISC_FISICA,441F01,1
IN_DISC_BIOLOGIA,145F01,0
IN_DISC_BIOLOGIA,145F02,0
IN_DISC_BIOLOGIA,421C01,1
IN_DISC_ESTUDOS_SOCIAIS,144F12,0
IN_DISC_ESTUDOS_SOCIAIS,145F10,0
IN_DISC_ESTUDOS_SOCIAIS,145F11,0
IN_DISC_ESTUDOS_SOCIAIS,145F24,0
IN_DISC_ESTUDOS_SOCIAIS,310C02,1
IN_DISC_ESTUDOS_SOCIAIS,312A01,1
IN_DISC_ESTUDOS_SOCIAIS,220H01,1
IN_DISC_ESTUDOS_SOCIAIS,225H01,1
IN_DISC_ESTUDOS_SOCIAIS,443G05,1
IN_DISC_HISTORIA,145F11,0
IN_DISC_HISTORIA,225H01,1
IN_DISC_GEOGRAFIA,145F10,0
IN_DISC_GEOGRAFIA,443G05,1
IN_DISC_SOCIOLOGIA,145F24,0
IN_DISC_SOCIOLOGIA,310C02,1
IN_DISC_SOCIOLOGIA,312A01,1
IN_DISC_FILOSOFIA,145F08,0
IN_DISC_FILOSOFIA,226F01,1
IN_DISC_ENSINO_RELIGIOSO,145F05,0
IN_DISC_ENSINO_RELIGIOSO,221T01,1"""

dict_normalize = {
    2014: {
        "IN_COM_PEDAGOGICA_1": "CO_AREA_COMPL_PEDAGOGICA_1",
        "IN_COM_PEDAGOGICA_2": "CO_AREA_COMPL_PEDAGOGICA_2",
        "IN_COM_PEDAGOGICA_3": "CO_AREA_COMPL_PEDAGOGICA_3",
    },
    2015: {
        "IN_COM_PEDAGOGICA_1": "CO_AREA_COMPL_PEDAGOGICA_1",
        "IN_COM_PEDAGOGICA_2": "CO_AREA_COMPL_PEDAGOGICA_2",
        "IN_COM_PEDAGOGICA_3": "CO_AREA_COMPL_PEDAGOGICA_3",
    },
    2016: {
        "IN_COM_PEDAGOGICA_1": "CO_AREA_COMPL_PEDAGOGICA_1",
        "IN_COM_PEDAGOGICA_2": "CO_AREA_COMPL_PEDAGOGICA_2",
        "IN_COM_PEDAGOGICA_3": "CO_AREA_COMPL_PEDAGOGICA_3",
    },
    2017: {
        "IN_COM_PEDAGOGICA_1": "CO_AREA_COMPL_PEDAGOGICA_1",
        "IN_COM_PEDAGOGICA_2": "CO_AREA_COMPL_PEDAGOGICA_2",
        "IN_COM_PEDAGOGICA_3": "CO_AREA_COMPL_PEDAGOGICA_3",
    },
    2018: {
        "IN_COM_PEDAGOGICA_1": "CO_AREA_COMPL_PEDAGOGICA_1",
        "IN_COM_PEDAGOGICA_2": "CO_AREA_COMPL_PEDAGOGICA_2",
        "IN_COM_PEDAGOGICA_3": "CO_AREA_COMPL_PEDAGOGICA_3",
    },
    2019: {
        "IN_COM_PEDAGOGICA_1": "CO_AREA_COMPL_PEDAGOGICA_1",
        "IN_COM_PEDAGOGICA_2": "CO_AREA_COMPL_PEDAGOGICA_2",
        "IN_COM_PEDAGOGICA_3": "CO_AREA_COMPL_PEDAGOGICA_3",
    },
    2020: {},
}


def break_disciplinas(data, list_disciplina):
    cols_id = [x for x in list(data.columns) if x not in list_disciplina]
    list_dfs = []
    for disciplina in list_disciplina:
        list_dfs.append(
            data.query(f"{disciplina}==1")[cols_id].assign(DISCIPLINA_NOME=disciplina)
        )
    return pd.concat(list_dfs)


def get_dict_disciplinas(stringa_disc):
    dict_disc = {}
    for linha in stringa_disc.split("\n"):
        list_item = linha.split(",")
        if list_item[0] not in dict_disc:
            dict_disc[list_item[0]] = {"cod_licen": [], "cod_bach_pedago": []}
        if list_item[2] == "0":
            dict_disc[list_item[0]]["cod_licen"] = dict_disc[list_item[0]][
                "cod_licen"
            ] + [list_item[1]]
        elif list_item[2] == "1":
            dict_disc[list_item[0]]["cod_bach_pedago"] = dict_disc[list_item[0]][
                "cod_bach_pedago"
            ] + [list_item[1]]
    return dict_disc


def check_adequada(data_row, dict_disciplinas):
    # cursos adequados de licenciatura
    list_cod_licen = dict_disciplinas[data_row["DISCIPLINA_NOME"]]["cod_licen"]
    # cursos adequados de bacharelado com complementacao pedagogica
    list_cod_bach_pedago = dict_disciplinas[data_row["DISCIPLINA_NOME"]][
        "cod_bach_pedago"
    ]
    # cursos formados
    list_co_curso = [
        data_row["CO_CURSO_1"],
        data_row["CO_CURSO_2"],
        data_row["CO_CURSO_3"],
    ]
    # flag de complementacao pedagogica
    list_com_pedago = [
        data_row["CO_AREA_COMPL_PEDAGOGICA_1"],
        data_row["CO_AREA_COMPL_PEDAGOGICA_2"],
        data_row["CO_AREA_COMPL_PEDAGOGICA_3"],
    ]

    for index, cod_curso in enumerate(list_co_curso):
        if cod_curso in list_cod_licen:
            return 1
        if cod_curso in list_cod_bach_pedago:
            if list_com_pedago[index] == 1:
                return 1
    return 0


# fmt: off
def process_ensino_infantil(df_dim_docentes, year):

    dim_ensino_infantil = \
    (df_dim_docentes[['CO_MUNICIPIO','TP_ETAPA_ENSINO', 'TP_ESCOLARIDADE',
                'CO_CURSO_1', 'CO_AREA_COMPL_PEDAGOGICA_1',
                'CO_CURSO_2', 'CO_AREA_COMPL_PEDAGOGICA_2',
                'CO_CURSO_3', 'CO_AREA_COMPL_PEDAGOGICA_3']]
    .query("TP_ETAPA_ENSINO==[1,2,3]")
    .assign(**{k: lambda df_, k=k: df_[k].fillna(0).astype('uint8') for k in
                ['CO_AREA_COMPL_PEDAGOGICA_1', 'CO_AREA_COMPL_PEDAGOGICA_2',
                'CO_AREA_COMPL_PEDAGOGICA_3', 'TP_ETAPA_ENSINO','TP_ESCOLARIDADE']})
    .astype({'CO_MUNICIPIO':'uint32'})
    .reset_index(drop=True)
    .assign(GRADUACAO_COMPLETA=lambda x: x['TP_ESCOLARIDADE'].isin([4]).astype('uint8'))
    .drop(columns=['TP_ESCOLARIDADE'])
    .assign(POSSUI_PEDAGO_LICEN=lambda x:(
        (x['CO_CURSO_1'].isin(['142P01'])
        | x['CO_CURSO_2'].isin(['142P01'])
        | x['CO_CURSO_2'].isin(['142P01']))).astype('uint8'))
    .assign(POSSUI_PEDAGO_BACH=lambda x:(
        ((x['CO_CURSO_1'].isin(['142C01']) & x['CO_AREA_COMPL_PEDAGOGICA_1'])
        | (x['CO_CURSO_2'].isin(['142C01']) & x['CO_AREA_COMPL_PEDAGOGICA_2'])
        | (x['CO_CURSO_3'].isin(['142C01']) & x['CO_AREA_COMPL_PEDAGOGICA_3'])))
        .astype('uint8'))
    .assign(DISCIPLINA_ADEQUADA = lambda x: (
        x['GRADUACAO_COMPLETA'] & (
        x['POSSUI_PEDAGO_LICEN'] | x['POSSUI_PEDAGO_BACH']))
        .astype('uint8'))
    .assign(DISCIPLINA_TOTAL= np.uint8(1))
    .assign(ANO=np.uint16(year))
    .assign(ETAPA='1_ENSINO_INFANTIL')
    .assign(DISCIPLINA_NOME='MULTIDICIPLINAR')
    .reindex(['ANO','ETAPA','CO_MUNICIPIO', 'DISCIPLINA_NOME','GRADUACAO_COMPLETA',
            'POSSUI_PEDAGO_LICEN', 'POSSUI_PEDAGO_BACH',
            'DISCIPLINA_ADEQUADA','DISCIPLINA_TOTAL'],axis=1)
    .reindex(['ANO','ETAPA','CO_MUNICIPIO', 'DISCIPLINA_NOME',
            'DISCIPLINA_ADEQUADA','DISCIPLINA_TOTAL'],axis=1)
    .groupby(['ANO', 'ETAPA', 'CO_MUNICIPIO', 'DISCIPLINA_NOME']).sum().reset_index()
    .astype({'ANO':'uint16'})
    .assign(**{k: lambda df_, k=k: df_[k].fillna(0).astype('uint32') for k in
                (['CO_MUNICIPIO','DISCIPLINA_ADEQUADA', 'DISCIPLINA_TOTAL'])})
    )
    return dim_ensino_infantil

# fmt: off
def process_fund_anos_iniciais(df_dim_docentes, year):

    dim_fund_anos_iniciais =\
    (df_dim_docentes[[
        'CO_MUNICIPIO', 'TP_ETAPA_ENSINO', 'TP_ESCOLARIDADE',
        'CO_CURSO_1', 'CO_AREA_COMPL_PEDAGOGICA_1',
        'CO_CURSO_2', 'CO_AREA_COMPL_PEDAGOGICA_2',
        'CO_CURSO_3', 'CO_AREA_COMPL_PEDAGOGICA_3']+cols_disciplinas]
    .query("TP_ETAPA_ENSINO==[4,5,6,7,8,14,15,16,17,18]")
    .assign(**{k: lambda df_, k=k: df_[k].fillna(0).astype('uint8') for k in
                (['CO_AREA_COMPL_PEDAGOGICA_1', 'CO_AREA_COMPL_PEDAGOGICA_2',
                  'CO_AREA_COMPL_PEDAGOGICA_3', 'TP_ETAPA_ENSINO']+cols_disciplinas)})
    .astype({'CO_MUNICIPIO':'uint32'})
    .pipe(lambda x:break_disciplinas(x, cols_disciplinas))
    .assign(DISCIPLINA_NOME=lambda x: x['DISCIPLINA_NOME'].replace(
        {'IN_DISC_LINGUA_INGLES':'IN_DISC_LINGUA_ESTRANGEIRA',
         'IN_DISC_LINGUA_ESPANHOL':'IN_DISC_LINGUA_ESTRANGEIRA',
         'IN_DISC_LINGUA_FRANCES':'IN_DISC_LINGUA_ESTRANGEIRA',
         'IN_DISC_LINGUA_OUTRA':'IN_DISC_LINGUA_ESTRANGEIRA'}))
    .reset_index(drop=True)
    .assign(GRADUACAO_COMPLETA=lambda x:
            x['TP_ESCOLARIDADE'].isin([4]).astype('uint8'))
    .assign(POSSUI_PEDAGO_LICEN=lambda x:(
        (x['CO_CURSO_1'].isin(['142P01'])
        | x['CO_CURSO_2'].isin(['142P01'])
        | x['CO_CURSO_2'].isin(['142P01']))).astype('uint8'))
    .assign(POSSUI_PEDAGO_BACH=lambda x:(
        ((x['CO_CURSO_1'].isin(['142C01']) & x['CO_AREA_COMPL_PEDAGOGICA_1'])
        | (x['CO_CURSO_2'].isin(['142C01']) & x['CO_AREA_COMPL_PEDAGOGICA_2'])
        | (x['CO_CURSO_3'].isin(['142C01']) & x['CO_AREA_COMPL_PEDAGOGICA_3'])))
        .astype('uint8'))
    .assign(DISC_LING_ESTRANG=lambda x:(x['DISCIPLINA_NOME'].isin(
        ['IN_DISC_LINGUA_ESTRANGEIRA'])).astype('uint8'))
    .assign(POSSUI_CURSO_LING_ESTRANG=lambda x:(
        (x['CO_CURSO_1'].isin(['145F14', '145F17'])
        | (x['CO_CURSO_1'].isin(['222L01', '220L03']) & x['CO_AREA_COMPL_PEDAGOGICA_1']))
        | (x['CO_CURSO_2'].isin(['145F14', '145F17'])
            | (x['CO_CURSO_2'].isin(['222L01', '220L03']) & x['CO_AREA_COMPL_PEDAGOGICA_2']))
        | (x['CO_CURSO_3'].isin(['145F14', '145F17'])
            | (x['CO_CURSO_3'].isin(['222L01', '220L03']) & x['CO_AREA_COMPL_PEDAGOGICA_3']))).astype('uint8'))
    .assign(ADEQUADA_LING_ESTRANG=lambda x:(x['DISC_LING_ESTRANG'] &
                                            x['POSSUI_CURSO_LING_ESTRANG']).astype('uint8'))
    .assign(ADEQUADA_DEMAIS=lambda x:(x['POSSUI_PEDAGO_LICEN'] |
                                    x['POSSUI_PEDAGO_BACH']).astype('uint8'))
    .assign(ADEQUADA_CURSO=lambda x:(
        x['ADEQUADA_LING_ESTRANG'].where(x['DISC_LING_ESTRANG'].isin([1]),
                                        x['ADEQUADA_DEMAIS'])).astype('uint8'))
    .assign(DISCIPLINA_ADEQUADA = lambda x: (
        x['GRADUACAO_COMPLETA'] & x['ADEQUADA_CURSO']).astype('uint8'))
    .assign(DISCIPLINA_TOTAL= np.uint8(1))
    .assign(ANO=np.uint16(year))
    .assign(ETAPA='2_FUND_ANOS_INICIAIS')
    .reindex(['ANO', 'ETAPA', 'CO_MUNICIPIO', 'GRADUACAO_COMPLETA',
              'POSSUI_PEDAGO_LICEN', 'POSSUI_PEDAGO_BACH',
              'DISC_LING_ESTRANG', 'POSSUI_CURSO_LING_ESTRANG',
              'DISCIPLINA_NOME','DISCIPLINA_ADEQUADA','DISCIPLINA_TOTAL'],axis=1)
    .reindex(['ANO','ETAPA','CO_MUNICIPIO', 'DISCIPLINA_NOME',
                'DISCIPLINA_ADEQUADA','DISCIPLINA_TOTAL'],axis=1)
    .groupby(['ANO', 'ETAPA', 'CO_MUNICIPIO', 'DISCIPLINA_NOME']).sum().reset_index()
    .astype({'ANO':'uint16'})
    .assign(**{k: lambda df_, k=k: df_[k].fillna(0).astype('uint32') for k in
                (['CO_MUNICIPIO','DISCIPLINA_ADEQUADA', 'DISCIPLINA_TOTAL'])})
    )
    return dim_fund_anos_iniciais

# fmt: off
def process_fund_finais_ens_medio(df_dim_docentes, year, dict_disciplinas):

    dim_fund_finais_ens_medio = \
    (df_dim_docentes[['CO_MUNICIPIO', 'TP_ETAPA_ENSINO', 'TP_ESCOLARIDADE',
                      'CO_CURSO_1', 'CO_AREA_COMPL_PEDAGOGICA_1',
                      'CO_CURSO_2', 'CO_AREA_COMPL_PEDAGOGICA_2',
                      'CO_CURSO_3', 'CO_AREA_COMPL_PEDAGOGICA_3']+cols_disciplinas]
    .query("TP_ETAPA_ENSINO==[9,10,11,12,13,19,20,21,41,22,23,24,25,26,27,28,29,35,36,37,38]")
    .assign(**{k: lambda df_, k=k: df_[k].fillna(0).astype('uint8') for k in
                (['CO_AREA_COMPL_PEDAGOGICA_1', 'CO_AREA_COMPL_PEDAGOGICA_2',
                'CO_AREA_COMPL_PEDAGOGICA_3', 'TP_ETAPA_ENSINO']+cols_disciplinas)})
    .assign(ETAPA=0)
    .assign(ETAPA=lambda x:x['ETAPA'].where(~x['TP_ETAPA_ENSINO'].isin([9,10,11,12,13,19,20,21,41,22,23,24]), '3_FUND_ANOS_FINAIS'))
    .assign(ETAPA=lambda x:x['ETAPA'].where(~x['TP_ETAPA_ENSINO'].isin([25,26,27,28,29,35,36,37,38]), '4_ENSINO_MEDIO'))
    .drop(columns=['TP_ETAPA_ENSINO'])
    .query('ETAPA!=0')
    .pipe(lambda x:break_disciplinas(x, cols_disciplinas))
    .assign(DISCIPLINA_NOME=lambda x: x['DISCIPLINA_NOME'].replace(
        {'IN_DISC_LINGUA_INGLES':'IN_DISC_LINGUA_ESTRANGEIRA',
        'IN_DISC_LINGUA_ESPANHOL':'IN_DISC_LINGUA_ESTRANGEIRA',
        'IN_DISC_LINGUA_FRANCES':'IN_DISC_LINGUA_ESTRANGEIRA',
        'IN_DISC_LINGUA_OUTRA':'IN_DISC_LINGUA_ESTRANGEIRA'}))
    .reset_index(drop=True)
    .assign(ADEQUADA_CURSO=lambda x:
            x.apply(lambda row:check_adequada(row, dict_disciplinas),axis=1))
    .assign(GRADUACAO_COMPLETA=lambda x:
            x['TP_ESCOLARIDADE'].isin([4]).astype('uint8'))
    .assign(DISCIPLINA_ADEQUADA = lambda x: (
        x['GRADUACAO_COMPLETA'] & x['ADEQUADA_CURSO']).astype('uint8'))
    .assign(DISCIPLINA_TOTAL= np.uint8(1))
    .assign(ANO=np.uint16(year))
    .reindex(['ANO','ETAPA','CO_MUNICIPIO', 'DISCIPLINA_NOME',
            'DISCIPLINA_ADEQUADA','DISCIPLINA_TOTAL'],axis=1)
    .groupby(['ANO', 'ETAPA', 'CO_MUNICIPIO', 'DISCIPLINA_NOME']).sum().reset_index()
    .astype({'ANO':'uint16'})
    .assign(**{k: lambda df_, k=k: df_[k].fillna(0).astype('uint32') for k in
                (['CO_MUNICIPIO','DISCIPLINA_ADEQUADA', 'DISCIPLINA_TOTAL'])})
    )
    return dim_fund_finais_ens_medio

# fmt: off
def model(dbt, fal):


    # load
    df_dim_docentes = dbt.source("raw", "DIM_DOCENTES_CO_2020")
    year = 2020

    dict_disciplinas = get_dict_disciplinas(stringa_disc)

    df_dim_educ_bas_docentes_15 = pd.DataFrame()
    df_dim_docentes = (df_dim_docentes
        .rename(columns=dict_normalize[year]))[
            ['CO_MUNICIPIO', 'TP_ETAPA_ENSINO', 'TP_ESCOLARIDADE',
             'CO_CURSO_1', 'CO_AREA_COMPL_PEDAGOGICA_1',
             'CO_CURSO_2', 'CO_AREA_COMPL_PEDAGOGICA_2',
             'CO_CURSO_3', 'CO_AREA_COMPL_PEDAGOGICA_3']+cols_disciplinas]

    # ensino infantil
    dim_ensino_infantil = process_ensino_infantil(df_dim_docentes, year)

    # fund_anos_iniciais
    dim_fund_anos_iniciais = process_fund_anos_iniciais(df_dim_docentes, year)

    # fund_finais_ens_medio
    dim_fund_finais_ens_medio = process_fund_finais_ens_medio(df_dim_docentes,
                                                              year,
                                                              dict_disciplinas)

    df_dim_educ_bas_docentes_15 = pd.concat([df_dim_educ_bas_docentes_15,
                                            dim_ensino_infantil,
                                            dim_fund_anos_iniciais,
                                            dim_fund_finais_ens_medio])
    return df_dim_educ_bas_docentes_15


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
    sources = {"raw.DIM_DOCENTES_CO_2020": "\"postgres\".\"raw\".\"DIM_DOCENTES_CO_2020\""}
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
    identifier = "dim_educ_bas_docentes_15_2020_co"
    
    def __repr__(self):
        return '"postgres"."dbt_staging"."dim_educ_bas_docentes_15_2020_co"'


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
      'postgres.dbt_staging.dim_educ_bas_docentes_15_2020_co',
      df
  )