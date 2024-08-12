
  
    

  create  table "postgres"."dbt_staging"."dim_educ_bas_docentes_15_reshape_disciplinas__dbt_tmp"
  
  
    as
  
  (
    WITH DOCENTES_RAW as (
        SELECT
            *,
            '1_ENSINO_INFANTIL' as "ETAPA",
            -- Cancel courses that "in progress"
            CASE WHEN "TP_SITUACAO_CURSO_1"=1 THEN "CO_CURSO_1" ELSE '' END AS "COD_CURSO_1",
            CASE WHEN "TP_SITUACAO_CURSO_2"=1 THEN "CO_CURSO_2" ELSE '' END AS "COD_CURSO_2",
            CASE WHEN "TP_SITUACAO_CURSO_3"=1 THEN "CO_CURSO_3" ELSE '' END AS "COD_CURSO_3"
        FROM (
            
            
            
                
                SELECT
                    2014 as "ANO", "CO_MUNICIPIO" as "FK_MUNICIPIO_CODIGO",
                    "TP_ETAPA_ENSINO", "TP_DEPENDENCIA","TP_TIPO_DOCENTE", "CO_CURSO_1", "CO_CURSO_2", "CO_CURSO_3", "TP_SITUACAO_CURSO_1", "TP_SITUACAO_CURSO_2", "TP_SITUACAO_CURSO_3", "IN_DISC_LINGUA_PORTUGUESA", "IN_DISC_LINGUA_INGLES", "IN_DISC_LINGUA_ESPANHOL", "IN_DISC_LINGUA_FRANCES", "IN_DISC_LINGUA_OUTRA", "IN_DISC_ARTES", "IN_DISC_EDUCACAO_FISICA", "IN_DISC_MATEMATICA", "IN_DISC_CIENCIAS", "IN_DISC_QUIMICA", "IN_DISC_FISICA", "IN_DISC_BIOLOGIA", "IN_DISC_ESTUDOS_SOCIAIS", "IN_DISC_HISTORIA", "IN_DISC_GEOGRAFIA", "IN_DISC_SOCIOLOGIA", "IN_DISC_FILOSOFIA", "IN_DISC_ENSINO_RELIGIOSO", "IN_COM_PEDAGOGICA_1", "IN_COM_PEDAGOGICA_2", "IN_COM_PEDAGOGICA_3"
                FROM
                    "postgres"."raw"."DIM_DOCENTES_CO_2014"
                
                
            
            
            ) as temp
        WHERE "TP_ETAPA_ENSINO" in (4,5,6,7,8,14,15,16,17,18,9, 10, 11, 12, 13, 19, 20, 21, 41, 22, 23, 24,25, 26, 27, 28, 29, 35, 36, 37, 38) and "TP_TIPO_DOCENTE" in (1, 5, 6)
            ),
    RESHAPE_DISCIPLINAS as (
            
            
            SELECT 'IN_DISC_LINGUA_PORTUGUESA' as "DISCIPLINA_NOME",
                "ANO", "FK_MUNICIPIO_CODIGO", "TP_DEPENDENCIA", "TP_ETAPA_ENSINO", "TP_TIPO_DOCENTE", "CO_CURSO_1", "CO_CURSO_2", "CO_CURSO_3", "TP_SITUACAO_CURSO_1", "TP_SITUACAO_CURSO_2", "TP_SITUACAO_CURSO_3", "IN_COM_PEDAGOGICA_1", "IN_COM_PEDAGOGICA_2", "IN_COM_PEDAGOGICA_3"
            FROM DOCENTES_RAW
            WHERE "IN_DISC_LINGUA_PORTUGUESA"=1
            
            UNION ALL
            
            
            SELECT 'IN_DISC_LINGUA_INGLES' as "DISCIPLINA_NOME",
                "ANO", "FK_MUNICIPIO_CODIGO", "TP_DEPENDENCIA", "TP_ETAPA_ENSINO", "TP_TIPO_DOCENTE", "CO_CURSO_1", "CO_CURSO_2", "CO_CURSO_3", "TP_SITUACAO_CURSO_1", "TP_SITUACAO_CURSO_2", "TP_SITUACAO_CURSO_3", "IN_COM_PEDAGOGICA_1", "IN_COM_PEDAGOGICA_2", "IN_COM_PEDAGOGICA_3"
            FROM DOCENTES_RAW
            WHERE "IN_DISC_LINGUA_INGLES"=1
            
            
            )
SELECT
    *
FROM RESHAPE_DISCIPLINAS
  );
  