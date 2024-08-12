| Nome da Variável          | Descrição da Variável                                                                             | Tipo   | Categoria   | Observação   |
|:--------------------------|:--------------------------------------------------------------------------------------------------|:-------|:------------|:-------------|
|                           |                                                                                                   |        |             |              |
| ID_FCT_META_TRES          | ID númerico para a meta.                                                                          | INT    |             |              |
| ANO                       | Ano do registro.                                                                                  | INT    |             |              |
| FK_ESTADO_CODIGO          | Código do Estado.                                                                                 | INT    |             |              |
| FK_MUNICIPIO_CODIGO       | Código do Município.                                                                              | INT    |             |              |
| INDICADOR                 | Define a qual indicador o registro pertence.                                                      | CHAR   | 3A,3B       |              |
| QT_MAT_IND                | Quantidade de matrículas  da faixa.                                                               | INT    |             |              |
| POP_ESTIMADA_IND_ORIGINAL | População estimada para aquela faixa em determinado ano.                                          | INT    |             |              |
| POP_ESTIMADA_IND_AJUSTADA | População estimada ajustada a partir das matrículas para os casos dos marcadores das colunas FLAG | INT    |             |              |
| FLAG_SUBESTIMADA          | Quando Quantidade de Matrículas é superior a População Estimada                                   | INT    | 1, 0        |              |
| FLAG_MUNIC_NOVO           | Quando População Estimada não é possível de ser calculada                                         | INT    | 1, 0        |              |
| PP_ATENDIMENTO_IND        | Porcentagem de Atendimento do Indicador                                                           | FLOAT  |             |              |