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
colunas_vendas_produtos = ['ID Item Compra', 'ID Venda', 'ID Produto', 'Preço Unitário', 'Quantidade']
colunas_compras = [
    'ID Compra', 'Data', 'ID Fornecedor', 'Custo (R$)', 'Situação do Pagamento', 
    'Situação da Entrega', 'Forma de Pagamento'
]
colunas_compras_produtos = ['ID Item Compra', 'ID Compra', 'ID Produto', 'Preço Unitário', 'Quantidade']
colunas_cliente = [
    'ID Cliente', 'Nome', 'Tipo', 'CPF/CNPJ', 'Endereço', 'Bairro', 'Telefone', 
    'Referência', 'Situação'
]
colunas_fornecedor = ['ID Fornecedor', 'Nome', 'CNPJ', 'Endereço', 'Bairro', 'Telefone']
colunas_produtos = ['ID Produto', 'Nome', 'Unidade de Medida']
colunas_estoques = ['ID Estoque', 'ID Produto', 'Quantidade']
meses = {
    'January': 'Janeiro',
    'February': 'Fevereiro',
    'March': 'Março',
    'April': 'Abril',
    'May': 'Maio',
    'June': 'Junho',
    'July': 'Julho',
    'August': 'Agosto',
    'September': 'Setembro',
    'October': 'Outubro',
    'November': 'Novembro',
    'December': 'Dezembro'
}

#título da página
col1, col2 = st.columns([.2, .8])
with col1:
    st.image('img/logo.png')
with col2:
    st.title('Tijolada')
    st.subheader('Dashboard')

#abas da página
tab1, tab2, tab3, tab4 = st.tabs(['Compras', 'Vendas', 'Produtos', 'Estoque'])

with tab1:
    colunas_compras = [
    'ID Compra', 'Data', 'ID Fornecedor', 'Custo (R$)', 'Situação do Pagamento', 
    'Situação da Entrega', 'Forma de Pagamento'
    ]
    colunas_compras_produtos = ['ID Item Compra', 'ID Compra', 'ID Produto', 'Preço Unitário', 'Quantidade']
    colunas_fornecedor = ['ID Fornecedor', 'Nome', 'CNPJ', 'Endereço', 'Bairro', 'Telefone']
    colunas_produtos = ['ID Produto', 'Nome', 'Unidade de Medida']
    
    st.subheader('Indicadores de Compras 🛒')
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
    #vendas no ano selecionado
    df_compras = pd.DataFrame(utils.consulta_compras(), columns=colunas_compras)
    df_compras = df_compras[df_compras.Data.dt.year == data.year]
    #fornecedores no ano selecionado
    df_fornecedor =  pd.DataFrame(utils.consulta_fornecedores(), columns=colunas_fornecedor)
    df_fornecedor = pd.merge(df_compras, df_fornecedor, how='outer', on='ID Fornecedor')
    #produtos no ano selecionado
    df_produtos = pd.DataFrame(utils.consulta_produtos(), columns=colunas_produtos)
    df_compras_produtos = pd.DataFrame(utils.consulta_compras_produtos(), columns=colunas_compras_produtos)
    df_compras_produtos = pd.merge(df_compras, df_compras_produtos, how='outer', on='ID Compra')
    df_compras_produtos = pd.merge(df_compras_produtos, df_produtos, how='outer', on='ID Produto')
    #cards
    #---------------------------------------------------------------
    total_custo_dia = utils.formata_valor(df_compras[(df_compras.Data.dt.date == data) & (df_compras['Situação do Pagamento'] == 'Realizado')]['Custo (R$)'].astype('float').sum())
    total_custo_mes = utils.formata_valor(df_compras[(df_compras.Data.dt.month == data.month) & (df_compras['Situação do Pagamento'] == 'Realizado')]['Custo (R$)'].astype('float').sum())
    total_custo_ano = utils.formata_valor(df_compras[df_compras['Situação do Pagamento'] == 'Realizado']['Custo (R$)'].astype('float').sum())
    #dashboard
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric('**Custo total do dia**', f'R$ {total_custo_dia}')
    with col2:
        st.metric('**Custo total do mês**', f'R$ {total_custo_mes}')
    with col3:
        st.metric('**Custo total do ano**', f'R$ {total_custo_ano}')
    #graficos
    #---------------------------------------------------------------
    #custo mensal no ano selecionado
    utils.fig_custo_mensal(df_compras, data, meses)
    #custo por fornecedor no ano selecionado
    utils.fig_custo_fornecedor(df_fornecedor, data)
    #custo mensal por produto no ano selecionado
    df_compras_produtos
    input_produtos = st.multiselect(
        key='seletor_produtos_compra',
        label='Produtos',
        options=[row[1] for row in utils.consulta_produtos()],
        default=[row[1] for row in utils.consulta_produtos()],
        max_selections=10,
        help='Selecione produtos para análise'
    )
    produtos = list(input_produtos.values())
    utils.fig_custo_por_produto(df_compras_produtos, data, produtos, meses)
    st.warning('Em desenvolvimento')

with tab2:
    colunas_venda = [
    'ID Venda', 'Data', 'ID Cliente', 'Endereço de Entrega', 'Bairro de Entrega', 'Observações', 
    'Faturamento (R$)', 'Situação do Pagamento', 'Situação da Entrega', 'Forma de Pagamento'
    ]
    colunas_vendas_produtos = ['ID Item Compra', 'ID Venda', 'ID Produto', 'Preço Unitário', 'Quantidade']
    colunas_cliente = [
    'ID Cliente', 'Nome', 'Tipo', 'CPF/CNPJ', 'Endereço', 'Bairro', 'Telefone', 
    'Referência', 'Situação'
    ]
    
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
    #cards
    #---------------------------------------------------------------
    total_faturamento_dia = utils.formata_valor(df_vendas[(df_vendas.Data.dt.date == data) & (df_vendas['Situação do Pagamento'] == 'Realizado')]['Faturamento (R$)'].astype('float').sum())
    total_faturamento_mes = utils.(df_vendas[(df_vendas.Data.dt.month == data.month) & (df_vendas['Situação do Pagamento'] == 'Realizado')]['Faturamento (R$)'].astype('float').sum())
    total_faturamento_ano = utils.formata_valor(df_vendas[df_vendas['Situação do Pagamento'] == 'Realizado']['Faturamento (R$)'].astype('float').sum())
    #dashboard
    #---------------------------------------------------------------
    #cars
    #---------------------------------------------------------------
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric('**Faturamento total do dia**', f'R$ {total_faturamento_dia}')
    with col2:
        st.metric('**Faturamento total do mes**', f'R$ {total_faturamento_mes}')
    with col3:
        st.metric('**Faturamento total do ano**', f'R$ {total_faturamento_ano}')
    #graficos
    #---------------------------------------------------------------
    #faturamento mensal
    utils.fig_faturamento_mensal(df_vendas, data, meses)
    #faturamento por cliente
    utils.fig_faturamento_cliente(df_clientes, data)
    st.warning('Em desenvolvimento')

with tab3:
    st.subheader('Produtos 🛍️')
    st.warning('Em desenvolvimento')