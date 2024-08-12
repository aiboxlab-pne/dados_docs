
  
    

  create  table "postgres"."dbt_staging"."dim_educ_bas_docentes_15c_2014_to_2018__dbt_tmp"
  
  
    as
  
  (
    WITH FORMACOES_ADEQUADAS_LICENCIATURA as (
        SELECT "DISCIPLINA" as "DISCIPLINA_NOME","CURSO_COD","COM_PEDAGO"
        FROM "postgres"."raw"."DIM_FORMACAO_ADEQUADA"
        WHERE "COM_PEDAGO"=0),
    FORMACOES_ADEQUADAS_BACHARELADO as (
        SELECT "DISCIPLINA" as "DISCIPLINA_NOME","CURSO_COD","COM_PEDAGO"
        FROM "postgres"."raw"."DIM_FORMACAO_ADEQUADA"
        WHERE "COM_PEDAGO"=1),
    DIM_CURSO_SUPERIOR as (
        SELECT "CURSO", "CODIGO"
        FROM "postgres"."raw"."DIM_CURSO_SUPERIOR"),
    DOCENTES_RAW as (
        SELECT
            CASE
                WHEN "TP_ETAPA_ENSINO" in (9, 10, 11, 12, 13, 19, 20, 21, 41, 22, 23, 24) THEN '3_FUND_ANOS_FINAIS'
                WHEN "TP_ETAPA_ENSINO" in (25, 26, 27, 28, 29, 35, 36, 37, 38) THEN '4_ENSINO_MEDIO'
                ELSE '' END AS "ETAPA",
            CASE
                WHEN "DISCIPLINA_NOME" IN ('IN_DISC_LINGUA_INGLES', 'IN_DISC_LINGUA_ESPANHOL', 'IN_DISC_LINGUA_FRANCES', 'IN_DISC_LINGUA_OUTRA') THEN 'IN_DISC_LINGUA_ESTRANGEIRA'
                ELSE "DISCIPLINA_NOME"
            END AS "DISCIPLINA_NOME",
            "ANO", "FK_MUNICIPIO_CODIGO", "TP_DEPENDENCIA", "TP_ETAPA_ENSINO", "TP_TIPO_DOCENTE", "COD_CURSO_1", "COD_CURSO_2", "COD_CURSO_3", "TP_SITUACAO_CURSO_1", "TP_SITUACAO_CURSO_2", "TP_SITUACAO_CURSO_3", "IN_COM_PEDAGOGICA_1", "IN_COM_PEDAGOGICA_2", "IN_COM_PEDAGOGICA_3"
        FROM
            "postgres"."dbt_staging"."dim_educ_bas_docentes_15_2014_to_2018_reshape_disc"
        WHERE "TP_ETAPA_ENSINO" in (9, 10, 11, 12, 13, 19, 20, 21, 41, 22, 23, 24, 25, 26, 27, 28, 29, 35, 36, 37, 38)),
    ADEQUACAO_BASE as (
        SELECT
            CASE WHEN "C_1_ADQ_LICEN_ESPECIFICA"=1 OR "C_1_ADQ_BACH_ESPECIFICA"=1 OR
                      "C_2_ADQ_LICEN_ESPECIFICA"=1 OR "C_2_ADQ_BACH_ESPECIFICA"=1 OR
                      "C_3_ADQ_LICEN_ESPECIFICA"=1 OR "C_3_ADQ_BACH_ESPECIFICA"=1
                      THEN 1 ELSE 0
                END AS "FORMACAO_ADEQUADA_ESPECIFICA",
            "DISCIPLINA_NOME", "ANO", "FK_MUNICIPIO_CODIGO", "TP_DEPENDENCIA", "TP_ETAPA_ENSINO", "TP_TIPO_DOCENTE", "COD_CURSO_1", "COD_CURSO_2", "COD_CURSO_3", "TP_SITUACAO_CURSO_1", "TP_SITUACAO_CURSO_2", "TP_SITUACAO_CURSO_3", "IN_COM_PEDAGOGICA_1", "IN_COM_PEDAGOGICA_2", "IN_COM_PEDAGOGICA_3", "ETAPA"
            --*
        FROM (
            SELECT *,
                CASE WHEN "IN_COM_PEDAGOGICA_1"=1 AND "C_1_ADQ_BACH_PRE_ESPECIFICA"=1 THEN 1 ELSE 0 END AS "C_1_ADQ_BACH_ESPECIFICA",
                CASE WHEN "IN_COM_PEDAGOGICA_2"=1 AND "C_2_ADQ_BACH_PRE_ESPECIFICA"=1 THEN 1 ELSE 0 END AS "C_2_ADQ_BACH_ESPECIFICA",
                CASE WHEN "IN_COM_PEDAGOGICA_3"=1 AND "C_3_ADQ_BACH_PRE_ESPECIFICA"=1 THEN 1 ELSE 0 END AS "C_3_ADQ_BACH_ESPECIFICA"
            FROM (
                SELECT *,
                    CASE WHEN EXISTS (
                            SELECT 1
                            FROM FORMACOES_ADEQUADAS_LICENCIATURA
                            WHERE FORMACOES_ADEQUADAS_LICENCIATURA."DISCIPLINA_NOME" = DOCENTES_RAW."DISCIPLINA_NOME" AND
                                  FORMACOES_ADEQUADAS_LICENCIATURA."CURSO_COD" = DOCENTES_RAW."COD_CURSO_1"
                        ) THEN 1 ELSE 0
                    END AS "C_1_ADQ_LICEN_ESPECIFICA",
                    CASE WHEN EXISTS (
                            SELECT 1
                            FROM FORMACOES_ADEQUADAS_LICENCIATURA
                            WHERE FORMACOES_ADEQUADAS_LICENCIATURA."DISCIPLINA_NOME" = DOCENTES_RAW."DISCIPLINA_NOME" AND
                                  FORMACOES_ADEQUADAS_LICENCIATURA."CURSO_COD" = DOCENTES_RAW."COD_CURSO_2"
                        ) THEN 1 ELSE 0
                    END AS "C_2_ADQ_LICEN_ESPECIFICA",
                    CASE WHEN EXISTS (
                            SELECT 1
                            FROM FORMACOES_ADEQUADAS_LICENCIATURA
                            WHERE FORMACOES_ADEQUADAS_LICENCIATURA."DISCIPLINA_NOME" = DOCENTES_RAW."DISCIPLINA_NOME" AND
                                  FORMACOES_ADEQUADAS_LICENCIATURA."CURSO_COD" = DOCENTES_RAW."COD_CURSO_3"
                        ) THEN 1 ELSE 0
                    END AS "C_3_ADQ_LICEN_ESPECIFICA",
                    CASE WHEN EXISTS (
                            SELECT 1
                            FROM FORMACOES_ADEQUADAS_BACHARELADO
                            WHERE FORMACOES_ADEQUADAS_BACHARELADO."DISCIPLINA_NOME" = DOCENTES_RAW."DISCIPLINA_NOME" AND
                                  FORMACOES_ADEQUADAS_BACHARELADO."CURSO_COD" = DOCENTES_RAW."COD_CURSO_1"
                        ) THEN 1 ELSE 0
                    END AS "C_1_ADQ_BACH_PRE_ESPECIFICA",
                    CASE WHEN EXISTS (
                            SELECT 1
                            FROM FORMACOES_ADEQUADAS_BACHARELADO
                            WHERE FORMACOES_ADEQUADAS_BACHARELADO."DISCIPLINA_NOME" = DOCENTES_RAW."DISCIPLINA_NOME" AND
                                  FORMACOES_ADEQUADAS_BACHARELADO."CURSO_COD" = DOCENTES_RAW."COD_CURSO_2"
                        ) THEN 1 ELSE 0
                    END AS "C_2_ADQ_BACH_PRE_ESPECIFICA",
                    CASE WHEN EXISTS (
                            SELECT 1
                            FROM FORMACOES_ADEQUADAS_BACHARELADO
                            WHERE FORMACOES_ADEQUADAS_BACHARELADO."DISCIPLINA_NOME" = DOCENTES_RAW."DISCIPLINA_NOME" AND
                                  FORMACOES_ADEQUADAS_BACHARELADO."CURSO_COD" = DOCENTES_RAW."COD_CURSO_3"
                        ) THEN 1 ELSE 0
                    END AS "C_3_ADQ_BACH_PRE_ESPECIFICA"
                FROM
                    DOCENTES_RAW) as adq_especifica_pre) as adq_especifica),
    ADEQUACAO_FINAL as (
        SELECT
            CASE WHEN "DISCIPLINA_NOME"='IN_DISC_LINGUA_ESTRANGEIRA' THEN "FORMACAO_ADEQUADA_ESPECIFICA" ELSE
            CASE WHEN "FORMACAO_ADEQUADA_ESPECIFICA"=1 THEN 1 ELSE 0
            END END AS "FORMACAO_ADEQUADA",
            1 as "DOCENCIA_TOTAL",
            *
        FROM ADEQUACAO_BASE),
    CODIGOS_FORMACAO as(
        SELECT
            CONCAT(COALESCE("COD_CURSO_1", ''), '|', COALESCE("COD_CURSO_2", ''), '|', COALESCE("COD_CURSO_3", '')) AS "CODIGO_FORMACAO_DRAFT",
            *
        FROM ADEQUACAO_FINAL),
    NOMES_FORMACAO as (
        SELECT
            CONCAT(COALESCE("FORMACAO_1"."CURSO", ''), '|', COALESCE("FORMACAO_2"."CURSO", ''), '|', COALESCE("FORMACAO_3"."CURSO", '')) AS "NOME_FORMACAO_DRAFT",
            *
        FROM CODIGOS_FORMACAO
        LEFT JOIN DIM_CURSO_SUPERIOR AS "FORMACAO_1" ON CODIGOS_FORMACAO."COD_CURSO_1" = "FORMACAO_1"."CODIGO"
        LEFT JOIN DIM_CURSO_SUPERIOR AS "FORMACAO_2" ON CODIGOS_FORMACAO."COD_CURSO_2" = "FORMACAO_2"."CODIGO"
        LEFT JOIN DIM_CURSO_SUPERIOR AS "FORMACAO_3" ON CODIGOS_FORMACAO."COD_CURSO_3" = "FORMACAO_3"."CODIGO"),
    RESULTADOS_FORMACAO_ADEQUADA as (
        SELECT
            "ANO", "ETAPA", "FK_MUNICIPIO_CODIGO", "TP_DEPENDENCIA", "DISCIPLINA_NOME",
            REGEXP_REPLACE("CODIGO_FORMACAO_DRAFT", '\|*$', '') AS "FORMACAO_COD",
            REGEXP_REPLACE("NOME_FORMACAO_DRAFT", '\|*$', '') AS "FORMACAO_NOME",
            "FORMACAO_ADEQUADA", "DOCENCIA_TOTAL"
        FROM NOMES_FORMACAO)

SELECT
    "ANO", "ETAPA", "FK_MUNICIPIO_CODIGO", "TP_DEPENDENCIA", "DISCIPLINA_NOME", "FORMACAO_COD", "FORMACAO_NOME",
    SUM("FORMACAO_ADEQUADA") AS "FORMACAO_ADEQUADA",
    SUM("DOCENCIA_TOTAL") AS "DOCENCIA_TOTAL"
FROM RESULTADOS_FORMACAO_ADEQUADA
GROUP BY
    "ANO", "FK_MUNICIPIO_CODIGO", "ETAPA", "TP_DEPENDENCIA", "DISCIPLINA_NOME", "FORMACAO_COD", "FORMACAO_NOME"
ORDER BY
    "FK_MUNICIPIO_CODIGO", "FORMACAO_ADEQUADA", "DISCIPLINA_NOME"
  );
  