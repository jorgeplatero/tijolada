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

colunas_venda = [
    'ID Venda', 'Data', 'ID Cliente', 'Endereço de Entrega', 'Bairro de Entrega', 'Observações', 
    'Preço Total', 'Situação do Pagamento', 'Situação da Entrega', 'Forma de Pagamento'
]
colunas_itens_venda = ['ID Item de Venda', 'ID Venda', 'ID Produto', 'Preço Unitário', 'Quantidade']
colunas_estoques = ['ID', 'ID Produto', 'Quantidade em Estoque']
colunas_produtos = ['ID Produto', 'Nome', 'Unidade de Medida']

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
        options=['Cadastrar', 'Alterar', 'Excluír', 'Consultar'],
        index=None,
        placeholder='Selecione uma opção do menu',
        label_visibility='collapsed'                  
    )
#opcao cadastrar
if opcoes_menu_vendas == 'Cadastrar':
    #formulario
    forms.insert_vendas()
    #dados
    try:
        st.write('')
        df_estoques = pd.DataFrame(utils.consulta_estoques(), columns=colunas_estoques)[['ID Produto', 'Quantidade em Estoque']]
        df_produtos = pd.DataFrame(utils.consulta_produtos(), columns=colunas_produtos)
        df_estoques_produtos = pd.merge(df_produtos, df_estoques, how='outer', on='ID Produto')
        st.dataframe(df_estoques_produtos.sort_values(by='ID Produto'), hide_index=True)
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
            df_vendas = pd.DataFrame(utils.consulta_vendas(), columns=colunas_venda)
            st.dataframe(df_vendas.sort_values(by='ID Venda'), hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')
    elif opcoes_alterar == 'Itens de Venda':
        #formulario
        forms.update_vendas_produtos()
        #dados
        try:
            df_vendas_produtos = pd.DataFrame(utils.consulta_vendas_produtos(), columns=colunas_itens_venda)
            df_produtos = pd.DataFrame(utils.consulta_produtos(), columns=colunas_produtos)[['ID Produto', 'Nome']]
            df_vendas_produtos = pd.merge(df_vendas_produtos, df_produtos, how='outer', on='ID Produto')
            df_vendas_produtos = df_vendas_produtos[['ID Item de Venda', 'ID Venda', 'ID Produto', 'Nome', 'Preço Unitário', 'Quantidade']]
            st.dataframe(df_vendas_produtos.sort_values(by='ID Item de Venda'), hide_index=True)

        except Exception as e:
            st.error(f'Erro durante consulta: {e}')  
#opcao excluir
elif opcoes_menu_vendas == 'Excluír':
    st.write('**Opções**')
    opcoes_excluir = st.radio(
        label='**Opções**', 
        options=['Venda', 'Itens de Venda'], 
        captions=[
            'Excluír venda',
            'Excluír itens de venda'
        ], 
        horizontal=True,
        label_visibility='collapsed'
    )
    if opcoes_excluir == 'Venda':
        #formulario
        forms.delete_vendas()
        #dados
        try:
            df_vendas = pd.DataFrame(utils.consulta_vendas(), columns=colunas_venda)
            st.dataframe(df_vendas.sort_values(by='ID Venda'), hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')  
    elif opcoes_excluir == 'Itens de Venda':
        #formulario
        forms.delete_vendas_produtos()
        #dados
        try:
            df_vendas_produtos = pd.DataFrame(utils.consulta_vendas_produtos(), columns=colunas_itens_venda)
            st.dataframe(df_vendas_produtos.sort_values(by='ID Item de Venda'), hide_index=True)
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
            df_vendas = pd.DataFrame(utils.consulta_vendas(), columns=colunas_venda)
            st.dataframe(df_vendas.sort_values(by='ID Venda'), hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')  
    elif opcoes_consultar == 'Itens de Venda':
        #dados
        try:
            df_vendas_produtos = pd.DataFrame(utils.consulta_vendas_produtos(), columns=colunas_itens_venda)
            df_produtos = pd.DataFrame(utils.consulta_produtos(), columns=colunas_produtos)[['ID Produto', 'Nome']]
            df_vendas_produtos = pd.merge(df_vendas_produtos, df_produtos, how='outer', on='ID Produto')
            df_vendas_produtos = df_vendas_produtos[['ID Item de Venda', 'ID Venda', 'ID Produto', 'Nome', 'Preço Unitário', 'Quantidade']]
            st.dataframe(df_vendas_produtos.sort_values(by='ID Item de Venda'), hide_index=True)
        except Exception as e:
            st.error(f'Erro durante consulta: {e}')