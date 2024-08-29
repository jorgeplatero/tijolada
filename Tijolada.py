import streamlit as st
import warnings
warnings.filterwarnings('ignore')


if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False


def login():
    col1, col2 = st.columns([.6, .4])
    with col1:
        col3, col4 = st.columns([.2, .8])
        with col3:
            st.image('img/logo.png')
        with col4:
            st.title('Tijolada')
            st.subheader('Materiais para sua construção')
    with col2:
        with st.form(key='login'):
            usuario = st.text_input(label='Usuário')
            senha = st.text_input(label='Senha', type='password')
            botao_login = st.form_submit_button('Entrar')
        if botao_login:
            if usuario == st.secrets['usuario'] and senha == st.secrets['senha']:
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error('Aceso negado! Usuário e/ou senha incorretos.')


def logout():
    st.success('Bem-vindo!')
    if st.button('Log out'):
        st.session_state.logged_in = False
        st.session_state.authentication_status = None
        st.rerun()

st.set_page_config(
    page_title='Tijolada', 
    page_icon='🧱',
    layout='wide'
)

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