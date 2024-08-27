import streamlit as st
from pathlib import Path
import streamlit_authenticator as stauth
import pickle
import warnings
warnings.filterwarnings('ignore')


st.set_page_config(
    page_title='Página Inicial', 
    page_icon='🧱',
    layout='wide'
)

#título
col1, col2 = st.columns([.2, .8])
with col1:
    st.image('img/logo.png')
with col2:
    st.title('Tijolada')
    st.subheader('Materiais para sua construção')
    

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

def login():
    if st.button('Log in'):
        st.session_state.logged_in = True
        st.rerun()


def logout():
    if st.button('Log out'):
        st.session_state.logged_in = False
        st.rerun()


login_page = st.Page(login, title='Log in', icon=':material/login:')
logout_page = st.Page(logout, title='Log out', icon=':material/logout:', default=True)
cadastros = st.Page('pages/cadastros.py', title='Cadastro', icon=':material/app_registration:')
compras = st.Page('pages/compras.py', title='Compras', icon=':material/add_shopping_cart:')
vendas = st.Page('pages/vendas.py', title='Vendas', icon=':material/remove_shopping_cart:')
estoque = st.Page('pages/estoque.py', title='Estoque', icon=':material/warehouse:')
dashboard = st.Page('pages/dashboard.py', title='Dashboard', icon=':material/dashboard:')

if st.session_state.logged_in:
    pg = st.navigation(
        {
            'Conta': [logout_page],
            'PDV': [cadastros, compras, estoque, vendas],
            'Dados': [dashboard],
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()
