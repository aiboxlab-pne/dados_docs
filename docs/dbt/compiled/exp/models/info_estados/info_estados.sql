WITH estados_info AS (
    SELECT
        CAST(estados."UF_CODIGO" AS INT) as "ESTADO_CODIGO",
		estados."UF_NOME" as "ESTADO_NOME",
		estados."UF_SIGLA" as "ESTADO_SIGLA",
        estados_area."AR_UF_2021" as "AREA_GEOGRAFICA",
		estados_capitais."CAPITAL",
		estados_censo_atlas."RDPC",
		estados_censo_atlas."IDHM",
		estados_censo_atlas."IDHM_R",
		estados_censo_atlas."IDHM_E",
		estados_censo_atlas."IDHM_L"
    FROM
        "postgres"."raw"."DIM_ESTADOS" AS estados

	JOIN
        "postgres"."raw"."DIM_ESTADOS_AREA" AS estados_area
    ON
        estados."UF_CODIGO" = estados_area."CD_UF"

    JOIN
        "postgres"."raw"."DIM_ESTADOS_CAPITAIS" AS estados_capitais
    ON
        estados."UF_SIGLA" = estados_capitais."SIGLA"

	JOIN
    (
        SELECT *
        FROM "postgres"."raw"."DIM_ESTADOS_CENSO_ATLAS_2013"
        WHERE "ANO" = 2010
    ) AS estados_censo_atlas
	ON
		estados."UF_CODIGO" = estados_censo_atlas."UF"
)

SELECT
    *
FROM
    estados_info