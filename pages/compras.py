import pandas as pd
import streamlit as st
import utils.utils as utils
import warnings
warnings.filterwarnings('ignore')


st.set_page_config(
    page_title='Tijolada | Compras', 
    page_icon='img/ico.ico',
    layout='wide'
)

colunas_compras = [
    'ID', 'Data', 'ID Fornecedor', 'Preço Total', 'Situação do Pagamento', 
    'Situação da Entrega', 'Forma de Pagamento'
]
colunas_itens_compra = ['ID', 'ID Compra', 'ID Produto', 'Preço Unitário', 'Quantidade']
colunas_produtos = ['ID', 'Nome', 'Unidade de Medida']

col1, col2 = st.columns([.2, .8])
with col1:
    st.image('img/logo.png')
with col2:
    st.title('Tijolada')
    st.subheader('Compras')

#menu    
opcoes_menu_compras = st.selectbox(
    '**Operações**', 
    options=['Cadastrar', 'Alterar', 'Excluír', 'Consultar'],
    index=None,
    placeholder='Selecione uma opção do menu...'                          
)

if opcoes_menu_compras == 'Cadastrar':
    #formulario
    utils.insert_compras()
    #dados
    try:
        df_produtos = pd.DataFrame(utils.consulta_produtos(), columns=colunas_produtos)
        st.dataframe(df_produtos.sort_values(by='ID'), use_container_width=False, hide_index=True)
    except Exception as e:
        st.error(f'Erro durante consulta: {e}')
    
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
        utils.update_compras()
        #dados
        try:
            df_compras = pd.DataFrame(utils.consulta_compras(), columns=colunas_compras)
            st.dataframe(df_compras.sort_values(by='ID'), hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')
            pass
        
    elif opcoes_alterar == 'Itens de Compra':
        #formulario
        utils.update_compras_produtos()
        #dados
        try:
            df_compras_produtos = pd.DataFrame(utils.consulta_compras_produtos(), columns=colunas_itens_compra)
            st.dataframe(df_compras_produtos.sort_values(by='ID'), hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')
            pass   

elif opcoes_menu_compras == 'Excluír':
    opcoes_excluir = st.radio(
        '**Opções**', ['Compra', 'Itens de Compra'], 
        captions=[
            'Excluír compra',
            'Excluír itens de compra'
        ], 
        horizontal=True
    )
    if opcoes_excluir == 'Compra':
        #formulario
        utils.delete_compras()
        #dados
        try:
            df_compras = pd.DataFrame(utils.consulta_compras(), columns=colunas_compras)
            st.dataframe(df_compras.sort_values(by='ID'), hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')
            pass
    elif opcoes_excluir == 'Itens de Compra':
        #formulario
        utils.delete_compras_produtos()
        #dados
        try:
            df_compras_produtos = pd.DataFrame(utils.consulta_compras_produtos(), columns=colunas_itens_compra)
            st.dataframe(df_compras_produtos.sort_values(by='ID'), hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')
            pass  
        
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
            df_compras = pd.DataFrame(utils.consulta_compras(), columns=colunas_compras)
            st.dataframe(df_compras.sort_values(by='ID'), hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')
            pass
    elif opcoes_consultar == 'Itens de Compra':
        #dados
        try:
            df_compras_produtos = pd.DataFrame(utils.consulta_compras_produtos(), columns=colunas_itens_compra)
            st.dataframe(df_compras_produtos.sort_values(by='ID'), hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')
            pass   