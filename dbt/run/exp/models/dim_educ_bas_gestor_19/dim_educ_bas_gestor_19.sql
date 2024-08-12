
  
    

  create  table "postgres"."dbt_staging"."dim_educ_bas_gestor_19__dbt_tmp"
  
  
    as
  
  (
    


SELECT
    "NU_ANO_CENSO",
    "CO_MUNICIPIO",
    "TP_DEPENDENCIA",
    "TP_CARGO_GESTOR",
    "TP_TIPO_ACESSO_CARGO"
FROM
    "postgres"."raw"."DIM_CENSO_EDUC_BASICA_GESTOR_2019"

UNION ALL


SELECT
    "NU_ANO_CENSO",
    "CO_MUNICIPIO",
    "TP_DEPENDENCIA",
    "TP_CARGO_GESTOR",
    "TP_TIPO_ACESSO_CARGO"
FROM
    "postgres"."raw"."DIM_CENSO_EDUC_BASICA_GESTOR_2020"


  );
  