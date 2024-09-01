import streamlit as st
import os
import time
import warnings
warnings.filterwarnings('ignore')


#importando o arquivo CSS
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'style.css')

with open(file_path) as f:
    css = f.read()

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False


def login():
    st.set_page_config(
        page_title='Tijolada | Login', 
        page_icon='img/ico.ico',
        layout='wide'
    )
    _, col2, _ = st.columns([.3, .4, .3])
    with col2:
        col1, col2 = st.columns([.4, .6])
        with col1:
            st.image('img/logo.png')
        with col2:
            st.title('Tijolada')
            st.subheader('Materiais para sua construção')
        with st.form(key='login'):
            usuario = st.text_input(label='**Usuário**')
            senha = st.text_input(label='**Senha**', type='password')
            botao_login = st.form_submit_button('**Entrar**')
        if botao_login:
            if usuario == st.secrets['usuario'] and senha == st.secrets['senha']:
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error('Acesso negado! Usuário e/ou senha incorretos.')


def logout():
    st.set_page_config(
        page_title='Tijolada | Configurações', 
        page_icon='img/ico.ico',
        layout='wide'

    )
    #título da página
    col1, col2 = st.columns([.2, .8])
    with col1:
        st.image('img/logo.png')
    with col2:
        st.title('Tijolada')
        st.subheader('Configurações')
    st.write('Bem-vindo ao Tijolada!')
    if st.button('**Sair**'):
        st.session_state.logged_in = False
        st.session_state.authentication_status = None
        st.rerun()


login_page = st.Page(login, title='Log in', icon=':material/login:')
logout_page = st.Page(logout, title='Configurações', icon=':material/settings:', default =True)
cadastros = st.Page('pages/cadastros.py', title='Cadastro', icon=':material/app_registration:')
compras = st.Page('pages/compras.py', title='Compras', icon=':material/add_shopping_cart:',)
vendas = st.Page('pages/vendas.py', title='Vendas', icon=':material/remove_shopping_cart:')
estoque = st.Page('pages/estoque.py', title='Estoque', icon=':material/warehouse:')
dashboard = st.Page('pages/dashboard.py', title='Dashboard', icon=':material/dashboard:')

if st.session_state.logged_in:
    pg = st.navigation(
        {
            'MENU': [cadastros, compras, estoque, vendas],
            'DADOS': [dashboard],
            'CONTA': [logout_page],
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()

st.write(f'<style>{css}</style>', unsafe_allow_html=True)