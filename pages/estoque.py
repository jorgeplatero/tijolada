import pandas as pd
import streamlit as st
import utils.utils as utils
import warnings
warnings.filterwarnings('ignore')


columns_estoques = ['ID', 'ID Produto', 'Quantidade',]

#dados
try:
    df_estoques = pd.DataFrame(utils.consulta_estoques(), columns=columns_estoques)
    st.dataframe(df_estoques, hide_index=True)
except Exception as e:
    print(st.error(e))