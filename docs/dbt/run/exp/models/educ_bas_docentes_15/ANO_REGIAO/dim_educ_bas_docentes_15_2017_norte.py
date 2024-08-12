import numpy as np
import pandas as pd

cols_disciplinas = [
    "IN_DISC_LINGUA_PORTUGUESA",
    "IN_DISC_LINGUA_INGLES",
    "IN_DISC_LINGUA_ESPANHOL",
    "IN_DISC_LINGUA_FRANCES",
    "IN_DISC_LINGUA_OUTRA",
    "IN_DISC_ARTES",
    "IN_DISC_EDUCACAO_FISICA",
    "IN_DISC_MATEMATICA",
    "IN_DISC_CIENCIAS",
    "IN_DISC_QUIMICA",
    "IN_DISC_FISICA",
    "IN_DISC_BIOLOGIA",
    "IN_DISC_ESTUDOS_SOCIAIS",
    "IN_DISC_HISTORIA",
    "IN_DISC_GEOGRAFIA",
    "IN_DISC_SOCIOLOGIA",
    "IN_DISC_FILOSOFIA",
    "IN_DISC_ENSINO_RELIGIOSO",
]

cols_compl = [
    "IN_COM_PEDAGOGICA_1",
    "IN_COM_PEDAGOGICA_2",
    "IN_COM_PEDAGOGICA_3",
    "CO_AREA_COMPL_PEDAGOGICA_1",
    "CO_AREA_COMPL_PEDAGOGICA_2",
    "CO_AREA_COMPL_PEDAGOGICA_3",
]

str_formacao_adequada_v1 = """IN_DISC_LINGUA_PORTUGUESA,145F15,0
IN_DISC_LINGUA_PORTUGUESA,145F17,0
IN_DISC_LINGUA_PORTUGUESA,223L01,1
IN_DISC_LINGUA_PORTUGUESA,220L03,1
IN_DISC_LINGUA_ESTRANGEIRA,145F14,0
IN_DISC_LINGUA_ESTRANGEIRA,145F17,0
IN_DISC_LINGUA_ESTRANGEIRA,222L01,1
IN_DISC_LINGUA_ESTRANGEIRA,220L03,1
IN_DISC_ARTES,146F02,0
IN_DISC_ARTES,146F04,0
IN_DISC_ARTES,146F07,0
IN_DISC_ARTES,146F20,0
IN_DISC_ARTES,146F22,0
IN_DISC_ARTES,210A01,1
IN_DISC_ARTES,211A02,1
IN_DISC_ARTES,212D01,1
IN_DISC_ARTES,212M02,1
IN_DISC_ARTES,212T01,1
IN_DISC_EDUCACAO_FISICA,146F15,0
IN_DISC_EDUCACAO_FISICA,720E01,1
IN_DISC_MATEMATICA,145F18,0
IN_DISC_MATEMATICA,461M01,1
IN_DISC_CIENCIAS,145F01,0
IN_DISC_CIENCIAS,145F02,0
IN_DISC_CIENCIAS,145F09,0
IN_DISC_CIENCIAS,145F21,0
IN_DISC_CIENCIAS,442Q01,1
IN_DISC_CIENCIAS,441F01,1
IN_DISC_CIENCIAS,421C01,1
IN_DISC_CIENCIAS,440C01,1
IN_DISC_QUIMICA,145F02,0
IN_DISC_QUIMICA,145F21,0
IN_DISC_QUIMICA,442Q01,1
IN_DISC_FISICA,145F02,0
IN_DISC_FISICA,145F09,0
IN_DISC_FISICA,441F01,1
IN_DISC_BIOLOGIA,145F01,0
IN_DISC_BIOLOGIA,145F02,0
IN_DISC_BIOLOGIA,421C01,1
IN_DISC_ESTUDOS_SOCIAIS,144F12,0
IN_DISC_ESTUDOS_SOCIAIS,145F10,0
IN_DISC_ESTUDOS_SOCIAIS,145F11,0
IN_DISC_ESTUDOS_SOCIAIS,145F24,0
IN_DISC_ESTUDOS_SOCIAIS,310C02,1
IN_DISC_ESTUDOS_SOCIAIS,312A01,1
IN_DISC_ESTUDOS_SOCIAIS,220H01,1
IN_DISC_ESTUDOS_SOCIAIS,225H01,1
IN_DISC_ESTUDOS_SOCIAIS,443G05,1
IN_DISC_HISTORIA,145F11,0
IN_DISC_HISTORIA,225H01,1
IN_DISC_GEOGRAFIA,145F10,0
IN_DISC_GEOGRAFIA,443G05,1
IN_DISC_SOCIOLOGIA,145F24,0
IN_DISC_SOCIOLOGIA,310C02,1
IN_DISC_SOCIOLOGIA,312A01,1
IN_DISC_FILOSOFIA,145F08,0
IN_DISC_FILOSOFIA,226F01,1
IN_DISC_ENSINO_RELIGIOSO,145F05,0
IN_DISC_ENSINO_RELIGIOSO,221T01,1
MULTIDISCIPLINAR,142P01,0
MULTIDISCIPLINAR,142C01,1"""

str_formacao_adequada_v2 = """IN_DISC_LINGUA_PORTUGUESA,0115L111,0
IN_DISC_LINGUA_PORTUGUESA,0115L121,0
IN_DISC_LINGUA_PORTUGUESA,0115L131,0
IN_DISC_LINGUA_PORTUGUESA,0115L141,0
IN_DISC_LINGUA_PORTUGUESA,0115L151,0
IN_DISC_LINGUA_PORTUGUESA,0115L161,0
IN_DISC_LINGUA_PORTUGUESA,0115L171,0
IN_DISC_LINGUA_PORTUGUESA,0115L181,0
IN_DISC_LINGUA_PORTUGUESA,0115L191,0
IN_DISC_LINGUA_PORTUGUESA,0115L201,0
IN_DISC_LINGUA_PORTUGUESA,0231L122,1
IN_DISC_LINGUA_PORTUGUESA,0231L132,1
IN_DISC_LINGUA_PORTUGUESA,0231L142,1
IN_DISC_LINGUA_PORTUGUESA,0231L152,1
IN_DISC_LINGUA_PORTUGUESA,0231L162,1
IN_DISC_LINGUA_PORTUGUESA,0231L172,1
IN_DISC_LINGUA_PORTUGUESA,0231L182,1
IN_DISC_LINGUA_PORTUGUESA,0231L192,1
IN_DISC_LINGUA_PORTUGUESA,0231L202,1
IN_DISC_LINGUA_PORTUGUESA,0231L212,1
IN_DISC_LINGUA_ESTRANGEIRA,0115L011,0
IN_DISC_LINGUA_ESTRANGEIRA,0115L021,0
IN_DISC_LINGUA_ESTRANGEIRA,0115L031,0
IN_DISC_LINGUA_ESTRANGEIRA,0115L041,0
IN_DISC_LINGUA_ESTRANGEIRA,0115L051,0
IN_DISC_LINGUA_ESTRANGEIRA,0115L061,0
IN_DISC_LINGUA_ESTRANGEIRA,0115L081,0
IN_DISC_LINGUA_ESTRANGEIRA,0115L091,0
IN_DISC_LINGUA_ESTRANGEIRA,0115L101,0
IN_DISC_LINGUA_ESTRANGEIRA,0115L111,0
IN_DISC_LINGUA_ESTRANGEIRA,0115L121,0
IN_DISC_LINGUA_ESTRANGEIRA,0115L141,0
IN_DISC_LINGUA_ESTRANGEIRA,0115L151,0
IN_DISC_LINGUA_ESTRANGEIRA,0115L161,0
IN_DISC_LINGUA_ESTRANGEIRA,0115L171,0
IN_DISC_LINGUA_ESTRANGEIRA,0115L191,0
IN_DISC_LINGUA_ESTRANGEIRA,0115L201,0
IN_DISC_LINGUA_ESTRANGEIRA,0115L211,0
IN_DISC_LINGUA_ESTRANGEIRA,0231L012,1
IN_DISC_LINGUA_ESTRANGEIRA,0231L032,1
IN_DISC_LINGUA_ESTRANGEIRA,0231L042,1
IN_DISC_LINGUA_ESTRANGEIRA,0231L052,1
IN_DISC_LINGUA_ESTRANGEIRA,0231L062,1
IN_DISC_LINGUA_ESTRANGEIRA,0231L072,1
IN_DISC_LINGUA_ESTRANGEIRA,0231L092,1
IN_DISC_LINGUA_ESTRANGEIRA,0231L112,1
IN_DISC_LINGUA_ESTRANGEIRA,0231L122,1
IN_DISC_LINGUA_ESTRANGEIRA,0231L132,1
IN_DISC_LINGUA_ESTRANGEIRA,0231L142,1
IN_DISC_LINGUA_ESTRANGEIRA,0231L152,1
IN_DISC_LINGUA_ESTRANGEIRA,0231L162,1
IN_DISC_LINGUA_ESTRANGEIRA,0231L172,1
IN_DISC_LINGUA_ESTRANGEIRA,0231L182,1
IN_DISC_LINGUA_ESTRANGEIRA,0231L202,1
IN_DISC_LINGUA_ESTRANGEIRA,0231L212,1
IN_DISC_LINGUA_ESTRANGEIRA,0231L222,1
IN_DISC_ARTES,0114A011,0
IN_DISC_ARTES,0114A014,0
IN_DISC_ARTES,0114A021,0
IN_DISC_ARTES,0213A012,1
IN_DISC_ARTES,0213A022,1
IN_DISC_ARTES,0213A032,1
IN_DISC_ARTES,0213H012,1
IN_DISC_ARTES,0215A012,1
IN_DISC_ARTES,0288P012,1
IN_DISC_ARTES,0215D012,1
IN_DISC_ARTES,0215M012,1
IN_DISC_ARTES,0215T012,1
IN_DISC_EDUCACAO_FISICA,0114E031,0
IN_DISC_EDUCACAO_FISICA,0915E012,1
IN_DISC_MATEMATICA,0114M011,0
IN_DISC_MATEMATICA,0541M012,1
IN_DISC_MATEMATICA,0541M022,1
IN_DISC_CIENCIAS,0114C021,0
IN_DISC_CIENCIAS,0521C012,1
IN_DISC_CIENCIAS,0114B011,0
IN_DISC_CIENCIAS,0114F021,0
IN_DISC_CIENCIAS,0114Q011,0
IN_DISC_CIENCIAS,0511B012,1
IN_DISC_CIENCIAS,0512B012,1
IN_DISC_CIENCIAS,0512B022,1
IN_DISC_CIENCIAS,0521E012,1
IN_DISC_CIENCIAS,0531Q012,1
IN_DISC_CIENCIAS,0533F012,1
IN_DISC_CIENCIAS,0533F022,1
IN_DISC_CIENCIAS,0588P012,1
IN_DISC_QUIMICA,0114C021,0
IN_DISC_QUIMICA,0531Q012,1
IN_DISC_FISICA,0114C021,0
IN_DISC_FISICA,0114F021,0
IN_DISC_FISICA,0533F012,1
IN_DISC_FISICA,0533F022,1
IN_DISC_BIOLOGIA,0114C021,0
IN_DISC_BIOLOGIA,0114B011,0
IN_DISC_BIOLOGIA,0511B012,1
IN_DISC_ESTUDOS_SOCIAIS,0114G011,0
IN_DISC_ESTUDOS_SOCIAIS,0312G012,1
IN_DISC_ESTUDOS_SOCIAIS,0312A012,1
IN_DISC_ESTUDOS_SOCIAIS,0114H011,0
IN_DISC_ESTUDOS_SOCIAIS,0222H012,1
IN_DISC_ESTUDOS_SOCIAIS,0114C031,0
IN_DISC_ESTUDOS_SOCIAIS,0312C022,1
IN_DISC_ESTUDOS_SOCIAIS,0588P012,1
IN_DISC_HISTORIA,0114H011,0
IN_DISC_HISTORIA,0222H012,1
IN_DISC_GEOGRAFIA,0114G011,0
IN_DISC_GEOGRAFIA,0312G012,1
IN_DISC_SOCIOLOGIA,0114C031,0
IN_DISC_SOCIOLOGIA,0312C022,1
IN_DISC_SOCIOLOGIA,0312A012,1
IN_DISC_FILOSOFIA,0114F011,0
IN_DISC_FILOSOFIA,0223F012,1
IN_DISC_ENSINO_RELIGIOSO,0221T012,1
IN_DISC_ENSINO_RELIGIOSO,0114E071,0
IN_DISC_ENSINO_RELIGIOSO,0221C012,1
MULTIDISCIPLINAR,0111P022,1
MULTIDISCIPLINAR,0113P011,0
MULTIDISCIPLINAR,0113P012,1"""

