---
title: Prova
summary: Colocando a solução em Produção.
authors:
    - Luciano
    - Pedro
    - Brisa
date: 2021-24-12
---

# Exploratory Data Analysis

Como foi explicado nos tópicos anteriores, iremos construir 4 diferentes classificadores e ambos terão sua análise exploratória dos dados, pois precisarão de uma nova coleta. 

Nesse primeiro momento, nós estamos focados na criação do primeiro classificador, que vai buscar classificar se a questão é Ensino Fundamental I e II (EFI e EFII) ou Ensino Médio (EM).

## Target

Sendo assim, foram coletados 100k de observações onde seguem a seguinte distribuição:

- **Médio e Pré-Vestibular**: 35676
- **Fundamental II**: 33790
- **Fundamental I**: 18379
- **Outras (Concurso, Militar, OAB)**: 12155

Aqui já foi identificado que precisaremos dropar algumas observações que não são úteis para nosso problema, que seriam as classes: Concurso, Militar e OAB.

## Drop de Colunas

O dataset também trouxe dados sobre o Componente Curricular, porém, como estamos tratando de uma cadeia de classificadores, essa é uma informação que a princípio o modelo não teria, e consequentemente não teria acesso também aos assuntos. Sendo assim, optamos por dropar essas colunas e permanecendo apenas com:

- id (int): id da questão no banco
- question: texto da questão
- bulletType: tipo da questão
- scholar_lvl: nível escolar (EM, EFI, EFII)

## BulletType

Essa variável trás 7 tipos de questões:

1. Somatória
2. Múltipla Escolha
3. Certo e Errado
4. Discursiva
5. Redação ou items que é necessário enviar foto da resolução
6. Questões com mais de uma alternativa certa
7. Não representa nada em específico

Dessa forma, entendemos que drop os tipos 5, 6 e 7 faria sentido:

- Redação não está envolvida no componente curricular de Linguagens e sua Tecnologias
- Tipo 6 possui muito poucas observações.
- Ao observar o conteúdo da questões tipo 7, não existe uma ordem no formato dessas questões, por isso, iremos dropar também.

E a distribuição da variável `BulletType` ficou assim:

1. 2968
2. 68604
3. 1179
4. 13881
5. 999
6. 5
7. 209

Onde temos muito mais **questões do tipo múltipla-escolha**, provavelmente por ser a mais utilizada em simulados tipo Enem. 


## Question

Sendo assim, nos resta analisar a variável principal do dataset (`question`). Apesar de ter uma série de análises que seria interessante realizar, observamos que maior parte delas necessitaria de um texto o mais limpo possível. 

O texto das questões são exibidos no formato web, então temos uma quantidade bem grande **tags html** para remover. Então esse se tornou nosso primeiro step do data cleaning. Seguimos com uma remoção de números, pois existem muitos números indicando alternativas das questões, assim que em questões somatórias existe a contagem das respostas (00, 11, 22 ...).

Realizar uma contagem dos números pode ser uma boa variável quando estivermos classificando o Componente Curricular.

Após isso, seguimos as seguintes etapas: 

- Remoção de pontuação
- lowercase das palavras
- remoção de stopwords padrões baseada na lib NLTK.





