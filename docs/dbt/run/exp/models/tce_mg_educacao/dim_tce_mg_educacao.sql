
  
    

  create  table "postgres"."dbt_staging"."dim_tce_mg_educacao__dbt_tmp"
  
  
    as
  
  (
    select
    "NUM_ANO_REFERENCIA" as "ANO"
    , "COD_MUNICIPIO" as "FK_MUNICIPIO_CODIGO"
    , "DSC_SUBFUNCAO" as "SUBFUNCAO"
    , "DSC_PROGRAMA" as "PROGRAMA"
    , "DSC_ACAO" as "ACAO"
    , "DSC_SUBACAO" as "SUBACAO"
    , ROUND(CAST("VLR_PAGAMENTO" as numeric), 2) as "VALOR_PAGO"
from
    "postgres"."raw"."DIM_TCE_MG_EDUCACAO"
  );
  