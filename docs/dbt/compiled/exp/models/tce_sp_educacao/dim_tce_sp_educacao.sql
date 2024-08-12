
select
    "ANO_EXERCICIO" as "ANO"
    , "CODIGO_MUNICIPIO_IBGE" as "FK_MUNICIPIO_CODIGO"
    , "DS_SUBFUNCAO_GOVERNO"
    , ROUND(CAST("VL_DESPESA" as numeric),2) as "VALOR_PAGO"
from
    "postgres"."raw"."DIM_TCE_SP_DESPESAS_2014"
where
    "DS_FUNCAO_GOVERNO" = 'EDUCAÇÃO' AND "TP_DESPESA" = 'Valor Pago'

union all


select
    "ANO_EXERCICIO" as "ANO"
    , "CODIGO_MUNICIPIO_IBGE" as "FK_MUNICIPIO_CODIGO"
    , "DS_SUBFUNCAO_GOVERNO"
    , ROUND(CAST("VL_DESPESA" as numeric),2) as "VALOR_PAGO"
from
    "postgres"."raw"."DIM_TCE_SP_DESPESAS_2015"
where
    "DS_FUNCAO_GOVERNO" = 'EDUCAÇÃO' AND "TP_DESPESA" = 'Valor Pago'

union all


select
    "ANO_EXERCICIO" as "ANO"
    , "CODIGO_MUNICIPIO_IBGE" as "FK_MUNICIPIO_CODIGO"
    , "DS_SUBFUNCAO_GOVERNO"
    , ROUND(CAST("VL_DESPESA" as numeric),2) as "VALOR_PAGO"
from
    "postgres"."raw"."DIM_TCE_SP_DESPESAS_2016"
where
    "DS_FUNCAO_GOVERNO" = 'EDUCAÇÃO' AND "TP_DESPESA" = 'Valor Pago'

union all


select
    "ANO_EXERCICIO" as "ANO"
    , "CODIGO_MUNICIPIO_IBGE" as "FK_MUNICIPIO_CODIGO"
    , "DS_SUBFUNCAO_GOVERNO"
    , ROUND(CAST("VL_DESPESA" as numeric),2) as "VALOR_PAGO"
from
    "postgres"."raw"."DIM_TCE_SP_DESPESAS_2017"
where
    "DS_FUNCAO_GOVERNO" = 'EDUCAÇÃO' AND "TP_DESPESA" = 'Valor Pago'

union all


select
    "ANO_EXERCICIO" as "ANO"
    , "CODIGO_MUNICIPIO_IBGE" as "FK_MUNICIPIO_CODIGO"
    , "DS_SUBFUNCAO_GOVERNO"
    , ROUND(CAST("VL_DESPESA" as numeric),2) as "VALOR_PAGO"
from
    "postgres"."raw"."DIM_TCE_SP_DESPESAS_2018"
where
    "DS_FUNCAO_GOVERNO" = 'EDUCAÇÃO' AND "TP_DESPESA" = 'Valor Pago'

union all


select
    "ANO_EXERCICIO" as "ANO"
    , "CODIGO_MUNICIPIO_IBGE" as "FK_MUNICIPIO_CODIGO"
    , "DS_SUBFUNCAO_GOVERNO"
    , ROUND(CAST("VL_DESPESA" as numeric),2) as "VALOR_PAGO"
from
    "postgres"."raw"."DIM_TCE_SP_DESPESAS_2019"
where
    "DS_FUNCAO_GOVERNO" = 'EDUCAÇÃO' AND "TP_DESPESA" = 'Valor Pago'

union all


select
    "ANO_EXERCICIO" as "ANO"
    , "CODIGO_MUNICIPIO_IBGE" as "FK_MUNICIPIO_CODIGO"
    , "DS_SUBFUNCAO_GOVERNO"
    , ROUND(CAST("VL_DESPESA" as numeric),2) as "VALOR_PAGO"
from
    "postgres"."raw"."DIM_TCE_SP_DESPESAS_2020"
where
    "DS_FUNCAO_GOVERNO" = 'EDUCAÇÃO' AND "TP_DESPESA" = 'Valor Pago'

union all


select
    "ANO_EXERCICIO" as "ANO"
    , "CODIGO_MUNICIPIO_IBGE" as "FK_MUNICIPIO_CODIGO"
    , "DS_SUBFUNCAO_GOVERNO"
    , ROUND(CAST("VL_DESPESA" as numeric),2) as "VALOR_PAGO"
from
    "postgres"."raw"."DIM_TCE_SP_DESPESAS_2021"
where
    "DS_FUNCAO_GOVERNO" = 'EDUCAÇÃO' AND "TP_DESPESA" = 'Valor Pago'

union all


select
    "ANO_EXERCICIO" as "ANO"
    , "CODIGO_MUNICIPIO_IBGE" as "FK_MUNICIPIO_CODIGO"
    , "DS_SUBFUNCAO_GOVERNO"
    , ROUND(CAST("VL_DESPESA" as numeric),2) as "VALOR_PAGO"
from
    "postgres"."raw"."DIM_TCE_SP_DESPESAS_2022"
where
    "DS_FUNCAO_GOVERNO" = 'EDUCAÇÃO' AND "TP_DESPESA" = 'Valor Pago'

union all


select
    "ANO_EXERCICIO" as "ANO"
    , "CODIGO_MUNICIPIO_IBGE" as "FK_MUNICIPIO_CODIGO"
    , "DS_SUBFUNCAO_GOVERNO"
    , ROUND(CAST("VL_DESPESA" as numeric),2) as "VALOR_PAGO"
from
    "postgres"."raw"."DIM_TCE_SP_DESPESAS_2023"
where
    "DS_FUNCAO_GOVERNO" = 'EDUCAÇÃO' AND "TP_DESPESA" = 'Valor Pago'

