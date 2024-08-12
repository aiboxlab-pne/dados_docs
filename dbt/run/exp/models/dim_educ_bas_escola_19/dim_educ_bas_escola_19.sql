
  
    

  create  table "postgres"."dbt_staging"."dim_educ_bas_escola_19__dbt_tmp"
  
  
    as
  
  (
    


SELECT
    "NU_ANO_CENSO",
    "CO_MUNICIPIO",
    "TP_DEPENDENCIA",
    "TP_SITUACAO_FUNCIONAMENTO",
    "IN_ORGAO_ASS_PAIS",
    "IN_ORGAO_ASS_PAIS_MESTRES",
    "IN_ORGAO_CONSELHO_ESCOLAR",
    "IN_ORGAO_GREMIO_ESTUDANTIL"
FROM
    "postgres"."raw"."DIM_EDUC_BASICA_ESCOLA_2019"

UNION ALL


SELECT
    "NU_ANO_CENSO",
    "CO_MUNICIPIO",
    "TP_DEPENDENCIA",
    "TP_SITUACAO_FUNCIONAMENTO",
    "IN_ORGAO_ASS_PAIS",
    "IN_ORGAO_ASS_PAIS_MESTRES",
    "IN_ORGAO_CONSELHO_ESCOLAR",
    "IN_ORGAO_GREMIO_ESTUDANTIL"
FROM
    "postgres"."raw"."DIM_EDUC_BASICA_ESCOLA_2020"


  );
  