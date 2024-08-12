
    
    

with all_values as (

    select
        REDE as value_field,
        count(*) as n_records

    from "postgres"."dbt_serving"."fct_meta_sete_municipal"
    group by REDE

)

select *
from all_values
where value_field not in (
    'MUNICIPAL','PÚBLICA'
)


