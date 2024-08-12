

SELECT
    CAST("NU_ANO_CENSO" AS INT) AS "ANO",
    CAST("CO_MUNICIPIO" AS INT) AS "FK_MUNICIPIO_CODIGO",
    CAST("TP_NIVEL_ACADEMICO" AS INT) AS "TP_NIVEL_ACADEMICO",
    CAST("TP_CATEGORIA_ADMINISTRATIVA" AS INT) AS "TP_CATEGORIA_ADMINISTRATIVA",
    CAST(SUM("QT_MAT") AS INT) AS "QT_MAT",
    CAST(SUM("QT_MAT_18_24") AS INT) AS "QT_MAT_18_24",
    CAST(SUM("QT_CONC_18_24") AS INT) AS "QT_CONC_18_24"
FROM (
    
    SELECT "NU_ANO_CENSO", "CO_MUNICIPIO", "TP_NIVEL_ACADEMICO",
           "TP_CATEGORIA_ADMINISTRATIVA", "QT_MAT", "QT_MAT_18_24",
           "QT_CONC_18_24"
    FROM "postgres"."raw"."DIM_EDUC_SUP_MATRICULA_2009"
    
    UNION ALL
   
   
    SELECT "NU_ANO_CENSO", "CO_MUNICIPIO", "TP_NIVEL_ACADEMICO",
           "TP_CATEGORIA_ADMINISTRATIVA", "QT_MAT", "QT_MAT_18_24",
           "QT_CONC_18_24"
    FROM "postgres"."raw"."DIM_EDUC_SUP_MATRICULA_2010"
    
    UNION ALL
   
   
    SELECT "NU_ANO_CENSO", "CO_MUNICIPIO", "TP_NIVEL_ACADEMICO",
           "TP_CATEGORIA_ADMINISTRATIVA", "QT_MAT", "QT_MAT_18_24",
           "QT_CONC_18_24"
    FROM "postgres"."raw"."DIM_EDUC_SUP_MATRICULA_2011"
    
    UNION ALL
   
   
    SELECT "NU_ANO_CENSO", "CO_MUNICIPIO", "TP_NIVEL_ACADEMICO",
           "TP_CATEGORIA_ADMINISTRATIVA", "QT_MAT", "QT_MAT_18_24",
           "QT_CONC_18_24"
    FROM "postgres"."raw"."DIM_EDUC_SUP_MATRICULA_2012"
    
    UNION ALL
   
   
    SELECT "NU_ANO_CENSO", "CO_MUNICIPIO", "TP_NIVEL_ACADEMICO",
           "TP_CATEGORIA_ADMINISTRATIVA", "QT_MAT", "QT_MAT_18_24",
           "QT_CONC_18_24"
    FROM "postgres"."raw"."DIM_EDUC_SUP_MATRICULA_2013"
    
    UNION ALL
   
   
    SELECT "NU_ANO_CENSO", "CO_MUNICIPIO", "TP_NIVEL_ACADEMICO",
           "TP_CATEGORIA_ADMINISTRATIVA", "QT_MAT", "QT_MAT_18_24",
           "QT_CONC_18_24"
    FROM "postgres"."raw"."DIM_EDUC_SUP_MATRICULA_2014"
    
    UNION ALL
   
   
    SELECT "NU_ANO_CENSO", "CO_MUNICIPIO", "TP_NIVEL_ACADEMICO",
           "TP_CATEGORIA_ADMINISTRATIVA", "QT_MAT", "QT_MAT_18_24",
           "QT_CONC_18_24"
    FROM "postgres"."raw"."DIM_EDUC_SUP_MATRICULA_2015"
    
    UNION ALL
   
   
    SELECT "NU_ANO_CENSO", "CO_MUNICIPIO", "TP_NIVEL_ACADEMICO",
           "TP_CATEGORIA_ADMINISTRATIVA", "QT_MAT", "QT_MAT_18_24",
           "QT_CONC_18_24"
    FROM "postgres"."raw"."DIM_EDUC_SUP_MATRICULA_2016"
    
    UNION ALL
   
   
    SELECT "NU_ANO_CENSO", "CO_MUNICIPIO", "TP_NIVEL_ACADEMICO",
           "TP_CATEGORIA_ADMINISTRATIVA", "QT_MAT", "QT_MAT_18_24",
           "QT_CONC_18_24"
    FROM "postgres"."raw"."DIM_EDUC_SUP_MATRICULA_2017"
    
    UNION ALL
   
   
    SELECT "NU_ANO_CENSO", "CO_MUNICIPIO", "TP_NIVEL_ACADEMICO",
           "TP_CATEGORIA_ADMINISTRATIVA", "QT_MAT", "QT_MAT_18_24",
           "QT_CONC_18_24"
    FROM "postgres"."raw"."DIM_EDUC_SUP_MATRICULA_2018"
    
    UNION ALL
   
   
    SELECT "NU_ANO_CENSO", "CO_MUNICIPIO", "TP_NIVEL_ACADEMICO",
           "TP_CATEGORIA_ADMINISTRATIVA", "QT_MAT", "QT_MAT_18_24",
           "QT_CONC_18_24"
    FROM "postgres"."raw"."DIM_EDUC_SUP_MATRICULA_2019"
    
    UNION ALL
   
   
    SELECT "NU_ANO_CENSO", "CO_MUNICIPIO", "TP_NIVEL_ACADEMICO",
           "TP_CATEGORIA_ADMINISTRATIVA", "QT_MAT", "QT_MAT_18_24",
           "QT_CONC_18_24"
    FROM "postgres"."raw"."DIM_EDUC_SUP_MATRICULA_2020"
    
    UNION ALL
   
   
    SELECT "NU_ANO_CENSO", "CO_MUNICIPIO", "TP_NIVEL_ACADEMICO",
           "TP_CATEGORIA_ADMINISTRATIVA", "QT_MAT", "QT_MAT_18_24",
           "QT_CONC_18_24"
    FROM "postgres"."raw"."DIM_EDUC_SUP_MATRICULA_2021"
    
    UNION ALL
   
   
    SELECT "NU_ANO_CENSO", "CO_MUNICIPIO", "TP_NIVEL_ACADEMICO",
           "TP_CATEGORIA_ADMINISTRATIVA", "QT_MAT", "QT_MAT_18_24",
           "QT_CONC_18_24"
    FROM "postgres"."raw"."DIM_EDUC_SUP_MATRICULA_2022"
    
   
) AS educ_sup_12
GROUP BY "NU_ANO_CENSO", "CO_MUNICIPIO", "TP_CATEGORIA_ADMINISTRATIVA", "TP_NIVEL_ACADEMICO"
ORDER BY "ANO", "FK_MUNICIPIO_CODIGO"