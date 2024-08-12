


SELECT
    "ANO",
    "FK_MUNICIPIO_CODIGO",
    COUNT("CO_PESSOA_FISICA") as "QT_PROF",
    SUM("POSSUI_POS") as "POSSUI_POS",
    SUM("POSSUI_FC") as "POSSUI_FC"
FROM
    (SELECT
        CAST("ANO_CENSO" AS INT) AS "ANO",
        CAST("FK_COD_MUNICIPIO" AS INT) AS "FK_MUNICIPIO_CODIGO",
        CAST("FK_COD_DOCENTE" AS BIGINT) AS "CO_PESSOA_FISICA",
        CASE
            WHEN
                "ID_ESPECIALIZACAO" = 1 OR
                "ID_MESTRADO" = 1 OR
                "ID_DOUTORADO" = 1
            THEN 1
            ELSE 0
        END AS "POSSUI_POS",
        CASE
            WHEN
                "ID_ESPECIFICO_CRECHE" = 1 OR
                "ID_ESPECIFICO_PRE_ESCOLA" = 1 OR
                "ID_ESPECIFICO_ANOS_INICIAIS" = 1 OR
                "ID_ESPECIFICO_ANOS_FINAIS" = 1 OR
                "ID_ESPECIFICO_ENS_MEDIO" = 1 OR
                "ID_ESPECIFICO_EJA" = 1 OR
                "ID_ESPECIFICO_NEC_ESP" = 1 OR
                "ID_ESPECIFICO_ED_INDIGENA" = 1 OR
                "ID_ESPECIFICO_CAMPO" = 1 OR
                "ID_ESPECIFICO_AMBIENTAL" = 1 OR
                "ID_ESPECIFICO_DIR_HUMANOS" = 1 OR
                "ID_ESPECIFICO_DIV_SEXUAL" = 1 OR
                "ID_ESPECIFICO_DIR_ADOLESC" = 1 OR
                "ID_ESPECIFICO_AFRO" = 1 OR
                "ID_ESPECIFICO_OUTROS" = 1
            THEN 1
            ELSE 0
        END AS "POSSUI_FC"
    FROM
        "postgres"."raw"."DIM_DOCENTES_NORTE_2014"
    ) AS TEMP
GROUP BY "ANO", "FK_MUNICIPIO_CODIGO"

UNION ALL


SELECT
    "ANO",
    "FK_MUNICIPIO_CODIGO",
    COUNT("CO_PESSOA_FISICA") as "QT_PROF",
    SUM("POSSUI_POS") as "POSSUI_POS",
    SUM("POSSUI_FC") as "POSSUI_FC"
FROM
    (SELECT
        CAST("ANO_CENSO" AS INT) AS "ANO",
        CAST("FK_COD_MUNICIPIO" AS INT) AS "FK_MUNICIPIO_CODIGO",
        CAST("FK_COD_DOCENTE" AS BIGINT) AS "CO_PESSOA_FISICA",
        CASE
            WHEN
                "ID_ESPECIALIZACAO" = 1 OR
                "ID_MESTRADO" = 1 OR
                "ID_DOUTORADO" = 1
            THEN 1
            ELSE 0
        END AS "POSSUI_POS",
        CASE
            WHEN
                "ID_ESPECIFICO_CRECHE" = 1 OR
                "ID_ESPECIFICO_PRE_ESCOLA" = 1 OR
                "ID_ESPECIFICO_ANOS_INICIAIS" = 1 OR
                "ID_ESPECIFICO_ANOS_FINAIS" = 1 OR
                "ID_ESPECIFICO_ENS_MEDIO" = 1 OR
                "ID_ESPECIFICO_EJA" = 1 OR
                "ID_ESPECIFICO_NEC_ESP" = 1 OR
                "ID_ESPECIFICO_ED_INDIGENA" = 1 OR
                "ID_ESPECIFICO_CAMPO" = 1 OR
                "ID_ESPECIFICO_AMBIENTAL" = 1 OR
                "ID_ESPECIFICO_DIR_HUMANOS" = 1 OR
                "ID_ESPECIFICO_DIV_SEXUAL" = 1 OR
                "ID_ESPECIFICO_DIR_ADOLESC" = 1 OR
                "ID_ESPECIFICO_AFRO" = 1 OR
                "ID_ESPECIFICO_OUTROS" = 1
            THEN 1
            ELSE 0
        END AS "POSSUI_FC"
    FROM
        "postgres"."raw"."DIM_DOCENTES_NORDESTE_2014"
    ) AS TEMP
GROUP BY "ANO", "FK_MUNICIPIO_CODIGO"

UNION ALL


SELECT
    "ANO",
    "FK_MUNICIPIO_CODIGO",
    COUNT("CO_PESSOA_FISICA") as "QT_PROF",
    SUM("POSSUI_POS") as "POSSUI_POS",
    SUM("POSSUI_FC") as "POSSUI_FC"
