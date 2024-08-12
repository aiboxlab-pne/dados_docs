with base as (
    
        select
            "ANO"
            , "ESFERAADMINISTRATIVA" as "MUNICIPIO_NOME"
            , "DESCRICAOGRUPONATUREZA" as "GRUPO_NATUREZA"
            , "DESCRICAOCATEGORIA" as "CATEGORIA"
            , "PAGA" as "VALOR_PAGO"
        from
            "postgres"."raw"."DIM_TCE_ES_DESPESAS_2014"
        where
            "DESCRICAOFUNCAO" = 'EDUCAÇÃO'
        union all
    
        select
            "ANO"
            , "ESFERAADMINISTRATIVA" as "MUNICIPIO_NOME"
            , "DESCRICAOGRUPONATUREZA" as "GRUPO_NATUREZA"
            , "DESCRICAOCATEGORIA" as "CATEGORIA"
            , "PAGA" as "VALOR_PAGO"
        from
            "postgres"."raw"."DIM_TCE_ES_DESPESAS_2015"
        where
            "DESCRICAOFUNCAO" = 'EDUCAÇÃO'
        union all
    
        select
            "ANO"
            , "ESFERAADMINISTRATIVA" as "MUNICIPIO_NOME"
            , "DESCRICAOGRUPONATUREZA" as "GRUPO_NATUREZA"
            , "DESCRICAOCATEGORIA" as "CATEGORIA"
            , "PAGA" as "VALOR_PAGO"
        from
            "postgres"."raw"."DIM_TCE_ES_DESPESAS_2016"
        where
            "DESCRICAOFUNCAO" = 'EDUCAÇÃO'
        union all
    
        select
            "ANO"
            , "ESFERAADMINISTRATIVA" as "MUNICIPIO_NOME"
            , "DESCRICAOGRUPONATUREZA" as "GRUPO_NATUREZA"
            , "DESCRICAOCATEGORIA" as "CATEGORIA"
            , "PAGA" as "VALOR_PAGO"
        from
            "postgres"."raw"."DIM_TCE_ES_DESPESAS_2017"
        where
            "DESCRICAOFUNCAO" = 'EDUCAÇÃO'
        union all
    
        select
            "ANO"
            , "ESFERAADMINISTRATIVA" as "MUNICIPIO_NOME"
            , "DESCRICAOGRUPONATUREZA" as "GRUPO_NATUREZA"
            , "DESCRICAOCATEGORIA" as "CATEGORIA"
            , "PAGA" as "VALOR_PAGO"
        from
            "postgres"."raw"."DIM_TCE_ES_DESPESAS_2018"
        where
            "DESCRICAOFUNCAO" = 'EDUCAÇÃO'
        union all
    
        select
            "ANO"
            , "ESFERAADMINISTRATIVA" as "MUNICIPIO_NOME"
            , "DESCRICAOGRUPONATUREZA" as "GRUPO_NATUREZA"
            , "DESCRICAOCATEGORIA" as "CATEGORIA"
            , "PAGA" as "VALOR_PAGO"
        from
            "postgres"."raw"."DIM_TCE_ES_DESPESAS_2019"
        where
            "DESCRICAOFUNCAO" = 'EDUCAÇÃO'
        union all
    
        select
            "ANO"
            , "ESFERAADMINISTRATIVA" as "MUNICIPIO_NOME"
            , "DESCRICAOGRUPONATUREZA" as "GRUPO_NATUREZA"
            , "DESCRICAOCATEGORIA" as "CATEGORIA"
            , "PAGA" as "VALOR_PAGO"
        from
            "postgres"."raw"."DIM_TCE_ES_DESPESAS_2020"
        where
            "DESCRICAOFUNCAO" = 'EDUCAÇÃO'
        union all
    
        select
            "ANO"
            , "ESFERAADMINISTRATIVA" as "MUNICIPIO_NOME"
            , "DESCRICAOGRUPONATUREZA" as "GRUPO_NATUREZA"
            , "DESCRICAOCATEGORIA" as "CATEGORIA"
            , "PAGA" as "VALOR_PAGO"
        from
            "postgres"."raw"."DIM_TCE_ES_DESPESAS_2021"
        where
            "DESCRICAOFUNCAO" = 'EDUCAÇÃO'
        union all
    
        select
            "ANO"
            , "ESFERAADMINISTRATIVA" as "MUNICIPIO_NOME"
            , "DESCRICAOGRUPONATUREZA" as "GRUPO_NATUREZA"
            , "DESCRICAOCATEGORIA" as "CATEGORIA"
            , "PAGA" as "VALOR_PAGO"
        from
            "postgres"."raw"."DIM_TCE_ES_DESPESAS_2022"
        where
            "DESCRICAOFUNCAO" = 'EDUCAÇÃO'
        union all
    
        select
            "ANO"
            , "ESFERAADMINISTRATIVA" as "MUNICIPIO_NOME"
            , "DESCRICAOGRUPONATUREZA" as "GRUPO_NATUREZA"
            , "DESCRICAOCATEGORIA" as "CATEGORIA"
            , "PAGA" as "VALOR_PAGO"
        from
            "postgres"."raw"."DIM_TCE_ES_DESPESAS_2023"
        where
            "DESCRICAOFUNCAO" = 'EDUCAÇÃO'
        
    
    ),
info_municipios as (select
    "MUNICIPIO_CODIGO" as "FK_MUNICIPIO_CODIGO"
    , "MUNICIPIO_NOME"
from
    "postgres"."dbt_staging"."info_municipios" )

select
    base."ANO"
    , base."MUNICIPIO_NOME"
    , info_municipios."FK_MUNICIPIO_CODIGO"
    , base."GRUPO_NATUREZA"
    , base."CATEGORIA"
    , ROUND(CAST(base."VALOR_PAGO" as numeric), 2) as "VALOR_PAGO"
from base
left join info_municipios
on base."MUNICIPIO_NOME" = info_municipios."MUNICIPIO_NOME"