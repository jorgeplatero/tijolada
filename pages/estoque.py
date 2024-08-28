import pandas as pd
import streamlit as st
import utils.utils as utils
import warnings
warnings.filterwarnings('ignore')


columns_estoques = ['ID', 'ID Produto', 'Quantidade',]

col1, col2 = st.columns([.2, .8])
with col1:
    st.image('img/logo.png')
with col2:
    st.title('Tijolada')
    st.subheader('Estoque')

#dados
try:
    st.write('')
    df_estoques = pd.DataFrame(utils.consulta_estoques(), columns=columns_estoques)
    st.dataframe(df_estoques, hide_index=True)
except Exception as e:
    print(st.error(e))