
  
    

  create  table "postgres"."dbt_staging"."dim_censo_educ_basica_desagregado_matricula_4__dbt_tmp"
  
  
    as
  
  (
    

SELECT
    "ANO"
    , "FK_MUNICIPIO_CODIGO"
    , "IN_NECESSIDADE_ESPECIAL"
    , "IN_ESPECIAL_EXCLUSIVA"
    , "TP_ETAPA_ENSINO"
    , "TP_TIPO_TURMA"
    , COUNT(*) AS "COUNT_MATRICULA"
FROM (
    SELECT
        "NU_ANO_CENSO" as "ANO"
        , "NU_IDADE"
        , "CO_MUNICIPIO" as "FK_MUNICIPIO_CODIGO"
        , "IN_NECESSIDADE_ESPECIAL"
        , "IN_ESPECIAL_EXCLUSIVA"
        , "TP_ETAPA_ENSINO"
        , "TP_TIPO_TURMA"
    FROM
        "postgres"."raw"."DIM_CENSO_EDUC_BASICA_DESAGREGADO_MATRICULA_4_2014"
    WHERE
        "IN_NECESSIDADE_ESPECIAL" = 1
        AND "NU_IDADE" >= 4
        AND "NU_IDADE" <= 17
        AND "TP_ETAPA_ENSINO" IN (
            1, 2, 4, 5, 6, 7, 14, 15, 16, 17, 18, 8, 9, 10, 11, 19, 20, 21, 41,
            25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 68, 65,
            67, 69, 70, 71, 73, 74)
    ) as "ALL"
GROUP BY "ANO", "FK_MUNICIPIO_CODIGO", "IN_NECESSIDADE_ESPECIAL",
         "IN_ESPECIAL_EXCLUSIVA", "TP_ETAPA_ENSINO", "TP_TIPO_TURMA"

UNION ALL


SELECT
    "ANO"
    , "FK_MUNICIPIO_CODIGO"
    , "IN_NECESSIDADE_ESPECIAL"
    , "IN_ESPECIAL_EXCLUSIVA"
    , "TP_ETAPA_ENSINO"
    , "TP_TIPO_TURMA"
    , COUNT(*) AS "COUNT_MATRICULA"
FROM (
    SELECT
        "NU_ANO_CENSO" as "ANO"
        , "NU_IDADE"
        , "CO_MUNICIPIO" as "FK_MUNICIPIO_CODIGO"
        , "IN_NECESSIDADE_ESPECIAL"
        , "IN_ESPECIAL_EXCLUSIVA"
        , "TP_ETAPA_ENSINO"
        , "TP_TIPO_TURMA"
    FROM
        "postgres"."raw"."DIM_CENSO_EDUC_BASICA_DESAGREGADO_MATRICULA_4_2015"
    WHERE
        "IN_NECESSIDADE_ESPECIAL" = 1
        AND "NU_IDADE" >= 4
        AND "NU_IDADE" <= 17
        AND "TP_ETAPA_ENSINO" IN (
            1, 2, 4, 5, 6, 7, 14, 15, 16, 17, 18, 8, 9, 10, 11, 19, 20, 21, 41,
            25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 68, 65,
            67, 69, 70, 71, 73, 74)
    ) as "ALL"
GROUP BY "ANO", "FK_MUNICIPIO_CODIGO", "IN_NECESSIDADE_ESPECIAL",
         "IN_ESPECIAL_EXCLUSIVA", "TP_ETAPA_ENSINO", "TP_TIPO_TURMA"

UNION ALL


SELECT
    "ANO"
    , "FK_MUNICIPIO_CODIGO"
    , "IN_NECESSIDADE_ESPECIAL"
    , "IN_ESPECIAL_EXCLUSIVA"
    , "TP_ETAPA_ENSINO"
    , "TP_TIPO_TURMA"
    , COUNT(*) AS "COUNT_MATRICULA"
FROM (
    SELECT
        "NU_ANO_CENSO" as "ANO"
        , "NU_IDADE"
        , "CO_MUNICIPIO" as "FK_MUNICIPIO_CODIGO"
        , "IN_NECESSIDADE_ESPECIAL"
        , "IN_ESPECIAL_EXCLUSIVA"
        , "TP_ETAPA_ENSINO"
        , "TP_TIPO_TURMA"
    FROM
        "postgres"."raw"."DIM_CENSO_EDUC_BASICA_DESAGREGADO_MATRICULA_4_2016"
    WHERE
        "IN_NECESSIDADE_ESPECIAL" = 1
        AND "NU_IDADE" >= 4
        AND "NU_IDADE" <= 17
        AND "TP_ETAPA_ENSINO" IN (
            1, 2, 4, 5, 6, 7, 14, 15, 16, 17, 18, 8, 9, 10, 11, 19, 20, 21, 41,
            25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 68, 65,
            67, 69, 70, 71, 73, 74)
    ) as "ALL"
GROUP BY "ANO", "FK_MUNICIPIO_CODIGO", "IN_NECESSIDADE_ESPECIAL",
         "IN_ESPECIAL_EXCLUSIVA", "TP_ETAPA_ENSINO", "TP_TIPO_TURMA"

UNION ALL


SELECT
    "ANO"
    , "FK_MUNICIPIO_CODIGO"
    , "IN_NECESSIDADE_ESPECIAL"
    , "IN_ESPECIAL_EXCLUSIVA"
    , "TP_ETAPA_ENSINO"
    , "TP_TIPO_TURMA"
    , COUNT(*) AS "COUNT_MATRICULA"
FROM (
    SELECT
        "NU_ANO_CENSO" as "ANO"
        , "NU_IDADE"
        , "CO_MUNICIPIO" as "FK_MUNICIPIO_CODIGO"
        , "IN_NECESSIDADE_ESPECIAL"
        , "IN_ESPECIAL_EXCLUSIVA"
        , "TP_ETAPA_ENSINO"
        , "TP_TIPO_TURMA"
    FROM
        "postgres"."raw"."DIM_CENSO_EDUC_BASICA_DESAGREGADO_MATRICULA_4_2017"
    WHERE
        "IN_NECESSIDADE_ESPECIAL" = 1
        AND "NU_IDADE" >= 4
        AND "NU_IDADE" <= 17
        AND "TP_ETAPA_ENSINO" IN (
            1, 2, 4, 5, 6, 7, 14, 15, 16, 17, 18, 8, 9, 10, 11, 19, 20, 21, 41,
            25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 68, 65,
            67, 69, 70, 71, 73, 74)
    ) as "ALL"
GROUP BY "ANO", "FK_MUNICIPIO_CODIGO", "IN_NECESSIDADE_ESPECIAL",
         "IN_ESPECIAL_EXCLUSIVA", "TP_ETAPA_ENSINO", "TP_TIPO_TURMA"

UNION ALL


SELECT
    "ANO"
    , "FK_MUNICIPIO_CODIGO"
    , "IN_NECESSIDADE_ESPECIAL"
    , "IN_ESPECIAL_EXCLUSIVA"
    , "TP_ETAPA_ENSINO"
    , "TP_TIPO_TURMA"
    , COUNT(*) AS "COUNT_MATRICULA"
FROM (
    SELECT
        "NU_ANO_CENSO" as "ANO"
        , "NU_IDADE"
        , "CO_MUNICIPIO" as "FK_MUNICIPIO_CODIGO"
        , "IN_NECESSIDADE_ESPECIAL"
        , "IN_ESPECIAL_EXCLUSIVA"
        , "TP_ETAPA_ENSINO"
        , "TP_TIPO_TURMA"
    FROM
        "postgres"."raw"."DIM_CENSO_EDUC_BASICA_DESAGREGADO_MATRICULA_4_2018"
    WHERE
        "IN_NECESSIDADE_ESPECIAL" = 1
        AND "NU_IDADE" >= 4
        AND "NU_IDADE" <= 17
        AND "TP_ETAPA_ENSINO" IN (
            1, 2, 4, 5, 6, 7, 14, 15, 16, 17, 18, 8, 9, 10, 11, 19, 20, 21, 41,
            25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 68, 65,
            67, 69, 70, 71, 73, 74)
    ) as "ALL"
GROUP BY "ANO", "FK_MUNICIPIO_CODIGO", "IN_NECESSIDADE_ESPECIAL",
         "IN_ESPECIAL_EXCLUSIVA", "TP_ETAPA_ENSINO", "TP_TIPO_TURMA"



UNION ALL



SELECT
    "ANO"
    , "FK_MUNICIPIO_CODIGO"
    , "IN_NECESSIDADE_ESPECIAL"
    , "IN_ESPECIAL_EXCLUSIVA"
    , "TP_ETAPA_ENSINO"
    , "TP_TIPO_TURMA"
    , COUNT(*) AS "COUNT_MATRICULA"
FROM (
    SELECT
        "NU_ANO_CENSO" as "ANO"
        , "NU_IDADE"
        , "CO_MUNICIPIO" as "FK_MUNICIPIO_CODIGO"
        , "IN_NECESSIDADE_ESPECIAL"
        , "IN_ESPECIAL_EXCLUSIVA"
        , "TP_ETAPA_ENSINO"
        , "TP_TIPO_ATENDIMENTO_TURMA" as "TP_TIPO_TURMA"
    FROM
        "postgres"."raw"."DIM_CENSO_EDUC_BASICA_DESAGREGADO_MATRICULA_4_2019"
    WHERE
        "IN_NECESSIDADE_ESPECIAL" = 1
        AND "NU_IDADE" >= 4
        AND "NU_IDADE" <= 17
        AND "TP_ETAPA_ENSINO" IN (
            1, 2, 4, 5, 6, 7, 14, 15, 16, 17, 18, 8, 9, 10, 11, 19, 20, 21, 41,
            25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 68, 65,
            67, 69, 70, 71, 73, 74)
    ) as "ALL"
GROUP BY "ANO", "FK_MUNICIPIO_CODIGO", "IN_NECESSIDADE_ESPECIAL",
         "IN_ESPECIAL_EXCLUSIVA", "TP_ETAPA_ENSINO", "TP_TIPO_TURMA"

UNION ALL


SELECT
    "ANO"
    , "FK_MUNICIPIO_CODIGO"
    , "IN_NECESSIDADE_ESPECIAL"
    , "IN_ESPECIAL_EXCLUSIVA"
    , "TP_ETAPA_ENSINO"
    , "TP_TIPO_TURMA"
    , COUNT(*) AS "COUNT_MATRICULA"
FROM (
    SELECT
        "NU_ANO_CENSO" as "ANO"
        , "NU_IDADE"
        , "CO_MUNICIPIO" as "FK_MUNICIPIO_CODIGO"
        , "IN_NECESSIDADE_ESPECIAL"
        , "IN_ESPECIAL_EXCLUSIVA"
        , "TP_ETAPA_ENSINO"
        , "TP_TIPO_ATENDIMENTO_TURMA" as "TP_TIPO_TURMA"
    FROM
        "postgres"."raw"."DIM_CENSO_EDUC_BASICA_DESAGREGADO_MATRICULA_4_2020"
    WHERE
        "IN_NECESSIDADE_ESPECIAL" = 1
        AND "NU_IDADE" >= 4
        AND "NU_IDADE" <= 17
        AND "TP_ETAPA_ENSINO" IN (
            1, 2, 4, 5, 6, 7, 14, 15, 16, 17, 18, 8, 9, 10, 11, 19, 20, 21, 41,
            25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 68, 65,
            67, 69, 70, 71, 73, 74)
    ) as "ALL"
GROUP BY "ANO", "FK_MUNICIPIO_CODIGO", "IN_NECESSIDADE_ESPECIAL",
         "IN_ESPECIAL_EXCLUSIVA", "TP_ETAPA_ENSINO", "TP_TIPO_TURMA"


  );
  