str_area_compl_pedago = """IN_DISC_LINGUA_PORTUGUESA,6
IN_DISC_LINGUA_ESTRANGEIRA,7
IN_DISC_LINGUA_ESTRANGEIRA,8
IN_DISC_LINGUA_ESTRANGEIRA,30
IN_DISC_LINGUA_ESTRANGEIRA,9
IN_DISC_ARTES,10
IN_DISC_EDUCACAO_FISICA,11
IN_DISC_MATEMATICA,3
IN_DISC_CIENCIAS,5
IN_DISC_QUIMICA,1
IN_DISC_FISICA,2
IN_DISC_BIOLOGIA,4
IN_DISC_ESTUDOS_SOCIAIS,28
IN_DISC_HISTORIA,12
IN_DISC_GEOGRAFIA,13
IN_DISC_SOCIOLOGIA,29
IN_DISC_FILOSOFIA,14
IN_DISC_ENSINO_RELIGIOSO,26
MULTIDISCIPLINAR,25"""

str_curso_nome = """142A01|Processos Escolares - Tecnológico|v1
142C01|Pedagogia (Ciências da Educação) - Bacharelado|v1
142P01|Pedagogia - Licenciatura|v1
144F12|Licenciatura Interdisciplinar em Ciências Humanas - Licenciatura|v1
144F13|Licenciatura Intercultural Indígena - Licenciatura |v1
145F01|Ciências Biológicas - Licenciatura|v1
145F02|Ciências Naturais - Licenciatura|v1
145F05|Educação Religiosa - Licenciatura|v1
145F08|Filosofia - Licenciatura|v1
145F09|Física - Licenciatura|v1
145F10|Geografia - Licenciatura|v1
145F11|História - Licenciatura|v1
145F14|Letras - Língua Estrangeira - Licenciatura|v1
145F15|Letras - Língua Portuguesa - Licenciatura|v1
145F17|Letras - Língua Portuguesa e Estrangeira - Licenciatura|v1
145F18|Matemática - Licenciatura|v1
145F21|Química - Licenciatura|v1
145F24|Ciências Sociais - Licenciatura|v1
145F28|Libras - Licenciatura|v1
146F02|Licenciatura Interdisciplinar em Artes (Educação Artística) - Licenciatura|v1
146F04|Artes Visuais - Licenciatura|v1
146F05|Informática - Licenciatura|v1
146F07|Dança - Licenciatura|v1
146F09|Licenciatura Interdisciplinar em Educação no Campo - Licenciatura|v1
146F15|Educação Física - Licenciatura|v1
146F20|Música - Licenciatura|v1
146F22|Teatro - Licenciatura|v1
146P01|Licenciatura para a Educação Profissional e Tecnológica - Licenciatura|v1
210A01|Bacharelado Interdisciplinar em Artes - Bacharelado|v1
211A02|Artes Visuais - Bacharelado|v1
212C02|Produção cênica - Tecnológico|v1
212D01|Dança - Bacharelado|v1
212M02|Música - Bacharelado|v1
212T01|Teatro - Bacharelado|v1
213A05|Produção audiovisual - Tecnológico|v1
213C06|Design gráfico - Tecnológico|v1
213C07|Carnaval - Tecnológico|v1
213F01|Fotografia - Tecnológico|v1
213P02|Produção multimídia - Tecnológico|v1
213P03|Produção fonográfica - Tecnológico|v1
213P05|Produção publicitária - Tecnológico|v1
213P07|Produção Cultural - Tecnológico|v1
214D02|Design de moda - Tecnológico|v1
214D05|Design - Bacharelado|v1
214D06|Design de Interiores  - Tecnológico|v1
214M01|Moda - Bacharelado|v1
214P01|Design de produto - Tecnológico|v1
215C02|Conservação e restauro - Tecnológico|v1
215F01|Fabricação de Instrumentos Musicais - Tecnológico|v1
220H01|Bacharelado Interdisciplinar Ciências Humanas - Bacharelado |v1
220L03|Letras - Língua Portuguesa e Estrangeira - Bacharelado|v1
221T01|Teologia - Bacharelado|v1
222L01|Letras - Língua Estrangeira - Bacharelado|v1
223C01|Comunicação assistiva - Tecnológico|v1
223L01|Letras - Língua Portuguesa - Bacharelado|v1
223L02|Libras - Bacharelado|v1
225A01|Arqueologia - Bacharelado|v1
225H01|História - Bacharelado|v1
225M01|Museologia - Bacharelado|v1
225M02|Museografia - Tecnológico|v1
226F01|Filosofia - Bacharelado|v1
310C02|Ciências Sociais - Bacharelado|v1
311P02|Psicologia - Bacharelado|v1
312A01|Antropologia - Bacharelado|v1
313C01|Ciência política - Bacharelado|v1
313R01|Relações Internacionais - Bacharelado|v1
314E02|Ciências Econômicas - Bacharelado|v1
321C01|Cinema e Audiovisual - Bacharelado|v1
321C02|Comunicação Social (Área Geral) - Bacharelado|v1
321J01|Jornalismo - Bacharelado|v1
321R01|Radio, TV, Internet - Bacharelado|v1
322A01|Arquivologia - Bacharelado|v1
322B01|Biblioteconomia - Bacharelado|v1
340N02|Comércio exterior - Tecnológico|v1
341N01|Negócios imobiliários - Tecnológico|v1
342C01|Comunicação institucional - Tecnológico|v1
342M02|Marketing - Tecnológico|v1
342P02|Publicidade e Propaganda - Bacharelado|v1
342R01|Relações Públicas - Bacharelado|v1
343S01|Gestão de Seguros - Teconológico|v1
344C02|Ciências Contábeis - Bacharelado|v1
345A01|Administração - Bacharelado|v1
345A02|Gestão de cooperativas  - Tecnológico|v1
345A07|Gestão hospitalar  - Tecnológico|v1
345A10|Gestão pública  - Tecnológico|v1
345C01|Processos gerenciais  - Tecnológico|v1
345G09|Gestão de recursos humanos  - Tecnológico|v1
345G10|Gestão da qualidade  - Tecnológico|v1
345G13|Logística  - Tecnológico|v1
345G16|Gestão comercial  - Tecnológico|v1
345G17|Gestão financeira  - Tecnológico|v1
345G26|Gestão de segurança privada - Tecnológico|v1
346S01|Secretariado  - Tecnológico|v1
346S03|Secretariado Executivo - Bacharelado|v1
380D01|Direito - Bacharelado|v1
421B07|Biomedicina - Bacharelado|v1
421B12|Biotecnologia - Tecnológico|v1
421C01|Ciências Biológicas - Bacharelado|v1
422S01|Saneamento ambiental - Tecnológico|v1
440C01|Bacharelado Interdisciplinar em Ciência e Tecnologia  - Bacharelado|v1
441F01|Física - Bacharelado|v1
441R01|Física Medica e Radioterapia - Bacharelado|v1
442Q01|Química - Bacharelado|v1
443C01|Ciência da Terra - Licenciatura|v1
443G03|Geofísica - Bacharelado|v1
443G05|Geografia - Bacharelado|v1
443G06|Geologia - Bacharelado|v1
443M01|Meteorologia - Bacharelado|v1
443O01|Oceanografia - Bacharelado|v1
461M01|Matemática - Bacharelado|v1
462C01|Ciências Atuariais - Bacharelado|v1
462E01|Estatística - Bacharelado|v1
481A01|Redes de computadores - Tecnológico|v1
481B01|Banco de dados - Tecnológico|v1
481C01|Ciência da Computação - Bacharelado|v1
481T01|Gestão da tecnologia da informação - Tecnológico|v1
481T02|Jogos Digitais - Tecnológico|v1
482U01|Sistemas para internet - Tecnológico|v1
483S01|Análise e desenvolvimento de sistemas / Segurança da informação - Tecnológico|v1
483S02|Sistemas de Informação - Bacharelado|v1
520A01|Automação industrial - Tecnológico|v1
520E01|Engenharia - Bacharelado|v1
520E04|Engenharia de Materiais - Bacharelado|v1
520E05|Engenharia de Produção - Bacharelado|v1
520E09|Engenharia Ambiental e Sanitária - Bacharelado|v1
520G01|Geoprocessamento - Tecnológico|v1
520M01|Manutenção industrial - Tecnológico|v1
520P02|Gestão da produção industrial - Tecnológico|v1
520T01|Gestão de telecomunicações - Tecnológico|v1
521E05|Engenharia Mecânica - Bacharelado|v1
521E06|Engenharia Metalúrgica - Bacharelado|v1
521M03|Mecânica de precisão - Tecnológico|v1
521T02|Processos metalúrgicos - Tecnológico|v1
521T03|Fabricação mecânica - Tecnológico|v1
522D02|Sistemas elétricos - Tecnológico|v1
522E06|Engenharia Elétrica - Bacharelado|v1
522E08|Sistemas de energia - Tecnológico|v1
522R01|Refrigeração/Aquecimento - Tecnológico|v1
522T02|Eletrotécnica industrial - Tecnológico|v1
523B01|Engenharia Biomédica - Bacharelado|v1
523E04|Engenharia de Computação - Bacharelado|v1
523E09|Engenharia Eletrônica - Bacharelado|v1
523E10|Engenharia mecatrônica - Bacharelado|v1
523E11|Engenharia de Controle e Automação - Bacharelado|v1
523E12|Engenharia de Telecomunicações - Bacharelado|v1
523M01|Sistemas biomédicos - Tecnológico|v1
523S03|Sistemas eletrônicos - Tecnológico|v1
523T01|Redes de telecomunicações / Sistemas de telecomunicações - Tecnológico|v1
523T04|Mecatrônica industrial - Tecnológico|v1
523T05|Telemática - Tecnológico|v1
523T06|Eletrônica industrial - Tecnológico|v1
524E01|Engenharia de Bioprocessos - Bacharelado|v1
524E06|Engenharia nuclear - Bacharelado|v1
524E07|Engenharia Química - Bacharelado|v1
524T03|Processos químicos - Tecnológico|v1
524T04|Biocombustíveis - Tecnológico|v1
525A01|Mecanização Agrícola - Tecnológico|v1
525C04|Construção naval - Tecnológico|v1
525E04|Engenharia Aeronáutica - Bacharelado|v1
525E05|Engenharia automotiva - Bacharelado|v1
525E08|Engenharia Naval - Bacharelado|v1
525M01|Manutenção de aeronaves - Tecnológico|v1
525S01|Sistemas Automotivos - Tecnológico|v1
540F02|Produção Joalheira/Design de jóias e gemas - Tecnológico|v1
540F03|Produção Gráfica  - Tecnológico|v1
541E01|Engenharia de Alimentos - Bacharelado|v1
541I02|Laticínios  - Tecnológico|v1
541P05|Processamento de Carnes  - Tecnológico|v1
541P09|Viticultura e Enologia  - Tecnológico|v1
541T01|Alimentos  - Tecnológico|v1
541T02|Produção Sucroalcooleira  - Tecnológico|v1
541T03|Produção de Cachaça  - Tecnológico|v1
542B01|Bioenergia - Tecnológico|v1
542E03|Engenharia Têxtil - Bacharelado|v1
542I01|Produção de vestuário  - Tecnológico|v1
542I02|Produção têxtil  - Tecnológico|v1
543C01|Cerâmica - Tecnológico|v1
543F03|Produção moveleira  - Tecnológico|v1
543F05|Papel e celulose  - Tecnológico|v1
543P06|Polímeros - Tecnológico|v1
544E01|Engenharia de Minas - Bacharelado|v1
544E05|Petróleo e gás  - Tecnológico|v1
544E07|Engenharia de Petróleo - Bacharelado|v1
544M02|Mineração e extração - Tecnológico|v1
544R01|Rochas ornamentais  - Tecnológico|v1
544T01|Tecnologia de Mineração - Tecnológico|v1
581A05|Arquitetura e Urbanismo - Bacharelado|v1
582A01|Obras hidráulicas - Tecnológico|v1
582A02|Agrimensura - Tecnológico|v1
582C05|Construção de Edifícios - Tecnológico|v1
582E02|Engenharia Cartográfica e de Agrimensura - Bacharelado|v1
582E03|Engenharia Civil - Bacharelado|v1
582M02|Material de construção - Tecnológico|v1
582O01|Controle de obras - Tecnológico|v1
582T04|Estradas - Tecnológico|v1
621A03|Agroindústria - Tecnológico|v1
621A04|Agronomia - Bacharelado|v1
621A06|Agroecologia - Tecnológico|v1
621E03|Engenharia Agrícola - Bacharelado|v1
621M02|Produção Agrícola - Tecnológico|v1
621T01|Irrigação e Drenagem - Tecnológico|v1
621T03|Agronegócio - Tecnológico|v1
621T04|Cafeicultura - Tecnológico|v1
621T05|Produção de Grãos - Tecnológico|v1
621Z01|Zootecnia - Bacharelado|v1
622H01|Horticultura - Tecnológico|v1
623E01|Engenharia Florestal - Bacharelado|v1
623S01|Silvicultura - Tecnológico|v1
624A01|Aqüicultura - Tecnológico|v1
624E01|Engenharia de Pesca - Bacharelado|v1
624T01|Produção Pesqueira - Tecnológico|v1
641M01|Medicina Veterinária - Bacharelado|v1
720E01|Educação Física - Bacharelado|v1
720N01|Naturologia - Bacharelado|v1
720S01|Bacharelado Interdisciplinar Ciências da Saúde - Bacharelado|v1
721M01|Medicina - Bacharelado|v1
721O02|Oftálmica - Tecnológico|v1
723E01|Enfermagem - Bacharelado|v1
724O01|Odontologia - Bacharelado|v1
725T06|Radiologia - Tecnológico|v1
726F01|Fisioterapia - Bacharelado|v1
726F03|Fonoaudiologia - Bacharelado|v1
726N02|Nutrição - Bacharelado|v1
726O01|Óptica e Optometria - Tecnológico |v1
726Q01|Quiropraxia - Bacharelado|v1
726T01|Terapia Ocupacional - Bacharelado|v1
727F01|Farmácia - Bacharelado|v1
762S01|Serviço Social - Bacharelado|v1
811G01|Gastronomia - Tecnológico|v1
811H02|Hotelaria - Tecnológico|v1
811H03|Hotelaria Hospitalar - Tecnológico|v1
812E01|Eventos - Tecnológico|v1
812P01|Gestão de Turismo - Tecnológico|v1
812T01|Turismo - Bacharelado|v1
813F02|Futebol - Tecnológico|v1
813G02|Gestão desportiva e de lazer - Tecnológico|v1
814E02|Economia doméstica - Bacharelado|v1
815E01|Estética e Cosmética - Tecnológico|v1
840A01|Pilotagem profissional de aeronaves - Tecnológico|v1
840C04|Ciências Aeronáuticas - Bacharelado*|v1
840C05|Ciências Navais - Bacharelado*|v1
840N02|Sistemas de navegação fluvial - Tecnológico|v1
840S01|Gestão portuária - Tecnológico|v1
840S02|Transporte aéreo - Tecnológico|v1
840T02|Transporte terrestre - Tecnológico|v1
850G01|Processos ambientais / Gestão ambiental - Tecnológico|v1
861S02|Segurança no trânsito / Segurança pública - Tecnológico|v1
861S03|Serviços penais - Tecnológico|v1
862S01|Segurança no trabalho - Tecnológico|v1
863C01|Ciências Militares - Bacharelado*|v1
863C02|Ciências da Logística - Bacharelado*|v1
863F01|Formação Militar - Bacharelado*|v1
999990|Outro curso de formação superior - Licenciatura|v1
999991|Outro curso de formação superior - Bacharelado|v1
999992|Outro curso de formação superior - Tecnológico|v1
0111C012|Ciência da educação - Bacharelado|v2
0111C014|Ciência da educação - Sequencial|v2
0111P013|Processos escolares - Tecnológico|v2
0111P022|Psicopedagogia - Bacharelado|v2
0111P024|Psicopedagogia - Sequencial|v2
0112E011|Educação infantil formação de professor - Licenciatura|v2
0113E011|Educação do campo formação de professor - Licenciatura|v2
0113E021|Educação especial formação de professor - Licenciatura|v2
0113E031|Educação indígena formação de professor - Licenciatura|v2
0113F011|Formação pedagógica de professor para a educação básica - Licenciatura|v2
0113F014|Formação pedagógica de professor para a educação básica - Sequencial|v2
0113P011|Pedagogia - Licenciatura|v2
0113P012|Pedagogia - Bacharelado|v2
0113P014|Pedagogia - Sequencial|v2
0114A011|Artes formação de professor - Licenciatura|v2
0114A014|Artes formação de professor - Sequencial|v2
0114A021|Artes visuais formação de professor - Licenciatura|v2
0114B011|Biologia formação de professor - Licenciatura|v2
0114C011|Ciências agrárias formação de professor - Licenciatura|v2
0114C021|Ciências naturais formação de professor - Licenciatura|v2
0114C031|Ciências sociais formação de professor - Licenciatura|v2
0114C041|Cinema e audiovisual formação de professor - Licenciatura|v2
0114C051|Computação formação de professor - Licenciatura|v2
0114D011|Dança formação de professor - Licenciatura|v2
0114E011|Economia doméstica formação de professor - Licenciatura|v2
0114E021|Educação do campo em áreas de conhecimento da educação básica formação de professor - Licenciatura|v2
0114E031|Educação física formação de professor - Licenciatura|v2
0114E041|Educação indígena em áreas de conhecimento da educação básica formação de professor - Licenciatura|v2
0114E051|Enfermagem formação de professor - Licenciatura|v2
0114E061|Ensino profissionalizante em área específica formação de professor - Licenciatura|v2
0114E071|Ensino religioso formação de professor - Licenciatura|v2
0114E081|Estatística formação de professor - Licenciatura|v2
0114F011|Filosofia formação de professor - Licenciatura|v2
0114F021|Física formação de professor - Licenciatura|v2
0114G011|Geografia formação de professor - Licenciatura|v2
0114H011|História formação de professor - Licenciatura|v2
0114M011|Matemática formação de professor - Licenciatura|v2
0114M021|Música formação de professor - Licenciatura|v2
0114P011|Psicologia formação de professor - Licenciatura|v2
0114Q011|Química formação de professor - Licenciatura|v2
0114T011|Teatro formação de professor - Licenciatura|v2
0115L011|Letras alemão formação de professor - Licenciatura|v2
0115L021|Letras espanhol formação de professor - Licenciatura|v2
0115L031|Letras francês formação de professor - Licenciatura|v2
0115L041|Letras inglês formação de professor - Licenciatura|v2
0115L051|Letras italiano formação de professor  - Licenciatura|v2
0115L061|Letras japonês formação de professor  - Licenciatura|v2
0115L071|Letras língua brasileira de sinais formação de professor - Licenciatura|v2
0115L081|Letras línguas estrangeiras clássicas formação de professor - Licenciatura|v2
0115L091|Letras linguística formação de professor  - Licenciatura|v2
0115L101|Letras outras línguas estrangeiras modernas formação de professor  - Licenciatura|v2
0115L111|Letras português alemão formação de professor - Licenciatura|v2
0115L121|Letras português espanhol formação de professor - Licenciatura|v2
0115L131|Letras português formação de professor - Licenciatura|v2
0115L141|Letras português francês formação de professor - Licenciatura|v2
0115L151|Letras português inglês formação de professor - Licenciatura|v2
0115L161|Letras português italiano formação de professor - Licenciatura|v2
0115L171|Letras português japonês formação de professor - Licenciatura|v2
0115L181|Letras português língua brasileira de sinais formação de professor - Licenciatura|v2
0115L191|Letras português línguas estrangeiras clássicas formação de professor - Licenciatura|v2
0115L201|Letras português outras línguas estrangeiras modernas formação de professor - Licenciatura|v2
0115L211|Letras tradutor e intérprete formação de professor - Licenciatura|v2
0188P011|Programas interdisciplinares abrangendo educação - Licenciatura|v2
0188P012|Programas interdisciplinares abrangendo educação - Bacharelado|v2
0188P013|Programas interdisciplinares abrangendo educação - Tecnológico|v2
0211A012|Animação - Bacharelado|v2
0211A013|Animação - Tecnológico|v2
0211A014|Animação - Sequencial|v2
0211C012|Cinema e audiovisual - Bacharelado|v2
0211C013|Cinema e audiovisual - Tecnológico|v2
0211C014|Cinema e audiovisual - Sequencial|v2
0211C023|Comunicação assistiva - Tecnológico|v2
0211D012|Design gráfico - Bacharelado|v2
0211D013|Design gráfico - Tecnológico|v2
0211D014|Design gráfico - Sequencial|v2
0211F012|Fotografia - Bacharelado|v2
0211F013|Fotografia - Tecnológico|v2
0211F014|Fotografia - Sequencial|v2
0211P012|Produção audiovisual - Bacharelado|v2
0211P013|Produção audiovisual - Tecnológico|v2
0211P014|Produção audiovisual - Sequencial|v2
0211P023|Produção cênica - Tecnológico|v2
0211P032|Produção cultural - Bacharelado|v2
0211P033|Produção cultural - Tecnológico|v2
0211P034|Produção cultural - Sequencial|v2
0211P043|Produção fonográfica - Tecnológico|v2
0211P052|Produção multimídia - Bacharelado|v2
0211P053|Produção multimídia - Tecnológico|v2
0211P054|Produção multimídia - Sequencial|v2
0212D012|Desenho industrial - Bacharelado|v2
0212D022|Design - Bacharelado|v2
0212D023|Design - Tecnológico|v2
0212D032|Design de interiores - Bacharelado|v2
0212D033|Design de interiores - Tecnológico|v2
0212D034|Design de interiores - Sequencial|v2
0212D042|Design de produto - Bacharelado|v2
0212D043|Design de produto - Tecnológico|v2
0212D044|Design de produto - Sequencial|v2
0212M012|Moda - Bacharelado|v2
0212M013|Moda - Tecnológico|v2
0212M014|Moda - Sequencial|v2
0213A012|Artes - Bacharelado|v2
0213A013|Artes - Tecnológico|v2
0213A014|Artes - Sequencial|v2
0213A022|Artes plásticas - Bacharelado|v2
0213A023|Artes plásticas - Tecnológico|v2
0213A024|Artes plásticas - Sequencial|v2
0213A032|Artes visuais - Bacharelado|v2
0213A033|Artes visuais - Tecnológico|v2
0213H012|História da arte - Bacharelado|v2
0214F013|Fabricação de instrumentos musicais não industrial - Tecnológico|v2
0215A012|Artes cênicas - Bacharelado|v2
0215A013|Artes cênicas - Tecnológico|v2
0215D012|Dança - Bacharelado|v2
0215D013|Dança - Tecnológico|v2
0215M012|Música - Bacharelado|v2
0215M013|Música  - Tecnológico|v2
0215M014|Música - Sequencial|v2
0215T012|Teatro - Bacharelado|v2
0215T013|Teatro - Tecnológico|v2
0221C012|Ciências da religião - Bacharelado|v2
0221T012|Teologia - Bacharelado|v2
0221T014|Teologia - Sequencial|v2
0222A012|Arqueologia - Bacharelado|v2
0222A013|Arqueologia - Tecnológico|v2
0222C012|Conservação e restauro - Bacharelado|v2
0222C013|Conservação e restauro - Tecnológico|v2
0222H012|História - Bacharelado|v2
0222H014|História - Sequencial|v2
0223F012|Filosofia - Bacharelado|v2
0223F014|Filosofia - Sequencial|v2
0231L012|Letras alemão - Bacharelado|v2
0231L023|Letras escrita criativa - Tecnológico|v2
0231L024|Letras escrita criativa - Sequencial|v2
0231L032|Letras espanhol - Bacharelado|v2
0231L034|Letras espanhol - Sequencial|v2
0231L042|Letras francês - Bacharelado|v2
0231L052|Letras inglês - Bacharelado|v2
0231L054|Letras inglês - Sequencial|v2
0231L062|Letras italiano - Bacharelado|v2
0231L072|Letras japonês - Bacharelado|v2
0231L082|Letras língua brasileira de sinais - Bacharelado|v2
0231L083|Letras língua brasileira de sinais - Tecnológico|v2
0231L084|Letras língua brasileira de sinais - Sequencial|v2
0231L092|Letras línguas estrangeiras clássicas  - Bacharelado|v2
0231L094|Letras línguas estrangeiras clássicas - Sequencial|v2
0231L102|Letras linguística - Bacharelado|v2
0231L112|Letras outras línguas estrangeiras modernas  - Bacharelado|v2
0231L122|Letras português - Bacharelado|v2
0231L124|Letras português - Sequencial|v2
0231L132|Letras português alemão  - Bacharelado|v2
0231L142|Letras português espanhol - Bacharelado|v2
0231L152|Letras português francês - Bacharelado|v2
0231L162|Letras português inglês - Bacharelado|v2
0231L172|Letras português italiano - Bacharelado|v2
0231L182|Letras português japonês  - Bacharelado|v2
0231L192|Letras português língua brasileira de sinais - Bacharelado|v2
0231L202|Letras português línguas estrangeiras clássicas  - Bacharelado|v2
0231L212|Letras português outras línguas estrangeiras modernas - Bacharelado|v2
0231L222|Letras tradutor e intérprete - Bacharelado|v2
0231L223|Letras tradutor e intérprete - Tecnológico|v2
0231L224|Letras tradutor e intérprete - Sequencial|v2
0288P012|Programas interdisciplinares abrangendo artes e humanidades - Bacharelado|v2
0288P014|Programas interdisciplinares abrangendo artes e humanidades - Sequencial|v2
0311E012|Economia - Bacharelado|v2
0311E014|Economia - Sequencial|v2
0312A012|Antropologia - Bacharelado|v2
0312A014|Antropologia - Sequencial|v2
0312C012|Ciência política - Bacharelado|v2
0312C014|Ciência política  - Sequencial|v2
0312C022|Ciências sociais - Bacharelado|v2
0312C024|Ciências sociais - Sequencial|v2
0312G012|Geografia - Bacharelado|v2
0312R012|Relações internacionais - Bacharelado|v2
0312R014|Relações internacionais - Sequencial|v2
0312S012|Sociologia - Bacharelado|v2
0312S014|Sociologia - Sequencial|v2
0313P012|Psicologia - Bacharelado|v2
0313P014|Psicologia - Sequencial|v2
0321C012|Comunicação social - Bacharelado|v2
0321J012|Jornalismo - Bacharelado|v2
0321J014|Jornalismo - Sequencial|v2
0321P012|Produção editorial - Bacharelado|v2
0321P013|Produção editorial - Tecnológico|v2
0321P014|Produção editorial - Sequencial|v2
0321R012|Rádio, TV e internet - Bacharelado|v2
0321R013|Rádio, TV e internet - Tecnológico|v2
0321R014|Rádio, TV e internet - Sequencial|v2
0322A012|Arquivologia - Bacharelado|v2
0322B012|Biblioteconomia - Bacharelado|v2
0322G012|Gestão da informação - Bacharelado|v2
0322G014|Gestão da informação - Sequencial|v2
0322M012|Museologia - Bacharelado|v2
0322M013|Museologia - Tecnológico|v2
0322M014|Museologia - Sequencial|v2
0388P012|Programas interdisciplinares abrangendo ciências sociais, jornalismo e informação - Bacharelado|v2
0388P014|Programas interdisciplinares abrangendo ciências sociais, jornalismo e informação - Sequencial|v2
0411C012|Contabilidade - Bacharelado|v2
0411C013|Contabilidade  - Tecnológico|v2
0411C014|Contabilidade - Sequencial|v2
0412G012|Gestão financeira - Bacharelado|v2
0412G013|Gestão financeira  - Tecnológico|v2
0412G014|Gestão financeira - Sequencial|v2
0412S013|Seguros - Tecnológico|v2
0412S014|Seguros - Sequencial|v2
0413A012|Administração  - Bacharelado|v2
0413A014|Administração - Sequencial|v2
0413A022|Administração pública - Bacharelado|v2
0413A023|Administração pública - Tecnológico|v2
0413A024|Administração pública - Sequencial|v2
0413C012|Comércio exterior - Bacharelado|v2
0413C013|Comércio exterior - Tecnológico|v2
0413C014|Comércio exterior - Sequencial|v2
0413E012|Empreendedorismo - Bacharelado|v2
0413E013|Empreendedorismo - Tecnológico|v2
0413E014|Empreendedorismo - Sequencial|v2
0413G013|Gestão da produção - Tecnológico|v2
0413G014|Gestão da produção - Sequencial|v2
0413G023|Gestão da qualidade - Tecnológico|v2
0413G024|Gestão da qualidade - Sequencial|v2
0413G032|Gestão da saúde - Bacharelado|v2
0413G033|Gestão da saúde - Tecnológico|v2
0413G034|Gestão da saúde - Sequencial|v2
0413G042|Gestão de cooperativas - Bacharelado|v2
0413G043|Gestão de cooperativas - Tecnológico|v2
0413G044|Gestão de cooperativas - Sequencial|v2
0413G052|Gestão de negócios - Bacharelado|v2
0413G053|Gestão de negócios - Tecnológico|v2
0413G054|Gestão de negócios - Sequencial|v2
0413G062|Gestão de negócios internacionais - Bacharelado|v2
0413G064|Gestão de negócios internacionais - Sequencial|v2
0413G073|Gestão de pessoas - Tecnológico|v2
0413G074|Gestão de pessoas - Sequencial|v2
0413G083|Gestão de serviços - Tecnológico|v2
0413G084|Gestão de serviços - Sequencial|v2
0413G092|Gestão do agronegócio - Bacharelado|v2
0413G093|Gestão do agronegócio - Tecnológico|v2
0413G094|Gestão do agronegócio - Sequencial|v2
0413G103|Gestão estratégica - Tecnológico|v2
0413G104|Gestão estratégica - Sequencial|v2
0413G113|Gestão hospitalar - Tecnológico|v2
0413G114|Gestão hospitalar - Sequencial|v2
0413G122|Gestão pública - Bacharelado|v2
0413G123|Gestão pública - Tecnológico|v2
0413G124|Gestão pública - Sequencial|v2
0413L012|Logística - Bacharelado|v2
0413L013|Logística - Tecnológico|v2
0413L014|Logística - Sequencial|v2
0414M012|Marketing - Bacharelado|v2
0414M013|Marketing - Tecnológico|v2
0414M014|Marketing - Sequencial|v2
0414P012|Publicidade e propaganda - Bacharelado|v2
0414P013|Publicidade e propaganda - Tecnológico|v2
0414P014|Publicidade e propaganda - Sequencial|v2
0414R012|Relações públicas - Bacharelado|v2
0414R013|Relações públicas - Tecnológico|v2
0414R014|Relações públicas - Sequencial|v2
0415S012|Secretariado - Bacharelado|v2
0415S013|Secretariado - Tecnológico|v2
0415S014|Secretariado - Sequencial|v2
0416G013|Gestão comercial - Tecnológico|v2
0416G014|Gestão comercial - Sequencial|v2
0416N012|Negócios imobiliários - Bacharelado|v2
0416N013|Negócios imobiliários - Tecnológico|v2
0416N014|Negócios imobiliários - Sequencial|v2
0421D012|Direito - Bacharelado|v2
0421D013|Direito - Tecnológico|v2
0421D014|Direito - Sequencial|v2
0488P012|Programas interdisciplinares abrangendo negócios, administração e direito - Bacharelado|v2
0488P013|Programas interdisciplinares abrangendo negócios, administração e direito - Tecnológico|v2
0511B012|Biologia - Bacharelado|v2
0511B014|Biologia - Sequencial|v2
0512B012|Bioquímica - Bacharelado|v2
0512B022|Biotecnologia - Bacharelado|v2
0512B023|Biotecnologia - Tecnológico|v2
0512B024|Biotecnologia - Sequencial|v2
0512T013|Toxicologia - Tecnológico|v2
0521C012|Ciências ambientais - Bacharelado|v2
0521C014|Ciências ambientais - Sequencial|v2
0521E012|Ecologia - Bacharelado|v2
0531Q012|Química - Bacharelado|v2
0531Q013|Química - Tecnológico|v2
0531Q022|Química industrial e tecnológica - Bacharelado|v2
0531Q023|Química industrial e tecnológica - Tecnológico|v2
0531Q024|Química industrial e tecnológica - Sequencial|v2
0532G012|Geofísica - Bacharelado|v2
0532G022|Geologia - Bacharelado|v2
0532G033|Geoprocessamento - Tecnológico|v2
0532M012|Meteorologia - Bacharelado|v2
0532O012|Oceanografia - Bacharelado|v2
0533A012|Astronomia - Bacharelado|v2
0533F012|Física - Bacharelado|v2
0533F022|Física aplicada - Bacharelado|v2
0533F024|Física aplicada - Sequencial|v2
0533F032|Física médica - Bacharelado|v2
0541M012|Matemática - Bacharelado|v2
0541M014|Matemática - Sequencial|v2
0541M022|Matemática aplicada e computacional - Bacharelado|v2
0542C012|Ciências atuariais - Bacharelado|v2
0542E012|Estatística - Bacharelado|v2
0542E014|Estatística - Sequencial|v2
0588P012|Programas interdisciplinares abrangendo ciências naturais, matemática e estatística - Bacharelado|v2
0588P013|Programas interdisciplinares abrangendo ciências naturais, matemática e estatística  - Tecnológico|v2
0588P014|Programas interdisciplinares abrangendo ciências naturais, matemática e estatística  - Sequencial|v2
0612B013|Banco de dados - Tecnológico|v2
0612B014|Banco de dados - Sequencial|v2
0612D013|Defesa cibernética - Tecnológico|v2
0612G013|Gestão da tecnologia da informação - Tecnológico|v2
0612G014|Gestão da tecnologia da informação  - Sequencial|v2
0612R012|Redes de computadores - Bacharelado|v2
0612R013|Redes de computadores - Tecnológico|v2
0612R014|Redes de computadores - Sequencial|v2
0613E012|Engenharia de software - Bacharelado|v2
0613E013|Engenharia de software - Tecnológico|v2
0613E014|Engenharia de software - Sequencial|v2
0613J012|Jogos digitais - Bacharelado|v2
0613J013|Jogos digitais - Tecnológico|v2
0613J014|Jogos digitais - Sequencial|v2
0614C012|Ciência da computação - Bacharelado|v2
0614C013|Ciência da computação - Tecnológico|v2
0614C014|Ciência da computação - Sequencial|v2
0615S013|Segurança da informação - Tecnológico|v2
0615S014|Segurança da informação - Sequencial|v2
0615S022|Sistemas de informação - Bacharelado|v2
0615S023|Sistemas de informação - Tecnológico|v2
0615S024|Sistemas de informação - Sequencial|v2
0615S032|Sistemas para internet - Bacharelado|v2
0615S033|Sistemas para internet - Tecnológico|v2
0615S034|Sistemas para internet - Sequencial|v2
0616E012|Engenharia de computação (DCN Computação) - Bacharelado|v2
0616S013|Sistemas embarcados - Tecnológico|v2
0688P012|Programas interdisciplinares abrangendo computação e Tecnologias da Informação e Comunicação (TIC) - Bacharelado|v2
0688P013|Programas interdisciplinares abrangendo computação e Tecnologias da Informação e Comunicação (TIC) - Tecnológico|v2
0710E012|Engenharia - Bacharelado|v2
0711B013|Biocombustíveis - Tecnológico|v2
0711E012|Engenharia bioquímica - Bacharelado|v2
0711E022|Engenharia de bioprocessos - Bacharelado|v2
0711E032|Engenharia de biotecnologia - Bacharelado|v2
0711E042|Engenharia de nanotecnologia - Bacharelado|v2
0711E052|Engenharia química - Bacharelado|v2
0712E012|Engenharia ambiental - Bacharelado|v2
0712E022|Engenharia ambiental e sanitária - Bacharelado|v2
0712G012|Gestão ambiental - Bacharelado|v2
0712G013|Gestão ambiental - Tecnológico|v2
0712G014|Gestão ambiental - Sequencial|v2
0712G023|Gestão de resíduos  - Tecnológico|v2
0712G024|Gestão de resíduos - Sequencial|v2
0712S013|Saneamento ambiental  - Tecnológico|v2
0713E013|Eletrotécnica industrial  - Tecnológico|v2
0713E023|Energias renováveis  - Tecnológico|v2
0713E032|Engenharia bioenergética - Bacharelado|v2
0713E042|Engenharia de energia - Bacharelado|v2
0713E052|Engenharia elétrica - Bacharelado|v2
0713E062|Engenharia nuclear - Bacharelado|v2
0713R013|Refrigeração e climatização - Tecnológico|v2
0713S012|Sistemas elétricos - Bacharelado|v2
0713S013|Sistemas elétricos - Tecnológico|v2
0713S014|Sistemas elétricos - Sequencial|v2
0714A013|Automação industrial - Tecnológico|v2
0714A014|Automação industrial - Sequencial|v2
0714E013|Eletrônica industrial - Tecnológico|v2
0714E022|Engenharia acústica - Bacharelado|v2
0714E032|Engenharia biomédica - Bacharelado|v2
0714E042|Engenharia de computação (DCN Engenharia) - Bacharelado|v2
0714E052|Engenharia de controle e automação - Bacharelado|v2
0714E062|Engenharia de informação - Bacharelado|v2
0714E072|Engenharia de telecomunicações - Bacharelado|v2
0714E082|Engenharia eletrônica - Bacharelado|v2
0714E092|Engenharia mecatrônica - Bacharelado|v2
0714G013|Gestão de telecomunicações - Tecnológico|v2
0714G014|Gestão de telecomunicações - Sequencial|v2
0714M013|Mecatrônica industrial - Tecnológico|v2
0714M014|Mecatrônica industrial - Sequencial|v2
0714R013|Redes de telecomunicações - Tecnológico|v2
0714S013|Sistemas biomédicos - Tecnológico|v2
0714S023|Sistemas de telecomunicações - Tecnológico|v2
0714S024|Sistemas de telecomunicações - Sequencial|v2
0714T013|Telemática - Tecnológico|v2
0714T014|Telemática - Sequencial|v2
0715E012|Engenharia física - Bacharelado|v2
0715E022|Engenharia mecânica - Bacharelado|v2
0715E032|Engenharia metalúrgica - Bacharelado|v2
0715F013|Fabricação mecânica - Tecnológico|v2
0715M013|Manutenção industrial - Tecnológico|v2
0715M014|Manutenção industrial - Sequencial|v2
0715M023|Mecânica de precisão - Tecnológico|v2
0715P013|Processos metalúrgicos - Tecnológico|v2
0715P014|Processos metalúrgicos - Sequencial|v2
0715S013|Soldagem - Tecnológico|v2
0715S014|Soldagem - Sequencial|v2
0716A013|Aeroespacial - Tecnológico|v2
0716C013|Construção naval - Tecnológico|v2
0716E012|Engenharia aeroespacial - Bacharelado|v2
0716E022|Engenharia aeronáutica - Bacharelado|v2
0716E023|Engenharia aeronáutica - Tecnológico|v2
0716E032|Engenharia automotiva - Bacharelado|v2
0716E042|Engenharia ferroviária e metroviária - Bacharelado|v2
0716E052|Engenharia naval - Bacharelado|v2
0716M013|Manutenção de aeronaves - Tecnológico|v2
0716M014|Manutenção de aeronaves - Sequencial|v2
0716S013|Sistemas automotivos - Tecnológico|v2
0716S023|Sistemas de navegação fluvial - Tecnológico|v2
0721A012|Alimentos - Bacharelado|v2
0721A013|Alimentos - Tecnológico|v2
0721A014|Alimentos - Sequencial|v2
0721E012|Engenharia de alimentos - Bacharelado|v2
0721L012|Laticínios - Bacharelado|v2
0721L013|Laticínios - Tecnológico|v2
0721P013|Processamento de carnes - Tecnológico|v2
0721P023|Produção de cachaça - Tecnológico|v2
0721P033|Produção sucroalcooleira - Tecnológico|v2
0721P034|Produção sucroalcooleira - Sequencial|v2
0721P043|Produção de cerveja - Tecnológico|v2
0722C013|Cerâmica - Tecnológico|v2
0722C023|Ciências dos materiais - Tecnológico|v2
0722C024|Ciências dos materiais - Sequencial|v2
0722E012|Engenharia de materiais - Bacharelado|v2
0722P013|Papel e celulose - Tecnológico|v2
0722P022|Polímeros - Bacharelado|v2
0722P023|Polímeros - Tecnológico|v2
0722P033|Produção joalheira - Tecnológico|v2
0722P043|Produção moveleira - Tecnológico|v2
0723E012|Engenharia têxtil - Bacharelado|v2
0723P013|Produção de vestuário - Tecnológico|v2
0723P022|Produção têxtil - Bacharelado|v2
0723P023|Produção têxtil - Tecnológico|v2
0724E012|Engenharia de minas - Bacharelado|v2
0724E022|Engenharia de petróleo - Bacharelado|v2
0724E032|Engenharia geológica - Bacharelado|v2
0724M013|Mineração - Tecnológico|v2
0724P013|Petróleo e gás - Tecnológico|v2
0724R013|Rochas ornamentais - Tecnológico|v2
0725E012|Engenharia de manufatura - Bacharelado|v2
0725E013|Engenharia de manufatura - Tecnológico|v2
0725E022|Engenharia de produção - Bacharelado|v2
0725E032|Engenharia industrial - Bacharelado|v2
0725P013|Produção gráfica - Tecnológico|v2
0725P023|Produção industrial - Tecnológico|v2
0731A013|Agrimensura - Tecnológico|v2
0731A022|Arquitetura e urbanismo - Bacharelado|v2
0731A023|Arquitetura e urbanismo - Tecnológico|v2
0731A024|Arquitetura e urbanismo - Sequencial|v2
0731E012|Engenharia cartográfica - Bacharelado|v2
0731E022|Engenharia de agrimensura - Bacharelado|v2
0731E024|Engenharia de agrimensura - Sequencial|v2
0731E032|Engenharia de agrimensura e cartográfica - Bacharelado|v2
0732C013|Construção de edifícios - Tecnológico|v2
0732C023|Controle de obras - Tecnológico|v2
0732C024|Controle de obras - Sequencial|v2
0732E012|Engenharia civil - Bacharelado|v2
0732E022|Engenharia de recursos hídricos - Bacharelado|v2
0732E032|Engenharia de transportes - Bacharelado|v2
0732E042|Engenharia portuária - Bacharelado|v2
0732E053|Estradas - Tecnológico|v2
0732G013|Gestão de recursos hídricos - Tecnológico|v2
0732M013|Material de construção - Tecnológico|v2
0788P012|Programas interdisciplinares abrangendo engenharia, produção e construção - Bacharelado|v2
0811A012|Agroecologia - Bacharelado|v2
0811A013|Agroecologia - Tecnológico|v2
0811A022|Agroindústria - Bacharelado|v2
0811A023|Agroindústria - Tecnológico|v2
0811A024|Agroindústria - Sequencial|v2
0811A032|Agronegócio - Bacharelado|v2
0811A033|Agronegócio - Tecnológico|v2
0811A042|Agronomia - Bacharelado|v2
0811A043|Agronomia - Tecnológico|v2
0811A053|Agropecuária - Tecnológico|v2
0811C013|Cafeicultura - Tecnológico|v2
0811E012|Engenharia agrícola - Bacharelado|v2
0811E013|Engenharia agrícola - Tecnológico|v2
0811E022|Engenharia de biossistemas - Bacharelado|v2
0811F013|Fruticultura - Tecnológico|v2
0811F014|Fruticultura - Sequencial|v2
0811I013|Irrigação e drenagem - Tecnológico|v2
0811M013|Manejo da produção agrícola - Tecnológico|v2
0811V012|Viticultura e enologia - Bacharelado|v2
0811V013|Viticultura e enologia - Tecnológico|v2
0811Z012|Zootecnia - Bacharelado|v2
0811Z013|Zootecnia - Tecnológico|v2
0811Z014|Zootecnia - Sequencial|v2
0812H013|Horticultura - Tecnológico|v2
0821E012|Engenharia florestal - Bacharelado|v2
0821E013|Engenharia florestal - Tecnológico|v2
0821S013|Silvicultura - Tecnológico|v2
0831A012|Aquicultura - Bacharelado|v2
0831A013|Aquicultura - Tecnológico|v2
0831A014|Aquicultura - Sequencial|v2
0831E012|Engenharia de pesca - Bacharelado|v2
0831P013|Produção pesqueira - Tecnológico|v2
0841M012|Medicina veterinária - Bacharelado|v2
0841M013|Medicina veterinária - Tecnológico|v2
0841M014|Medicina veterinária - Sequencial|v2
0888P012|Programas interdisciplinares abrangendo agricultura, silvicultura, pesca e veterinária - Bacharelado|v2
0911O012|Odontologia - Bacharelado|v2
0911O014|Odontologia - Sequencial|v2
0912M012|Medicina - Bacharelado|v2
0912M013|Medicina - Tecnológico|v2
0912M014|Medicina - Sequencial|v2
0913E012|Enfermagem - Bacharelado|v2
0913E014|Enfermagem - Sequencial|v2
0914B012|Biomedicina - Bacharelado|v2
0914B014|Biomedicina - Sequencial|v2
0914O013|Oftálmica - Tecnológico|v2
0914O022|Optometria - Bacharelado|v2
0914O023|Optometria - Tecnológico|v2
0914P013|Prótese e órtese - Tecnológico|v2
0914P014|Prótese e órtese - Sequencial|v2
0914R013|Radiologia - Tecnológico|v2
0914R014|Radiologia - Sequencial|v2
0915E012|Educação física - Bacharelado|v2
0915E014|Educação física  - Sequencial|v2
0915F012|Fisioterapia - Bacharelado|v2
0915F022|Fonoaudiologia - Bacharelado|v2
0915N012|Nutrição - Bacharelado|v2
0915N013|Nutrição - Tecnológico|v2
0915N014|Nutrição - Sequencial|v2
0915P012|Podologia - Bacharelado|v2
0915P013|Podologia - Tecnológico|v2
0915T012|Terapia ocupacional - Bacharelado|v2
0916F012|Farmácia - Bacharelado|v2
0916F013|Farmácia - Tecnológico|v2
0916F014|Farmácia - Sequencial|v2
0917M012|Musicoterapia - Bacharelado|v2
0917P012|Práticas integrativas - Bacharelado|v2
0917P013|Práticas integrativas - Tecnológico|v2
0917P014|Práticas integrativas - Sequencial|v2
0918S012|Saúde coletiva - Bacharelado|v2
0918S013|Saúde coletiva - Tecnológico|v2
0918S014|Saúde coletiva - Sequencial|v2
0918S022|Saúde pública - Bacharelado|v2
0918S023|Saúde pública - Tecnológico|v2
0918S024|Saúde pública - Sequencial|v2
0921A014|Assistência a idosos e a deficientes - Sequencial|v2
0921G012|Gerontologia - Bacharelado|v2
0921G013|Gerontologia - Tecnológico|v2
0921G014|Gerontologia - Sequencial|v2
0923S012|Serviço social - Bacharelado|v2
0923S013|Serviço social - Tecnológico|v2
0923S014|Serviço social - Sequencial|v2
0988P012|Programas interdisciplinares abrangendo saúde e bem-estar - Bacharelado|v2
0988P013|Programas interdisciplinares abrangendo saúde e bem-estar - Tecnológico|v2
0988P014|Programas interdisciplinares abrangendo saúde e bem-estar - Sequencial|v2
1011E012|Economia doméstica - Bacharelado|v2
1012E012|Estética e cosmética - Bacharelado|v2
1012E013|Estética e cosmética - Tecnológico|v2
1012E014|Estética e cosmética - Sequencial|v2
1013G012|Gastronomia - Bacharelado|v2
1013G013|Gastronomia - Tecnológico|v2
1013G014|Gastronomia - Sequencial|v2
1014F013|Formação de técnicos e treinadores esportivos - Tecnológico|v2
1014F014|Formação de técnicos e treinadores esportivos - Sequencial|v2
1014G012|Gestão desportiva e de lazer - Bacharelado|v2
1014G013|Gestão desportiva e de lazer - Tecnológico|v2
1014G014|Gestão desportiva e de lazer - Sequencial|v2
1015E013|Eventos - Tecnológico|v2
1015E014|Eventos - Sequencial|v2
1015H012|Hotelaria - Bacharelado|v2
1015H013|Hotelaria - Tecnológico|v2
1015H014|Hotelaria - Sequencial|v2
1015T012|Turismo - Bacharelado|v2
1015T013|Turismo - Tecnológico|v2
1015T014|Turismo - Sequencial|v2
1022S012|Segurança no trabalho - Bacharelado|v2
1022S013|Segurança no trabalho - Tecnológico|v2
1022S014|Segurança no trabalho - Sequencial|v2
1031C012|Ciências militares - Bacharelado|v2
1032I013|Investigação e perícia - Tecnológico|v2
1032I014|Investigação e perícia - Sequencial|v2
1032S013|Segurança no trânsito - Tecnológico|v2
1032S014|Segurança no trânsito - Sequencial|v2
1032S023|Segurança privada - Tecnológico|v2
1032S024|Segurança privada - Sequencial|v2
1032S032|Segurança pública - Bacharelado|v2
1032S033|Segurança pública - Tecnológico|v2
1032S034|Segurança pública - Sequencial|v2
1032S043|Serviços penais - Tecnológico|v2
1032S044|Serviços penais - Sequencial|v2
1041C012|Ciências aeronáuticas - Bacharelado|v2
1041C013|Ciências aeronáuticas - Tecnológico|v2
1041C014|Ciências aeronáuticas - Sequencial|v2
1041G013|Gestão portuária - Tecnológico|v2
1041G014|Gestão portuária - Sequencial|v2
1041T013|Transporte aéreo - Tecnológico|v2
1041T023|Transporte terrestre - Tecnológico|v2
1041T024|Transporte terrestre  - Sequencial|v2"""


