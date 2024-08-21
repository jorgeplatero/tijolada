import pandas as pd
import streamlit as st
import utils.utils as utils
import warnings
warnings.filterwarnings('ignore')


columns_estoques = [
    'ID', 'ID Produto', 'Unidade de Medida',
]

try:
    st.write('Dados')
    df_estoques = pd.DataFrame(utils.consulta_estoques(), columns=columns_estoques)
    st.table(df_estoques)
except:
    pass