import pandas as pd
import streamlit as st
import modules.form_module as forms
import modules.utils_module as utils
import warnings
warnings.filterwarnings('ignore')


st.set_page_config(
    page_title='Tijolada | Compras', 
    page_icon='img/ico.ico',
    layout='wide'
)

colunas_compras = [
    'ID Compra', 'Data', 'ID Fornecedor', 'Preço Total', 'Situação do Pagamento', 
    'Situação da Entrega', 'Forma de Pagamento'
]
colunas_itens_compra = ['ID Item de Compra', 'ID Compra', 'ID Produto', 'Preço Unitário', 'Quantidade']
colunas_produtos = ['ID Produto', 'Nome', 'Unidade de Medida']
colunas_fornecedor = ['ID Fornecedor', 'Nome', 'CNPJ', 'Endereço', 'Bairro', 'Telefone']

df_produtos = pd.DataFrame(utils.consulta_produtos(), columns=colunas_produtos)
df_fornecedores = pd.DataFrame(utils.consulta_fornecedores(), columns=colunas_fornecedor)
df_compras = pd.DataFrame(utils.consulta_compras(), columns=colunas_compras)
df_compras_produtos = pd.DataFrame(utils.consulta_compras_produtos(), columns=colunas_itens_compra)

#titulo da pagina
col1, col2 = st.columns([.2, .8])
with col1:
    st.image('img/logo.png')
with col2:
    st.title('Tijolada')
    st.subheader('Compras')

#menu    
st.write('**Operações**')
col1, _ = st.columns(2)
with col1:
    opcoes_menu_compras = st.selectbox(
        label='**Operações**', 
        options=['Cadastrar', 'Alterar', 'Excluir', 'Consultar'],
        index=None,
        placeholder='Selecione uma opção do menu'    ,
        label_visibility='collapsed'                      
    )
#opcao cadastrar
if opcoes_menu_compras == 'Cadastrar':
    #formulario
    forms.insert_compras()
    #dados
    col1, col2 = st.columns(2)
    with col1:
        try:
            st.write('**Fornecedores**')
            st.dataframe(df_fornecedores.iloc[:, 0:3].sort_values(by='ID Fornecedor'), use_container_width=False, hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')
            pass
    with col2:
        try:
            st.write('**Produtos**')
            st.dataframe(df_produtos.sort_values(by='ID Produto'), use_container_width=False, hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')
            pass
#opcao alterar
elif opcoes_menu_compras == 'Alterar':
    opcoes_alterar = st.radio(
        '**Opções**', ['Compra', 'Itens de Compra'], 
        captions=[
            'Alterar compra',
            'Alterar itens de compra'
        ], 
        horizontal=True
    )
    if opcoes_alterar == 'Compra':
        #formulario
        forms.update_compras()
        #dados
        try:
            st.write('Compras')
            st.dataframe(df_compras.sort_values(by='ID Compra'), hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')
            pass
    elif opcoes_alterar == 'Itens de Compra':
        #formulario
        forms.update_compras_produtos()
        #dados
        try:
            st.write('Itens de Compra')
            df_compras_produtos_alterar = pd.merge(df_compras_produtos, df_produtos[['ID Produto', 'Nome']], how='left', on='ID Produto')
            df_compras_produtos_alterar = pd.merge(df_compras, df_compras_produtos_alterar, how='inner', on='ID Compra')
            df_compras_produtos_alterar = df_compras_produtos_alterar[['ID Item de Compra', 'Data', 'ID Compra', 'ID Produto', 'Nome', 'Preço Unitário', 'Quantidade']]
            st.dataframe(df_compras_produtos_alterar.sort_values(by='ID Item de Compra'), hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')
            pass   
#opcao excluir
elif opcoes_menu_compras == 'Excluir':
    opcoes_excluir = st.radio(
        '**Opções**', ['Compra', 'Itens de Compra'], 
        captions=[
            'Excluir compra',
            'Excluir itens de compra'
        ], 
        horizontal=True
    )
    if opcoes_excluir == 'Compra':
        #formulario
        forms.delete_compras()
        #dados
        try:
            st.write('Compras')
            st.dataframe(df_compras.sort_values(by='ID Compra'), hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')
            pass
    elif opcoes_excluir == 'Itens de Compra':
        #formulario
        forms.delete_compras_produtos()
        #dados
        try:
            st.write('Itens de Compra')
            df_compras_produtos_excluir = pd.merge(df_compras_produtos, df_produtos[['ID Produto', 'Nome']], how='left', on='ID Produto')
            df_compras_produtos_excluir = pd.merge(df_compras, df_compras_produtos_excluir, how='inner', on='ID Compra')
            df_compras_produtos_excluir = df_compras_produtos_excluir[['ID Item de Compra', 'Data', 'ID Compra', 'ID Produto', 'Nome', 'Preço Unitário', 'Quantidade']]
            st.dataframe(df_compras_produtos_excluir.sort_values(by='ID Item de Compra'), hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')
            pass  
#opcao consultar
elif opcoes_menu_compras == 'Consultar':
    opcoes_consultar = st.radio(
        '**Opções**', ['Compra', 'Itens de Compra'], 
        captions=[
            'Consultar compra',
            'Consultar itens de compra'
        ], 
        horizontal=True
    )
    if opcoes_consultar == 'Compra':
        #dados
        try:
            st.dataframe(df_compras.sort_values(by='ID Compra'), hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')
            pass
    elif opcoes_consultar == 'Itens de Compra':
        #dados
        try:
            df_compras_produtos_consultar = pd.merge(df_compras_produtos, df_produtos[['ID Produto', 'Nome']], how='outer', on='ID Produto')
            df_compras_produtos_consultar = df_compras_produtos_consultar[['ID Item de Compra', 'ID Compra', 'ID Produto', 'Nome', 'Preço Unitário', 'Quantidade']]
            st.dataframe(df_compras_produtos_consultar.sort_values(by='ID Item de Compra'), hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')
            pass   