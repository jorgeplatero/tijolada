import pandas as pd
import streamlit as st
import utils.utils as utils
import warnings
warnings.filterwarnings('ignore')


st.set_page_config(
    page_title='Página Inicial', 
    page_icon='🏗️',
    layout='wide'
)


columns_venda = [
    'ID', 'Data', 'ID Cliente', 'Endereço de Entrega', 'Bairro de Entrega', 'Observações', 
    'Preço Total', 'Situação do Pagamento', 'Situação da Entrega', 'Forma de Pagamento'
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
    #formulario
    st.write('Cadastro')
    #utils.insert_vendas()

elif opcao_menu_vendas == 'Editar':
    st.write('Edição')

elif opcao_menu_vendas == 'Consultar':
    #dados
    try:
        st.write('Dados')
        df_vendas = pd.DataFrame(utils.consulta_vendas(), columns=columns_venda)
        st.table(df_vendas)
    except:
        pass
