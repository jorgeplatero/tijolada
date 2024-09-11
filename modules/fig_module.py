import streamlit as st
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')


#graficos
#---------------------------------------------------------------

#evolução de despesas no ano selecionado
def fig_evolucao_despesa(df, data):
    df_compras_custo_mensal = df.sort_values('Data')
    df_compras_custo_mensal['Data'] = df_compras_custo_mensal['Data'].dt.date
    df_compras_custo_mensal = df_compras_custo_mensal.groupby('Data')['Custo (R$)'].sum().reset_index()
    fig = px.line(
        data_frame=df_compras_custo_mensal, 
        x='Data', 
        y='Custo (R$)',
        hover_name='Data',
        labels={'Custo (R$)': 'Despesa (R$)'}
    )
    fig.update_layout(
        title=f'Evolução de Despesas em {data.year}',
        xaxis_title='Data', 
        yaxis_showticklabels=True,
        height=500
    )
    fig.update_traces(
        textposition='top center',
        hovertemplate='Data: %{hovertext}<br>Despesa: R$ %{y:.2f}'
    )
    st.plotly_chart(fig)


#despesa por fornecedor no ano selecionado
def fig_despesa_por_fornecedor(df, data):
    df_custo_por_fornecedor = df
    df_custo_por_fornecedor = df_custo_por_fornecedor.groupby('Nome')['Custo (R$)'].sum().reset_index()
    df_custo_por_fornecedor = df_custo_por_fornecedor.sort_values('Custo (R$)', ascending=False).head()
    df_custo_por_fornecedor['Custo (R$)'] = df_custo_por_fornecedor['Custo (R$)'].astype('float64')
    fig = px.bar(
        data_frame=df_custo_por_fornecedor, 
        x='Nome', 
        y='Custo (R$)',
        text=df_custo_por_fornecedor['Custo (R$)'].apply(lambda x: f'R$ {x:.2f}'),
        color='Custo (R$)',
        hover_name='Nome',
        labels={'Custo (R$)': 'Despesa (R$)'}
    )
    fig.update_layout(
        title=f'Top 5 Clientes em {data.year}',
        xaxis_type='category',
        yaxis_showticklabels=False,
        height=500
    )
    fig.update_traces(
        showlegend=False,
        textposition='outside',
        hovertemplate='Nome: %{hovertext}<br>Custo: R$ %{y:.2f}'
    )
    fig.update_xaxes(
        tickangle=45
    )
    st.plotly_chart(fig)


#evolução da despesa por produto no ano selecionado
def fig_evolucao_despesa_por_produto(df, data, produtos):
    df_despesa_por_produto = df.sort_values('Data')
    df_despesa_por_produto['Data'] = df_despesa_por_produto['Data'].dt.date
    df_despesa_por_produto['Despesa (R$)'] = df_despesa_por_produto['Preço Unitário (R$)'].astype(float) * df_despesa_por_produto['Quantidade']
    df_despesa_por_produto = df_despesa_por_produto.groupby(['Data', 'Nome'])['Despesa (R$)'].sum().reset_index().sort_values('Data')
    df_despesa_por_produto = df_despesa_por_produto[df_despesa_por_produto['Nome'].isin(produtos)]
    fig = px.line(
        data_frame=df_despesa_por_produto, 
        x='Data', 
        y='Despesa (R$)',
        text=df_despesa_por_produto['Despesa (R$)'].apply(lambda x: f'R$ {x:.2f}'),
        hover_name='Nome',
        color='Nome'
    )
    fig.update_layout(
        title=f'Evolução da Despesa Por Produto em {data.year}',
        xaxis_title='Data', 
        yaxis_showticklabels=False,
        height=500
    )
    fig.update_traces(
        textposition='top center',
        hovertemplate='Produto: %{hovertext}<br>Despesa (R$): %{y:.2f}<br>Data: %{x}'
    )
    st.plotly_chart(fig)


