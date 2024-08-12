-- 55 seg


    SELECT
        "ANO", "ETAPA", "FK_MUNICIPIO_CODIGO", "TP_DEPENDENCIA",
        REPLACE("DISCIPLINA_NOME", 'IN_DISC_', '') AS "DISCIPLINA_NOME",
        "FORMACAO_COD", "FORMACAO_NOME", "FORMACAO_ADEQUADA", "DOCENCIA_TOTAL"
    FROM
        "postgres"."dbt_staging"."dim_educ_bas_docentes_15a_2014_to_2018"

    UNION ALL


    SELECT
        "ANO", "ETAPA", "FK_MUNICIPIO_CODIGO", "TP_DEPENDENCIA",
        REPLACE("DISCIPLINA_NOME", 'IN_DISC_', '') AS "DISCIPLINA_NOME",
        "FORMACAO_COD", "FORMACAO_NOME", "FORMACAO_ADEQUADA", "DOCENCIA_TOTAL"
    FROM
        "postgres"."dbt_staging"."dim_educ_bas_docentes_15a_2019_2020"

    UNION ALL


    SELECT
        "ANO", "ETAPA", "FK_MUNICIPIO_CODIGO", "TP_DEPENDENCIA",
        REPLACE("DISCIPLINA_NOME", 'IN_DISC_', '') AS "DISCIPLINA_NOME",
        "FORMACAO_COD", "FORMACAO_NOME", "FORMACAO_ADEQUADA", "DOCENCIA_TOTAL"
    FROM
        "postgres"."dbt_staging"."dim_educ_bas_docentes_15b_2014_to_2018"

    UNION ALL


    SELECT
        "ANO", "ETAPA", "FK_MUNICIPIO_CODIGO", "TP_DEPENDENCIA",
        REPLACE("DISCIPLINA_NOME", 'IN_DISC_', '') AS "DISCIPLINA_NOME",
        "FORMACAO_COD", "FORMACAO_NOME", "FORMACAO_ADEQUADA", "DOCENCIA_TOTAL"
    FROM
        "postgres"."dbt_staging"."dim_educ_bas_docentes_15b_2019_2020"

    UNION ALL


    SELECT
        "ANO", "ETAPA", "FK_MUNICIPIO_CODIGO", "TP_DEPENDENCIA",
        REPLACE("DISCIPLINA_NOME", 'IN_DISC_', '') AS "DISCIPLINA_NOME",
        "FORMACAO_COD", "FORMACAO_NOME", "FORMACAO_ADEQUADA", "DOCENCIA_TOTAL"
    FROM
        "postgres"."dbt_staging"."dim_educ_bas_docentes_15cd_2014_to_2018"

    UNION ALL


    SELECT
        "ANO", "ETAPA", "FK_MUNICIPIO_CODIGO", "TP_DEPENDENCIA",
        REPLACE("DISCIPLINA_NOME", 'IN_DISC_', '') AS "DISCIPLINA_NOME",
        "FORMACAO_COD", "FORMACAO_NOME", "FORMACAO_ADEQUADA", "DOCENCIA_TOTAL"
    FROM
        "postgres"."dbt_staging"."dim_educ_bas_docentes_15cd_2019_2020"