def get_dict_formacao_adequada_licen(stringa_disc):
    dict_disc = {}
    for linha in stringa_disc.split("\n"):
        list_item = linha.split(",")
        if list_item[0] not in dict_disc:
            dict_disc[list_item[0]] = []
        if list_item[2] == "0":
            dict_disc[list_item[0]] = dict_disc[list_item[0]] + [list_item[1]]
    return {chave: tuple(valor) for chave, valor in dict_disc.items()}


def get_dict_formacao_adequada_bach(stringa_disc):
    dict_disc = {}
    for linha in stringa_disc.split("\n"):
        list_item = linha.split(",")
        if list_item[0] not in dict_disc:
            dict_disc[list_item[0]] = []
        if list_item[2] == "1":
            dict_disc[list_item[0]] = dict_disc[list_item[0]] + [list_item[1]]
    return {chave: tuple(valor) for chave, valor in dict_disc.items()}


def get_dict_area_compl_pedago(stringa_compl):
    dict_disc = {}
    for linha in stringa_compl.split("\n"):
        list_item = linha.split(",")
        if list_item[0] not in dict_disc:
            dict_disc[list_item[0]] = []
        dict_disc[list_item[0]] = dict_disc[list_item[0]] + [int(list_item[1])]
    return dict_disc


def get_df_formacao_nome(stringa_compl):
    list_code = []
    list_nome = []
    for linha in stringa_compl.split("\n"):
        list_item = linha.split("|")
        list_code.append(list_item[0])
        list_nome.append(list_item[1])

    return (
        pd.DataFrame(data={"FORMACAO_COD": list_code, "FORMACAO_NOME": list_nome})
        .assign(
            FORMACAO_NOME=lambda x: x.apply(
                lambda row: row["FORMACAO_NOME"]
                .replace(" - ", "-")
                .replace(" ", "_")
                .replace(",", "-"),
                axis=1,
            )
        )
        .set_index("FORMACAO_COD")
    )


