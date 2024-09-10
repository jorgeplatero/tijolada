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
    'ID Compra', 'Data', 'ID Fornecedor', 'Preço Total', 'Situação do Pagamento', 
    'Situação da Entrega', 'Forma de Pagamento'
]
colunas_itens_compra = ['ID Item de Compra', 'ID Compra', 'ID Produto', 'Preço Unitário', 'Quantidade']
colunas_produtos = ['ID Produto', 'Nome', 'Unidade de Medida']

#titulo da pagina
col1, col2 = st.columns([.2, .8])
with col1:
    st.image('img/logo.png')
with col2:
    st.title('Tijolada')
    st.subheader('Compras')

#menu    
st.write('**Operações**')
opcoes_menu_compras = st.selectbox(
    label='**Operações**', 
    options=['Cadastrar', 'Alterar', 'Excluír', 'Consultar'],
    index=None,
    placeholder='Selecione uma opção do menu'    ,
    label_visibility='collapsed'                      
)
#opcao cadastrar
if opcoes_menu_compras == 'Cadastrar':
    #formulario
    utils.insert_compras()
    #dados
    try:
        df_produtos = pd.DataFrame(utils.consulta_produtos(), columns=colunas_produtos)
        st.dataframe(df_produtos.sort_values(by='ID Produto'), use_container_width=False, hide_index=True)
    except Exception as e:
        st.error(f'Erro durante consulta: {e}')
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
        utils.update_compras()
        #dados
        try:
            df_compras = pd.DataFrame(utils.consulta_compras(), columns=colunas_compras)
            st.dataframe(df_compras.sort_values(by='ID Compra'), hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')
            pass
    elif opcoes_alterar == 'Itens de Compra':
        #formulario
        utils.update_compras_produtos()
        #dados
        try:
            df_compras_produtos = pd.DataFrame(utils.consulta_compras_produtos(), columns=colunas_itens_compra)     
            df_produtos = pd.DataFrame(utils.consulta_produtos(), columns=colunas_produtos)[['ID Produto', 'Nome']]
            df_compras_produtos = pd.merge(df_compras_produtos, df_produtos, how='outer', on='ID Produto')
            df_compras_produtos = df_compras_produtos[['ID Item de Compra', 'ID Compra', 'ID Produto', 'Nome', 'Preço Unitário', 'Quantidade']]
            st.dataframe(df_compras_produtos.sort_values(by='ID Item de Compra'), hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')
            pass   
#opcao excluir
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
            st.dataframe(df_compras.sort_values(by='ID Compra'), hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')
            pass
    elif opcoes_excluir == 'Itens de Compra':
        #formulario
        utils.delete_compras_produtos()
        #dados
        try:
            df_compras_produtos = pd.DataFrame(utils.consulta_compras_produtos(), columns=colunas_itens_compra)
            st.dataframe(df_compras_produtos.sort_values(by='ID Item de Compra'), hide_index=True)
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
            df_compras = pd.DataFrame(utils.consulta_compras(), columns=colunas_compras)
            st.dataframe(df_compras.sort_values(by='ID Compra'), hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')
            pass
    elif opcoes_consultar == 'Itens de Compra':
        #dados
        try:
            df_compras_produtos = pd.DataFrame(utils.consulta_compras_produtos(), columns=colunas_itens_compra)     
            df_produtos = pd.DataFrame(utils.consulta_produtos(), columns=colunas_produtos)[['ID Produto', 'Nome']]
            df_compras_produtos = pd.merge(df_compras_produtos, df_produtos, how='outer', on='ID Produto')
            df_compras_produtos = df_compras_produtos[['ID Item de Compra', 'ID Compra', 'ID Produto', 'Nome', 'Preço Unitário', 'Quantidade']]
            st.dataframe(df_compras_produtos.sort_values(by='ID Item de Compra'), hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')
            pass   