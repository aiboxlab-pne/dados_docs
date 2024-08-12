
    
    

with all_values as (

    select
        INDICADOR as value_field,
        count(*) as n_records

    from "postgres"."dbt_serving"."fct_meta_sete_estadual"
    group by INDICADOR

)

select *
from all_values
where value_field not in (
    '7A','7B','7C'
)


