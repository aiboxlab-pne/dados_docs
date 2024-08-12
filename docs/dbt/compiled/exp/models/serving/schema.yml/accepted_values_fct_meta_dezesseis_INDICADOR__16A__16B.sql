
    
    

with all_values as (

    select
        INDICADOR as value_field,
        count(*) as n_records

    from "postgres"."dbt_serving"."fct_meta_dezesseis"
    group by INDICADOR

)

select *
from all_values
where value_field not in (
    '16A','16B'
)


