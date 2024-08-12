

SELECT
   CAST("NU_ANO_CENSO" AS INT) AS "ANO",
   CAST("CO_MUNICIPIO" AS INT) AS "FK_MUNICIPIO_CODIGO",
   SUM("QT_MAT_INF_INT") AS "QT_MAT_INF_INT",
   SUM("QT_MAT_FUND_INT") AS "QT_MAT_FUND_INT",
   SUM("QT_MAT_MED_INT") AS "QT_MAT_MED_INT",
   SUM("QT_MAT_INF") AS "QT_MAT_INF",
   SUM("QT_MAT_FUND") AS "QT_MAT_FUND",
   SUM("QT_MAT_MED") AS "QT_MAT_MED"
FROM (
   
   SELECT "NU_ANO_CENSO", "CO_MUNICIPIO", "TP_DEPENDENCIA", "QT_MAT_INF_INT", "QT_MAT_FUND_INT", "QT_MAT_MED_INT", "QT_MAT_INF", "QT_MAT_FUND", "QT_MAT_MED" FROM "postgres"."raw"."DIM_MICRODADOS_ED_BASICA_2014" WHERE "TP_DEPENDENCIA"!=4
   
   UNION ALL
   
   
   SELECT "NU_ANO_CENSO", "CO_MUNICIPIO", "TP_DEPENDENCIA", "QT_MAT_INF_INT", "QT_MAT_FUND_INT", "QT_MAT_MED_INT", "QT_MAT_INF", "QT_MAT_FUND", "QT_MAT_MED" FROM "postgres"."raw"."DIM_MICRODADOS_ED_BASICA_2015" WHERE "TP_DEPENDENCIA"!=4
   
   UNION ALL
   
   
   SELECT "NU_ANO_CENSO", "CO_MUNICIPIO", "TP_DEPENDENCIA", "QT_MAT_INF_INT", "QT_MAT_FUND_INT", "QT_MAT_MED_INT", "QT_MAT_INF", "QT_MAT_FUND", "QT_MAT_MED" FROM "postgres"."raw"."DIM_MICRODADOS_ED_BASICA_2016" WHERE "TP_DEPENDENCIA"!=4
   
   UNION ALL
   
   
   SELECT "NU_ANO_CENSO", "CO_MUNICIPIO", "TP_DEPENDENCIA", "QT_MAT_INF_INT", "QT_MAT_FUND_INT", "QT_MAT_MED_INT", "QT_MAT_INF", "QT_MAT_FUND", "QT_MAT_MED" FROM "postgres"."raw"."DIM_MICRODADOS_ED_BASICA_2017" WHERE "TP_DEPENDENCIA"!=4
   
   UNION ALL
   
   
   SELECT "NU_ANO_CENSO", "CO_MUNICIPIO", "TP_DEPENDENCIA", "QT_MAT_INF_INT", "QT_MAT_FUND_INT", "QT_MAT_MED_INT", "QT_MAT_INF", "QT_MAT_FUND", "QT_MAT_MED" FROM "postgres"."raw"."DIM_MICRODADOS_ED_BASICA_2018" WHERE "TP_DEPENDENCIA"!=4
   
   UNION ALL
   
   
   SELECT "NU_ANO_CENSO", "CO_MUNICIPIO", "TP_DEPENDENCIA", "QT_MAT_INF_INT", "QT_MAT_FUND_INT", "QT_MAT_MED_INT", "QT_MAT_INF", "QT_MAT_FUND", "QT_MAT_MED" FROM "postgres"."raw"."DIM_MICRODADOS_ED_BASICA_2019" WHERE "TP_DEPENDENCIA"!=4
   
   UNION ALL
   
   
   SELECT "NU_ANO_CENSO", "CO_MUNICIPIO", "TP_DEPENDENCIA", "QT_MAT_INF_INT", "QT_MAT_FUND_INT", "QT_MAT_MED_INT", "QT_MAT_INF", "QT_MAT_FUND", "QT_MAT_MED" FROM "postgres"."raw"."DIM_MICRODADOS_ED_BASICA_2020" WHERE "TP_DEPENDENCIA"!=4
   
   UNION ALL
   
   
   SELECT "NU_ANO_CENSO", "CO_MUNICIPIO", "TP_DEPENDENCIA", "QT_MAT_INF_INT", "QT_MAT_FUND_INT", "QT_MAT_MED_INT", "QT_MAT_INF", "QT_MAT_FUND", "QT_MAT_MED" FROM "postgres"."raw"."DIM_MICRODADOS_ED_BASICA_2021" WHERE "TP_DEPENDENCIA"!=4
   
   
) AS matriculas_meta_6a
GROUP BY "NU_ANO_CENSO", "CO_MUNICIPIO"
ORDER BY "NU_ANO_CENSO", "FK_MUNICIPIO_CODIGO"