#evolucao do faturamento no ano selecionado
def fig_evolucao_faturamento(df, data):
    df_vendas_faturamento_mensal = df.sort_values('Data')
    df_vendas_faturamento_mensal['Data'] = df_vendas_faturamento_mensal['Data'].dt.date
    df_vendas_faturamento_mensal = df_vendas_faturamento_mensal[df_vendas_faturamento_mensal['Situação do Pagamento'] == 'Realizado']
    df_vendas_faturamento_mensal = df_vendas_faturamento_mensal.groupby('Data')['Faturamento (R$)'].sum().reset_index()
    fig = px.line(
        data_frame=df_vendas_faturamento_mensal, 
        x='Data', 
        y='Faturamento (R$)',
        hover_name='Data'
    )
    fig.update_layout(
        title=f'Faturamento Mensal em {data.year}',
        xaxis_title='Data',
        height=500
    )
    fig.update_traces(
        textposition='top center',
        hovertemplate='Data: %{hovertext}<br>Faturamento: R$ %{y:.2f}'
    )
    st.plotly_chart(fig)
    

#faturamento por cliente no ano selecionado
def fig_faturamento_por_cliente(df, data):
    df_faturamento_por_cliente = df[df['Situação do Pagamento'] == 'Realizado']
    df_faturamento_por_cliente = df_faturamento_por_cliente.groupby('Nome')['Faturamento (R$)'].sum().reset_index()
    df_faturamento_por_cliente = df_faturamento_por_cliente.sort_values('Faturamento (R$)', ascending=False).head()
    df_faturamento_por_cliente['Faturamento (R$)'] = df_faturamento_por_cliente['Faturamento (R$)'].astype('float64')
    fig = px.bar(
        data_frame=df_faturamento_por_cliente, 
        x='Nome', 
        y='Faturamento (R$)',
        text=df_faturamento_por_cliente['Faturamento (R$)'].apply(lambda x: f'R$ {x:.2f}'),
        color='Faturamento (R$)',
        hover_name='Nome'
    )
    fig.update_layout(
        title=f'Top 5 Clientes em {data.year}',
        xaxis_type='category',
        yaxis_showticklabels=False,
        height=500
    )
    fig.update_traces(
        showlegend=False,
        textposition='outside',
        hovertemplate='Nome: %{hovertext}<br>Faturamento: R$ %{y:.2f}'
    )
    fig.update_xaxes(
        tickangle=45
    )
    st.plotly_chart(fig)


#evolução do faturamento por produto no ano selecionado
def fig_evolucao_faturamento_por_produto(df, data, produtos):
    df_faturamento_por_produto = df.sort_values('Data')
    df_faturamento_por_produto['Data'] = df_faturamento_por_produto['Data'].dt.date
    df_faturamento_por_produto['Faturamento (R$)'] = df_faturamento_por_produto['Preço Unitário (R$)'].astype(float) * df_faturamento_por_produto['Quantidade']
    df_faturamento_por_produto = df_faturamento_por_produto.groupby(['Data', 'Nome'])['Faturamento (R$)'].sum().reset_index().sort_values('Data')
    df_faturamento_por_produto = df_faturamento_por_produto[df_faturamento_por_produto['Nome'].isin(produtos)]
    fig = px.line(
        data_frame=df_faturamento_por_produto, 
        x='Data', 
        y='Faturamento (R$)',
        text=df_faturamento_por_produto['Faturamento (R$)'].apply(lambda x: f'R$ {x:.2f}'),
        hover_name='Nome',
        color='Nome',
    )
    fig.update_layout(
        title=f'Evolução do Faturamento Por Produto em {data.year}',
        xaxis_title='Data', 
        yaxis_showticklabels=False,
        height=500
    )
    fig.update_traces(
        textposition='top center',
        hovertemplate='Produto: %{hovertext}<br>Faturamento (R$): %{y:.2f}<br>Data: %{x}'
    )
    st.plotly_chart(fig)
