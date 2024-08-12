
  
    

  create  table "postgres"."dbt_staging"."dim_educ_bas_docentes_15_group__dbt_tmp"
  
  
    as
  
  (
    SELECT
    "ANO",
    "ETAPA",
    "FK_MUNICIPIO_CODIGO",
    SUM("FORMACAO_ADEQUADA") as "FORMACAO_ADEQUADA",
    SUM("DOCENCIA_TOTAL") as "DOCENCIA_TOTAL"
FROM
    "postgres"."dbt_staging"."dim_educ_bas_docentes_15"
GROUP BY
    "ANO",
    "ETAPA",
    "FK_MUNICIPIO_CODIGO"
  );
  