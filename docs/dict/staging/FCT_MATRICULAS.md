| Nome da Coluna        | Descrição                                                                   | Tipo   | Categorias                              | Observação    |
|:----------------------|:----------------------------------------------------------------------------|:-------|:----------------------------------------|:--------------|
| ANO                   | Ano do censo que a matrícula foi realizada.                                 | INT    |                                         |               |
| FK_ESTADO_ID          | Código do estado em que a matrícula foi realizada.                          | INT    |                                         |               |
| FK_MUNICIPIO_ID       | Código do município em que a matrícula foi realizada.                       | INT    |                                         |               |
| FK_ESCOLA_ID          | Código do instituição de ensino  em que a matrícula foi realizada.          | INT    |                                         |               |
| GENERO                | Genero a qual o aluno pertence.                                             | INT    | 1-Masculino                             |               |
|                       |                                                                             |        | 2-Feminino                              |               |
| GRUPO_ETNICO          | Grupo étnico a qual o aluno pertence.                                       | INT    | 0-Não declarada                         |               |
|                       |                                                                             |        | 1-Branca                                |               |
|                       |                                                                             |        | 2-Preta                                 |               |
|                       |                                                                             |        | 3-Parda                                 |               |
|                       |                                                                             |        | 4-Amarela                               |               |
|                       |                                                                             |        | 5-Indígena                              |               |
| IDADE_REFERENCIA      | Idade do aluno até a realização do censo naquele ano.                       | INT    |                                         |               |
| FK_FAIXAS_ETARIAS_ID  | Código da faixa etária definida pelo INEP em que a matrícula foi realizada. | INT    |                                         |               |
| NIVEL_EDUCACIONAL     | Nível educacional definido pelo INEP que a matrícula foi realizada.         | INT    | 1-Creche                                |               |
|                       |                                                                             |        | 2-Pré-Escola                            |               |
|                       |                                                                             |        | 3-Educação Infantil Unificada           |               |
|                       |                                                                             |        | 4-Ensino Fundamental -anos iniciais     |               |
|                       |                                                                             |        | 5-Ensino Fundamental -anos finais       |               |
|                       |                                                                             |        | 6-Ensino Médio                          |               |
|                       |                                                                             |        | 7-Turmas multisseriadas e multieatapas  |               |
|                       |                                                                             |        | 8-EJA -Ensino Fundamental               |               |
|                       |                                                                             |        | 9-EJA -Ensino Médio                     |               |
|                       |                                                                             |        | 10-Educação Profissional                |               |
|                       |                                                                             |        | 11-Não classificada                     |               |
| QUANTIDADE_MATRICULAS | Quantidade de matrículas registradas.                                       | INT    |                                         |               |