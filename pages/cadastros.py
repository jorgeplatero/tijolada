import pandas as pd
import streamlit as st
import modules.form_module as forms
import modules.utils_module as utils
import warnings
warnings.filterwarnings('ignore')


st.set_page_config(
    page_title='Tijolada | Cadastro', 
    page_icon='img/ico.ico',
    layout='wide'
)

colunas_cliente = [
    'ID', 'Nome', 'Tipo', 'CPF/CNPJ', 'Endereço', 'Bairro', 'Telefone', 
    'Referência', 'Situação'
]
colunas_fornecedor = ['ID', 'Nome', 'CNPJ', 'Endereço', 'Bairro', 'Telefone']
colunas_produtos = ['ID', 'Nome', 'Unidade de Medida']

#titulo da pagina
col1, col2 = st.columns([.2, .8])
with col1:
    st.image('img/logo.png')
with col2:
    st.title('Tijolada')
    st.subheader('Cadastro')

#menu
st.write('**Opções**')
opcao_menu_cadastros = st.selectbox(
    label='**Opções**', 
    options=['Cliente', 'Fornecedor', 'Produto'],
    index=None,
    placeholder='Selecione uma opção do menu',
    label_visibility='collapsed'                          
)
#opcao cliente
if opcao_menu_cadastros == 'Cliente':
    st.write('**Operação**')
    opcoes_cadastro_clientes = st.radio(
        label='**Operação**', 
        options=['Cadastrar', 'Alterar'], 
        captions=[
            'Incluir cliente',
            'Alterar cadastro de cliente'
        ], 
        horizontal=True,
        label_visibility='collapsed'
    )
    if opcoes_cadastro_clientes =='Cadastrar':
        #formulario
        forms.insert_clientes()
    elif opcoes_cadastro_clientes == 'Alterar':
        #formulario
        forms.update_clientes()
    #dados
    try:
        df_clientes = pd.DataFrame(utils.consulta_clientes(), columns=colunas_cliente)
        st.dataframe(df_clientes.sort_values(by='ID'), use_container_width=False, hide_index=True)
    except Exception as e:
        st.error(f'Erro durante consulta: {e}')
#opcao fornecedor        
elif opcao_menu_cadastros == 'Fornecedor':
    st.write('**Operação**')
    opcoes_cadastro_fornecedor = st.radio(
        label='**Operação**', 
        options=['Cadastrar', 'Alterar'], 
        captions=[
            'Incluir fornecedor',
            'Alterar cadastro de fornecedor'
        ], 
        horizontal=True,
        label_visibility='collapsed'
    )
    if opcoes_cadastro_fornecedor =='Cadastrar':
        #formulario
        forms.insert_fornecedores()
    elif opcoes_cadastro_fornecedor == 'Alterar':
        #formulario
        forms.update_fornecedores()
    #dados
    try:
        df_fornecedores = pd.DataFrame(utils.consulta_fornecedores(), columns=colunas_fornecedor)
        st.dataframe(df_fornecedores.sort_values(by='ID'), use_container_width=False, hide_index=True)
    except Exception as e:
        st.error(f'Erro durante consulta: {e}')
#opcao cadastro
elif opcao_menu_cadastros == 'Produto':
    st.write('**Operação**')
    opcoes_cadastro_produto = st.radio(
        label='**Operação**', 
        options=['Cadastrar', 'Alterar'], 
        captions=[
            'Incluir produto',
            'Alterar cadastro de produto'
        ], 
        horizontal=True,
        label_visibility='collapsed'
    )
    if opcoes_cadastro_produto =='Cadastrar':
        #formulario
        forms.insert_produtos()
    elif opcoes_cadastro_produto == 'Alterar':
        #formulario
        forms.update_produtos()
    #dados
    try:
        df_produtos = pd.DataFrame(utils.consulta_produtos(), columns=colunas_produtos)
        st.dataframe(df_produtos.sort_values(by='ID'), use_container_width=False, hide_index=True)
    except Exception as e:
        st.error(f'Erro durante consulta: {e}')