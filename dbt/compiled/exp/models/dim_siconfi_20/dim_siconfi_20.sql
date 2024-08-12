


SELECT
    *
FROM
    (SELECT
        2013 AS "ANO",
        CAST("COD_IBGE" AS INT) AS "FK_MUNICIPIO_CODIGO",
        "CONTA",
        SUM("VALOR") as "VALOR"
    FROM
        "postgres"."raw"."DIM_SICONFI_MUN_DESPESASPORFUNCAO_2013"
    WHERE
        "CONTA" IN ('12 - Educação', '28.847 - Transferências para a Educação Básica')
    GROUP BY "ANO", "COD_IBGE", "CONTA"
    ORDER BY "ANO", "FK_MUNICIPIO_CODIGO") AS TEMP
    
    UNION ALL


SELECT
    *
FROM
    (SELECT
        2014 AS "ANO",
        CAST("COD_IBGE" AS INT) AS "FK_MUNICIPIO_CODIGO",
        "CONTA",
        SUM("VALOR") as "VALOR"
    FROM
        "postgres"."raw"."DIM_SICONFI_MUN_DESPESASPORFUNCAO_2014"
    WHERE
        "CONTA" IN ('12 - Educação', '28.847 - Transferências para a Educação Básica')
    GROUP BY "ANO", "COD_IBGE", "CONTA"
    ORDER BY "ANO", "FK_MUNICIPIO_CODIGO") AS TEMP
    
    UNION ALL


SELECT
    *
FROM
    (SELECT
        2015 AS "ANO",
        CAST("COD_IBGE" AS INT) AS "FK_MUNICIPIO_CODIGO",
        "CONTA",
        SUM("VALOR") as "VALOR"
    FROM
        "postgres"."raw"."DIM_SICONFI_MUN_DESPESASPORFUNCAO_2015"
    WHERE
        "CONTA" IN ('12 - Educação', '28.847 - Transferências para a Educação Básica')
    GROUP BY "ANO", "COD_IBGE", "CONTA"
    ORDER BY "ANO", "FK_MUNICIPIO_CODIGO") AS TEMP
    
    UNION ALL


SELECT
    *
FROM
    (SELECT
        2016 AS "ANO",
        CAST("COD_IBGE" AS INT) AS "FK_MUNICIPIO_CODIGO",
        "CONTA",
        SUM("VALOR") as "VALOR"
    FROM
        "postgres"."raw"."DIM_SICONFI_MUN_DESPESASPORFUNCAO_2016"
    WHERE
        "CONTA" IN ('12 - Educação', '28.847 - Transferências para a Educação Básica')
    GROUP BY "ANO", "COD_IBGE", "CONTA"
    ORDER BY "ANO", "FK_MUNICIPIO_CODIGO") AS TEMP
    
    UNION ALL


SELECT
    *
FROM
    (SELECT
        2017 AS "ANO",
        CAST("COD_IBGE" AS INT) AS "FK_MUNICIPIO_CODIGO",
        "CONTA",
        SUM("VALOR") as "VALOR"
    FROM
        "postgres"."raw"."DIM_SICONFI_MUN_DESPESASPORFUNCAO_2017"
    WHERE
        "CONTA" IN ('12 - Educação', '28.847 - Transferências para a Educação Básica')
    GROUP BY "ANO", "COD_IBGE", "CONTA"
    ORDER BY "ANO", "FK_MUNICIPIO_CODIGO") AS TEMP
    
    UNION ALL


SELECT
    *
FROM
    (SELECT
        2018 AS "ANO",
        CAST("COD_IBGE" AS INT) AS "FK_MUNICIPIO_CODIGO",
        "CONTA",
        SUM("VALOR") as "VALOR"
    FROM
        "postgres"."raw"."DIM_SICONFI_MUN_DESPESASPORFUNCAO_2018"
    WHERE
        "CONTA" IN ('12 - Educação', '28.847 - Transferências para a Educação Básica')
    GROUP BY "ANO", "COD_IBGE", "CONTA"
    ORDER BY "ANO", "FK_MUNICIPIO_CODIGO") AS TEMP
    
    UNION ALL


SELECT
    *
FROM
    (SELECT
        2019 AS "ANO",
        CAST("COD_IBGE" AS INT) AS "FK_MUNICIPIO_CODIGO",
        "CONTA",
        SUM("VALOR") as "VALOR"
    FROM
        "postgres"."raw"."DIM_SICONFI_MUN_DESPESASPORFUNCAO_2019"
    WHERE
        "CONTA" IN ('12 - Educação', '28.847 - Transferências para a Educação Básica')
    GROUP BY "ANO", "COD_IBGE", "CONTA"
    ORDER BY "ANO", "FK_MUNICIPIO_CODIGO") AS TEMP
    
    UNION ALL


SELECT
    *
FROM
    (SELECT
        2020 AS "ANO",
        CAST("COD_IBGE" AS INT) AS "FK_MUNICIPIO_CODIGO",
        "CONTA",
        SUM("VALOR") as "VALOR"
    FROM
        "postgres"."raw"."DIM_SICONFI_MUN_DESPESASPORFUNCAO_2020"
    WHERE
        "CONTA" IN ('12 - Educação', '28.847 - Transferências para a Educação Básica')
    GROUP BY "ANO", "COD_IBGE", "CONTA"
    ORDER BY "ANO", "FK_MUNICIPIO_CODIGO") AS TEMP
    
    UNION ALL


SELECT
    *
FROM
    (SELECT
        2021 AS "ANO",
        CAST("COD_IBGE" AS INT) AS "FK_MUNICIPIO_CODIGO",
        "CONTA",
        SUM("VALOR") as "VALOR"
    FROM
        "postgres"."raw"."DIM_SICONFI_MUN_DESPESASPORFUNCAO_2021"
    WHERE
        "CONTA" IN ('12 - Educação', '28.847 - Transferências para a Educação Básica')
    GROUP BY "ANO", "COD_IBGE", "CONTA"
    ORDER BY "ANO", "FK_MUNICIPIO_CODIGO") AS TEMP
    
    UNION ALL


SELECT
    *
FROM
    (SELECT
        2022 AS "ANO",
        CAST("COD_IBGE" AS INT) AS "FK_MUNICIPIO_CODIGO",
        "CONTA",
        SUM("VALOR") as "VALOR"
    FROM
        "postgres"."raw"."DIM_SICONFI_MUN_DESPESASPORFUNCAO_2022"
    WHERE
        "CONTA" IN ('12 - Educação', '28.847 - Transferências para a Educação Básica')
    GROUP BY "ANO", "COD_IBGE", "CONTA"
    ORDER BY "ANO", "FK_MUNICIPIO_CODIGO") AS TEMP
    
