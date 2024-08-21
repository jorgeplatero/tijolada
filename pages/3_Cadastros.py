import pandas as pd
import streamlit as st
import utils.utils as utils
import warnings
warnings.filterwarnings('ignore')


columns_cliente = [
    'ID', 'Nome', 'Tipo', 'CPF/CNPJ', 'Endereço', 'Bairro', 'Telefone', 'Referência', 'Situação'
]

columns_fornecedor = [
    'ID', 'Nome', 'CNPJ', 'Endereço', 'Bairro', 'Telefone'
]

#título
col1, col2 = st.columns([.2, .8])
with col1:
    st.image('img/logo.png', width=120)
with col2:
    st.title('Streamlit Materiais de Construção')

opcao_menu_cadastros = st.selectbox(
    'Menu', 
    options=['Cliente', 'Fornecedor'],
    index=None,
    placeholder='Selecione uma opção do menu...'                          
)
if opcao_menu_cadastros == 'Cliente':
    #formulario
    st.write('Cadastrado')
    utils.insert_clientes()
    #dados
    try:
        st.write('Dados')
        df_clientes = pd.DataFrame(utils.consulta_clientes(), columns=columns_cliente)
        st.table(df_clientes)
    except:
        pass
elif opcao_menu_cadastros == 'Fornecedor':
    st.write('Dados')
    df_fornecedores = pd.DataFrame(utils.consulta_fornecedores(), columns=columns_fornecedor)
    st.table(df_fornecedores)
