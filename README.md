# CRUD com PostgreSQL e Streamlit

## Descrição do Projeto

Este projeto se traduz em uma aplicação que oferece uma interface intuitiva para interação com banco de dados e foi desenvolvida com o objetivo de permitir a realização de todas as operações CRUD. Ademais, a aplicação conta com um dashboard dinâmico desenvolvido com a biblioteca Plotly, para uma análise completa dos dados regsitrados pelo usuário. O dashboard permite visualizar dados em tempo real por meio de gráficos interativos, oferecendo insights valiosos para a tomada de decisões do negócio.

Benefícios das ferramentas utilizadas

Desenvolvimento acelerado: o Streamlit simplifica o desenvolvimento de aplicações web, permitindo a criação de interfaces rapidamente.
Facilidade de uso: a interface amigável do Streamlit facilita a interação com o banco de dados, mesmo para usuários não técnicos.
Análise de dados aprimorada: o dashboard de Plotly oferece insights valiosos sobre os dados, permitindo uma melhor tomada de decisões.

## Arquitetura do Projeto

![arquitetura do projeto]()

### Banco de Dados

O ERD abaixo ilustra o esquema utilizado.

![erd]()

### ETL dos Dados

Os dados são extraídos da interface Streamlit dada as requisições do usuário e carregadas do banco de dados via python. O fluxo inverso é realizado para exibir dados registrados na interface Streamlit para o usuário, bem como para exibir os indicadores dashboard.

## Tecnologias Utilizadas

<img src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg' width='50' height='50'/> 
<img src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-plain-wordmark.svg' width='50' height='50'/> 
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/streamlit/streamlit-original-wordmark.svg" width="60" height="60"/> 

## Fontes de Dados

Os dados foram gerados para teste via Google AI Studio. Os <a style='text-decoration:none;'href='https://github.com/jorgeplatero/building_supply_stock/blob/2cbf74051f8710545d9bb2e31f8365c1bf8d1242/services/prompts.txt' target='_blank'>prompts</a> e as <a style='text-decoration:none;'href='https://github.com/jorgeplatero/building_supply_stock/blob/2cbf74051f8710545d9bb2e31f8365c1bf8d1242/services/inserts.sql' target='_blank'>requisições</a>, assim como as <a style='text-decoration:none;'href='https://github.com/jorgeplatero/building_supply_stock/blob/2cbf74051f8710545d9bb2e31f8365c1bf8d1242/services/tables.sql' target='_blank'>tabelas</a> podem ser conultados no repositório.
