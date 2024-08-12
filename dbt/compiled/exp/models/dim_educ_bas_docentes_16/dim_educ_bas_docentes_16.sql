

SELECT *
FROM (
    
        SELECT * FROM "postgres"."dbt_staging"."dim_educ_bas_docentes_16_2014"
        
        UNION ALL
    
    
        SELECT * FROM "postgres"."dbt_staging"."dim_educ_bas_docentes_16_2015"
        
        UNION ALL
    
    
        SELECT * FROM "postgres"."dbt_staging"."dim_educ_bas_docentes_16_2016"
        
        UNION ALL
    
    
        SELECT * FROM "postgres"."dbt_staging"."dim_educ_bas_docentes_16_2017"
        
        UNION ALL
    
    
        SELECT * FROM "postgres"."dbt_staging"."dim_educ_bas_docentes_16_2018"
        
        UNION ALL
    
    
        SELECT * FROM "postgres"."dbt_staging"."dim_educ_bas_docentes_16_2019"
        
        UNION ALL
    
    
        SELECT * FROM "postgres"."dbt_staging"."dim_educ_bas_docentes_16_2020"
        
    
) as doc