# fmt: off
def process_formacao_adequada_v1(temp_df2, year):
    # complementação pedagógica por curso. versão até 2018
    return (temp_df2
     .assign(licen_adequada=lambda x:x['DISCIPLINA_NOME'].map(dict_formacao_adequada_year_licen[year]))
     .assign(bach_adequada=lambda x:x['DISCIPLINA_NOME'].map(dict_formacao_adequada_year_bach[year]))
     .assign(FORMACAO_ADEQUADA=lambda x:np.select(
         [x.pipe(lambda data: np.vectorize(lambda curso, adequados: curso in adequados)(data['CO_CURSO_1'].values,  data['licen_adequada'].values) & x['TP_SITUACAO_CURSO_1'].isin([1])),
          x.pipe(lambda data: np.vectorize(lambda curso, adequados: curso in adequados)(data['CO_CURSO_1'].values, data['bach_adequada'].values) & x['IN_COM_PEDAGOGICA_1'].isin([1]) & x['TP_SITUACAO_CURSO_1'].isin([1])),
          x.pipe(lambda data: np.vectorize(lambda curso, adequados: curso in adequados)(data['CO_CURSO_2'].values,  data['licen_adequada'].values) & x['TP_SITUACAO_CURSO_2'].isin([1])),
          x.pipe(lambda data: np.vectorize(lambda curso, adequados: curso in adequados)(data['CO_CURSO_2'].values, data['bach_adequada'].values) & x['IN_COM_PEDAGOGICA_2'].isin([1]) & x['TP_SITUACAO_CURSO_2'].isin([1])),
          x.pipe(lambda data: np.vectorize(lambda curso, adequados: curso in adequados)(data['CO_CURSO_3'].values,  data['licen_adequada'].values) & x['TP_SITUACAO_CURSO_3'].isin([1])),
          x.pipe(lambda data: np.vectorize(lambda curso, adequados: curso in adequados)(data['CO_CURSO_3'].values, data['bach_adequada'].values) & x['IN_COM_PEDAGOGICA_3'].isin([1]) & x['TP_SITUACAO_CURSO_3'].isin([1]))],
         [True, True, True, True, True, True], default=False))
           )['FORMACAO_ADEQUADA'].astype(np.uint8)

