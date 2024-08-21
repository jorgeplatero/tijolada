import streamlit as st
import warnings
warnings.filterwarnings('ignore')


st.set_page_config(
    page_title='Página Inicial', 
    page_icon='🏗️',
    layout='wide'
)


#título
col1, col2 = st.columns([.2, .8])
with col1:
    st.image('img/logo.png', width=120)
with col2:
    st.title('Streamlit Materiais de Construção')

opcao_menu_vendas = st.selectbox(
    'Menu', 
    options=['Cadastrar', 'Alterar', 'Consultar'],
    index=None,
    placeholder='Selecione uma opção do menu...'                          
)
st.write('Você selecionou:', opcao_menu_vendas)

if opcao_menu_vendas == 'Cadastrar':
    st.write('Cadastrar')

elif opcao_menu_vendas == 'Alterar':
    st.write('Alterar')

elif opcao_menu_vendas == 'Consultar':
    st.write('Consultar')
