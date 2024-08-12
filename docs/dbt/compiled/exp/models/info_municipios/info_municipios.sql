WITH municipios_info AS (
    SELECT
        municipios."CD_MUN" as "MUNICIPIO_CODIGO",
        municipios."NM_MUN" as  "MUNICIPIO_NOME",
        municipios."AREA_KM2" as "AREA_GEOGRAFICA",
        estados."UF_CODIGO" as "ESTADO_CODIGO",
        estados."UF_NOME" as "ESTADO_NOME",
        municipios."SIGLA_UF" as "ESTADO_SIGLA",
        estados."REGIAO_CODIGO",
        estados."REGIAO_NOME"
    FROM
        "postgres"."raw"."DIM_MUNICIPIOS_MALHA_2022" as municipios

    LEFT JOIN
        "postgres"."raw"."DIM_ESTADOS" AS estados
    ON
        estados."UF_SIGLA" = municipios."SIGLA_UF"
)
SELECT
    *
FROM
    municipios_info
WHERE
    "MUNICIPIO_CODIGO" NOT IN (4300001, 4300002)