# fmt: off
def process_formacao_adequada_v2(temp_df, year):
    # complementação pedagógica por área. versão a partir de 2019
    return (temp_df
         .assign(licen_adequada=lambda x:x['DISCIPLINA_NOME'].map(dict_formacao_adequada_year_licen[year]))
         .assign(bach_adequada=lambda x:x['DISCIPLINA_NOME'].map(dict_formacao_adequada_year_bach[year]))
         .assign(area_compl_pedago=lambda x:x['DISCIPLINA_NOME'].map(dict_area_compl_pedago))

         .assign(adq_pedago_1=lambda x:x.pipe(lambda data: np.vectorize(lambda value, accepted_values: value in accepted_values)(data['CO_AREA_COMPL_PEDAGOGICA_1'].values, data['area_compl_pedago'].values)) )
         .assign(adq_pedago_2=lambda x:x.pipe(lambda data: np.vectorize(lambda value, accepted_values: value in accepted_values)(data['CO_AREA_COMPL_PEDAGOGICA_2'].values, data['area_compl_pedago'].values)) )
         .assign(adq_pedago_3=lambda x:x.pipe(lambda data: np.vectorize(lambda value, accepted_values: value in accepted_values)(data['CO_AREA_COMPL_PEDAGOGICA_3'].values, data['area_compl_pedago'].values)) )
         .assign(adq_pedago=lambda x:x['adq_pedago_1'] | x['adq_pedago_2'] | x['adq_pedago_3'])

         .assign(FORMACAO_ADEQUADA=lambda x:np.select([
              x.pipe(lambda data: np.vectorize(lambda curso, adequados: curso in adequados)(data['CO_CURSO_1'].values,  data['licen_adequada'].values) & x['TP_SITUACAO_CURSO_1'].isin([1])),
              x.pipe(lambda data: np.vectorize(lambda curso, adequados: curso in adequados)(data['CO_CURSO_1'].values, data['bach_adequada'].values) & x['adq_pedago'] & x['TP_SITUACAO_CURSO_1'].isin([1])),
              x.pipe(lambda data: np.vectorize(lambda curso, adequados: curso in adequados)(data['CO_CURSO_2'].values,  data['licen_adequada'].values) & x['TP_SITUACAO_CURSO_2'].isin([1])),
              x.pipe(lambda data: np.vectorize(lambda curso, adequados: curso in adequados)(data['CO_CURSO_2'].values, data['bach_adequada'].values) & x['adq_pedago'] & x['TP_SITUACAO_CURSO_2'].isin([1])),
              x.pipe(lambda data: np.vectorize(lambda curso, adequados: curso in adequados)(data['CO_CURSO_3'].values,  data['licen_adequada'].values) & x['TP_SITUACAO_CURSO_3'].isin([1])),
              x.pipe(lambda data: np.vectorize(lambda curso, adequados: curso in adequados)(data['CO_CURSO_3'].values, data['bach_adequada'].values) & x['adq_pedago'] & x['TP_SITUACAO_CURSO_3'].isin([1]))
         ],
             [True, True, True, True, True, True], default=False))
    )['FORMACAO_ADEQUADA'].astype(np.uint8)


