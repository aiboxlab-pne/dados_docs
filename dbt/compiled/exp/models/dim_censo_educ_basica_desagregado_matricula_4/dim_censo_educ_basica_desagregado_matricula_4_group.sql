SELECT
    "ANO"
    , "NU_IDADE"
    , "FK_MUNICIPIO_CODIGO"
    , "IN_NECESSIDADE_ESPECIAL"
    , "IN_ESPECIAL_EXCLUSIVA"
    , "TP_ETAPA_ENSINO"
    , "TP_TIPO_TURMA"
    , COUNT(*) AS quantidade
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
    
    UNION ALL
    
    
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
    
    

    UNION ALL
    

    
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
    
    UNION ALL
    
    
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
    
    
) as "ALL"
GROUP BY "ANO", "FK_MUNICIPIO_CODIGO", "NU_IDADE", "IN_NECESSIDADE_ESPECIAL", "IN_ESPECIAL_EXCLUSIVA", "TP_ETAPA_ENSINO", "TP_TIPO_TURMA"