


SELECT
    "NU_ANO_CENSO",
    "CO_MUNICIPIO",
    "TP_DEPENDENCIA",
    "TP_CARGO_GESTOR",
    "TP_TIPO_ACESSO_CARGO"
FROM
    "postgres"."raw"."DIM_CENSO_EDUC_BASICA_GESTOR_2019"

UNION ALL


SELECT
    "NU_ANO_CENSO",
    "CO_MUNICIPIO",
    "TP_DEPENDENCIA",
    "TP_CARGO_GESTOR",
    "TP_TIPO_ACESSO_CARGO"
FROM
    "postgres"."raw"."DIM_CENSO_EDUC_BASICA_GESTOR_2020"

