import pandas as pd
import streamlit as st
import utils.utils as utils
import warnings
warnings.filterwarnings('ignore')


columns_cliente = [
    'ID', 'Nome', 'Tipo', 'CPF/CNPJ', 'Endereço', 'Bairro', 'Telefone', 
    'Referência', 'Situação'
]

columns_fornecedor = ['ID', 'Nome', 'CNPJ', 'Endereço', 'Bairro', 'Telefone']

columns_produtos = ['ID', 'Nome', 'Unidade de Medida']

#título
col1, col2 = st.columns([.2, .8])
with col1:
    st.image('img/logo.png')
with col2:
    st.title('Streamlit Materiais de Construção')

#menu
opcao_menu_cadastros = st.selectbox(
    'Menu', 
    options=['Cliente', 'Fornecedor', 'Produto'],
    index=None,
    placeholder='Selecione uma opção do menu...'                          
)
if opcao_menu_cadastros == 'Cliente':
    #formulario
    st.write('Cadastro')
    utils.insert_clientes()
    #dados
    try:
        st.write('Dados')
        df_clientes = pd.DataFrame(utils.consulta_clientes(), columns=columns_cliente)
        st.table(df_clientes)
    except:
        pass
    
elif opcao_menu_cadastros == 'Fornecedor':
    #formulario
    st.write('Cadastro')
    utils.insert_fornecedores()
    #dados
    try:
        st.write('Dados')
        df_fornecedores = pd.DataFrame(utils.consulta_fornecedores(), columns=columns_fornecedor)
        st.table(df_fornecedores)
    except:
        pass
    
elif opcao_menu_cadastros == 'Produto':
    #formulario
    st.write('Cadastro')
    utils.insert_produtos()
    #dados
    try:
        st.write('Dados')
        df_produtos = pd.DataFrame(utils.consulta_produtos(), columns=columns_produtos)
        st.table(df_produtos)
    except:
        pass