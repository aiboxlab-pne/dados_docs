
  
    

  create  table "postgres"."dbt_staging"."ztest_15a_co_norte_2014_t2__dbt_tmp"
  
  
    as
  
  (
    WITH FORMACAO_ADEQUADA_LICEN as (
        SELECT "DISCIPLINA" as "DISCIPLINA_NOME","CURSO_COD","COM_PEDAGO"
        FROM "postgres"."raw"."DIM_FORMACAO_ADEQUADA"
        WHERE "COM_PEDAGO"=0),
    FORMACAO_ADEQUADA_BACH as (
        SELECT "DISCIPLINA" as "DISCIPLINA_NOME","CURSO_COD","COM_PEDAGO"
        FROM "postgres"."raw"."DIM_FORMACAO_ADEQUADA"
        WHERE "COM_PEDAGO"=1),
    TB_COD_CURSO as (
        SELECT
            "FK_MUNICIPIO_CODIGO", "TP_ETAPA_ENSINO", "TP_DEPENDENCIA","TP_TIPO_DOCENTE", "CO_CURSO_1", "CO_CURSO_2", "CO_CURSO_3", "TP_SITUACAO_CURSO_1", "TP_SITUACAO_CURSO_2", "TP_SITUACAO_CURSO_3", "IN_DISC_LINGUA_PORTUGUESA", "IN_DISC_LINGUA_INGLES", "IN_DISC_LINGUA_ESPANHOL", "IN_DISC_LINGUA_FRANCES", "IN_DISC_LINGUA_OUTRA", "IN_DISC_ARTES", "IN_DISC_EDUCACAO_FISICA", "IN_DISC_MATEMATICA", "IN_DISC_CIENCIAS", "IN_DISC_QUIMICA", "IN_DISC_FISICA", "IN_DISC_BIOLOGIA", "IN_DISC_ESTUDOS_SOCIAIS", "IN_DISC_HISTORIA", "IN_DISC_GEOGRAFIA", "IN_DISC_SOCIOLOGIA", "IN_DISC_FILOSOFIA", "IN_DISC_ENSINO_RELIGIOSO", "IN_COM_PEDAGOGICA_1", "IN_COM_PEDAGOGICA_2", "IN_COM_PEDAGOGICA_3",
            'MULTIDISCIPLINAR' as "DISCIPLINA_NOME",
            "ANO",
            '1_ENSINO_INFANTIL' as "ETAPA",
            CASE WHEN "TP_SITUACAO_CURSO_1"=1 THEN "CO_CURSO_1" ELSE '' END AS "COD_CURSO_1",
            CASE WHEN "TP_SITUACAO_CURSO_2"=1 THEN "CO_CURSO_2" ELSE '' END AS "COD_CURSO_2",
            CASE WHEN "TP_SITUACAO_CURSO_3"=1 THEN "CO_CURSO_3" ELSE '' END AS "COD_CURSO_3"
        FROM
            (
            
            
            
                
                SELECT
                    *, 2014 as "ANO", "CO_MUNICIPIO" as "FK_MUNICIPIO_CODIGO"
                FROM
                    "postgres"."raw"."DIM_DOCENTES_CO_2014"
                
                UNION ALL
                
                
                SELECT
                    *, 2015 as "ANO", "CO_MUNICIPIO" as "FK_MUNICIPIO_CODIGO"
                FROM
                    "postgres"."raw"."DIM_DOCENTES_CO_2015"
                
                
            
                UNION ALL
            
            
                
                SELECT
                    *, 2014 as "ANO", "CO_MUNICIPIO" as "FK_MUNICIPIO_CODIGO"
                FROM
                    "postgres"."raw"."DIM_DOCENTES_NORTE_2014"
                
                UNION ALL
                
                
                SELECT
                    *, 2015 as "ANO", "CO_MUNICIPIO" as "FK_MUNICIPIO_CODIGO"
                FROM
                    "postgres"."raw"."DIM_DOCENTES_NORTE_2015"
                
                
            
            
            ) as tbs_raw
        WHERE "TP_ETAPA_ENSINO" in (1, 2, 3) and "TP_TIPO_DOCENTE" in (1, 5, 6)),
    TB_MERGED as (
        SELECT *,
            CASE WHEN EXISTS (
                    SELECT 1
                    FROM FORMACAO_ADEQUADA_LICEN
                    WHERE FORMACAO_ADEQUADA_LICEN."DISCIPLINA_NOME" = "DISCIPLINA_NOME" AND
                          FORMACAO_ADEQUADA_LICEN."CURSO_COD" = "COD_CURSO_1"
                ) THEN 1 ELSE 0
            END AS "CURSO_1_ADEQUADO_LICEN",
            CASE WHEN EXISTS (
                    SELECT 1
                    FROM FORMACAO_ADEQUADA_BACH
                    WHERE FORMACAO_ADEQUADA_BACH."DISCIPLINA_NOME" = "DISCIPLINA_NOME" AND
                          FORMACAO_ADEQUADA_BACH."CURSO_COD" = "COD_CURSO_1"
                ) THEN 1 ELSE 0
            END AS "CURSO_1_BACH",
            CASE WHEN EXISTS (
                    SELECT 1
                    FROM FORMACAO_ADEQUADA_LICEN
                    WHERE FORMACAO_ADEQUADA_LICEN."DISCIPLINA_NOME" = "DISCIPLINA_NOME" AND
                          FORMACAO_ADEQUADA_LICEN."CURSO_COD" = "COD_CURSO_2"
                ) THEN 1 ELSE 0
            END AS "CURSO_2_ADEQUADO_LICEN",
            CASE WHEN EXISTS (
                    SELECT 1
                    FROM FORMACAO_ADEQUADA_BACH
                    WHERE FORMACAO_ADEQUADA_BACH."DISCIPLINA_NOME" = "DISCIPLINA_NOME" AND
                          FORMACAO_ADEQUADA_BACH."CURSO_COD" = "COD_CURSO_2"
                ) THEN 1 ELSE 0
            END AS "CURSO_2_BACH",
            CASE WHEN EXISTS (
                    SELECT 1
                    FROM FORMACAO_ADEQUADA_LICEN
                    WHERE FORMACAO_ADEQUADA_LICEN."DISCIPLINA_NOME" = "DISCIPLINA_NOME" AND
                          FORMACAO_ADEQUADA_LICEN."CURSO_COD" = "COD_CURSO_3"
                ) THEN 1 ELSE 0
            END AS "CURSO_3_ADEQUADO_LICEN",
            CASE WHEN EXISTS (
                    SELECT 1
                    FROM FORMACAO_ADEQUADA_BACH
                    WHERE FORMACAO_ADEQUADA_BACH."DISCIPLINA_NOME" = "DISCIPLINA_NOME" AND
                          FORMACAO_ADEQUADA_BACH."CURSO_COD" = "COD_CURSO_3"
                ) THEN 1 ELSE 0
            END AS "CURSO_3_BACH"
        FROM
            TB_COD_CURSO),
    TB_ADEQUACOES as (SELECT *,
            CASE WHEN "IN_COM_PEDAGOGICA_1"=1 AND "CURSO_1_BACH"=1 THEN 1 ELSE 0
                END AS "CURSO_1_ADEQUADO_BACH",
            CASE WHEN "IN_COM_PEDAGOGICA_2"=1 AND "CURSO_2_BACH"=1 THEN 1 ELSE 0
                END AS "CURSO_2_ADEQUADO_BACH",
            CASE WHEN "IN_COM_PEDAGOGICA_3"=1 AND "CURSO_3_BACH"=1 THEN 1 ELSE 0
                END AS "CURSO_3_ADEQUADO_BACH"
        FROM TB_MERGED),
    TB_CODIGO_FORMACAO as(
        SELECT *,
            COALESCE("COD_CURSO_1", '') || '|' || COALESCE("COD_CURSO_2", '') || '|' || COALESCE("COD_CURSO_3", '') AS "CODIGO_FORMACAO_DRAFT",
            CASE WHEN "CURSO_1_ADEQUADO_LICEN"=1 OR "CURSO_1_ADEQUADO_BACH"=1 OR
                      "CURSO_2_ADEQUADO_LICEN"=1 OR "CURSO_2_ADEQUADO_BACH"=1 OR
                      "CURSO_3_ADEQUADO_LICEN"=1 OR "CURSO_3_ADEQUADO_BACH"=1
                      THEN 1 ELSE 0
                END AS "FORMACAO_ADEQUADA",
            1 as "DOCENCIA_TOTAL"
        FROM TB_ADEQUACOES),
    TB_NOME_FORMACAO as (
        SELECT *,
            COALESCE("FORMACAO_1"."CURSO", '') || '|' || COALESCE("FORMACAO_2"."CURSO", '') || '|' || COALESCE("FORMACAO_3"."CURSO", '') AS "NOME_FORMACAO_DRAFT"
        FROM TB_CODIGO_FORMACAO
        LEFT JOIN "postgres"."raw"."DIM_CURSO_SUPERIOR" AS "FORMACAO_1"
        ON TB_CODIGO_FORMACAO."COD_CURSO_1" = "FORMACAO_1"."CODIGO"
        LEFT JOIN "postgres"."raw"."DIM_CURSO_SUPERIOR" AS "FORMACAO_2"
        ON TB_CODIGO_FORMACAO."COD_CURSO_2" = "FORMACAO_2"."CODIGO"
        LEFT JOIN "postgres"."raw"."DIM_CURSO_SUPERIOR" AS "FORMACAO_3"
        ON TB_CODIGO_FORMACAO."COD_CURSO_3" = "FORMACAO_3"."CODIGO"),
    TB_CONTINUO as (
        SELECT
            "ANO", "ETAPA", "FK_MUNICIPIO_CODIGO", "TP_DEPENDENCIA", "DISCIPLINA_NOME",
            REGEXP_REPLACE("CODIGO_FORMACAO_DRAFT", '\|*$', '') AS "FORMACAO_COD",
            REGEXP_REPLACE("NOME_FORMACAO_DRAFT", '\|*$', '') AS "FORMACAO_NOME",
            "FORMACAO_ADEQUADA", "DOCENCIA_TOTAL"
        FROM TB_NOME_FORMACAO)

SELECT
    "ANO", "ETAPA", "FK_MUNICIPIO_CODIGO", "TP_DEPENDENCIA", "DISCIPLINA_NOME", "FORMACAO_COD", "FORMACAO_NOME",
    SUM("FORMACAO_ADEQUADA") AS "FORMACAO_ADEQUADA",
    SUM("DOCENCIA_TOTAL") AS "DOCENCIA_TOTAL"
FROM TB_CONTINUO
GROUP BY
    "ANO", "ETAPA", "FK_MUNICIPIO_CODIGO", "TP_DEPENDENCIA", "DISCIPLINA_NOME", "FORMACAO_COD", "FORMACAO_NOME"
ORDER BY
    "FK_MUNICIPIO_CODIGO", "TP_DEPENDENCIA", "DISCIPLINA_NOME", "FORMACAO_ADEQUADA"
  );
  