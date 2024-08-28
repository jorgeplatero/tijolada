import streamlit as st
import streamlit_authenticator as stauth
import pickle
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')


if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False


'''password = st.text_input('Password', type='password')
 
if password == st.secrets['password']:
    st.success('Access permitido!')
else:
    st.error('Acesso negado!')'''
    
def autenticar():
    names = ['jorge', 'rosana']
    usernames = ['jorge', 'rosana']

    file_path = Path(__file__).parent / 'hashed_pw.pkl'
    with file_path.open('rb') as file:
        hashed_passwords = pickle.load(file)
    authenticator = stauth.Authenticate(names, usernames, hashed_passwords, 'tijolada', 'abcde')
    name, authentication_status, username = authenticator.login('Login', 'sidebar')
    if authentication_status == False:
        st.write('')
        st.error('Usuário/senha incorretos')
    elif authentication_status == None:
        st.write('')
        st.warning('Digite usuário e senha')
    return authentication_status, name, username 


def login():
    col1, col2 = st.columns([.2, .8])
    with col1:
        st.image('img/logo.png')
    with col2:
        st.title('Tijolada')
        st.subheader('Materiais para sua construção')
    if 'authentication_status' not in st.session_state or not st.session_state.authentication_status:
        st.session_state.authentication_status, st.session_state.name, st.session_state.username = autenticar()
    if st.session_state.authentication_status:
        st.session_state.logged_in = True
        st.rerun()


def logout():
    if st.button('Log out'):
        st.session_state.logged_in = False
        st.session_state.authentication_status = None
        st.rerun()

st.set_page_config(
    page_title='Página Inicial', 
    page_icon='🧱',
    layout='wide'
)

login_page = st.Page(login, title='Log in', icon=':material/login:')
logout_page = st.Page(logout, title='Log out', icon=':material/login:')
cadastros = st.Page('pages/cadastros.py', title='Cadastro', icon=':material/app_registration:')
compras = st.Page('pages/compras.py', title='Compras', icon=':material/add_shopping_cart:')
vendas = st.Page('pages/vendas.py', title='Vendas', icon=':material/remove_shopping_cart:')
estoque = st.Page('pages/estoque.py', title='Estoque', icon=':material/warehouse:')
dashboard = st.Page('pages/dashboard.py', title='Dashboard', icon=':material/dashboard:', default =True)

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