def process_formacao_adequada(temp_df, year):
    dict_process= {
        2014: process_formacao_adequada_v1,
        2015: process_formacao_adequada_v1,
        2016: process_formacao_adequada_v1,
        2017: process_formacao_adequada_v1,
        2018: process_formacao_adequada_v1,
        2019: process_formacao_adequada_v2,
        2020: process_formacao_adequada_v2}
    process = dict_process[year]
    return process(temp_df, year)

def break_disciplinas(data, list_disciplina):
    cols_id = [x for x in list(data.columns) if x not in list_disciplina]
    list_dfs=[]
    for disciplina in list_disciplina:
        list_dfs.append(data
              .query(f'{disciplina}==1')[cols_id]
              .assign(DISCIPLINA_NOME=disciplina)
        )
    return pd.concat(list_dfs)

# fmt: off
def process_ensino_infantil(df_dim_docentes, df_formacao_nome, year):

    return (df_dim_docentes
        .pipe(lambda y:y.reindex(
            ['CO_MUNICIPIO', 'TP_DEPENDENCIA', 'TP_ETAPA_ENSINO',
             'TP_ESCOLARIDADE', 'TP_TIPO_DOCENTE',
             'CO_CURSO_1', 'CO_CURSO_2', 'CO_CURSO_3',
             'TP_SITUACAO_CURSO_1','TP_SITUACAO_CURSO_2','TP_SITUACAO_CURSO_3'] +
            [x for x in cols_compl if x in y.columns],axis=1))
        .query("TP_ETAPA_ENSINO==[1,2,3] and TP_TIPO_DOCENTE==[1,5,6]")
        .assign(DISCIPLINA_NOME='MULTIDISCIPLINAR')
        .assign(FORMACAO_ADEQUADA=lambda x: process_formacao_adequada(x, year))
        .assign(FORMACAO_COD=lambda x:x.apply( lambda row:'|'.join(sorted(
            [y for y in [str(row['CO_CURSO_1']), str(row['CO_CURSO_2']), str(row['CO_CURSO_3'])]
            if y != 'None'])), axis=1))
        .assign(FORMACAO_NOME_1=lambda x:x[['CO_CURSO_1']].merge(df_formacao_nome,left_on='CO_CURSO_1',right_index=True,how='left')['FORMACAO_NOME'].where(x['TP_SITUACAO_CURSO_1'].isin([1]),np.nan))
        .assign(FORMACAO_NOME_2=lambda x:x[['CO_CURSO_2']].merge(df_formacao_nome,left_on='CO_CURSO_2',right_index=True,how='left')['FORMACAO_NOME'].where(x['TP_SITUACAO_CURSO_2'].isin([1]),np.nan))
        .assign(FORMACAO_NOME_3=lambda x:x[['CO_CURSO_3']].merge(df_formacao_nome,left_on='CO_CURSO_3',right_index=True,how='left')['FORMACAO_NOME'].where(x['TP_SITUACAO_CURSO_3'].isin([1]),np.nan))
        .assign(FORMACAO_NOME=lambda x:x.apply( lambda row:'|'.join(sorted(
            [y for y in [str(row['FORMACAO_NOME_1']), str(row['FORMACAO_NOME_2']), str(row['FORMACAO_NOME_3'])]
            if y != 'nan'])), axis=1))
        .assign(FORMACAO_COD=lambda x:x['FORMACAO_COD'].replace('','-'))
        .assign(FORMACAO_NOME=lambda x:x['FORMACAO_NOME'].replace('','-'))
        .assign(DOCENCIA_TOTAL= np.uint8(1))
        .assign(ETAPA='1_ENSINO_INFANTIL')
        .assign(ANO=np.uint16(year))
        .reindex(['ANO','ETAPA', 'CO_MUNICIPIO', 'TP_DEPENDENCIA', 'DISCIPLINA_NOME',
                'FORMACAO_COD', 'FORMACAO_NOME','FORMACAO_ADEQUADA', 'DOCENCIA_TOTAL'],axis=1)
        .groupby(['ANO', 'ETAPA', 'CO_MUNICIPIO', 'TP_DEPENDENCIA',
                'DISCIPLINA_NOME','FORMACAO_COD','FORMACAO_NOME']).sum().reset_index()
        .astype({'CO_MUNICIPIO':'uint32'})
        .astype({'TP_DEPENDENCIA':'uint8'})
        .astype({'ANO':'uint16'})
        .assign(**{k: lambda df_, k=k: df_[k].fillna(0).astype('uint32') for k in
                    (['CO_MUNICIPIO','FORMACAO_ADEQUADA', 'DOCENCIA_TOTAL'])})
        )

