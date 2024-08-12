

with __dbt__cte__matricula_ept_2014 as (
with with_col_publico as (
    select
        "NU_ANO_CENSO" as "ANO"
        , "CO_MUNICIPIO" as "FK_MUNICIPIO_CODIGO"
        , case when "TP_DEPENDENCIA" in (1,2,3) then 1 else 0 end as PUBLICO
    from
        "postgres"."raw"."DIM_CENSO_EDUC_BASICA_DESAGREGADO_MATRICULA_11_2014"
    where
        "TP_ETAPA_ENSINO" in (30, 31, 32, 33, 34, 35, 36, 37, 38, 39)
),
ept_privado as (
    select
        "ANO"
        , "FK_MUNICIPIO_CODIGO"
        , count("FK_MUNICIPIO_CODIGO") as "EPT_PRIVADO"
    from 
        with_col_publico
    where 
        PUBLICO = 0
    group by "ANO", "FK_MUNICIPIO_CODIGO"
),
ept_publico as (
    select
        "ANO"
        , "FK_MUNICIPIO_CODIGO"
        , count("FK_MUNICIPIO_CODIGO") as "EPT_PUBLICO"
    from 
        with_col_publico
    where 
        PUBLICO = 1
    group by "ANO", "FK_MUNICIPIO_CODIGO"
),
matricula_ept as (
    select
        COALESCE(ept_publico."ANO", ept_privado."ANO") as "ANO"
        , COALESCE(ept_publico."FK_MUNICIPIO_CODIGO", ept_privado."FK_MUNICIPIO_CODIGO") as "FK_MUNICIPIO_CODIGO"
        , COALESCE(ept_publico."EPT_PUBLICO",0) as "EPT_PUBLICO"
        , COALESCE(ept_privado."EPT_PRIVADO", 0) as "EPT_PRIVADO"
    from ept_publico
    full join ept_privado
        on ept_publico."ANO" = ept_privado."ANO"
        and ept_publico."FK_MUNICIPIO_CODIGO" = ept_privado."FK_MUNICIPIO_CODIGO"
            
)
select * from matricula_ept
),  __dbt__cte__matricula_ept_2015 as (
with with_col_publico as (
    select
        "NU_ANO_CENSO" as "ANO"
        , "CO_MUNICIPIO" as "FK_MUNICIPIO_CODIGO"
        , case when "TP_DEPENDENCIA" in (1,2,3) then 1 else 0 end as PUBLICO
    from
        "postgres"."raw"."DIM_CENSO_EDUC_BASICA_DESAGREGADO_MATRICULA_11_2015"
    where
        "TP_ETAPA_ENSINO" in (30, 31, 32, 33, 34, 35, 36, 37, 38, 39)
),
ept_privado as (
    select
        "ANO"
        , "FK_MUNICIPIO_CODIGO"
        , count("FK_MUNICIPIO_CODIGO") as "EPT_PRIVADO"
    from
        with_col_publico
    where
        PUBLICO = 0
    group by "ANO", "FK_MUNICIPIO_CODIGO"
),
ept_publico as (
    select
        "ANO"
        , "FK_MUNICIPIO_CODIGO"
        , count("FK_MUNICIPIO_CODIGO") as "EPT_PUBLICO"
    from
        with_col_publico
    where
        PUBLICO = 1
    group by "ANO", "FK_MUNICIPIO_CODIGO"
),
matricula_ept as (
    select
        COALESCE(ept_publico."ANO", ept_privado."ANO") as "ANO"
        , COALESCE(ept_publico."FK_MUNICIPIO_CODIGO", ept_privado."FK_MUNICIPIO_CODIGO") as "FK_MUNICIPIO_CODIGO"
        , COALESCE(ept_publico."EPT_PUBLICO",0) as "EPT_PUBLICO"
        , COALESCE(ept_privado."EPT_PRIVADO", 0) as "EPT_PRIVADO"
    from ept_publico
    full join ept_privado
        on ept_publico."ANO" = ept_privado."ANO"
        and ept_publico."FK_MUNICIPIO_CODIGO" = ept_privado."FK_MUNICIPIO_CODIGO"

)
select * from matricula_ept
),  __dbt__cte__matricula_ept_2016 as (
with with_col_publico as (
    select
        "NU_ANO_CENSO" as "ANO"
        , "CO_MUNICIPIO" as "FK_MUNICIPIO_CODIGO"
        , case when "TP_DEPENDENCIA" in (1,2,3) then 1 else 0 end as PUBLICO
    from
        "postgres"."raw"."DIM_CENSO_EDUC_BASICA_DESAGREGADO_MATRICULA_11_2016"
    where
        "TP_ETAPA_ENSINO" in (30, 31, 32, 33, 34, 35, 36, 37, 38, 39)
),
ept_privado as (
    select
        "ANO"
        , "FK_MUNICIPIO_CODIGO"
        , count("FK_MUNICIPIO_CODIGO") as "EPT_PRIVADO"
    from
        with_col_publico
    where
        PUBLICO = 0
    group by "ANO", "FK_MUNICIPIO_CODIGO"
),
ept_publico as (
    select
        "ANO"
        , "FK_MUNICIPIO_CODIGO"
        , count("FK_MUNICIPIO_CODIGO") as "EPT_PUBLICO"
    from
        with_col_publico
    where
        PUBLICO = 1
    group by "ANO", "FK_MUNICIPIO_CODIGO"
),
matricula_ept as (
    select
        COALESCE(ept_publico."ANO", ept_privado."ANO") as "ANO"
        , COALESCE(ept_publico."FK_MUNICIPIO_CODIGO", ept_privado."FK_MUNICIPIO_CODIGO") as "FK_MUNICIPIO_CODIGO"
        , COALESCE(ept_publico."EPT_PUBLICO",0) as "EPT_PUBLICO"
        , COALESCE(ept_privado."EPT_PRIVADO", 0) as "EPT_PRIVADO"
    from ept_publico
    full join ept_privado
        on ept_publico."ANO" = ept_privado."ANO"
        and ept_publico."FK_MUNICIPIO_CODIGO" = ept_privado."FK_MUNICIPIO_CODIGO"

)
select * from matricula_ept
),  __dbt__cte__matricula_ept_2017 as (
with with_col_publico as (
    select
        "NU_ANO_CENSO" as "ANO"
        , "CO_MUNICIPIO" as "FK_MUNICIPIO_CODIGO"
        , case when "TP_DEPENDENCIA" in (1,2,3) then 1 else 0 end as PUBLICO
    from
        "postgres"."raw"."DIM_CENSO_EDUC_BASICA_DESAGREGADO_MATRICULA_11_2017"
    where
        "TP_ETAPA_ENSINO" in (30, 31, 32, 33, 34, 35, 36, 37, 38, 39)
),
ept_privado as (
    select
        "ANO"
        , "FK_MUNICIPIO_CODIGO"
        , count("FK_MUNICIPIO_CODIGO") as "EPT_PRIVADO"
    from
        with_col_publico
    where
        PUBLICO = 0
    group by "ANO", "FK_MUNICIPIO_CODIGO"
),
ept_publico as (
    select
        "ANO"
        , "FK_MUNICIPIO_CODIGO"
        , count("FK_MUNICIPIO_CODIGO") as "EPT_PUBLICO"
    from
        with_col_publico
    where
        PUBLICO = 1
    group by "ANO", "FK_MUNICIPIO_CODIGO"
),
matricula_ept as (
    select
        COALESCE(ept_publico."ANO", ept_privado."ANO") as "ANO"
        , COALESCE(ept_publico."FK_MUNICIPIO_CODIGO", ept_privado."FK_MUNICIPIO_CODIGO") as "FK_MUNICIPIO_CODIGO"
        , COALESCE(ept_publico."EPT_PUBLICO",0) as "EPT_PUBLICO"
        , COALESCE(ept_privado."EPT_PRIVADO", 0) as "EPT_PRIVADO"
    from ept_publico
    full join ept_privado
        on ept_publico."ANO" = ept_privado."ANO"
        and ept_publico."FK_MUNICIPIO_CODIGO" = ept_privado."FK_MUNICIPIO_CODIGO"

)
select * from matricula_ept
),  __dbt__cte__matricula_ept_2018 as (
with with_col_publico as (
    select
        "NU_ANO_CENSO" as "ANO"
        , "CO_MUNICIPIO" as "FK_MUNICIPIO_CODIGO"
        , case when "TP_DEPENDENCIA" in (1,2,3) then 1 else 0 end as PUBLICO
    from
        "postgres"."raw"."DIM_CENSO_EDUC_BASICA_DESAGREGADO_MATRICULA_11_2018"
    where
        "TP_ETAPA_ENSINO" in (30, 31, 32, 33, 34, 35, 36, 37, 38, 39)
),
ept_privado as (
    select
        "ANO"
        , "FK_MUNICIPIO_CODIGO"
        , count("FK_MUNICIPIO_CODIGO") as "EPT_PRIVADO"
    from
        with_col_publico
    where
        PUBLICO = 0
    group by "ANO", "FK_MUNICIPIO_CODIGO"
),
ept_publico as (
    select
        "ANO"
        , "FK_MUNICIPIO_CODIGO"
        , count("FK_MUNICIPIO_CODIGO") as "EPT_PUBLICO"
    from
        with_col_publico
    where
        PUBLICO = 1
    group by "ANO", "FK_MUNICIPIO_CODIGO"
),
matricula_ept as (
    select
        COALESCE(ept_publico."ANO", ept_privado."ANO") as "ANO"
        , COALESCE(ept_publico."FK_MUNICIPIO_CODIGO", ept_privado."FK_MUNICIPIO_CODIGO") as "FK_MUNICIPIO_CODIGO"
        , COALESCE(ept_publico."EPT_PUBLICO",0) as "EPT_PUBLICO"
        , COALESCE(ept_privado."EPT_PRIVADO", 0) as "EPT_PRIVADO"
    from ept_publico
    full join ept_privado
        on ept_publico."ANO" = ept_privado."ANO"
        and ept_publico."FK_MUNICIPIO_CODIGO" = ept_privado."FK_MUNICIPIO_CODIGO"

)
select * from matricula_ept
),  __dbt__cte__matricula_ept_2019 as (
with with_col_publico as (
    select
        "NU_ANO_CENSO" as "ANO"
        , "CO_MUNICIPIO" as "FK_MUNICIPIO_CODIGO"
        , case when "TP_DEPENDENCIA" in (1,2,3) then 1 else 0 end as PUBLICO
    from
        "postgres"."raw"."DIM_CENSO_EDUC_BASICA_DESAGREGADO_MATRICULA_11_2019"
    where
        "TP_ETAPA_ENSINO" in (30, 31, 32, 33, 34, 35, 36, 37, 38, 39)
),
ept_privado as (
    select
        "ANO"
        , "FK_MUNICIPIO_CODIGO"
        , count("FK_MUNICIPIO_CODIGO") as "EPT_PRIVADO"
    from
        with_col_publico
    where
        PUBLICO = 0
    group by "ANO", "FK_MUNICIPIO_CODIGO"
),
ept_publico as (
    select
        "ANO"
        , "FK_MUNICIPIO_CODIGO"
        , count("FK_MUNICIPIO_CODIGO") as "EPT_PUBLICO"
    from
        with_col_publico
    where
        PUBLICO = 1
    group by "ANO", "FK_MUNICIPIO_CODIGO"
),
matricula_ept as (
    select
        COALESCE(ept_publico."ANO", ept_privado."ANO") as "ANO"
        , COALESCE(ept_publico."FK_MUNICIPIO_CODIGO", ept_privado."FK_MUNICIPIO_CODIGO") as "FK_MUNICIPIO_CODIGO"
        , COALESCE(ept_publico."EPT_PUBLICO",0) as "EPT_PUBLICO"
        , COALESCE(ept_privado."EPT_PRIVADO", 0) as "EPT_PRIVADO"
    from ept_publico
    full join ept_privado
        on ept_publico."ANO" = ept_privado."ANO"
        and ept_publico."FK_MUNICIPIO_CODIGO" = ept_privado."FK_MUNICIPIO_CODIGO"

)
select * from matricula_ept
),  __dbt__cte__matricula_ept_2020 as (
with with_col_publico as (
    select
        "NU_ANO_CENSO" as "ANO"
        , "CO_MUNICIPIO" as "FK_MUNICIPIO_CODIGO"
        , case when "TP_DEPENDENCIA" in (1,2,3) then 1 else 0 end as PUBLICO
    from
        "postgres"."raw"."DIM_CENSO_EDUC_BASICA_DESAGREGADO_MATRICULA_11_2020"
    where
        "TP_ETAPA_ENSINO" in (30, 31, 32, 33, 34, 35, 36, 37, 38, 39)
),
ept_privado as (
    select
        "ANO"
        , "FK_MUNICIPIO_CODIGO"
        , count("FK_MUNICIPIO_CODIGO") as "EPT_PRIVADO"
    from
        with_col_publico
    where
        PUBLICO = 0
    group by "ANO", "FK_MUNICIPIO_CODIGO"
),
ept_publico as (
    select
        "ANO"
        , "FK_MUNICIPIO_CODIGO"
        , count("FK_MUNICIPIO_CODIGO") as "EPT_PUBLICO"
    from
        with_col_publico
    where
        PUBLICO = 1
    group by "ANO", "FK_MUNICIPIO_CODIGO"
),
matricula_ept as (
    select
        COALESCE(ept_publico."ANO", ept_privado."ANO") as "ANO"
        , COALESCE(ept_publico."FK_MUNICIPIO_CODIGO", ept_privado."FK_MUNICIPIO_CODIGO") as "FK_MUNICIPIO_CODIGO"
        , COALESCE(ept_publico."EPT_PUBLICO",0) as "EPT_PUBLICO"
        , COALESCE(ept_privado."EPT_PRIVADO", 0) as "EPT_PRIVADO"
    from ept_publico
    full join ept_privado
        on ept_publico."ANO" = ept_privado."ANO"
        and ept_publico."FK_MUNICIPIO_CODIGO" = ept_privado."FK_MUNICIPIO_CODIGO"

)
select * from matricula_ept
)select *
from __dbt__cte__matricula_ept_2014

UNION ALL




select *
from __dbt__cte__matricula_ept_2015

UNION ALL




select *
from __dbt__cte__matricula_ept_2016

UNION ALL




select *
from __dbt__cte__matricula_ept_2017

UNION ALL




select *
from __dbt__cte__matricula_ept_2018

UNION ALL




select *
from __dbt__cte__matricula_ept_2019

UNION ALL




select *
from __dbt__cte__matricula_ept_2020


