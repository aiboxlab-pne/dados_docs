
  
    

  create  table "postgres"."dbt_staging"."dim_educ_bas_docentes_15_co_2014_sample__dbt_tmp"
  
  
    as
  
  (
    SELECT
    *
FROM
    "postgres"."raw"."DIM_DOCENTES_CO_2014"
    LIMIT 100000
  );
  