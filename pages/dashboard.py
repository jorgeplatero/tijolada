import streamlit as st
import pandas as pd
import utils.utils as utils
import warnings
warnings.filterwarnings('ignore')


st.set_page_config(
    page_title='Tijolada | Dashboard', 
    page_icon='img/ico.ico',
    layout='wide'
)


colunas_venda = [
    'ID Venda', 'Data', 'ID Cliente', 'Endereço de Entrega', 'Bairro de Entrega', 'Observações', 
    'Faturamento (R$)', 'Situação do Pagamento', 'Situação da Entrega', 'Forma de Pagamento'
]
colunas_vendas_produtos = ['ID Item Compra', 'ID Venda', 'ID Produto', 'Preço Unitário (R$)', 'Quantidade']
colunas_compras = [
    'ID Compra', 'Data', 'ID Fornecedor', 'Custo (R$)', 'Situação do Pagamento', 
    'Situação da Entrega', 'Forma de Pagamento'
]
colunas_compras_produtos = ['ID Item Compra', 'ID Compra', 'ID Produto', 'Preço Unitário (R$)', 'Quantidade']
colunas_cliente = [
    'ID Cliente', 'Nome', 'Tipo', 'CPF/CNPJ', 'Endereço', 'Bairro', 'Telefone', 
    'Referência', 'Situação'
]
colunas_fornecedor = ['ID Fornecedor', 'Nome', 'CNPJ', 'Endereço', 'Bairro', 'Telefone']
colunas_produtos = ['ID Produto', 'Nome', 'Unidade de Medida']
colunas_estoques = ['ID Estoque', 'ID Produto', 'Quantidade']

#titulo da pagina
col1, col2 = st.columns([.2, .8])
with col1:
    st.image('img/logo.png')
with col2:
    st.title('Tijolada')
    st.subheader('Dashboard')

#abas da pagina
tab1, tab2, tab3, tab4 = st.tabs(['Compras', 'Vendas', 'Produtos', 'Estoque'])

with tab1:
    #titulo da aba
    st.subheader('Indicadores de Compras 🚚')
    st.write('')
    #seletor data
    col1, _ = st.columns([.2, .8])
    with col1:
        data = st.date_input(
            key='seletor_data_compra',
            label='**Data**',
            help='Escolha uma data para análise'
        )
    st.write('')
    #dataframes
    #---------------------------------------------------------------
    #compras no ano selecionado
    df_compras = pd.DataFrame(utils.consulta_compras(), columns=colunas_compras)
    df_compras = df_compras[df_compras.Data.dt.year == data.year]
    #fornecedores no ano selecionado
    df_fornecedor =  pd.DataFrame(utils.consulta_fornecedores(), columns=colunas_fornecedor)
    df_fornecedor = pd.merge(df_compras, df_fornecedor, how='outer', on='ID Fornecedor')
    #produtos no ano selecionado
    df_produtos = pd.DataFrame(utils.consulta_produtos(), columns=colunas_produtos)
    df_compras_produtos = pd.DataFrame(utils.consulta_compras_produtos(), columns=colunas_compras_produtos)
    df_compras_produtos = pd.merge(df_compras_produtos, df_compras, how='outer', on='ID Compra')
    df_compras_produtos = pd.merge(df_compras_produtos, df_produtos, how='left', on='ID Produto')
    #cards
    #---------------------------------------------------------------
    total_despesa_dia = utils.formata_valor(df_compras[(df_compras.Data.dt.date == data) & (df_compras['Situação do Pagamento'] == 'Realizado')]['Custo (R$)'].astype('float').sum())
    total_despesa_mes = utils.formata_valor(df_compras[(df_compras.Data.dt.month == data.month) & (df_compras['Situação do Pagamento'] == 'Realizado')]['Custo (R$)'].astype('float').sum())
    total_despesa_ano = utils.formata_valor(df_compras[df_compras['Situação do Pagamento'] == 'Realizado']['Custo (R$)'].astype('float').sum())
    #dashboard
    #---------------------------------------------------------------
    #cards
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric('**Despesa do dia**', f'R$ {total_despesa_dia}')
    with col2:
        st.metric('**Despesa do mês**', f'R$ {total_despesa_mes}')
    with col3:
        st.metric('**Despesa do ano**', f'R$ {total_despesa_ano}')
    #graficos
    #---------------------------------------------------------------
    utils.fig_evolucao_despesa(df_compras, data)
    utils.fig_despesa_por_fornecedor(df_fornecedor, data)
    input_produtos = st.multiselect(
        key='seletor_produtos_compra',
        label='**Produtos**',
        options=[row[1] for row in utils.consulta_produtos()],
        default=[row[1] for row in utils.consulta_produtos()][0],
        max_selections=10,
        help='Selecione produtos para análise'
    )
    produtos = list(input_produtos)
    utils.fig_evolucao_despesa_por_produto(df_compras_produtos, data, produtos)