# fmt: off
def process_fund_anos_iniciais(df_dim_docentes, df_formacao_nome, year):
    return (df_dim_docentes
        .pipe(lambda y:y.reindex(
            ['CO_MUNICIPIO', 'TP_DEPENDENCIA','TP_ETAPA_ENSINO', 'TP_ESCOLARIDADE',
            'TP_TIPO_DOCENTE', 'CO_CURSO_1', 'CO_CURSO_2', 'CO_CURSO_3',
            'TP_SITUACAO_CURSO_1','TP_SITUACAO_CURSO_2','TP_SITUACAO_CURSO_3'] +
            [x for x in cols_compl if x in y.columns]+cols_disciplinas,axis=1))
        .query("TP_ETAPA_ENSINO==[4,5,6,7,8,14,15,16,17,18] and TP_TIPO_DOCENTE==[1,5,6]")
        .drop(columns=['TP_ETAPA_ENSINO','TP_TIPO_DOCENTE'],axis=1)
        .pipe(lambda x:break_disciplinas(x, cols_disciplinas))
        .assign(DISCIPLINA_NOME=lambda x: x['DISCIPLINA_NOME'].replace(
            {'IN_DISC_LINGUA_INGLES':'IN_DISC_LINGUA_ESTRANGEIRA',
            'IN_DISC_LINGUA_ESPANHOL':'IN_DISC_LINGUA_ESTRANGEIRA',
            'IN_DISC_LINGUA_FRANCES':'IN_DISC_LINGUA_ESTRANGEIRA',
            'IN_DISC_LINGUA_OUTRA':'IN_DISC_LINGUA_ESTRANGEIRA'}))
        .assign(DISCIPLINA_NOME_BKP=lambda x: x['DISCIPLINA_NOME'])
        .assign(DISCIPLINA_NOME=lambda x: x['DISCIPLINA_NOME_BKP']
                .where(x['DISCIPLINA_NOME_BKP'].isin(['IN_DISC_LINGUA_ESTRANGEIRA']),
                        'MULTIDISCIPLINAR'))
        .reset_index(drop=True)
        .assign(FORMACAO_ADEQUADA=lambda x: process_formacao_adequada(x, year))
        .assign(DISCIPLINA_NOME=lambda x: x['DISCIPLINA_NOME_BKP'].str.replace('IN_DISC_',''))
        .drop(columns=['DISCIPLINA_NOME_BKP'])
        .assign(FORMACAO_COD=lambda x:x.apply( lambda row:'|'.join(sorted(
            [y for y in [str(row['CO_CURSO_1']), str(row['CO_CURSO_2']), str(row['CO_CURSO_3'])]
            if y != 'None'])), axis=1))
        .assign(FORMACAO_NOME_1=lambda x:x[['CO_CURSO_1']].merge(df_formacao_nome,left_on='CO_CURSO_1',right_index=True,how='left')['FORMACAO_NOME'].where(x['TP_SITUACAO_CURSO_1'].isin([1]),np.nan))
        .assign(FORMACAO_NOME_2=lambda x:x[['CO_CURSO_2']].merge(df_formacao_nome,left_on='CO_CURSO_2',right_index=True,how='left')['FORMACAO_NOME'].where(x['TP_SITUACAO_CURSO_2'].isin([1]),np.nan))
        .assign(FORMACAO_NOME_3=lambda x:x[['CO_CURSO_3']].merge(df_formacao_nome,left_on='CO_CURSO_3',right_index=True,how='left')['FORMACAO_NOME'].where(x['TP_SITUACAO_CURSO_3'].isin([1]),np.nan))
        .assign(FORMACAO_NOME=lambda x:x.apply( lambda row:'|'.join(sorted(
            [y for y in [str(row['FORMACAO_NOME_1']), str(row['FORMACAO_NOME_2']), str(row['FORMACAO_NOME_3'])]
            if y != 'nan'])), axis=1))
        .assign(FORMACAO_COD=lambda x:x['FORMACAO_COD'].replace('','-'))
        .assign(FORMACAO_NOME=lambda x:x['FORMACAO_NOME'].replace('','-'))
        .assign(DOCENCIA_TOTAL= np.uint8(1))
        .assign(ANO=np.uint16(year))
        .assign(ETAPA='2_FUND_ANOS_INICIAIS')
        .reindex(['ANO','ETAPA', 'CO_MUNICIPIO', 'TP_DEPENDENCIA', 'DISCIPLINA_NOME',
                'FORMACAO_COD', 'FORMACAO_NOME','FORMACAO_ADEQUADA', 'DOCENCIA_TOTAL'],axis=1)
        .groupby(['ANO', 'ETAPA', 'CO_MUNICIPIO', 'TP_DEPENDENCIA',
                'DISCIPLINA_NOME','FORMACAO_COD','FORMACAO_NOME']).sum().reset_index()
        .astype({'CO_MUNICIPIO':'uint32'})
        .astype({'TP_DEPENDENCIA':'uint8'})
        .astype({'ANO':'uint16'})
        .assign(**{k: lambda df_, k=k: df_[k].fillna(0).astype('uint32') for k in
                    (['CO_MUNICIPIO','FORMACAO_ADEQUADA', 'DOCENCIA_TOTAL'])})
        )
