with base as (
    select
        "ANO"
        , "REGIOES"
        , "FAIXA"
        , "ANALFABETO"
        , "RUDIMENTAR"
        , "ELEMENTAR"
        , "INTERMEDIARIO"
        , "PROFICIENTE"
        , "ANALFABETOS_FUNCIONAIS"
        , "ALFABETISMO_CONSOLIDADO"
    from
        "postgres"."raw"."DIM_ANALFABETISMO_FUNCIONAL"
)




    select
        "ANO"
        , "REGIOES"
        , "FAIXA"
        , 'ANALFABETO' as "CATEGORIA"
        , "ANALFABETO" as "QUANTIDADE"
    from
        base

    
        union all
    

    select
        "ANO"
        , "REGIOES"
        , "FAIXA"
        , 'RUDIMENTAR' as "CATEGORIA"
        , "RUDIMENTAR" as "QUANTIDADE"
    from
        base

    
        union all
    

    select
        "ANO"
        , "REGIOES"
        , "FAIXA"
        , 'ELEMENTAR' as "CATEGORIA"
        , "ELEMENTAR" as "QUANTIDADE"
    from
        base

    
        union all
    

    select
        "ANO"
        , "REGIOES"
        , "FAIXA"
        , 'INTERMEDIARIO' as "CATEGORIA"
        , "INTERMEDIARIO" as "QUANTIDADE"
    from
        base

    
        union all
    

    select
        "ANO"
        , "REGIOES"
        , "FAIXA"
        , 'PROFICIENTE' as "CATEGORIA"
        , "PROFICIENTE" as "QUANTIDADE"
    from
        base

    
        union all
    

    select
        "ANO"
        , "REGIOES"
        , "FAIXA"
        , 'ANALFABETOS_FUNCIONAIS' as "CATEGORIA"
        , "ANALFABETOS_FUNCIONAIS" as "QUANTIDADE"
    from
        base

    
        union all
    

    select
        "ANO"
        , "REGIOES"
        , "FAIXA"
        , 'ALFABETISMO_CONSOLIDADO' as "CATEGORIA"
        , "ALFABETISMO_CONSOLIDADO" as "QUANTIDADE"
    from
        base

    
