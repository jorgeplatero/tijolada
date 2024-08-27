import pandas as pd
import streamlit as st
import utils.utils as utils
import warnings
warnings.filterwarnings('ignore')


columns_compras = [
    'ID', 'Data', 'ID Fornecedor', 'Preço Total', 'Situação do Pagamento', 
    'Situação da Entrega', 'Forma de Pagamento'
]
columns_itens_compra = ['ID', 'ID Compra', 'ID Produto', 'Preço Unitário', 'Quantidade']

#título
col1, col2 = st.columns([.2, .8])
with col1:
    st.image('img/logo.png')
with col2:
    st.title('Streamlit Materiais de Construção')
    
opcao_menu_vendas = st.selectbox(
    '**Menu**', 
    options=['Cadastrar', 'Alterar', 'Consultar'],
    index=None,
    placeholder='Selecione uma opção do menu...'                          
)

if opcao_menu_vendas == 'Cadastrar':
    #formulario
    utils.insert_compras()
    
elif opcao_menu_vendas == 'Alterar':
    options = st.radio(
        '**Opções**', ['Compra', 'Itens de Compra'], 
        captions=[
            'Alterar compra',
            'Alterar itens da compra'
        ], 
        horizontal=True
    )
    
    if options == 'Compra':
        #formulario
        utils.update_compras()
        #dados
        try:
            df_compras = pd.DataFrame(utils.consulta_compras(), columns=columns_compras)
            st.dataframe(df_compras.sort_values(by='ID'), hide_index=True)
        except Exception as e:
            st.error(e)
            pass
        
    elif options == 'Itens de Compra':
        #formulario
        utils.update_compras_produtos()
        #dados
        try:
            df_compras_produtos = pd.DataFrame(utils.consulta_compras_produtos(), columns=columns_itens_compra)
            st.dataframe(df_compras_produtos.sort_values(by='ID'), hide_index=True)
        except Exception as e:
            st.error(e)
            pass   
        
elif opcao_menu_vendas == 'Consultar':
    #dados
    try:
        df_compras = pd.DataFrame(utils.consulta_compras(), columns=columns_compras)
        st.dataframe(df_compras.sort_values(by='ID'), hide_index=True)
    except Exception as e:
        st.error(e)
        pass