with tab2:
    #titulo da aba
    st.subheader('Indicadores de Vendas 🛒')
    st.write('')
    #seletor data
    col1, _ = st.columns([.2, .8])
    with col1:
        data = st.date_input(
            key='seletor_data_venda',
            label='**Data**',
            help='Escolha uma data para análise'
        )
    st.write('')
    #dataframes
    #---------------------------------------------------------------
    #vendas no ano selecionado
    df_vendas = pd.DataFrame(utils.consulta_vendas(), columns=colunas_venda)
    df_vendas = df_vendas[df_vendas.Data.dt.year == data.year]
    #clientes no ano selecionado
    df_clientes =  pd.DataFrame(utils.consulta_clientes(), columns=colunas_cliente)
    df_clientes = pd.merge(df_vendas, df_clientes, how='outer', on='ID Cliente')
    #produtos no ano selecionado
    df_produtos = pd.DataFrame(utils.consulta_produtos(), columns=colunas_produtos)
    df_vendas_produtos = pd.DataFrame(utils.consulta_vendas_produtos(), columns=colunas_vendas_produtos)
    df_vendas_produtos = pd.merge(df_vendas_produtos, df_vendas, how='outer', on='ID Venda')
    df_vendas_produtos = pd.merge(df_vendas_produtos, df_produtos, how='left', on='ID Produto')
    #cards
    #---------------------------------------------------------------
    total_faturamento_dia = utils.formata_valor(df_vendas[(df_vendas.Data.dt.date == data) & (df_vendas['Situação do Pagamento'] == 'Realizado')]['Faturamento (R$)'].astype('float').sum())
    total_faturamento_mes = utils.formata_valor(df_vendas[(df_vendas.Data.dt.month == data.month) & (df_vendas['Situação do Pagamento'] == 'Realizado')]['Faturamento (R$)'].astype('float').sum())
    total_faturamento_ano = utils.formata_valor(df_vendas[df_vendas['Situação do Pagamento'] == 'Realizado']['Faturamento (R$)'].astype('float').sum())
    #dashboard
    #---------------------------------------------------------------
    #cars
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric('**Faturamento do dia**', f'R$ {total_faturamento_dia}')
    with col2:
        st.metric('**Faturamento do mes**', f'R$ {total_faturamento_mes}')
    with col3:
        st.metric('**Faturamento do ano**', f'R$ {total_faturamento_ano}')
    #graficos
    utils.fig_evolucao_faturamento(df_vendas, data)
    utils.fig_faturamento_por_cliente(df_clientes, data)
    input_produtos = st.multiselect(
        key='seletor_produtos_venda',
        label='**Produtos**',
        options=[row[1] for row in utils.consulta_produtos()],
        default=[row[1] for row in utils.consulta_produtos()][0],
        max_selections=15,
        help='Selecione produtos para análise'
    )
    produtos = list(input_produtos)
    utils.fig_evolucao_faturamento_por_produto(df_vendas_produtos, data, produtos)

with tab3:
    #titulo da aba
    st.subheader('Produtos ⚒️')
    st.warning('Em desenvolvimento')

with tab4:
    #titulo da aba
    st.subheader('Estoque 📦')
    st.warning('Em desenvolvimento')