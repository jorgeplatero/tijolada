import pandas as pd
import streamlit as st
import modules.utils_module as utils
import warnings
warnings.filterwarnings('ignore')


st.set_page_config(
    page_title='Tijolada | Estoque', 
    page_icon='img/ico.ico',
    layout='wide'
)

colunas_estoques = ['ID', 'ID Produto', 'Quantidade']
colunas_produtos = ['ID Produto', 'Nome', 'Unidade de Medida']


#titulo da pagina
col1, col2 = st.columns([.2, .8])
with col1:
    st.image('img/logo.png')
with col2:
    st.title('Tijolada')
    st.subheader('Estoque')
    
#dados
try:
    st.write('')
    df_estoques = pd.DataFrame(utils.consulta_estoques(), columns=colunas_estoques)[['ID Produto', 'Quantidade']]
    df_produtos = pd.DataFrame(utils.consulta_produtos(), columns=colunas_produtos)
    df_estoques_produtos = pd.merge(df_produtos, df_estoques, how='left', on='ID Produto')
    df_estoques_produtos['Quantidade'] = df_estoques_produtos['Quantidade'].fillna(0)
    df_estoques_produtos['Nível'] = df_estoques_produtos['Quantidade'].apply(utils.categoriza_quantidade_estoque)
    st.dataframe(df_estoques_produtos.sort_values(by='ID Produto'), hide_index=True)
except Exception as e:
    print(st.error(f'Erro durante consulta: {e}'))