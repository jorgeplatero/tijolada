import streamlit as st
import pandas as pd
import utils.utils as utils
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')


st.set_page_config(
    page_title='Tijolada | Dashboard', 
    page_icon='img/ico.ico',
    layout='wide'
)

def formata_valor(valor, prefixo = ''):
    for unidade in ['', 'mil']:
        if valor < 1000:
            return f'{prefixo} {valor:.2f} {unidade}'
        valor /= 1000
    return f'{prefixo} {valor:.2f} milhões'


colunas_venda = [
    'ID Venda', 'Data', 'ID Cliente', 'Endereço de Entrega', 'Bairro de Entrega', 'Observações', 
    'Faturamento (R$)', 'Situação do Pagamento', 'Situação da Entrega', 'Forma de Pagamento'
]
colunas_itens_venda = ['ID Item Compra', 'ID Venda', 'ID Produto', 'Preço Unitário', 'Quantidade']
colunas_compras = [
    'ID Compra', 'Data', 'ID Fornecedor', 'Custo (R$)', 'Situação do Pagamento', 
    'Situação da Entrega', 'Forma de Pagamento'
]
colunas_itens_compra = ['ID Item Compra', 'ID Compra', 'ID Produto', 'Preço Unitário', 'Quantidade']
colunas_cliente = [
    'ID Cliente', 'Nome', 'Tipo', 'CPF/CNPJ', 'Endereço', 'Bairro', 'Telefone', 
    'Referência', 'Situação'
]
colunas_fornecedor = ['ID Fornecedor', 'Nome', 'CNPJ', 'Endereço', 'Bairro', 'Telefone']
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
tab1, tab2, tab3 = st.tabs(['Compras', 'Vendas', 'Estoque'])

with tab1:
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
    #clientes no ano selecionado
    df_fornecedor =  pd.DataFrame(utils.consulta_fornecedores(), columns=colunas_fornecedor)
    df_fornecedor = pd.merge(df_compras, df_fornecedor, how='outer', on='ID Fornecedor')
    #cards
    #---------------------------------------------------------------
    total_custo_dia = formata_valor(df_compras[(df_compras.Data.dt.date == data) & (df_compras['Situação do Pagamento'] == 'Realizado')]['Custo (R$)'].astype('float').sum())
    total_custo_mes = formata_valor(df_compras[(df_compras.Data.dt.month == data.month) & (df_compras['Situação do Pagamento'] == 'Realizado')]['Custo (R$)'].astype('float').sum())
    total_custo_ano = formata_valor(df_compras[df_compras['Situação do Pagamento'] == 'Realizado']['Custo (R$)'].astype('float').sum())

    #figuras
    #---------------------------------------------------------------
    #faturamento mensal
    df_compras_custo_mensal = df_compras[df_compras['Situação do Pagamento'] == 'Realizado']
    df_compras_custo_mensal['Mês'] = df_compras_custo_mensal['Data'].dt.to_period('M')
    df_compras_custo_mensal = df_compras_custo_mensal.groupby('Mês')['Custo (R$)'].sum().reset_index()
    df_compras_custo_mensal['Mês'] = df_compras_custo_mensal['Mês'].dt.strftime('%B')
    df_compras_custo_mensal['Mês'] = df_compras_custo_mensal['Mês'].map(meses)
    fig_custo_mensal = px.line(
        data_frame=df_compras_custo_mensal, 
        x='Mês', 
        y='Custo (R$)',
        text=df_compras_custo_mensal['Custo (R$)'].apply(lambda x: f'R$ {x:.2f}'),
        hover_name='Mês'
    )
    fig_custo_mensal.update_layout(
        title=f'Custo Mensal em {data.year}',
        xaxis_title='Mês', 
        yaxis_showticklabels=False
    )
    fig_custo_mensal.update_traces(
        textposition='top center',
        hovertemplate='Mês: %{hovertext}<br>Custo: R$ %{y:.2f}'
    )

    #faturamento por cliente
    df_custo_por_fornecedor = df_fornecedor[df_fornecedor['Situação do Pagamento'] == 'Realizado']
    df_custo_por_fornecedor = df_custo_por_fornecedor.groupby('Nome')['Custo (R$)'].sum().reset_index()
    df_custo_por_fornecedor = df_custo_por_fornecedor.sort_values('Custo (R$)', ascending=False).head()
    df_custo_por_fornecedor['Custo (R$)'] = df_custo_por_fornecedor['Custo (R$)'].astype('float64')
    fig_custo_fornecedor = px.bar(
        data_frame=df_custo_por_fornecedor, 
        x='Nome', 
        y='Custo (R$)',
        text=df_custo_por_fornecedor['Custo (R$)'].apply(lambda x: f'R$ {x:.2f}'),
        color='Custo (R$)',
        hover_name='Nome'
    )
    fig_custo_fornecedor.update_layout(
        title=f'Top 5 Clientes em {data.year}',
        xaxis_type='category',
        yaxis_showticklabels=False
    )
    fig_custo_fornecedor.update_traces(
        showlegend=False,
        textposition='outside',
        hovertemplate='Nome: %{hovertext}<br>Custo: R$ %{y:.2f}'
    )
    fig_custo_fornecedor.update_xaxes(
        tickangle=45
    )

    #dashboard
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(f'**Custo total em {data.day}/{data.month}/{data.year}**', f'R$ {total_custo_dia}')
    with col2:
        st.metric(f'**Custo total em {data.month}/{data.year}**', f'R$ {total_custo_mes}')
    with col3:
        st.metric(f'**Custo total em {data.year}**', f'R$ {total_custo_ano}')
    #graficos
    st.plotly_chart(fig_custo_mensal)
    st.plotly_chart(fig_custo_fornecedor)
    st.warning('Em desenvolvimento')

