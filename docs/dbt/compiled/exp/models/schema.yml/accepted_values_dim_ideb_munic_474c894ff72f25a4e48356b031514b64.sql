
    
    

with all_values as (

    select
        ORIGEM as value_field,
        count(*) as n_records

    from "postgres"."dbt_staging"."dim_ideb_municipal"
    group by ORIGEM

)

select *
from all_values
where value_field not in (
    'anos_iniciais','anos_finais','ensino_medio'
)


