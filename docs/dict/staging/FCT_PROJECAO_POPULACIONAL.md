| Nome da Coluna       | Descrição                            | Tipo   | Categorias   | Observação              |
|:---------------------|:-------------------------------------|:-------|:-------------|:------------------------|
| ANO                  | Ano referente a população projetada. | INT    |              |                         |
| FK_ESTADO_ID         | Código da UF.                        | INT    |              |                         |
| FK_MUNICIPIO_ID      | Código do Município.                 | INT    |              |                         |
| FK_FAIXAS_ETARIAS_ID | Código da Faixa que foi projetada.   | INT    | 1 a 11       | 1 = idade de 0 a 3      |
|                      |                                      |        |              | 2 = idade de 4 a 5      |
|                      |                                      |        |              | 3 = idade de 6 a 10     |
|                      |                                      |        |              | 4 = idade de 11 a 14    |
|                      |                                      |        |              | 5 = idade de 15 a 17    |
|                      |                                      |        |              | 6 = idade de 18 a 24    |
|                      |                                      |        |              | 7 = idade de 25 a 29    |
|                      |                                      |        |              | 8 = idade de 30 a 40    |
|                      |                                      |        |              | 9 = idade de 41 a 50    |
|                      |                                      |        |              | 10 = idade de 51 a 64   |
|                      |                                      |        |              | 11 = idade maior que 64 |
| QUANTIDADE_ESTIMADA  | Quantidade populacional estimada.    | INT    |              |                         |
| FK_METODO_ID         | Código                               | INT    |              |                         |