FROM
    (SELECT
        CAST("ANO_CENSO" AS INT) AS "ANO",
        CAST("FK_COD_MUNICIPIO" AS INT) AS "FK_MUNICIPIO_CODIGO",
        CAST("FK_COD_DOCENTE" AS BIGINT) AS "CO_PESSOA_FISICA",
        CASE
            WHEN
                "ID_ESPECIALIZACAO" = 1 OR
                "ID_MESTRADO" = 1 OR
                "ID_DOUTORADO" = 1
            THEN 1
            ELSE 0
        END AS "POSSUI_POS",
        CASE
            WHEN
                "ID_ESPECIFICO_CRECHE" = 1 OR
                "ID_ESPECIFICO_PRE_ESCOLA" = 1 OR
                "ID_ESPECIFICO_ANOS_INICIAIS" = 1 OR
                "ID_ESPECIFICO_ANOS_FINAIS" = 1 OR
                "ID_ESPECIFICO_ENS_MEDIO" = 1 OR
                "ID_ESPECIFICO_EJA" = 1 OR
                "ID_ESPECIFICO_NEC_ESP" = 1 OR
                "ID_ESPECIFICO_ED_INDIGENA" = 1 OR
                "ID_ESPECIFICO_CAMPO" = 1 OR
                "ID_ESPECIFICO_AMBIENTAL" = 1 OR
                "ID_ESPECIFICO_DIR_HUMANOS" = 1 OR
                "ID_ESPECIFICO_DIV_SEXUAL" = 1 OR
                "ID_ESPECIFICO_DIR_ADOLESC" = 1 OR
                "ID_ESPECIFICO_AFRO" = 1 OR
                "ID_ESPECIFICO_OUTROS" = 1
            THEN 1
            ELSE 0
        END AS "POSSUI_FC"
    FROM
        "postgres"."raw"."DIM_DOCENTES_CO_2014"
    ) AS TEMP
GROUP BY "ANO", "FK_MUNICIPIO_CODIGO"

UNION ALL


SELECT
    "ANO",
    "FK_MUNICIPIO_CODIGO",
    COUNT("CO_PESSOA_FISICA") as "QT_PROF",
    SUM("POSSUI_POS") as "POSSUI_POS",
    SUM("POSSUI_FC") as "POSSUI_FC"
FROM
    (SELECT
        CAST("ANO_CENSO" AS INT) AS "ANO",
        CAST("FK_COD_MUNICIPIO" AS INT) AS "FK_MUNICIPIO_CODIGO",
        CAST("FK_COD_DOCENTE" AS BIGINT) AS "CO_PESSOA_FISICA",
        CASE
            WHEN
                "ID_ESPECIALIZACAO" = 1 OR
                "ID_MESTRADO" = 1 OR
                "ID_DOUTORADO" = 1
            THEN 1
            ELSE 0
        END AS "POSSUI_POS",
        CASE
            WHEN
                "ID_ESPECIFICO_CRECHE" = 1 OR
                "ID_ESPECIFICO_PRE_ESCOLA" = 1 OR
                "ID_ESPECIFICO_ANOS_INICIAIS" = 1 OR
                "ID_ESPECIFICO_ANOS_FINAIS" = 1 OR
                "ID_ESPECIFICO_ENS_MEDIO" = 1 OR
                "ID_ESPECIFICO_EJA" = 1 OR
                "ID_ESPECIFICO_NEC_ESP" = 1 OR
                "ID_ESPECIFICO_ED_INDIGENA" = 1 OR
                "ID_ESPECIFICO_CAMPO" = 1 OR
                "ID_ESPECIFICO_AMBIENTAL" = 1 OR
                "ID_ESPECIFICO_DIR_HUMANOS" = 1 OR
                "ID_ESPECIFICO_DIV_SEXUAL" = 1 OR
                "ID_ESPECIFICO_DIR_ADOLESC" = 1 OR
                "ID_ESPECIFICO_AFRO" = 1 OR
                "ID_ESPECIFICO_OUTROS" = 1
            THEN 1
            ELSE 0
        END AS "POSSUI_FC"
    FROM
        "postgres"."raw"."DIM_DOCENTES_SUDESTE_2014"
    ) AS TEMP
GROUP BY "ANO", "FK_MUNICIPIO_CODIGO"

UNION ALL


SELECT
    "ANO",
    "FK_MUNICIPIO_CODIGO",
    COUNT("CO_PESSOA_FISICA") as "QT_PROF",
    SUM("POSSUI_POS") as "POSSUI_POS",
    SUM("POSSUI_FC") as "POSSUI_FC"
FROM
    (SELECT
        CAST("ANO_CENSO" AS INT) AS "ANO",
        CAST("FK_COD_MUNICIPIO" AS INT) AS "FK_MUNICIPIO_CODIGO",
        CAST("FK_COD_DOCENTE" AS BIGINT) AS "CO_PESSOA_FISICA",
        CASE
            WHEN
                "ID_ESPECIALIZACAO" = 1 OR
                "ID_MESTRADO" = 1 OR
                "ID_DOUTORADO" = 1
            THEN 1
            ELSE 0
        END AS "POSSUI_POS",
        CASE
            WHEN
                "ID_ESPECIFICO_CRECHE" = 1 OR
                "ID_ESPECIFICO_PRE_ESCOLA" = 1 OR
                "ID_ESPECIFICO_ANOS_INICIAIS" = 1 OR
                "ID_ESPECIFICO_ANOS_FINAIS" = 1 OR
                "ID_ESPECIFICO_ENS_MEDIO" = 1 OR
                "ID_ESPECIFICO_EJA" = 1 OR
                "ID_ESPECIFICO_NEC_ESP" = 1 OR
                "ID_ESPECIFICO_ED_INDIGENA" = 1 OR
                "ID_ESPECIFICO_CAMPO" = 1 OR
                "ID_ESPECIFICO_AMBIENTAL" = 1 OR
                "ID_ESPECIFICO_DIR_HUMANOS" = 1 OR
                "ID_ESPECIFICO_DIV_SEXUAL" = 1 OR
                "ID_ESPECIFICO_DIR_ADOLESC" = 1 OR
                "ID_ESPECIFICO_AFRO" = 1 OR
                "ID_ESPECIFICO_OUTROS" = 1
            THEN 1
            ELSE 0
        END AS "POSSUI_FC"
    FROM
        "postgres"."raw"."DIM_DOCENTES_SUL_2014"
    ) AS TEMP
GROUP BY "ANO", "FK_MUNICIPIO_CODIGO"

