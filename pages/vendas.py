import pandas as pd
import streamlit as st
import utils.utils as utils
import warnings
warnings.filterwarnings('ignore')


colunas_venda = [
    'ID', 'Data', 'ID Cliente', 'Endereço de Entrega', 'Bairro de Entrega', 'Observações', 
    'Preço Total', 'Situação do Pagamento', 'Situação da Entrega', 'Forma de Pagamento'
]
colunas_itens_venda = ['ID', 'ID Venda', 'ID Produto', 'Preço Unitário', 'Quantidade']
colunas_estoques = ['ID', 'ID Produto', 'Quantidade em Estoque']
colunas_produtos = ['ID Produto', 'Nome', 'Unidade de Medida']

col1, col2 = st.columns([.2, .8])
with col1:
    st.image('img/logo.png')
with col2:
    st.title('Tijolada')
    st.subheader('Vendas')

#menu
opcoes_menu_vendas = st.selectbox(
    '**Operações**', 
    options=['Cadastrar', 'Alterar', 'Excluír', 'Consultar'],
    index=None,
    placeholder='Selecione uma opção do menu...'                          
)

if opcoes_menu_vendas == 'Cadastrar':
    #formulario
    utils.insert_vendas()
    #dados
    try:
        st.write('')
        df_estoques = pd.DataFrame(utils.consulta_estoques(), columns=colunas_estoques)[['ID Produto', 'Quantidade em Estoque']]
        df_produtos = pd.DataFrame(utils.consulta_produtos(), columns=colunas_produtos)
        df_estoques_produtos = pd.merge(df_produtos, df_estoques, how='outer', on='ID Produto')
        st.dataframe(df_estoques_produtos.sort_values(by='ID Produto'), hide_index=True)
    except Exception as e:
        print(st.error(f'Erro durante consulta: {e}'))

elif opcoes_menu_vendas == 'Alterar':
    opcoes_alterar = st.radio(
        '**Opções**', ['Venda', 'Itens de Venda'], 
        captions=[
            'Alterar venda',
            'Alterar itens de venda'
        ], 
        horizontal=True
    )
    
    if opcoes_alterar == 'Venda':
        #formulario
        utils.update_vendas()
        #dados
        try:
            df_vendas = pd.DataFrame(utils.consulta_vendas(), columns=colunas_venda)
            st.dataframe(df_vendas.sort_values(by='ID'), hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')
        
    elif opcoes_alterar == 'Itens de Venda':
        #formulario
        utils.update_vendas_produtos()
        #dados
        try:
            df_vendas_produtos = pd.DataFrame(utils.consulta_vendas_produtos(), columns=colunas_itens_venda)
            st.dataframe(df_vendas_produtos.sort_values(by='ID'), hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')  

elif opcoes_menu_vendas == 'Excluír':
    opcoes_excluir = st.radio(
        '**Opções**', ['Venda', 'Itens de Venda'], 
        captions=[
            'Excluír venda',
            'Excluír itens de venda'
        ], 
        horizontal=True
    )
    if opcoes_excluir == 'Venda':
        #formulario
        utils.delete_vendas()
        #dados
        try:
            df_vendas = pd.DataFrame(utils.consulta_vendas(), columns=colunas_venda)
            st.dataframe(df_vendas.sort_values(by='ID'), hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')  
    elif opcoes_excluir == 'Itens de Venda':
        #formulario
        utils.delete_vendas_produtos()
        #dados
        try:
            df_vendas_produtos = pd.DataFrame(utils.consulta_vendas_produtos(), columns=colunas_itens_venda)
            st.dataframe(df_vendas_produtos.sort_values(by='ID'), hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')

elif opcoes_menu_vendas == 'Consultar':
    opcoes_consultar = st.radio(
        '**Opções**', ['Venda', 'Itens de Venda'], 
        captions=[
            'Consultar venda',
            'Consultar itens de venda'
        ], 
        horizontal=True
    )
    if opcoes_consultar == 'Venda':
        #dados
        try:
            df_vendas = pd.DataFrame(utils.consulta_vendas(), columns=colunas_venda)
            st.dataframe(df_vendas.sort_values(by='ID'), hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')  
    elif opcoes_consultar == 'Itens de Venda':
        #dados
        try:
            df_vendas_produtos = pd.DataFrame(utils.consulta_vendas_produtos(), columns=colunas_itens_venda)
            st.dataframe(df_vendas_produtos.sort_values(by='ID'), hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')