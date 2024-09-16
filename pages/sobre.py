import pandas as pd
import streamlit as st
import modules.form_module as forms
import modules.utils_module as utils
import warnings
warnings.filterwarnings('ignore')


st.set_page_config(
    page_title='Tijolada | Sobre', 
    page_icon='img/ico.ico',
    layout='wide'
)

#titulo da pagina
col1, col2 = st.columns([.2, .8])
with col1:
    st.image('img/logo.png')
with col2:
    st.title('Tijolada')
    st.subheader('Sobre o projeto')

st.markdown(
        '''
            <div style='text-align: justify;'>
                <h3>
                    CRUD com PostgreSQL e Streamlit
                </h3>
                <h4>
                    Descrição do Projeto
                </h4>
                <p>
                    Este projeto consiste em uma aplicação que oferece uma interface Streamlit para interação com 
                    banco de dados PostgreSQL e foi desenvolvida com o objetivo de permitir a realização de todas as 
                    operações CRUD. A aplicação também conta com um dashboard dinâmico para uma análise completa dos 
                    dados registrados pelo usuário. O dashboard permite visualizar dados em tempo real por meio de 
                    gráficos interativos.
                </p>
                <h4>
                    Benefícios das ferramentas utilizadas
                </h4>
                <ul>
                    <li>
                        🚀 <strong>Desenvolvimento acelerado:</strong> o Streamlit simplifica o desenvolvimento de aplicações web, permitindo a criação e alteração de interfaces 
                        de forma rápida e eficiente.
                    </li>
                    <li>
                        💡 <strong>Análise de dados aprimorada:</strong> um dashboard construído com a biblioteca Plotly é dinâmico e suporta uma infinidade de customizações.
                    </li>
                </ul>
            </div>
        ''',
    unsafe_allow_html=True
)
                
st.markdown(
        '''
            <div style='text-align: justify;'>                
                <h4>
                    Arquitetura do Projeto
                </h4>
            </div>
        ''',
        unsafe_allow_html=True
    )

_, cent, _ = st.columns([.2, .6, .2])
with cent:
    st.image('img/arquitetura_projeto_crud.png', caption='Arquitetura do projeto')

st.markdown(
        '''
            <div style='text-align: justify;'>                
                <h5>
                    Banco de Dados
                </h5>
                <p>
                    O banco de dados conta com triggers que têm por funcionalidade inserir os valores totais de compras e vendas dado de itens de compra que contêm e também de atualizar 
                    o estoque dada compra ou venda de produtos. O ERD abaixo ilustra o esquema utilizado.
                </p>
            </div>
        ''',
        unsafe_allow_html=True
    )

_, cent, _ = st.columns([.1, .8, .1])
with cent:
    st.image('img/erd_tijolada.png', caption='ERD')

st.markdown(
        '''
            <div style='text-align: justify;'>                
                <h5>
                    ETL dos Dados
                </h5>
                <p>
                    Os dados são extraídos da interface Streamlit dada as requisições do usuário e carregadas do banco de dados via python. O fluxo inverso é realizado para exibir dados 
                    registrados na interface Streamlit para o usuário, bem como para exibir os indicadores no dashboard.
                </p>
            </div>
        ''',
        unsafe_allow_html=True
    )

st.markdown(
        '''
            <div style='text-align: justify;'>                
                <h4>
                    Tecnologias Utilizadas
                </h4>
            </div>
            <ul>
                <li>
                    <img src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg' width='50' height='50'/>
                </li>
                <li>
                    <img src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-plain-wordmark.svg' width='50' height='50'/>
                </li>
                <li>
                    <img src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/streamlit/streamlit-original-wordmark.svg' width='60' height='60'/>
                </li>
            </ul>
        ''',
        unsafe_allow_html=True
    )

st.markdown(
        '''
            <div style='text-align: justify;'>                
                <h4>
                    Fontes de Dados
                </h4>
                <p>
                    Os dados foram gerados para teste via <a href='https://aistudio.google.com/app/prompts/new_chat?pli=1' style='text-decoration: none;'>Google AI Studio</a>. Os prompts e os comandos SQL utilizados para 
                    construção da base de dados e inserção de dados estão disponíveis neste <a href='https://github.com/jorgeplatero/building_supply_stock/tree/cff6147441cef4ab3b8044f47283de4e42f504aa/services' style='text-decoration: none;'>repositório</a>.
                </p>
            </div>
        ''',
        unsafe_allow_html=True
    )