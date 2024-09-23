# CRUD com PostgreSQL e Streamlit

<img src='https://github.com/jorgeplatero/tijolada/blob/8885db4add268b90f76b9aac7324273168902525/img/logo.png' width='150'/>

## Descrição do Projeto

Este projeto consiste em uma aplicação que oferece uma interface Streamlit para interação com banco de dados PostgreSQL e foi desenvolvida com o objetivo de permitir a realização de todas as operações CRUD. A aplicação também conta com um dashboard dinâmico para uma análise completa dos dados registrados pelo usuário, permitindo com que este possa visualizá-los em tempo real por meio de gráficos interativos.

**Benefícios das ferramentas utilizadas**

🚀Desenvolvimento acelerado: o Streamlit simplifica o desenvolvimento de aplicações web, permitindo a criação e alteração de interfaces de forma rápida e eficiente.

💡Análise de dados aprimorada: um dashboard construído com a biblioteca Plotly é dinâmico e suporta uma infinidade de customizações.

## Arquitetura do Projeto

<p align='center'><img src='img/arquitetura_projeto_crud.png'/ width=500></p>

### Banco de Dados

O banco de dados conta com triggers que têm por funcionalidade inserir os valores totais de compras e vendas dado a quantidade de itens inseridos e também de atualizar o estoque. O ERD abaixo ilustra o esquema utilizado.

![erd](https://github.com/jorgeplatero/building_supply_stock/blob/8885db4add268b90f76b9aac7324273168902525/img/erd_tijolada.png)

### ETL dos Dados

Os dados são extraídos da interface Streamlit dada as requisições do usuário e carregadas do banco de dados via python. O fluxo inverso é realizado para exibir dados registrados na interface Streamlit para o usuário, bem como para exibir os indicadores no dashboard.

## Tecnologias Utilizadas

<img src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg' width='50' height='50'/> 
<img src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-plain-wordmark.svg' width='50' height='50'/> 
<img src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/streamlit/streamlit-original-wordmark.svg' width='60' height='60'/> 

## Fontes de Dados

Os dados para teste foram gerados via [Google AI Studio](https://aistudio.google.com/app/prompts/new_chat?pli=1). Os prompts e os comandos SQL utilizados para construção da base de dados e inserção de dados estão disponíveis neste [repositório](https://github.com/jorgeplatero/tijolada/tree/5793c2aa3f6a697a88c3833fce101e501d87ab0e/docs).