with tab2:
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
    total_faturado_dia = formata_valor(df_vendas[(df_vendas.Data.dt.date == data) & (df_vendas['Situação do Pagamento'] == 'Realizado')]['Faturamento (R$)'].astype('float').sum())
    total_faturado_mes = formata_valor(df_vendas[(df_vendas.Data.dt.month == data.month) & (df_vendas['Situação do Pagamento'] == 'Realizado')]['Faturamento (R$)'].astype('float').sum())
    total_faturado_ano = formata_valor(df_vendas[df_vendas['Situação do Pagamento'] == 'Realizado']['Faturamento (R$)'].astype('float').sum())

    #figuras
    #---------------------------------------------------------------
    #faturamento mensal
    df_vendas_faturamento_mensal = df_vendas[df_vendas['Situação do Pagamento'] == 'Realizado']
    df_vendas_faturamento_mensal['Mês'] = df_vendas_faturamento_mensal['Data'].dt.to_period('M')
    df_vendas_faturamento_mensal = df_vendas_faturamento_mensal.groupby('Mês')['Faturamento (R$)'].sum().reset_index()
    df_vendas_faturamento_mensal['Mês'] = df_vendas_faturamento_mensal['Mês'].dt.strftime('%B')
    df_vendas_faturamento_mensal['Mês'] = df_vendas_faturamento_mensal['Mês'].map(meses)
    fig_faturamento_mensal = px.line(
        data_frame=df_vendas_faturamento_mensal, 
        x='Mês', 
        y='Faturamento (R$)',
        text=df_vendas_faturamento_mensal['Faturamento (R$)'].apply(lambda x: f'R$ {x:.2f}'),
        hover_name='Mês'
    )
    fig_faturamento_mensal.update_layout(
        title=f'Faturamento Mensal em {data.year}',
        xaxis_title='Mês', 
        yaxis_showticklabels=False
    )
    fig_faturamento_mensal.update_traces(
        textposition='top center',
        hovertemplate='Mês: %{hovertext}<br>Faturamento: R$ %{y:.2f}'
    )

    #faturamento por cliente
    df_faturamento_por_cliente = df_clientes[df_clientes['Situação do Pagamento'] == 'Realizado']
    df_faturamento_por_cliente = df_faturamento_por_cliente.groupby('Nome')['Faturamento (R$)'].sum().reset_index()
    df_faturamento_por_cliente = df_faturamento_por_cliente.sort_values('Faturamento (R$)', ascending=False).head()
    df_faturamento_por_cliente['Faturamento (R$)'] = df_faturamento_por_cliente['Faturamento (R$)'].astype('float64')
    fig_faturamento_cliente = px.bar(
        data_frame=df_faturamento_por_cliente, 
        x='Nome', 
        y='Faturamento (R$)',
        text=df_faturamento_por_cliente['Faturamento (R$)'].apply(lambda x: f'R$ {x:.2f}'),
        color='Faturamento (R$)',
        hover_name='Nome'
    )
    fig_faturamento_cliente.update_layout(
        title=f'Top 5 Clientes em {data.year}',
        xaxis_type='category',
        yaxis_showticklabels=False
    )
    fig_faturamento_cliente.update_traces(
        showlegend=False,
        textposition='outside',
        hovertemplate='Nome: %{hovertext}<br>Faturamento: R$ %{y:.2f}'
    )
    fig_faturamento_cliente.update_xaxes(
        tickangle=45
    )

    #dashboard
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(f'**Total faturado em {data.day}/{data.month}/{data.year}**', f'R$ {total_faturado_dia}')
    with col2:
        st.metric(f'**Total faturado em {data.month}/{data.year}**', f'R$ {total_faturado_mes}')
    with col3:
        st.metric(f'**Total faturado em {data.year}**', f'R$ {total_faturado_ano}')
    #graficos
    st.plotly_chart(fig_faturamento_mensal)
    st.plotly_chart(fig_faturamento_cliente)
    
with tab3:
    st.subheader('Estoque 📦')
    st.warning('Em desenvolvimento')