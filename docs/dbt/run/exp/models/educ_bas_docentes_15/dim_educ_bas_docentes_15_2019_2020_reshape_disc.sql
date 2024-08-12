
  
    

  create  table "postgres"."dbt_staging"."dim_educ_bas_docentes_15_2019_2020_reshape_disc__dbt_tmp"
  
  
    as
  
  (
    -- 9 min
WITH DOCENTES_RAW as (
        SELECT
            *,
            -- Cancel courses that "in progress"
            CASE WHEN "TP_SITUACAO_CURSO_1"=1 THEN "CO_CURSO_1" ELSE '' END AS "COD_CURSO_1",
            CASE WHEN "TP_SITUACAO_CURSO_2"=1 THEN "CO_CURSO_2" ELSE '' END AS "COD_CURSO_2",
            CASE WHEN "TP_SITUACAO_CURSO_3"=1 THEN "CO_CURSO_3" ELSE '' END AS "COD_CURSO_3"
        FROM (
            
            
            
                
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
                
                
            
            
            ) as temp
        WHERE "TP_ETAPA_ENSINO" in (4, 5, 6, 7, 8, 14, 15, 16, 17, 18, 9, 10, 11, 12, 13, 19, 20, 21, 41, 22, 23, 24,25, 26, 27, 28, 29, 35, 36, 37, 38) and "TP_TIPO_DOCENTE" in (1, 5, 6)
            ),
    RESHAPE_DISCIPLINAS as (
            
            
            SELECT DOCENTES_RAW.'IN_DISC_LINGUA_PORTUGUESA' as "DISCIPLINA_NOME",
                "ANO", "FK_MUNICIPIO_CODIGO", "TP_DEPENDENCIA", "TP_ETAPA_ENSINO", "TP_TIPO_DOCENTE", "COD_CURSO_1", "COD_CURSO_2", "COD_CURSO_3", "TP_SITUACAO_CURSO_1", "TP_SITUACAO_CURSO_2", "TP_SITUACAO_CURSO_3", "CO_AREA_COMPL_PEDAGOGICA_1", "CO_AREA_COMPL_PEDAGOGICA_2", "CO_AREA_COMPL_PEDAGOGICA_3"
            FROM DOCENTES_RAW
            WHERE "IN_DISC_LINGUA_PORTUGUESA"=1
            
            UNION ALL
            
            
            SELECT DOCENTES_RAW.'IN_DISC_LINGUA_INGLES' as "DISCIPLINA_NOME",
                "ANO", "FK_MUNICIPIO_CODIGO", "TP_DEPENDENCIA", "TP_ETAPA_ENSINO", "TP_TIPO_DOCENTE", "COD_CURSO_1", "COD_CURSO_2", "COD_CURSO_3", "TP_SITUACAO_CURSO_1", "TP_SITUACAO_CURSO_2", "TP_SITUACAO_CURSO_3", "CO_AREA_COMPL_PEDAGOGICA_1", "CO_AREA_COMPL_PEDAGOGICA_2", "CO_AREA_COMPL_PEDAGOGICA_3"
            FROM DOCENTES_RAW
            WHERE "IN_DISC_LINGUA_INGLES"=1
            
            UNION ALL
            
            
            SELECT DOCENTES_RAW.'IN_DISC_LINGUA_ESPANHOL' as "DISCIPLINA_NOME",
                "ANO", "FK_MUNICIPIO_CODIGO", "TP_DEPENDENCIA", "TP_ETAPA_ENSINO", "TP_TIPO_DOCENTE", "COD_CURSO_1", "COD_CURSO_2", "COD_CURSO_3", "TP_SITUACAO_CURSO_1", "TP_SITUACAO_CURSO_2", "TP_SITUACAO_CURSO_3", "CO_AREA_COMPL_PEDAGOGICA_1", "CO_AREA_COMPL_PEDAGOGICA_2", "CO_AREA_COMPL_PEDAGOGICA_3"
            FROM DOCENTES_RAW
            WHERE "IN_DISC_LINGUA_ESPANHOL"=1
            
            UNION ALL
            
            
            SELECT DOCENTES_RAW.'IN_DISC_LINGUA_FRANCES' as "DISCIPLINA_NOME",
                "ANO", "FK_MUNICIPIO_CODIGO", "TP_DEPENDENCIA", "TP_ETAPA_ENSINO", "TP_TIPO_DOCENTE", "COD_CURSO_1", "COD_CURSO_2", "COD_CURSO_3", "TP_SITUACAO_CURSO_1", "TP_SITUACAO_CURSO_2", "TP_SITUACAO_CURSO_3", "CO_AREA_COMPL_PEDAGOGICA_1", "CO_AREA_COMPL_PEDAGOGICA_2", "CO_AREA_COMPL_PEDAGOGICA_3"
            FROM DOCENTES_RAW
            WHERE "IN_DISC_LINGUA_FRANCES"=1
            
            UNION ALL
            
            
            SELECT DOCENTES_RAW.'IN_DISC_LINGUA_OUTRA' as "DISCIPLINA_NOME",
                "ANO", "FK_MUNICIPIO_CODIGO", "TP_DEPENDENCIA", "TP_ETAPA_ENSINO", "TP_TIPO_DOCENTE", "COD_CURSO_1", "COD_CURSO_2", "COD_CURSO_3", "TP_SITUACAO_CURSO_1", "TP_SITUACAO_CURSO_2", "TP_SITUACAO_CURSO_3", "CO_AREA_COMPL_PEDAGOGICA_1", "CO_AREA_COMPL_PEDAGOGICA_2", "CO_AREA_COMPL_PEDAGOGICA_3"
            FROM DOCENTES_RAW
            WHERE "IN_DISC_LINGUA_OUTRA"=1
            
            UNION ALL
            
            
            SELECT DOCENTES_RAW.'IN_DISC_ARTES' as "DISCIPLINA_NOME",
                "ANO", "FK_MUNICIPIO_CODIGO", "TP_DEPENDENCIA", "TP_ETAPA_ENSINO", "TP_TIPO_DOCENTE", "COD_CURSO_1", "COD_CURSO_2", "COD_CURSO_3", "TP_SITUACAO_CURSO_1", "TP_SITUACAO_CURSO_2", "TP_SITUACAO_CURSO_3", "CO_AREA_COMPL_PEDAGOGICA_1", "CO_AREA_COMPL_PEDAGOGICA_2", "CO_AREA_COMPL_PEDAGOGICA_3"
            FROM DOCENTES_RAW
            WHERE "IN_DISC_ARTES"=1
            
            UNION ALL
            
            
            SELECT DOCENTES_RAW.'IN_DISC_EDUCACAO_FISICA' as "DISCIPLINA_NOME",
                "ANO", "FK_MUNICIPIO_CODIGO", "TP_DEPENDENCIA", "TP_ETAPA_ENSINO", "TP_TIPO_DOCENTE", "COD_CURSO_1", "COD_CURSO_2", "COD_CURSO_3", "TP_SITUACAO_CURSO_1", "TP_SITUACAO_CURSO_2", "TP_SITUACAO_CURSO_3", "CO_AREA_COMPL_PEDAGOGICA_1", "CO_AREA_COMPL_PEDAGOGICA_2", "CO_AREA_COMPL_PEDAGOGICA_3"
            FROM DOCENTES_RAW
            WHERE "IN_DISC_EDUCACAO_FISICA"=1
            
            UNION ALL
            
            
            SELECT DOCENTES_RAW.'IN_DISC_MATEMATICA' as "DISCIPLINA_NOME",
                "ANO", "FK_MUNICIPIO_CODIGO", "TP_DEPENDENCIA", "TP_ETAPA_ENSINO", "TP_TIPO_DOCENTE", "COD_CURSO_1", "COD_CURSO_2", "COD_CURSO_3", "TP_SITUACAO_CURSO_1", "TP_SITUACAO_CURSO_2", "TP_SITUACAO_CURSO_3", "CO_AREA_COMPL_PEDAGOGICA_1", "CO_AREA_COMPL_PEDAGOGICA_2", "CO_AREA_COMPL_PEDAGOGICA_3"
            FROM DOCENTES_RAW
            WHERE "IN_DISC_MATEMATICA"=1
            
            UNION ALL
            
            
            SELECT DOCENTES_RAW.'IN_DISC_CIENCIAS' as "DISCIPLINA_NOME",
                "ANO", "FK_MUNICIPIO_CODIGO", "TP_DEPENDENCIA", "TP_ETAPA_ENSINO", "TP_TIPO_DOCENTE", "COD_CURSO_1", "COD_CURSO_2", "COD_CURSO_3", "TP_SITUACAO_CURSO_1", "TP_SITUACAO_CURSO_2", "TP_SITUACAO_CURSO_3", "CO_AREA_COMPL_PEDAGOGICA_1", "CO_AREA_COMPL_PEDAGOGICA_2", "CO_AREA_COMPL_PEDAGOGICA_3"
            FROM DOCENTES_RAW
            WHERE "IN_DISC_CIENCIAS"=1
            
            UNION ALL
            
            
            SELECT DOCENTES_RAW.'IN_DISC_QUIMICA' as "DISCIPLINA_NOME",
                "ANO", "FK_MUNICIPIO_CODIGO", "TP_DEPENDENCIA", "TP_ETAPA_ENSINO", "TP_TIPO_DOCENTE", "COD_CURSO_1", "COD_CURSO_2", "COD_CURSO_3", "TP_SITUACAO_CURSO_1", "TP_SITUACAO_CURSO_2", "TP_SITUACAO_CURSO_3", "CO_AREA_COMPL_PEDAGOGICA_1", "CO_AREA_COMPL_PEDAGOGICA_2", "CO_AREA_COMPL_PEDAGOGICA_3"
            FROM DOCENTES_RAW
            WHERE "IN_DISC_QUIMICA"=1
            
            UNION ALL
            
            
            SELECT DOCENTES_RAW.'IN_DISC_FISICA' as "DISCIPLINA_NOME",
                "ANO", "FK_MUNICIPIO_CODIGO", "TP_DEPENDENCIA", "TP_ETAPA_ENSINO", "TP_TIPO_DOCENTE", "COD_CURSO_1", "COD_CURSO_2", "COD_CURSO_3", "TP_SITUACAO_CURSO_1", "TP_SITUACAO_CURSO_2", "TP_SITUACAO_CURSO_3", "CO_AREA_COMPL_PEDAGOGICA_1", "CO_AREA_COMPL_PEDAGOGICA_2", "CO_AREA_COMPL_PEDAGOGICA_3"
            FROM DOCENTES_RAW
            WHERE "IN_DISC_FISICA"=1
            
            UNION ALL
            
            
            SELECT DOCENTES_RAW.'IN_DISC_BIOLOGIA' as "DISCIPLINA_NOME",
                "ANO", "FK_MUNICIPIO_CODIGO", "TP_DEPENDENCIA", "TP_ETAPA_ENSINO", "TP_TIPO_DOCENTE", "COD_CURSO_1", "COD_CURSO_2", "COD_CURSO_3", "TP_SITUACAO_CURSO_1", "TP_SITUACAO_CURSO_2", "TP_SITUACAO_CURSO_3", "CO_AREA_COMPL_PEDAGOGICA_1", "CO_AREA_COMPL_PEDAGOGICA_2", "CO_AREA_COMPL_PEDAGOGICA_3"
            FROM DOCENTES_RAW
            WHERE "IN_DISC_BIOLOGIA"=1
            
            UNION ALL
            
            
            SELECT DOCENTES_RAW.'IN_DISC_ESTUDOS_SOCIAIS' as "DISCIPLINA_NOME",
                "ANO", "FK_MUNICIPIO_CODIGO", "TP_DEPENDENCIA", "TP_ETAPA_ENSINO", "TP_TIPO_DOCENTE", "COD_CURSO_1", "COD_CURSO_2", "COD_CURSO_3", "TP_SITUACAO_CURSO_1", "TP_SITUACAO_CURSO_2", "TP_SITUACAO_CURSO_3", "CO_AREA_COMPL_PEDAGOGICA_1", "CO_AREA_COMPL_PEDAGOGICA_2", "CO_AREA_COMPL_PEDAGOGICA_3"
            FROM DOCENTES_RAW
            WHERE "IN_DISC_ESTUDOS_SOCIAIS"=1
            
            UNION ALL
            
            
            SELECT DOCENTES_RAW.'IN_DISC_HISTORIA' as "DISCIPLINA_NOME",
                "ANO", "FK_MUNICIPIO_CODIGO", "TP_DEPENDENCIA", "TP_ETAPA_ENSINO", "TP_TIPO_DOCENTE", "COD_CURSO_1", "COD_CURSO_2", "COD_CURSO_3", "TP_SITUACAO_CURSO_1", "TP_SITUACAO_CURSO_2", "TP_SITUACAO_CURSO_3", "CO_AREA_COMPL_PEDAGOGICA_1", "CO_AREA_COMPL_PEDAGOGICA_2", "CO_AREA_COMPL_PEDAGOGICA_3"
            FROM DOCENTES_RAW
            WHERE "IN_DISC_HISTORIA"=1
            
            UNION ALL
            
            
            SELECT DOCENTES_RAW.'IN_DISC_GEOGRAFIA' as "DISCIPLINA_NOME",
                "ANO", "FK_MUNICIPIO_CODIGO", "TP_DEPENDENCIA", "TP_ETAPA_ENSINO", "TP_TIPO_DOCENTE", "COD_CURSO_1", "COD_CURSO_2", "COD_CURSO_3", "TP_SITUACAO_CURSO_1", "TP_SITUACAO_CURSO_2", "TP_SITUACAO_CURSO_3", "CO_AREA_COMPL_PEDAGOGICA_1", "CO_AREA_COMPL_PEDAGOGICA_2", "CO_AREA_COMPL_PEDAGOGICA_3"
            FROM DOCENTES_RAW
            WHERE "IN_DISC_GEOGRAFIA"=1
            
            UNION ALL
            
            
            SELECT DOCENTES_RAW.'IN_DISC_SOCIOLOGIA' as "DISCIPLINA_NOME",
                "ANO", "FK_MUNICIPIO_CODIGO", "TP_DEPENDENCIA", "TP_ETAPA_ENSINO", "TP_TIPO_DOCENTE", "COD_CURSO_1", "COD_CURSO_2", "COD_CURSO_3", "TP_SITUACAO_CURSO_1", "TP_SITUACAO_CURSO_2", "TP_SITUACAO_CURSO_3", "CO_AREA_COMPL_PEDAGOGICA_1", "CO_AREA_COMPL_PEDAGOGICA_2", "CO_AREA_COMPL_PEDAGOGICA_3"
            FROM DOCENTES_RAW
            WHERE "IN_DISC_SOCIOLOGIA"=1
            
            UNION ALL
            
            
            SELECT DOCENTES_RAW.'IN_DISC_FILOSOFIA' as "DISCIPLINA_NOME",
                "ANO", "FK_MUNICIPIO_CODIGO", "TP_DEPENDENCIA", "TP_ETAPA_ENSINO", "TP_TIPO_DOCENTE", "COD_CURSO_1", "COD_CURSO_2", "COD_CURSO_3", "TP_SITUACAO_CURSO_1", "TP_SITUACAO_CURSO_2", "TP_SITUACAO_CURSO_3", "CO_AREA_COMPL_PEDAGOGICA_1", "CO_AREA_COMPL_PEDAGOGICA_2", "CO_AREA_COMPL_PEDAGOGICA_3"
            FROM DOCENTES_RAW
            WHERE "IN_DISC_FILOSOFIA"=1
            
            UNION ALL
            
            
            SELECT DOCENTES_RAW.'IN_DISC_ENSINO_RELIGIOSO' as "DISCIPLINA_NOME",
                "ANO", "FK_MUNICIPIO_CODIGO", "TP_DEPENDENCIA", "TP_ETAPA_ENSINO", "TP_TIPO_DOCENTE", "COD_CURSO_1", "COD_CURSO_2", "COD_CURSO_3", "TP_SITUACAO_CURSO_1", "TP_SITUACAO_CURSO_2", "TP_SITUACAO_CURSO_3", "CO_AREA_COMPL_PEDAGOGICA_1", "CO_AREA_COMPL_PEDAGOGICA_2", "CO_AREA_COMPL_PEDAGOGICA_3"
            FROM DOCENTES_RAW
            WHERE "IN_DISC_ENSINO_RELIGIOSO"=1
            
            
            )
SELECT
    *
FROM RESHAPE_DISCIPLINAS
  );
  