# CRUD com PostgreSQL e Streamlit

<img src='https://github.com/jorgeplatero/building_supply_stock/blob/8885db4add268b90f76b9aac7324273168902525/img/logo.png' width='150'/>

## Descrição do Projeto

Este projeto consiste em uma aplicação que oferece uma interface para interação com banco de dados e foi desenvolvida com o objetivo de permitir a realização de todas as operações CRUD. A aplicação também conta com um dashboard dinâmico desenvolvido com a biblioteca Plotly para uma análise completa dos dados registrados pelo usuário. O dashboard permite visualizar dados em tempo real por meio de gráficos interativos, oferecendo insights para a tomada de decisões do negócio.

**Benefícios das ferramentas utilizadas**

🚀Desenvolvimento acelerado: o Streamlit simplifica o desenvolvimento de aplicações web, permitindo a criação e alteração de interfaces de forma rápida e eficiente.

💡Análise de dados aprimorada: um dashboard construído com a biblioteca Plotly é dinâmico e suporta uma infinidade de customizações.

## Arquitetura do Projeto

<img src='https://github.com/jorgeplatero/building_supply_stock/blob/8885db4add268b90f76b9aac7324273168902525/img/arquitetura_projeto_crud.png' width='500'/>

### Banco de Dados

O banco de dados conta com triggers que têm por funcionalidade inserir os valores totais de compras e vendas dado de itens de compra que contêm e também de atualizar o estoque dada compra ou venda de produtos. O ERD abaixo ilustra o esquema utilizado.

![erd](https://github.com/jorgeplatero/building_supply_stock/blob/8885db4add268b90f76b9aac7324273168902525/img/erd_tijolada.png)

### ETL dos Dados

Os dados são extraídos da interface Streamlit dada as requisições do usuário e carregadas do banco de dados via python. O fluxo inverso é realizado para exibir dados registrados na interface Streamlit para o usuário, bem como para exibir os indicadores no dashboard.

## Tecnologias Utilizadas

<img src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg' width='50' height='50'/> 
<img src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-plain-wordmark.svg' width='50' height='50'/> 
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/streamlit/streamlit-original-wordmark.svg" width="60" height="60"/> 

## Fontes de Dados

Os dados foram gerados para teste via [Google AI Studio](https://aistudio.google.com/app/prompts/new_chat?pli=1). Os prompts e os comandos SQL utilizados para construção da base de dados e inserção de dados estão disponíveis neste [repositório](https://github.com/jorgeplatero/building_supply_stock/tree/cff6147441cef4ab3b8044f47283de4e42f504aa/services).
