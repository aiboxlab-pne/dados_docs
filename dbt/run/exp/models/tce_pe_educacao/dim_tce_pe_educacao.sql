
  
    

  create  table "postgres"."dbt_staging"."dim_tce_pe_educacao__dbt_tmp"
  
  
    as
  
  (
    with tb_municipio as (
    select
        "CODIGO",
        "CODIGOIBGE" as "FK_MUNICIPIO_CODIGO"
    from
        "postgres"."raw"."DIM_TCE_PE_MUNICIPIO"
)


select
    "ANO_REFERENCIA" as "ANO"
    , tb_municipio."FK_MUNICIPIO_CODIGO"
    , "NATUREZA"
    , ROUND(SUM(CAST("VALOR_PAGO" as numeric)),2) as "VALOR_PAGO"
from
    "postgres"."raw"."DIM_TCE_PE_DESPESAS_2014"
LEFT JOIN tb_municipio
ON "CODIGO_MUNICIPIO" = tb_municipio."CODIGO"
where
    "FUNCAO" = 'Educação'
group by
    "ANO", "FK_MUNICIPIO_CODIGO", "NATUREZA"

union all


select
    "ANO_REFERENCIA" as "ANO"
    , tb_municipio."FK_MUNICIPIO_CODIGO"
    , "NATUREZA"
    , ROUND(SUM(CAST("VALOR_PAGO" as numeric)),2) as "VALOR_PAGO"
from
    "postgres"."raw"."DIM_TCE_PE_DESPESAS_2015"
LEFT JOIN tb_municipio
ON "CODIGO_MUNICIPIO" = tb_municipio."CODIGO"
where
    "FUNCAO" = 'Educação'
group by
    "ANO", "FK_MUNICIPIO_CODIGO", "NATUREZA"

union all


select
    "ANO_REFERENCIA" as "ANO"
    , tb_municipio."FK_MUNICIPIO_CODIGO"
    , "NATUREZA"
    , ROUND(SUM(CAST("VALOR_PAGO" as numeric)),2) as "VALOR_PAGO"
from
    "postgres"."raw"."DIM_TCE_PE_DESPESAS_2016"
LEFT JOIN tb_municipio
ON "CODIGO_MUNICIPIO" = tb_municipio."CODIGO"
where
    "FUNCAO" = 'Educação'
group by
    "ANO", "FK_MUNICIPIO_CODIGO", "NATUREZA"

union all


select
    "ANO_REFERENCIA" as "ANO"
    , tb_municipio."FK_MUNICIPIO_CODIGO"
    , "NATUREZA"
    , ROUND(SUM(CAST("VALOR_PAGO" as numeric)),2) as "VALOR_PAGO"
from
    "postgres"."raw"."DIM_TCE_PE_DESPESAS_2017"
LEFT JOIN tb_municipio
ON "CODIGO_MUNICIPIO" = tb_municipio."CODIGO"
where
    "FUNCAO" = 'Educação'
group by
    "ANO", "FK_MUNICIPIO_CODIGO", "NATUREZA"

union all


select
    "ANO_REFERENCIA" as "ANO"
    , tb_municipio."FK_MUNICIPIO_CODIGO"
    , "NATUREZA"
    , ROUND(SUM(CAST("VALOR_PAGO" as numeric)),2) as "VALOR_PAGO"
from
    "postgres"."raw"."DIM_TCE_PE_DESPESAS_2018"
LEFT JOIN tb_municipio
ON "CODIGO_MUNICIPIO" = tb_municipio."CODIGO"
where
    "FUNCAO" = 'Educação'
group by
    "ANO", "FK_MUNICIPIO_CODIGO", "NATUREZA"

union all


select
    "ANO_REFERENCIA" as "ANO"
    , tb_municipio."FK_MUNICIPIO_CODIGO"
    , "NATUREZA"
    , ROUND(SUM(CAST("VALOR_PAGO" as numeric)),2) as "VALOR_PAGO"
from
    "postgres"."raw"."DIM_TCE_PE_DESPESAS_2019"
LEFT JOIN tb_municipio
ON "CODIGO_MUNICIPIO" = tb_municipio."CODIGO"
where
    "FUNCAO" = 'Educação'
group by
    "ANO", "FK_MUNICIPIO_CODIGO", "NATUREZA"

union all


select
    "ANO_REFERENCIA" as "ANO"
    , tb_municipio."FK_MUNICIPIO_CODIGO"
    , "NATUREZA"
    , ROUND(SUM(CAST("VALOR_PAGO" as numeric)),2) as "VALOR_PAGO"
from
    "postgres"."raw"."DIM_TCE_PE_DESPESAS_2020"
LEFT JOIN tb_municipio
ON "CODIGO_MUNICIPIO" = tb_municipio."CODIGO"
where
    "FUNCAO" = 'Educação'
group by
    "ANO", "FK_MUNICIPIO_CODIGO", "NATUREZA"

union all


select
    "ANO_REFERENCIA" as "ANO"
    , tb_municipio."FK_MUNICIPIO_CODIGO"
    , "NATUREZA"
    , ROUND(SUM(CAST("VALOR_PAGO" as numeric)),2) as "VALOR_PAGO"
from
    "postgres"."raw"."DIM_TCE_PE_DESPESAS_2021"
LEFT JOIN tb_municipio
ON "CODIGO_MUNICIPIO" = tb_municipio."CODIGO"
where
    "FUNCAO" = 'Educação'
group by
    "ANO", "FK_MUNICIPIO_CODIGO", "NATUREZA"

union all


select
    "ANO_REFERENCIA" as "ANO"
    , tb_municipio."FK_MUNICIPIO_CODIGO"
    , "NATUREZA"
    , ROUND(SUM(CAST("VALOR_PAGO" as numeric)),2) as "VALOR_PAGO"
from
    "postgres"."raw"."DIM_TCE_PE_DESPESAS_2022"
LEFT JOIN tb_municipio
ON "CODIGO_MUNICIPIO" = tb_municipio."CODIGO"
where
    "FUNCAO" = 'Educação'
group by
    "ANO", "FK_MUNICIPIO_CODIGO", "NATUREZA"

union all


select
    "ANO_REFERENCIA" as "ANO"
    , tb_municipio."FK_MUNICIPIO_CODIGO"
    , "NATUREZA"
    , ROUND(SUM(CAST("VALOR_PAGO" as numeric)),2) as "VALOR_PAGO"
from
    "postgres"."raw"."DIM_TCE_PE_DESPESAS_2023"
LEFT JOIN tb_municipio
ON "CODIGO_MUNICIPIO" = tb_municipio."CODIGO"
where
    "FUNCAO" = 'Educação'
group by
    "ANO", "FK_MUNICIPIO_CODIGO", "NATUREZA"


  );
  