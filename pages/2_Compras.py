import pandas as pd
import streamlit as st
import utils.utils as utils
import warnings
warnings.filterwarnings('ignore')


columns_compras = [
    'ID', 'Data', 'ID Fornecedor', 'ID Produto', 'Preço Total', 'Situação do Pagamento', 
    'Situação da Entrega', 'Forma de Pagamento'
]

#título
col1, col2 = st.columns([.2, .8])
with col1:
    st.image('img/logo.png')
with col2:
    st.title('Streamlit Materiais de Construção')
    
opcao_menu_vendas = st.selectbox(
    'Menu', 
    options=['Cadastrar', 'Editar', 'Consultar'],
    index=None,
    placeholder='Selecione uma opção do menu...'                          
)

if opcao_menu_vendas == 'Cadastrar':
    st.write('Cadastro')
    utils.insert_compras()

elif opcao_menu_vendas == 'Editar':
    st.write('Edição')

elif opcao_menu_vendas == 'Consultar':
    #dados
    try:
        st.write('Dados')
        df_compras = pd.DataFrame(utils.consulta_compras(), columns=columns_compras)
        st.dataframe(df_compras, hide_index=True)
        st.write('a')
    except Exception as e:
        st.write(e)
        pass