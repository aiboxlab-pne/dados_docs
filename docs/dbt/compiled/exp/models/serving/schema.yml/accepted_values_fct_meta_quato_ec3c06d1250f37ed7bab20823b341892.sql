
    
    

with all_values as (

    select
        GRAU_ACADEMICO as value_field,
        count(*) as n_records

    from "postgres"."dbt_serving"."fct_meta_quatorze"
    group by GRAU_ACADEMICO

)

select *
from all_values
where value_field not in (
    'MESTRADO','DOUTORADO'
)


