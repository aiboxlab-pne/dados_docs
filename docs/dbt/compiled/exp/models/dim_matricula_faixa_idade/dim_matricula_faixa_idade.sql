SELECT
    CAST("NU_ANO_CENSO" AS INT) AS "ANO",
    CAST("CO_MUNICIPIO" AS INT) AS "FK_MUNICIPIO_CODIGO",
    CAST(SUM("QT_MAT_BAS_0_3") AS INT) AS "QT_MAT_0_3",
    CAST(SUM("QT_MAT_BAS_4_5") AS INT) AS "QT_MAT_4_5",
    CAST(SUM("QT_MAT_BAS_6_10") AS INT) AS "QT_MAT_6_10",
    CAST(SUM("QT_MAT_BAS_11_14") AS INT) AS "QT_MAT_11_14",
    CAST(SUM("QT_MAT_BAS_15_17") AS INT) AS "QT_MAT_15_17"
FROM (
    SELECT "NU_ANO_CENSO", "CO_MUNICIPIO", "QT_MAT_BAS_0_3", "QT_MAT_BAS_4_5", "QT_MAT_BAS_6_10", "QT_MAT_BAS_11_14", "QT_MAT_BAS_15_17" FROM "postgres"."raw"."DIM_MICRODADOS_ED_BASICA_2014"
    UNION ALL
    SELECT "NU_ANO_CENSO", "CO_MUNICIPIO", "QT_MAT_BAS_0_3", "QT_MAT_BAS_4_5", "QT_MAT_BAS_6_10", "QT_MAT_BAS_11_14", "QT_MAT_BAS_15_17" FROM "postgres"."raw"."DIM_MICRODADOS_ED_BASICA_2015"
    UNION ALL
    SELECT "NU_ANO_CENSO", "CO_MUNICIPIO", "QT_MAT_BAS_0_3", "QT_MAT_BAS_4_5", "QT_MAT_BAS_6_10", "QT_MAT_BAS_11_14", "QT_MAT_BAS_15_17" FROM "postgres"."raw"."DIM_MICRODADOS_ED_BASICA_2016"
    UNION ALL
    SELECT "NU_ANO_CENSO", "CO_MUNICIPIO", "QT_MAT_BAS_0_3", "QT_MAT_BAS_4_5", "QT_MAT_BAS_6_10", "QT_MAT_BAS_11_14", "QT_MAT_BAS_15_17" FROM "postgres"."raw"."DIM_MICRODADOS_ED_BASICA_2017"
    UNION ALL
    SELECT "NU_ANO_CENSO", "CO_MUNICIPIO", "QT_MAT_BAS_0_3", "QT_MAT_BAS_4_5", "QT_MAT_BAS_6_10", "QT_MAT_BAS_11_14", "QT_MAT_BAS_15_17" FROM "postgres"."raw"."DIM_MICRODADOS_ED_BASICA_2018"
    UNION ALL
    SELECT "NU_ANO_CENSO", "CO_MUNICIPIO", "QT_MAT_BAS_0_3", "QT_MAT_BAS_4_5", "QT_MAT_BAS_6_10", "QT_MAT_BAS_11_14", "QT_MAT_BAS_15_17" FROM "postgres"."raw"."DIM_MICRODADOS_ED_BASICA_2019"
    UNION ALL
    SELECT "NU_ANO_CENSO", "CO_MUNICIPIO", "QT_MAT_BAS_0_3", "QT_MAT_BAS_4_5", "QT_MAT_BAS_6_10", "QT_MAT_BAS_11_14", "QT_MAT_BAS_15_17" FROM "postgres"."raw"."DIM_MICRODADOS_ED_BASICA_2020"
    UNION ALL
    SELECT "NU_ANO_CENSO", "CO_MUNICIPIO", "QT_MAT_BAS_0_3", "QT_MAT_BAS_4_5", "QT_MAT_BAS_6_10", "QT_MAT_BAS_11_14", "QT_MAT_BAS_15_17" FROM "postgres"."raw"."DIM_MICRODADOS_ED_BASICA_2021"
) AS dim_matricula_faixa_idade
GROUP BY "NU_ANO_CENSO", "CO_MUNICIPIO"