# fmt: off
def process_fund_finais_ens_medio(df_dim_docentes, df_formacao_nome, year):
    return (df_dim_docentes
        .pipe(lambda y:y.reindex(
            ['CO_MUNICIPIO', 'TP_DEPENDENCIA','TP_ETAPA_ENSINO', 'TP_ESCOLARIDADE',
            'TP_TIPO_DOCENTE', 'CO_CURSO_1', 'CO_CURSO_2', 'CO_CURSO_3',
            'TP_SITUACAO_CURSO_1','TP_SITUACAO_CURSO_2','TP_SITUACAO_CURSO_3'] +
            [x for x in cols_compl if x in y.columns]+cols_disciplinas,axis=1))
        .query("TP_ETAPA_ENSINO==[9,10,11,12,13,19,20,21,41,22,23,24,25,26,27,28,29,35,36,37,38] and TP_TIPO_DOCENTE==[1,5,6]")
        .drop(columns=['TP_TIPO_DOCENTE'],axis=1)
        .assign(ETAPA=0)
        .assign(ETAPA=lambda x:x['ETAPA'].where(~x['TP_ETAPA_ENSINO'].isin([9,10,11,12,13,19,20,21,41,22,23,24]), '3_FUND_ANOS_FINAIS'))
        .assign(ETAPA=lambda x:x['ETAPA'].where(~x['TP_ETAPA_ENSINO'].isin([25,26,27,28,29,35,36,37,38]), '4_ENSINO_MEDIO'))
        .drop(columns=['TP_ETAPA_ENSINO'],axis=1)
        .pipe(lambda x:break_disciplinas(x, cols_disciplinas))
        .assign(DISCIPLINA_NOME=lambda x: x['DISCIPLINA_NOME'].replace(
            {'IN_DISC_LINGUA_INGLES':'IN_DISC_LINGUA_ESTRANGEIRA',
            'IN_DISC_LINGUA_ESPANHOL':'IN_DISC_LINGUA_ESTRANGEIRA',
            'IN_DISC_LINGUA_FRANCES':'IN_DISC_LINGUA_ESTRANGEIRA',
            'IN_DISC_LINGUA_OUTRA':'IN_DISC_LINGUA_ESTRANGEIRA'}))
        .reset_index(drop=True)
        .assign(FORMACAO_ADEQUADA=lambda x: process_formacao_adequada(x, year))
        .assign(DISCIPLINA_NOME=lambda x: x['DISCIPLINA_NOME'].str.replace('IN_DISC_',''))
        .assign(FORMACAO_COD=lambda x:x.apply( lambda row:'|'.join(sorted(
            [y for y in [str(row['CO_CURSO_1']), str(row['CO_CURSO_2']), str(row['CO_CURSO_3'])]
            if y != 'None'])), axis=1))
        .assign(FORMACAO_NOME_1=lambda x:x[['CO_CURSO_1']].merge(df_formacao_nome,left_on='CO_CURSO_1',right_index=True,how='left')['FORMACAO_NOME'].where(x['TP_SITUACAO_CURSO_1'].isin([1]),np.nan))
        .assign(FORMACAO_NOME_2=lambda x:x[['CO_CURSO_2']].merge(df_formacao_nome,left_on='CO_CURSO_2',right_index=True,how='left')['FORMACAO_NOME'].where(x['TP_SITUACAO_CURSO_2'].isin([1]),np.nan))
        .assign(FORMACAO_NOME_3=lambda x:x[['CO_CURSO_3']].merge(df_formacao_nome,left_on='CO_CURSO_3',right_index=True,how='left')['FORMACAO_NOME'].where(x['TP_SITUACAO_CURSO_3'].isin([1]),np.nan))
        .assign(FORMACAO_NOME=lambda x:x.apply( lambda row:'|'.join(sorted(
            [y for y in [str(row['FORMACAO_NOME_1']), str(row['FORMACAO_NOME_2']), str(row['FORMACAO_NOME_3'])]
            if y != 'nan'])), axis=1))
        .assign(FORMACAO_COD=lambda x:x['FORMACAO_COD'].replace('','-'))
        .assign(FORMACAO_NOME=lambda x:x['FORMACAO_NOME'].replace('','-'))
        .assign(DOCENCIA_TOTAL= np.uint8(1))
        .assign(ANO=np.uint16(year))
        .reindex(['ANO','ETAPA', 'CO_MUNICIPIO', 'TP_DEPENDENCIA', 'DISCIPLINA_NOME',
                'FORMACAO_COD', 'FORMACAO_NOME','FORMACAO_ADEQUADA', 'DOCENCIA_TOTAL'],axis=1)
        .groupby(['ANO', 'ETAPA', 'CO_MUNICIPIO', 'TP_DEPENDENCIA',
                'DISCIPLINA_NOME','FORMACAO_COD','FORMACAO_NOME']).sum().reset_index()
        .astype({'CO_MUNICIPIO':'uint32'})
        .astype({'TP_DEPENDENCIA':'uint8'})
        .astype({'ANO':'uint16'})
        .assign(**{k: lambda df_, k=k: df_[k].fillna(0).astype('uint32') for k in
                    (['CO_MUNICIPIO','FORMACAO_ADEQUADA', 'DOCENCIA_TOTAL'])})
        )

dict_formacao_adequada_v1_licen = get_dict_formacao_adequada_licen(str_formacao_adequada_v1)
dict_formacao_adequada_v1_bach = get_dict_formacao_adequada_bach(str_formacao_adequada_v1)
dict_formacao_adequada_v2_licen = get_dict_formacao_adequada_licen(str_formacao_adequada_v2)
dict_formacao_adequada_v2_bach = get_dict_formacao_adequada_bach(str_formacao_adequada_v2)

dict_formacao_adequada_year_licen={2014: dict_formacao_adequada_v1_licen,
                    2015: dict_formacao_adequada_v1_licen,
                    2016: dict_formacao_adequada_v1_licen,
                    2017: dict_formacao_adequada_v1_licen,
                    2018: dict_formacao_adequada_v1_licen,
                    2019: dict_formacao_adequada_v1_licen,
                    2020: dict_formacao_adequada_v2_licen}
dict_formacao_adequada_year_bach={2014: dict_formacao_adequada_v1_bach,
                    2015: dict_formacao_adequada_v1_bach,
                    2016: dict_formacao_adequada_v1_bach,
                    2017: dict_formacao_adequada_v1_bach,
                    2018: dict_formacao_adequada_v1_bach,
                    2019: dict_formacao_adequada_v1_bach,
                    2020: dict_formacao_adequada_v2_bach}

dict_area_compl_pedago = get_dict_area_compl_pedago(str_area_compl_pedago)

# fmt: off
def model(dbt, fal):

    year = 2017
    # load
    df_dim_docentes = dbt.source("raw", "DIM_DOCENTES_NORTE_2017")

    df_formacao_nome = get_df_formacao_nome(str_curso_nome)


    # ensino infantil
    dim_ensino_infantil = process_ensino_infantil(df_dim_docentes,
                                                  df_formacao_nome,
                                                  year)

    # fund_anos_iniciais
    dim_fund_anos_iniciais = process_fund_anos_iniciais(df_dim_docentes,
                                                        df_formacao_nome,
                                                        year)

    # fund_finais_ens_medio
    dim_fund_finais_ens_medio = process_fund_finais_ens_medio(df_dim_docentes,
                                                              df_formacao_nome,
                                                              year)


    return pd.concat([dim_ensino_infantil,
                      dim_fund_anos_iniciais,
                      dim_fund_finais_ens_medio])


# This part is user provided model code
# you will need to copy the next section to run the code
# COMMAND ----------
# this part is dbt logic for get ref work, do not modify

def ref(*args, **kwargs):
    refs = {}
    key = '.'.join(args)
    version = kwargs.get("v") or kwargs.get("version")
    if version:
        key += f".v{version}"
    dbt_load_df_function = kwargs.get("dbt_load_df_function")
    return dbt_load_df_function(refs[key])


def source(*args, dbt_load_df_function):
    sources = {"raw.DIM_DOCENTES_NORTE_2017": "\"postgres\".\"raw\".\"DIM_DOCENTES_NORTE_2017\""}
    key = '.'.join(args)
    return dbt_load_df_function(sources[key])


config_dict = {}


class config:
    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def get(key, default=None):
        return config_dict.get(key, default)

class this:
    """dbt.this() or dbt.this.identifier"""
    database = "postgres"
    schema = "dbt_staging"
    identifier = "dim_educ_bas_docentes_15_2017_norte"
    
    def __repr__(self):
        return '"postgres"."dbt_staging"."dim_educ_bas_docentes_15_2017_norte"'


class dbtObj:
    def __init__(self, load_df_function) -> None:
        self.source = lambda *args: source(*args, dbt_load_df_function=load_df_function)
        self.ref = lambda *args, **kwargs: ref(*args, **kwargs, dbt_load_df_function=load_df_function)
        self.config = config
        self.this = this()
        self.is_incremental = False

# COMMAND ----------


# Generated by dbt-fal

def main(read_df, write_df, fal_context=None):
  dbt_context = dbtObj(read_df)
  df = model(dbt_context, fal_context)
  return write_df(
      'postgres.dbt_staging.dim_educ_bas_docentes_15_2017_norte',
      df
  )