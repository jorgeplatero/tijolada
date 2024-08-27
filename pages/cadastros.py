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

#menu
opcao_menu_cadastros = st.selectbox(
    '**Menu**', 
    options=['Cliente', 'Fornecedor', 'Produto'],
    index=None,
    placeholder='Selecione uma opção do menu...'                          
)

if opcao_menu_cadastros == 'Cliente':
    options = st.radio(
        '**Operação**', ['Cadastrar', 'Alterar'], 
        captions=[
            'Incluir cliente',
            'Alterar cadastro de cliente'
        ], 
        horizontal=True
    )
    if options =='Cadastrar':
        #formulario
        utils.insert_clientes()
    elif options == 'Alterar':
        #formulario
        utils.update_clientes()
    #dados
    try:
        df_clientes = pd.DataFrame(utils.consulta_clientes(), columns=columns_cliente)
        st.dataframe(df_clientes.sort_values(by='ID'), use_container_width=True, hide_index=True)
    except Exception as e:
        st.error(e)
        
elif opcao_menu_cadastros == 'Fornecedor':
    options = st.radio(
        '**Operação**', ['Cadastrar', 'Alterar'], 
        captions=[
            'Incluir fornecedor',
            'Alterar cadastro de fornecedor'
        ], 
        horizontal=True
    )
    if options =='Cadastrar':
        #formulario
        utils.insert_fornecedores()
    elif options == 'Alterar':
        #formulario
        utils.update_fornecedores()
    #dados
    try:
        df_fornecedores = pd.DataFrame(utils.consulta_fornecedores(), columns=columns_fornecedor)
        st.dataframe(df_fornecedores.sort_values(by='ID'), use_container_width=True, hide_index=True)
    except Exception as e:
        st.error(e)
    
elif opcao_menu_cadastros == 'Produto':
    options = st.radio(
        '**Operação**', ['Cadastrar', 'Alterar'], 
        captions=[
            'Incluir produto',
            'Alterar cadastro de produto'
        ], 
        horizontal=True
    )
    if options =='Cadastrar':
        #formulario
        utils.insert_produtos()
    elif options == 'Alterar':
        #formulario
        utils.update_produtos()
    #dados
    try:
        df_produtos = pd.DataFrame(utils.consulta_produtos(), columns=columns_produtos)
        st.dataframe(df_produtos.sort_values(by='ID'), use_container_width=True, hide_index=True)
    except Exception as e:
        st.error(e)