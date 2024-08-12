


SELECT
    "ANO",
    "FK_MUNICIPIO_CODIGO",
    COUNT("CO_PESSOA_FISICA") as "QT_PROF",
    SUM("POSSUI_POS") as "POSSUI_POS",
    SUM("POSSUI_FC") as "POSSUI_FC"
FROM
    (SELECT
        CAST("NU_ANO_CENSO" AS INT) AS "ANO",
        CAST("CO_MUNICIPIO" AS INT) AS "FK_MUNICIPIO_CODIGO",
        "ID_DOCENTE" AS "CO_PESSOA_FISICA",
        CASE
            WHEN
                "IN_ESPECIALIZACAO" = 1 OR
                "IN_MESTRADO" = 1 OR
                "IN_DOUTORADO" = 1
            THEN 1
            ELSE 0
        END AS "POSSUI_POS",
        CASE
            WHEN
                "IN_ESPECIFICO_CRECHE" = 1 OR
                "IN_ESPECIFICO_PRE_ESCOLA" = 1 OR
                "IN_ESPECIFICO_ANOS_INICIAIS" = 1 OR
                "IN_ESPECIFICO_ANOS_FINAIS" = 1 OR
                "IN_ESPECIFICO_ENS_MEDIO" = 1 OR
                "IN_ESPECIFICO_EJA" = 1 OR
                "IN_ESPECIFICO_ED_ESPECIAL" = 1 OR
                "IN_ESPECIFICO_ED_INDIGENA" = 1 OR
                "IN_ESPECIFICO_CAMPO" = 1 OR
                "IN_ESPECIFICO_AMBIENTAL" = 1 OR
                "IN_ESPECIFICO_DIR_HUMANOS" = 1 OR
                "IN_ESPECIFICO_DIV_SEXUAL" = 1 OR
                "IN_ESPECIFICO_DIR_ADOLESC" = 1 OR
                "IN_ESPECIFICO_AFRO" = 1 OR
                "IN_ESPECIFICO_OUTROS" = 1
            THEN 1
            ELSE 0
        END AS "POSSUI_FC"
    FROM
        "postgres"."raw"."DIM_DOCENTES_NORTE_2019"
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
        CAST("NU_ANO_CENSO" AS INT) AS "ANO",
        CAST("CO_MUNICIPIO" AS INT) AS "FK_MUNICIPIO_CODIGO",
        "ID_DOCENTE" AS "CO_PESSOA_FISICA",
        CASE
            WHEN
                "IN_ESPECIALIZACAO" = 1 OR
                "IN_MESTRADO" = 1 OR
                "IN_DOUTORADO" = 1
            THEN 1
            ELSE 0
        END AS "POSSUI_POS",
        CASE
            WHEN
                "IN_ESPECIFICO_CRECHE" = 1 OR
                "IN_ESPECIFICO_PRE_ESCOLA" = 1 OR
                "IN_ESPECIFICO_ANOS_INICIAIS" = 1 OR
                "IN_ESPECIFICO_ANOS_FINAIS" = 1 OR
                "IN_ESPECIFICO_ENS_MEDIO" = 1 OR
                "IN_ESPECIFICO_EJA" = 1 OR
                "IN_ESPECIFICO_ED_ESPECIAL" = 1 OR
                "IN_ESPECIFICO_ED_INDIGENA" = 1 OR
                "IN_ESPECIFICO_CAMPO" = 1 OR
                "IN_ESPECIFICO_AMBIENTAL" = 1 OR
                "IN_ESPECIFICO_DIR_HUMANOS" = 1 OR
                "IN_ESPECIFICO_DIV_SEXUAL" = 1 OR
                "IN_ESPECIFICO_DIR_ADOLESC" = 1 OR
                "IN_ESPECIFICO_AFRO" = 1 OR
                "IN_ESPECIFICO_OUTROS" = 1
            THEN 1
            ELSE 0
        END AS "POSSUI_FC"
    FROM
        "postgres"."raw"."DIM_DOCENTES_NORDESTE_2019"
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
        CAST("NU_ANO_CENSO" AS INT) AS "ANO",
        CAST("CO_MUNICIPIO" AS INT) AS "FK_MUNICIPIO_CODIGO",
        "ID_DOCENTE" AS "CO_PESSOA_FISICA",
        CASE
            WHEN
                "IN_ESPECIALIZACAO" = 1 OR
                "IN_MESTRADO" = 1 OR
                "IN_DOUTORADO" = 1
            THEN 1
            ELSE 0
        END AS "POSSUI_POS",
        CASE
            WHEN
                "IN_ESPECIFICO_CRECHE" = 1 OR
                "IN_ESPECIFICO_PRE_ESCOLA" = 1 OR
                "IN_ESPECIFICO_ANOS_INICIAIS" = 1 OR
                "IN_ESPECIFICO_ANOS_FINAIS" = 1 OR
                "IN_ESPECIFICO_ENS_MEDIO" = 1 OR
                "IN_ESPECIFICO_EJA" = 1 OR
                "IN_ESPECIFICO_ED_ESPECIAL" = 1 OR
                "IN_ESPECIFICO_ED_INDIGENA" = 1 OR
                "IN_ESPECIFICO_CAMPO" = 1 OR
                "IN_ESPECIFICO_AMBIENTAL" = 1 OR
                "IN_ESPECIFICO_DIR_HUMANOS" = 1 OR
                "IN_ESPECIFICO_DIV_SEXUAL" = 1 OR
                "IN_ESPECIFICO_DIR_ADOLESC" = 1 OR
                "IN_ESPECIFICO_AFRO" = 1 OR
                "IN_ESPECIFICO_OUTROS" = 1
            THEN 1
            ELSE 0
        END AS "POSSUI_FC"
    FROM
        "postgres"."raw"."DIM_DOCENTES_CO_2019"
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
        CAST("NU_ANO_CENSO" AS INT) AS "ANO",
        CAST("CO_MUNICIPIO" AS INT) AS "FK_MUNICIPIO_CODIGO",
        "ID_DOCENTE" AS "CO_PESSOA_FISICA",
        CASE
            WHEN
                "IN_ESPECIALIZACAO" = 1 OR
                "IN_MESTRADO" = 1 OR
                "IN_DOUTORADO" = 1
            THEN 1
            ELSE 0
        END AS "POSSUI_POS",
        CASE
            WHEN
                "IN_ESPECIFICO_CRECHE" = 1 OR
                "IN_ESPECIFICO_PRE_ESCOLA" = 1 OR
                "IN_ESPECIFICO_ANOS_INICIAIS" = 1 OR
                "IN_ESPECIFICO_ANOS_FINAIS" = 1 OR
                "IN_ESPECIFICO_ENS_MEDIO" = 1 OR
                "IN_ESPECIFICO_EJA" = 1 OR
                "IN_ESPECIFICO_ED_ESPECIAL" = 1 OR
                "IN_ESPECIFICO_ED_INDIGENA" = 1 OR
                "IN_ESPECIFICO_CAMPO" = 1 OR
                "IN_ESPECIFICO_AMBIENTAL" = 1 OR
                "IN_ESPECIFICO_DIR_HUMANOS" = 1 OR
                "IN_ESPECIFICO_DIV_SEXUAL" = 1 OR
                "IN_ESPECIFICO_DIR_ADOLESC" = 1 OR
                "IN_ESPECIFICO_AFRO" = 1 OR
                "IN_ESPECIFICO_OUTROS" = 1
            THEN 1
            ELSE 0
        END AS "POSSUI_FC"
    FROM
        "postgres"."raw"."DIM_DOCENTES_SUDESTE_2019"
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
        CAST("NU_ANO_CENSO" AS INT) AS "ANO",
        CAST("CO_MUNICIPIO" AS INT) AS "FK_MUNICIPIO_CODIGO",
        "ID_DOCENTE" AS "CO_PESSOA_FISICA",
        CASE
            WHEN
                "IN_ESPECIALIZACAO" = 1 OR
                "IN_MESTRADO" = 1 OR
                "IN_DOUTORADO" = 1
            THEN 1
            ELSE 0
        END AS "POSSUI_POS",
        CASE
            WHEN
                "IN_ESPECIFICO_CRECHE" = 1 OR
                "IN_ESPECIFICO_PRE_ESCOLA" = 1 OR
                "IN_ESPECIFICO_ANOS_INICIAIS" = 1 OR
                "IN_ESPECIFICO_ANOS_FINAIS" = 1 OR
                "IN_ESPECIFICO_ENS_MEDIO" = 1 OR
                "IN_ESPECIFICO_EJA" = 1 OR
                "IN_ESPECIFICO_ED_ESPECIAL" = 1 OR
                "IN_ESPECIFICO_ED_INDIGENA" = 1 OR
                "IN_ESPECIFICO_CAMPO" = 1 OR
                "IN_ESPECIFICO_AMBIENTAL" = 1 OR
                "IN_ESPECIFICO_DIR_HUMANOS" = 1 OR
                "IN_ESPECIFICO_DIV_SEXUAL" = 1 OR
                "IN_ESPECIFICO_DIR_ADOLESC" = 1 OR
                "IN_ESPECIFICO_AFRO" = 1 OR
                "IN_ESPECIFICO_OUTROS" = 1
            THEN 1
            ELSE 0
        END AS "POSSUI_FC"
    FROM
        "postgres"."raw"."DIM_DOCENTES_SUL_2019"
    ) AS TEMP
GROUP BY "ANO", "FK_MUNICIPIO_CODIGO"

