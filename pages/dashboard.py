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
colunas_cliente = [
    'ID Cliente', 'Nome', 'Tipo', 'CPF/CNPJ', 'Endereço', 'Bairro', 'Telefone', 
    'Referência', 'Situação'
]
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
    st.warning('Em desenvolvimento')

with tab2:
    st.subheader('Indicadores de Vendas 🛒')
    st.write('')
    #seletor data
    col1, _ = st.columns([.2, .8])
    with col1:
        data = st.date_input(
            label='**Data**',
            help='Escolha uma data para análise'
        )
    st.write('')
    #dataframes
    df_vendas = pd.DataFrame(utils.consulta_vendas(), columns=colunas_venda)
    df_vendas = df_vendas[df_vendas.Data.dt.year == data.year]
    df_clientes =  pd.DataFrame(utils.consulta_clientes(), columns=colunas_cliente)
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
    df_vendas_faturamento_cliente = pd.merge(df_vendas, df_clientes, how='outer', on='ID Cliente')
    df_vendas_faturamento_cliente = df_vendas_faturamento_cliente[df_vendas_faturamento_cliente['Situação do Pagamento'] == 'Realizado']
    df_vendas_faturamento_cliente = df_vendas_faturamento_cliente.groupby('Nome')['Faturamento (R$)'].sum().reset_index()
    df_vendas_faturamento_cliente = df_vendas_faturamento_cliente.sort_values('Faturamento (R$)', ascending=False).head()
    df_vendas_faturamento_cliente['Faturamento (R$)'] = df_vendas_faturamento_cliente['Faturamento (R$)'].astype('float64')
    fig_faturamento_cliente = px.bar(
        data_frame=df_vendas_faturamento_cliente, 
        x='Nome', 
        y='Faturamento (R$)',
        text=df_vendas_faturamento_cliente['Faturamento (R$)'].apply(lambda x: f'R$ {x:.2f}'),
        hover_name='Nome',
        color='Faturamento (R$)'
    )
    fig_faturamento_cliente.update_layout(
        title=f'Top 5 Clientes em {data.year}',
        xaxis_type='category',
        yaxis_showticklabels=False,
        width=800
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
        st.metric(f'**Total faturado no dia {data.day} do {data.month} de {data.year}**', f'R$ {total_faturado_dia}')
    with col2:
        st.metric(f'**Total faturado no mês {data.month}**', f'R$ {total_faturado_mes}')
    with col3:
        st.metric(f'**Total faturado no ano de {data.year}**', f'R$ {total_faturado_ano}')
    #graficos
    st.plotly_chart(fig_faturamento_mensal)
    st.plotly_chart(fig_faturamento_cliente)
    
with tab3:
    st.warning('Em desenvolvimento')