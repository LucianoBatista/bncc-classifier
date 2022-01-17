---
title: Dados e Solução
summary: Data tracking, Fonte e Base de Dados 
authors:
    - Luciano
    - Pedro
    - Brisa
    - Will
date: 2021-24-12
---

## Data Tracking

| Perguntas de Negócio      | Dados                          | Base/Calculada | Cálculo | Fonte de dado |
| ----------- | ------------------------------------ |------------------------|---------|---------------|
| Como classificar questões de acordo a BNCC?       | Questões previamente classificadas  | Calculada | {++à definir++} | Base de dados Studos |
| Como desenvolver raciocínio lógico/matemático nas escolas?       | Questões Classificadas | Calculada | {++à definir++} | Base de dados Studos |
| Como melhorar a eficiência do ensino na sala de aula?       | App com Questões Classificadas  | Calculada | {++à definir++} | Base de dados Studos |
| Como ajudar o professor na elaboração de avaliações e atividades nas escolas       | App com Questões Classificadas  | Calculada | {++à definir++} | Base de dados Studos |


## Fonte

Como fonte de dados, iremos utilizar uma base disponibilizada pela Studos, uma EdTech onde o integrante do grupo Luciano, trabalha. A base não contém informações sensíveis e conta com questões classificadas dentro dos códigos da BNCC, assim como informações necessárias para a criação dos quatro classificadores.

Contamos com a liberação de **+4M de questões classificadas** com suas áreas de conhecimento e assuntos. Dessas, **8.4k possuem classificação das habilidades da BNCC.**   Além disso, tem acesso público ao documento da BNCC contendo informações específicas dos códigos.


## Base de Dados

Como iremos trabalhar na construção de quatro classificadores é muito provável que ao longo do tempo precisemos adicionar ou remover variáveis da análise. No momento, o primeiro dataset que temos em mão para trabalhar vai conter as seguintes variáveis:

- **question (str)**: texto contendo o conteúdo da questão
- **bulletType (int)**: tipo da questão, se foi múltipla-escolha, certo ou errado, discursiva…
- **sst_name (str)**: assunto da questão
- **ss_name (str)**: disciplina da questão
- **ssa_name (str)**: área de conhecimento (Fundamental I, Fundamental II ou Ensino Médio)
- **code (str)**: conjunto de códigos da BNCC
- **description (str)**: descrição dos códigos da BNCC
