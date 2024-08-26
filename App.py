import streamlit as st


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
logout_page = st.Page(logout, title='Log out', icon=':material/logout:')
cadastros = st.Page('pages/cadastros.py', title='Dashboard', icon=':material/search:')
compras = st.Page('pages/compras.py', title='Bug reports', icon=':material/search:')
vendas = st.Page('pages/vendas.py', title='System alerts', icon=':material/search:', default=True)
estoque = st.Page('pages/estoque.py', title='Search', icon=':material/search:')
dashboard = st.Page('pages/dashboard.py', title='Search', icon=':material/dashboard:')

if st.session_state.logged_in:
    pg = st.navigation(
        {
            'Conta': [logout_page],
            'PDV': [cadastros, compras, estoque, vendas],
            'Dashboard': [dashboard],
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()
