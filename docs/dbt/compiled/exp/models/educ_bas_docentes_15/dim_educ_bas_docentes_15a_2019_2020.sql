-- 15 min
WITH FORMACOES_ADEQUADAS_LICENCIATURA as (
        SELECT "DISCIPLINA" as "DISCIPLINA_NOME","CURSO_COD","COM_PEDAGO"
        FROM "postgres"."raw"."DIM_FORMACAO_ADEQUADA"
        WHERE "COM_PEDAGO"=0),
    FORMACOES_ADEQUADAS_BACHARELADO as (
        SELECT "DISCIPLINA" as "DISCIPLINA_NOME","CURSO_COD","COM_PEDAGO"
        FROM "postgres"."raw"."DIM_FORMACAO_ADEQUADA"
        WHERE "COM_PEDAGO"=1),
    COMPLEMENTACAO_PEDAGOGICA as (
        SELECT "DISCIPLINA" as "DISCIPLINA_NOME_COMPL", "CO_AREA_COMPL"
        FROM "postgres"."raw"."DIM_COMPLEMENTACAO_PEDAGOGICA"),
    DOCENTES_RAW as (
        SELECT
            *,
            'MULTIDISCIPLINAR' as "DISCIPLINA_NOME",
            '1_ENSINO_INFANTIL' as "ETAPA",
            -- Cancel courses that "in progress"
            CASE WHEN "TP_SITUACAO_CURSO_1"=1 THEN "CO_CURSO_1" ELSE '' END AS "COD_CURSO_1",
            CASE WHEN "TP_SITUACAO_CURSO_2"=1 THEN "CO_CURSO_2" ELSE '' END AS "COD_CURSO_2",
            CASE WHEN "TP_SITUACAO_CURSO_3"=1 THEN "CO_CURSO_3" ELSE '' END AS "COD_CURSO_3"
        FROM
            (
            --  #}
            -- 
            
            
            
                
                SELECT
                    2019 as "ANO", "CO_MUNICIPIO" as "FK_MUNICIPIO_CODIGO",
                    "TP_ETAPA_ENSINO", "TP_DEPENDENCIA","TP_TIPO_DOCENTE", "CO_CURSO_1", "CO_CURSO_2", "CO_CURSO_3", "TP_SITUACAO_CURSO_1", "TP_SITUACAO_CURSO_2", "TP_SITUACAO_CURSO_3", "IN_DISC_LINGUA_PORTUGUESA", "IN_DISC_LINGUA_INGLES", "IN_DISC_LINGUA_ESPANHOL", "IN_DISC_LINGUA_FRANCES", "IN_DISC_LINGUA_OUTRA", "IN_DISC_ARTES", "IN_DISC_EDUCACAO_FISICA", "IN_DISC_MATEMATICA", "IN_DISC_CIENCIAS", "IN_DISC_QUIMICA", "IN_DISC_FISICA", "IN_DISC_BIOLOGIA", "IN_DISC_ESTUDOS_SOCIAIS", "IN_DISC_HISTORIA", "IN_DISC_GEOGRAFIA", "IN_DISC_SOCIOLOGIA", "IN_DISC_FILOSOFIA", "IN_DISC_ENSINO_RELIGIOSO", "CO_AREA_COMPL_PEDAGOGICA_1", "CO_AREA_COMPL_PEDAGOGICA_2", "CO_AREA_COMPL_PEDAGOGICA_3"
                FROM
                    "postgres"."raw"."DIM_DOCENTES_CO_2019"
                
                UNION ALL
                
                
                SELECT
                    2020 as "ANO", "CO_MUNICIPIO" as "FK_MUNICIPIO_CODIGO",
                    "TP_ETAPA_ENSINO", "TP_DEPENDENCIA","TP_TIPO_DOCENTE", "CO_CURSO_1", "CO_CURSO_2", "CO_CURSO_3", "TP_SITUACAO_CURSO_1", "TP_SITUACAO_CURSO_2", "TP_SITUACAO_CURSO_3", "IN_DISC_LINGUA_PORTUGUESA", "IN_DISC_LINGUA_INGLES", "IN_DISC_LINGUA_ESPANHOL", "IN_DISC_LINGUA_FRANCES", "IN_DISC_LINGUA_OUTRA", "IN_DISC_ARTES", "IN_DISC_EDUCACAO_FISICA", "IN_DISC_MATEMATICA", "IN_DISC_CIENCIAS", "IN_DISC_QUIMICA", "IN_DISC_FISICA", "IN_DISC_BIOLOGIA", "IN_DISC_ESTUDOS_SOCIAIS", "IN_DISC_HISTORIA", "IN_DISC_GEOGRAFIA", "IN_DISC_SOCIOLOGIA", "IN_DISC_FILOSOFIA", "IN_DISC_ENSINO_RELIGIOSO", "CO_AREA_COMPL_PEDAGOGICA_1", "CO_AREA_COMPL_PEDAGOGICA_2", "CO_AREA_COMPL_PEDAGOGICA_3"
                FROM
                    "postgres"."raw"."DIM_DOCENTES_CO_2020"
                
                
            
                UNION ALL
            
            
                
                SELECT
                    2019 as "ANO", "CO_MUNICIPIO" as "FK_MUNICIPIO_CODIGO",
                    "TP_ETAPA_ENSINO", "TP_DEPENDENCIA","TP_TIPO_DOCENTE", "CO_CURSO_1", "CO_CURSO_2", "CO_CURSO_3", "TP_SITUACAO_CURSO_1", "TP_SITUACAO_CURSO_2", "TP_SITUACAO_CURSO_3", "IN_DISC_LINGUA_PORTUGUESA", "IN_DISC_LINGUA_INGLES", "IN_DISC_LINGUA_ESPANHOL", "IN_DISC_LINGUA_FRANCES", "IN_DISC_LINGUA_OUTRA", "IN_DISC_ARTES", "IN_DISC_EDUCACAO_FISICA", "IN_DISC_MATEMATICA", "IN_DISC_CIENCIAS", "IN_DISC_QUIMICA", "IN_DISC_FISICA", "IN_DISC_BIOLOGIA", "IN_DISC_ESTUDOS_SOCIAIS", "IN_DISC_HISTORIA", "IN_DISC_GEOGRAFIA", "IN_DISC_SOCIOLOGIA", "IN_DISC_FILOSOFIA", "IN_DISC_ENSINO_RELIGIOSO", "CO_AREA_COMPL_PEDAGOGICA_1", "CO_AREA_COMPL_PEDAGOGICA_2", "CO_AREA_COMPL_PEDAGOGICA_3"
                FROM
                    "postgres"."raw"."DIM_DOCENTES_NORTE_2019"
                
                UNION ALL
                
                
                SELECT
                    2020 as "ANO", "CO_MUNICIPIO" as "FK_MUNICIPIO_CODIGO",
                    "TP_ETAPA_ENSINO", "TP_DEPENDENCIA","TP_TIPO_DOCENTE", "CO_CURSO_1", "CO_CURSO_2", "CO_CURSO_3", "TP_SITUACAO_CURSO_1", "TP_SITUACAO_CURSO_2", "TP_SITUACAO_CURSO_3", "IN_DISC_LINGUA_PORTUGUESA", "IN_DISC_LINGUA_INGLES", "IN_DISC_LINGUA_ESPANHOL", "IN_DISC_LINGUA_FRANCES", "IN_DISC_LINGUA_OUTRA", "IN_DISC_ARTES", "IN_DISC_EDUCACAO_FISICA", "IN_DISC_MATEMATICA", "IN_DISC_CIENCIAS", "IN_DISC_QUIMICA", "IN_DISC_FISICA", "IN_DISC_BIOLOGIA", "IN_DISC_ESTUDOS_SOCIAIS", "IN_DISC_HISTORIA", "IN_DISC_GEOGRAFIA", "IN_DISC_SOCIOLOGIA", "IN_DISC_FILOSOFIA", "IN_DISC_ENSINO_RELIGIOSO", "CO_AREA_COMPL_PEDAGOGICA_1", "CO_AREA_COMPL_PEDAGOGICA_2", "CO_AREA_COMPL_PEDAGOGICA_3"
                FROM
                    "postgres"."raw"."DIM_DOCENTES_NORTE_2020"
                
                
            
                UNION ALL
            
            
                
                SELECT
                    2019 as "ANO", "CO_MUNICIPIO" as "FK_MUNICIPIO_CODIGO",
                    "TP_ETAPA_ENSINO", "TP_DEPENDENCIA","TP_TIPO_DOCENTE", "CO_CURSO_1", "CO_CURSO_2", "CO_CURSO_3", "TP_SITUACAO_CURSO_1", "TP_SITUACAO_CURSO_2", "TP_SITUACAO_CURSO_3", "IN_DISC_LINGUA_PORTUGUESA", "IN_DISC_LINGUA_INGLES", "IN_DISC_LINGUA_ESPANHOL", "IN_DISC_LINGUA_FRANCES", "IN_DISC_LINGUA_OUTRA", "IN_DISC_ARTES", "IN_DISC_EDUCACAO_FISICA", "IN_DISC_MATEMATICA", "IN_DISC_CIENCIAS", "IN_DISC_QUIMICA", "IN_DISC_FISICA", "IN_DISC_BIOLOGIA", "IN_DISC_ESTUDOS_SOCIAIS", "IN_DISC_HISTORIA", "IN_DISC_GEOGRAFIA", "IN_DISC_SOCIOLOGIA", "IN_DISC_FILOSOFIA", "IN_DISC_ENSINO_RELIGIOSO", "CO_AREA_COMPL_PEDAGOGICA_1", "CO_AREA_COMPL_PEDAGOGICA_2", "CO_AREA_COMPL_PEDAGOGICA_3"
                FROM
                    "postgres"."raw"."DIM_DOCENTES_NORDESTE_2019"
                
                UNION ALL
                
                
                SELECT
                    2020 as "ANO", "CO_MUNICIPIO" as "FK_MUNICIPIO_CODIGO",
                    "TP_ETAPA_ENSINO", "TP_DEPENDENCIA","TP_TIPO_DOCENTE", "CO_CURSO_1", "CO_CURSO_2", "CO_CURSO_3", "TP_SITUACAO_CURSO_1", "TP_SITUACAO_CURSO_2", "TP_SITUACAO_CURSO_3", "IN_DISC_LINGUA_PORTUGUESA", "IN_DISC_LINGUA_INGLES", "IN_DISC_LINGUA_ESPANHOL", "IN_DISC_LINGUA_FRANCES", "IN_DISC_LINGUA_OUTRA", "IN_DISC_ARTES", "IN_DISC_EDUCACAO_FISICA", "IN_DISC_MATEMATICA", "IN_DISC_CIENCIAS", "IN_DISC_QUIMICA", "IN_DISC_FISICA", "IN_DISC_BIOLOGIA", "IN_DISC_ESTUDOS_SOCIAIS", "IN_DISC_HISTORIA", "IN_DISC_GEOGRAFIA", "IN_DISC_SOCIOLOGIA", "IN_DISC_FILOSOFIA", "IN_DISC_ENSINO_RELIGIOSO", "CO_AREA_COMPL_PEDAGOGICA_1", "CO_AREA_COMPL_PEDAGOGICA_2", "CO_AREA_COMPL_PEDAGOGICA_3"
                FROM
                    "postgres"."raw"."DIM_DOCENTES_NORDESTE_2020"
                
                
            
                UNION ALL
            
            
                
                SELECT
                    2019 as "ANO", "CO_MUNICIPIO" as "FK_MUNICIPIO_CODIGO",
                    "TP_ETAPA_ENSINO", "TP_DEPENDENCIA","TP_TIPO_DOCENTE", "CO_CURSO_1", "CO_CURSO_2", "CO_CURSO_3", "TP_SITUACAO_CURSO_1", "TP_SITUACAO_CURSO_2", "TP_SITUACAO_CURSO_3", "IN_DISC_LINGUA_PORTUGUESA", "IN_DISC_LINGUA_INGLES", "IN_DISC_LINGUA_ESPANHOL", "IN_DISC_LINGUA_FRANCES", "IN_DISC_LINGUA_OUTRA", "IN_DISC_ARTES", "IN_DISC_EDUCACAO_FISICA", "IN_DISC_MATEMATICA", "IN_DISC_CIENCIAS", "IN_DISC_QUIMICA", "IN_DISC_FISICA", "IN_DISC_BIOLOGIA", "IN_DISC_ESTUDOS_SOCIAIS", "IN_DISC_HISTORIA", "IN_DISC_GEOGRAFIA", "IN_DISC_SOCIOLOGIA", "IN_DISC_FILOSOFIA", "IN_DISC_ENSINO_RELIGIOSO", "CO_AREA_COMPL_PEDAGOGICA_1", "CO_AREA_COMPL_PEDAGOGICA_2", "CO_AREA_COMPL_PEDAGOGICA_3"
                FROM
                    "postgres"."raw"."DIM_DOCENTES_SUDESTE_2019"
                
                UNION ALL
                
                
                SELECT
                    2020 as "ANO", "CO_MUNICIPIO" as "FK_MUNICIPIO_CODIGO",
                    "TP_ETAPA_ENSINO", "TP_DEPENDENCIA","TP_TIPO_DOCENTE", "CO_CURSO_1", "CO_CURSO_2", "CO_CURSO_3", "TP_SITUACAO_CURSO_1", "TP_SITUACAO_CURSO_2", "TP_SITUACAO_CURSO_3", "IN_DISC_LINGUA_PORTUGUESA", "IN_DISC_LINGUA_INGLES", "IN_DISC_LINGUA_ESPANHOL", "IN_DISC_LINGUA_FRANCES", "IN_DISC_LINGUA_OUTRA", "IN_DISC_ARTES", "IN_DISC_EDUCACAO_FISICA", "IN_DISC_MATEMATICA", "IN_DISC_CIENCIAS", "IN_DISC_QUIMICA", "IN_DISC_FISICA", "IN_DISC_BIOLOGIA", "IN_DISC_ESTUDOS_SOCIAIS", "IN_DISC_HISTORIA", "IN_DISC_GEOGRAFIA", "IN_DISC_SOCIOLOGIA", "IN_DISC_FILOSOFIA", "IN_DISC_ENSINO_RELIGIOSO", "CO_AREA_COMPL_PEDAGOGICA_1", "CO_AREA_COMPL_PEDAGOGICA_2", "CO_AREA_COMPL_PEDAGOGICA_3"
                FROM
                    "postgres"."raw"."DIM_DOCENTES_SUDESTE_2020"
                
                
            
                UNION ALL
            
            
                
                SELECT
                    2019 as "ANO", "CO_MUNICIPIO" as "FK_MUNICIPIO_CODIGO",
                    "TP_ETAPA_ENSINO", "TP_DEPENDENCIA","TP_TIPO_DOCENTE", "CO_CURSO_1", "CO_CURSO_2", "CO_CURSO_3", "TP_SITUACAO_CURSO_1", "TP_SITUACAO_CURSO_2", "TP_SITUACAO_CURSO_3", "IN_DISC_LINGUA_PORTUGUESA", "IN_DISC_LINGUA_INGLES", "IN_DISC_LINGUA_ESPANHOL", "IN_DISC_LINGUA_FRANCES", "IN_DISC_LINGUA_OUTRA", "IN_DISC_ARTES", "IN_DISC_EDUCACAO_FISICA", "IN_DISC_MATEMATICA", "IN_DISC_CIENCIAS", "IN_DISC_QUIMICA", "IN_DISC_FISICA", "IN_DISC_BIOLOGIA", "IN_DISC_ESTUDOS_SOCIAIS", "IN_DISC_HISTORIA", "IN_DISC_GEOGRAFIA", "IN_DISC_SOCIOLOGIA", "IN_DISC_FILOSOFIA", "IN_DISC_ENSINO_RELIGIOSO", "CO_AREA_COMPL_PEDAGOGICA_1", "CO_AREA_COMPL_PEDAGOGICA_2", "CO_AREA_COMPL_PEDAGOGICA_3"
                FROM
                    "postgres"."raw"."DIM_DOCENTES_SUL_2019"
                
                UNION ALL
                
                
                SELECT
                    2020 as "ANO", "CO_MUNICIPIO" as "FK_MUNICIPIO_CODIGO",
                    "TP_ETAPA_ENSINO", "TP_DEPENDENCIA","TP_TIPO_DOCENTE", "CO_CURSO_1", "CO_CURSO_2", "CO_CURSO_3", "TP_SITUACAO_CURSO_1", "TP_SITUACAO_CURSO_2", "TP_SITUACAO_CURSO_3", "IN_DISC_LINGUA_PORTUGUESA", "IN_DISC_LINGUA_INGLES", "IN_DISC_LINGUA_ESPANHOL", "IN_DISC_LINGUA_FRANCES", "IN_DISC_LINGUA_OUTRA", "IN_DISC_ARTES", "IN_DISC_EDUCACAO_FISICA", "IN_DISC_MATEMATICA", "IN_DISC_CIENCIAS", "IN_DISC_QUIMICA", "IN_DISC_FISICA", "IN_DISC_BIOLOGIA", "IN_DISC_ESTUDOS_SOCIAIS", "IN_DISC_HISTORIA", "IN_DISC_GEOGRAFIA", "IN_DISC_SOCIOLOGIA", "IN_DISC_FILOSOFIA", "IN_DISC_ENSINO_RELIGIOSO", "CO_AREA_COMPL_PEDAGOGICA_1", "CO_AREA_COMPL_PEDAGOGICA_2", "CO_AREA_COMPL_PEDAGOGICA_3"
                FROM
                    "postgres"."raw"."DIM_DOCENTES_SUL_2020"
                
                
            
            
            ) as tbs_raw
        -- 'where clause' out of the loop was 15% faster than inside the loop
        WHERE "TP_ETAPA_ENSINO" in (1, 2, 3) and "TP_TIPO_DOCENTE" in (1, 5, 6)
        ),
    ADEQUACAO_BASE as (
        SELECT *,
            CASE WHEN EXISTS (
                    SELECT 1
                    FROM FORMACOES_ADEQUADAS_LICENCIATURA
                    WHERE FORMACOES_ADEQUADAS_LICENCIATURA."DISCIPLINA_NOME" = DOCENTES_RAW."DISCIPLINA_NOME" AND
                          FORMACOES_ADEQUADAS_LICENCIATURA."CURSO_COD" = DOCENTES_RAW."COD_CURSO_1"
                ) THEN 1 ELSE 0
            END AS "CURSO_1_ADEQUADO_LICEN",
            CASE WHEN EXISTS (
                    SELECT 1
                    FROM FORMACOES_ADEQUADAS_BACHARELADO
                    WHERE FORMACOES_ADEQUADAS_BACHARELADO."DISCIPLINA_NOME" = DOCENTES_RAW."DISCIPLINA_NOME" AND
                          FORMACOES_ADEQUADAS_BACHARELADO."CURSO_COD" = DOCENTES_RAW."COD_CURSO_1"
                ) THEN 1 ELSE 0
            END AS "CURSO_1_BACH",
            CASE WHEN EXISTS (
                    SELECT 1
                    FROM FORMACOES_ADEQUADAS_LICENCIATURA
                    WHERE FORMACOES_ADEQUADAS_LICENCIATURA."DISCIPLINA_NOME" = DOCENTES_RAW."DISCIPLINA_NOME" AND
                          FORMACOES_ADEQUADAS_LICENCIATURA."CURSO_COD" = DOCENTES_RAW."COD_CURSO_2"
                ) THEN 1 ELSE 0
            END AS "CURSO_2_ADEQUADO_LICEN",
            CASE WHEN EXISTS (
                    SELECT 1
                    FROM FORMACOES_ADEQUADAS_BACHARELADO
                    WHERE FORMACOES_ADEQUADAS_BACHARELADO."DISCIPLINA_NOME" = DOCENTES_RAW."DISCIPLINA_NOME" AND
                          FORMACOES_ADEQUADAS_BACHARELADO."CURSO_COD" = DOCENTES_RAW."COD_CURSO_2"
                ) THEN 1 ELSE 0
            END AS "CURSO_2_BACH",
            CASE WHEN EXISTS (
                    SELECT 1
                    FROM FORMACOES_ADEQUADAS_LICENCIATURA
                    WHERE FORMACOES_ADEQUADAS_LICENCIATURA."DISCIPLINA_NOME" = DOCENTES_RAW."DISCIPLINA_NOME" AND
                          FORMACOES_ADEQUADAS_LICENCIATURA."CURSO_COD" = DOCENTES_RAW."COD_CURSO_3"
                ) THEN 1 ELSE 0
            END AS "CURSO_3_ADEQUADO_LICEN",
            CASE WHEN EXISTS (
                    SELECT 1
                    FROM FORMACOES_ADEQUADAS_BACHARELADO
                    WHERE FORMACOES_ADEQUADAS_BACHARELADO."DISCIPLINA_NOME" = DOCENTES_RAW."DISCIPLINA_NOME" AND
                          FORMACOES_ADEQUADAS_BACHARELADO."CURSO_COD" = DOCENTES_RAW."COD_CURSO_3"
                ) THEN 1 ELSE 0
            END AS "CURSO_3_BACH"
        FROM
            DOCENTES_RAW),
    ADD_COMPL_PEDAGO_ADEQUADA as (
        SELECT *, "COMPL_1"."CO_AREA_COMPL" as "COD_COMPL_PEDAGOGICA_ADEQUADA"
        FROM ADEQUACAO_BASE
        LEFT JOIN COMPLEMENTACAO_PEDAGOGICA AS "COMPL_1" ON ADEQUACAO_BASE."DISCIPLINA_NOME" = "COMPL_1"."DISCIPLINA_NOME_COMPL"
    ),
    ADD_COMPL_PEDAGO_ADEQUADA2 as (
        SELECT *,
            CASE WHEN "CO_AREA_COMPL_PEDAGOGICA_1"="COD_COMPL_PEDAGOGICA_ADEQUADA" OR "CO_AREA_COMPL_PEDAGOGICA_2"="COD_COMPL_PEDAGOGICA_ADEQUADA" OR "CO_AREA_COMPL_PEDAGOGICA_3"="COD_COMPL_PEDAGOGICA_ADEQUADA"
                THEN 1 ELSE 0 END AS "FLAG_COMPL_PEDAGOGICA_ADEQUADA"
        FROM ADD_COMPL_PEDAGO_ADEQUADA
    ),
    ADEQUACAO_FINAL as (SELECT *,
            CASE WHEN "FLAG_COMPL_PEDAGOGICA_ADEQUADA"=1 AND "CURSO_1_BACH"=1 THEN 1 ELSE 0 END AS "CURSO_1_ADEQUADO_BACH",
            CASE WHEN "FLAG_COMPL_PEDAGOGICA_ADEQUADA"=1 AND "CURSO_2_BACH"=1 THEN 1 ELSE 0 END AS "CURSO_2_ADEQUADO_BACH",
            CASE WHEN "FLAG_COMPL_PEDAGOGICA_ADEQUADA"=1 AND "CURSO_3_BACH"=1 THEN 1 ELSE 0 END AS "CURSO_3_ADEQUADO_BACH"
        FROM ADD_COMPL_PEDAGO_ADEQUADA2
    ),
    CODIGOS_FORMACAO as(
        SELECT *,
            COALESCE("COD_CURSO_1", '') || '|' || COALESCE("COD_CURSO_2", '') || '|' || COALESCE("COD_CURSO_3", '') AS "CODIGO_FORMACAO_DRAFT",
            CASE WHEN "CURSO_1_ADEQUADO_LICEN"=1 OR "CURSO_1_ADEQUADO_BACH"=1 OR
                      "CURSO_2_ADEQUADO_LICEN"=1 OR "CURSO_2_ADEQUADO_BACH"=1 OR
                      "CURSO_3_ADEQUADO_LICEN"=1 OR "CURSO_3_ADEQUADO_BACH"=1
                      THEN 1 ELSE 0
                END AS "FORMACAO_ADEQUADA",
            1 as "DOCENCIA_TOTAL"
        FROM ADEQUACAO_FINAL),
    NOMES_FORMACAO as (
        SELECT *,
            COALESCE("FORMACAO_1"."CURSO", '') || '|' || COALESCE("FORMACAO_2"."CURSO", '') || '|' || COALESCE("FORMACAO_3"."CURSO", '') AS "NOME_FORMACAO_DRAFT"
        FROM CODIGOS_FORMACAO
        LEFT JOIN "postgres"."raw"."DIM_CURSO_SUPERIOR" AS "FORMACAO_1" ON CODIGOS_FORMACAO."COD_CURSO_1" = "FORMACAO_1"."CODIGO"
        LEFT JOIN "postgres"."raw"."DIM_CURSO_SUPERIOR" AS "FORMACAO_2" ON CODIGOS_FORMACAO."COD_CURSO_2" = "FORMACAO_2"."CODIGO"
        LEFT JOIN "postgres"."raw"."DIM_CURSO_SUPERIOR" AS "FORMACAO_3" ON CODIGOS_FORMACAO."COD_CURSO_3" = "FORMACAO_3"."CODIGO"),
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
    "FK_MUNICIPIO_CODIGO", "TP_DEPENDENCIA", "DISCIPLINA_NOME", "FORMACAO_ADEQUADA"