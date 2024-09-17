import pandas as pd
import streamlit as st
import modules.form_module as forms
import modules.utils_module as utils
import warnings
warnings.filterwarnings('ignore')


st.set_page_config(
    page_title='Tijolada | Vendas', 
    page_icon='img/ico.ico',
    layout='wide'
)

colunas_vendas = [
    'ID Venda', 'Data', 'ID Cliente', 'Endereço de Entrega', 'Bairro de Entrega', 'Observações', 
    'Preço Total', 'Situação do Pagamento', 'Situação da Entrega', 'Forma de Pagamento'
]
colunas_clientes = [
    'ID Cliente', 'Nome', 'Tipo', 'CPF/CNPJ', 'Endereço', 'Bairro', 'Telefone', 
    'Referência', 'Situação'
]
colunas_itens_venda = ['ID Item de Venda', 'ID Venda', 'ID Produto', 'Preço Unitário', 'Quantidade']
colunas_estoques = ['ID', 'ID Produto', 'Quantidade em Estoque']
colunas_produtos = ['ID Produto', 'Nome', 'Unidade de Medida']

df_vendas = pd.DataFrame(utils.consulta_vendas(), columns=colunas_vendas)
df_vendas_produtos = pd.DataFrame(utils.consulta_vendas_produtos(), columns=colunas_itens_venda) 
df_estoques = pd.DataFrame(utils.consulta_estoques(), columns=colunas_estoques)
df_produtos = pd.DataFrame(utils.consulta_produtos(), columns=colunas_produtos)
df_clientes = pd.DataFrame(utils.consulta_clientes(), columns=colunas_clientes)[['ID Cliente', 'Nome', 'CPF/CNPJ']]

#titulo da pagina
col1, col2 = st.columns([.2, .8])
with col1:
    st.image('img/logo.png')
with col2:
    st.title('Tijolada')
    st.subheader('Vendas')
    
#menu
st.write('**Operações**')
col1, _ = st.columns(2)
with col1:
    opcoes_menu_vendas = st.selectbox(
        label='**Operações**', 
        options=['Cadastrar', 'Alterar', 'Excluir', 'Consultar'],
        index=None,
        placeholder='Selecione uma opção do menu',
        label_visibility='collapsed'                  
    )
#opcao cadastrar
if opcoes_menu_vendas == 'Cadastrar':
    #formulario
    forms.insert_vendas()
    #dados
    col1, col2 = st.columns([.4, .6])
    with col1:
        try:
            st.write('**Clintes**')
            st.dataframe(df_clientes.iloc[:, 0:3].sort_values(by='ID Cliente'), hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')
            pass
    with col2:
        try:
            st.write('Estoque')
            df_estoques_produtos_cadastrar = pd.merge(df_produtos, df_estoques[['ID Produto', 'Quantidade em Estoque']], how='left', on='ID Produto')
            df_estoques_produtos_cadastrar['Quantidade em Estoque'] = df_estoques_produtos_cadastrar['Quantidade em Estoque'].fillna(0)
            st.dataframe(df_estoques_produtos_cadastrar.sort_values(by='ID Produto'), use_container_width=True, hide_index=True)
        except Exception as e:
            print(st.error(f'Erro durante consulta: {e}'))
#opcao alterar
elif opcoes_menu_vendas == 'Alterar':
    st.write('**Opções**')
    opcoes_alterar = st.radio(
        label='**Opções**', 
        options=['Venda', 'Itens de Venda'], 
        captions=[
            'Alterar venda',
            'Alterar itens de venda'
        ], 
        horizontal=True,
        label_visibility='collapsed'
    )
    if opcoes_alterar == 'Venda':
        #formulario
        forms.update_vendas()
        #dados
        try:
            st.write('Vendas')
            st.dataframe(df_vendas.sort_values(by='ID Venda'), hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')
    elif opcoes_alterar == 'Itens de Venda':
        #formulario
        forms.update_vendas_produtos()
        #dados
        try:
            st.write('Itens de Venda')     
            df_vendas_produtos_alterar = pd.merge(df_vendas_produtos, df_produtos[['ID Produto', 'Nome']], how='left', on='ID Produto')
            df_vendas_produtos_alterar = pd.merge(df_vendas, df_vendas_produtos_alterar, how='inner', on='ID Venda')
            df_vendas_produtos_alterar = df_vendas_produtos_alterar[['ID Item de Venda', 'Data', 'ID Venda', 'ID Produto', 'Nome', 'Preço Unitário', 'Quantidade']]
            st.dataframe(df_vendas_produtos_alterar.sort_values(by='ID Item de Venda'), hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')  
#opcao excluir
elif opcoes_menu_vendas == 'Excluir':
    st.write('**Opções**')
    opcoes_excluir = st.radio(
        label='**Opções**', 
        options=['Venda', 'Itens de Venda'], 
        captions=[
            'Excluir venda',
            'Excluir itens de venda'
        ], 
        horizontal=True,
        label_visibility='collapsed'
    )
    if opcoes_excluir == 'Venda':
        #formulario
        forms.delete_vendas()
        #dados
        try:
            st.write('Vendas')
            st.dataframe(df_vendas.sort_values(by='ID Venda'), hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')  
    elif opcoes_excluir == 'Itens de Venda':
        #formulario
        forms.delete_vendas_produtos()
        #dados
        try:
            st.write('Itens de Venda')
            df_vendas_produtos_excluir = pd.merge(df_vendas_produtos, df_produtos[['ID Produto', 'Nome']], how='left', on='ID Produto')
            df_vendas_produtos_excluir = pd.merge(df_vendas, df_vendas_produtos_excluir, how='inner', on='ID Venda')
            df_vendas_produtos_excluir = df_vendas_produtos_excluir[['ID Item de Venda', 'Data', 'ID Venda', 'ID Produto', 'Nome', 'Preço Unitário', 'Quantidade']]
            st.dataframe(df_vendas_produtos_excluir.sort_values(by='ID Item de Venda'), hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')
#opcao consultar
elif opcoes_menu_vendas == 'Consultar':
    st.write('**Opções**')
    opcoes_consultar = st.radio(
        label='**Opções**', 
        options=['Venda', 'Itens de Venda'], 
        captions=[
            'Consultar venda',
            'Consultar itens de venda'
        ], 
        horizontal=True,
        label_visibility='collapsed'
    )
    if opcoes_consultar == 'Venda':
        #dados
        try:
            st.dataframe(df_vendas.sort_values(by='ID Venda'), hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')  
    elif opcoes_consultar == 'Itens de Venda':
        #dados
        try:
            df_vendas_produtos_consultar = pd.merge(df_vendas_produtos, df_produtos[['ID Produto', 'Nome']], how='left', on='ID Produto')
            df_vendas_produtos_consultar = pd.merge(df_vendas, df_vendas_produtos_consultar, how='inner', on='ID Venda')
            df_vendas_produtos_consultar = df_vendas_produtos_consultar[['ID Item de Venda', 'Data', 'ID Venda', 'ID Produto', 'Nome', 'Preço Unitário', 'Quantidade']]
            st.dataframe(df_vendas_produtos_consultar.sort_values(by='ID Item de Venda'), hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')