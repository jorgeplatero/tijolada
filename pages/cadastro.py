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

colunas_clientes = [
    'ID Cliente', 'Nome', 'Tipo', 'CPF/CNPJ', 'Endereço', 'Bairro', 'Telefone', 
    'Referência', 'Situação'
]
colunas_fornecedores = ['ID Fornecedor', 'Nome', 'CNPJ', 'Endereço', 'Bairro', 'Telefone']
colunas_produtos = ['ID Produto', 'Nome', 'Unidade de Medida']

df_clientes = pd.DataFrame(utils.consulta_clientes(), columns=colunas_clientes)
df_fornecedores = pd.DataFrame(utils.consulta_fornecedores(), columns=colunas_fornecedores)
df_produtos = pd.DataFrame(utils.consulta_produtos(), columns=colunas_produtos)

#titulo da pagina
col1, col2 = st.columns([.2, .8])
with col1:
    st.image('img/logo.png')
with col2:
    st.title('Tijolada')
    st.subheader('Cadastro')

#menu
st.write('**Opções**')
col1, _ = st.columns(2)
with col1:
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
        st.write('**Clientes**')
        st.dataframe(df_clientes.sort_values(by='ID Cliente'), use_container_width=False, hide_index=True)
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
        st.write('**Fornecedores**')
        st.dataframe(df_fornecedores.sort_values(by='ID Fornecedor'), use_container_width=False, hide_index=True)
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
        st.write('**Produtos**')
        st.dataframe(df_produtos.sort_values(by='ID Produto'), use_container_width=False, hide_index=True)
    except Exception as e:
        st.error(f'Erro durante consulta: {e}')