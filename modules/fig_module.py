import streamlit as st
import plotly.express as px
import modules.utils_module as utils
import warnings
warnings.filterwarnings('ignore')


#graficos
#---------------------------------------------------------------

meses = {
        '01': 'Jan', '02': 'Fev', '03': 'Mar', '04': 'Abr', '05': 'Mai', '06': 'Jun', 
        '07': 'Jul', '08': 'Ago', '09': 'Set', '10': 'Out', '11': 'Nov', '12': 'Dez'
    }

#compras

#evolução de despesas no ano selecionado 
def fig_evolucao_despesa(df, data):
    df_evolucao_despesa = df.sort_values('Data')
    df_evolucao_despesa['Mês'] = df_evolucao_despesa['Data'].dt.strftime('%m')
    df_evolucao_despesa = df_evolucao_despesa.groupby('Mês')['Custo (R$)'].sum().reset_index()
    df_evolucao_despesa = df_evolucao_despesa.rename(columns={'Custo (R$)':'Despesa (R$)'})
    fig = px.line(
        data_frame=df_evolucao_despesa, 
        x='Mês', 
        y='Despesa (R$)',
        text=df_evolucao_despesa['Despesa (R$)'].apply(lambda x: f'R${utils.formata_valor(x)}'),
        hover_name=df_evolucao_despesa['Mês'].map(meses),
    )
    fig.update_layout(
        title=f'Evolução da Despesa em {data.year}',
        yaxis_showticklabels=False,
        xaxis_tickmode='array', 
        xaxis_tickvals = list(meses.keys()),  
        xaxis_ticktext = list(meses.values())
    )
    fig.update_traces(
        textposition='top center',
        hovertemplate='Mês: %{hovertext}<br>Despesa: %{text}'
    )
    st.plotly_chart(fig)
    

#despesa por fornecedor no ano selecionado
def fig_despesa_por_fornecedor(df, data):
    df_despesa_por_fornecedor = df
    df_despesa_por_fornecedor = df_despesa_por_fornecedor.groupby('Nome')['Custo (R$)'].sum().reset_index()
    df_despesa_por_fornecedor = df_despesa_por_fornecedor.sort_values('Custo (R$)', ascending=False).head()
    df_despesa_por_fornecedor['Despesa (R$)'] = df_despesa_por_fornecedor['Custo (R$)'].astype('float64')
    df_despesa_por_fornecedor = df_despesa_por_fornecedor.rename(columns={'Nome':'Fornecedor'})
    fig = px.bar(
        data_frame=df_despesa_por_fornecedor, 
        x='Fornecedor', 
        y='Despesa (R$)',
        text=df_despesa_por_fornecedor['Despesa (R$)'].apply(lambda x: f'R${utils.formata_valor(x)}'),
        hover_name='Fornecedor',
    )
    fig.update_layout(
        title=f'Top 5 Clientes em {data.year}',
        yaxis_showticklabels=False
    )
    fig.update_traces(
        textposition='outside',
        hovertemplate='Fornecedor: %{hovertext}<br>Despesa: %{text}'
    )
    st.plotly_chart(fig)


#evolução da despesa por produto no ano selecionado
def fig_evolucao_despesa_por_produto(df, data, produtos):
    df_despesa_por_produto = df.sort_values('Data')
    df_despesa_por_produto['Mês'] = df_despesa_por_produto['Data'].dt.strftime('%m')
    df_despesa_por_produto['Despesa (R$)'] = df_despesa_por_produto['Preço Unitário (R$)'].astype(float) * df_despesa_por_produto['Quantidade']
    df_despesa_por_produto = df_despesa_por_produto.groupby(['Mês', 'Nome'])['Despesa (R$)'].sum().reset_index().sort_values('Mês')
    df_despesa_por_produto = df_despesa_por_produto[df_despesa_por_produto['Nome'].isin(produtos)]
    st.dataframe(df_despesa_por_produto)
    fig = px.line(
        data_frame=df_despesa_por_produto, 
        x='Mês', 
        y='Despesa (R$)',
        text=df_despesa_por_produto['Despesa (R$)'].apply(lambda x: f'R${utils.formata_valor(x)}'),
        color='Nome'
    )
    fig.update_layout(
        title=f'Evolução da Despesa por Produto em {data.year}',
        yaxis_showticklabels=False,
        xaxis_tickmode='array', 
        xaxis_tickvals = list(meses.keys()),  
        xaxis_ticktext = list(meses.values())
    )
    fig.update_traces(
        textposition='top center',
        hovertemplate='Despesa: %{text}<br>Data: %{x}',
    )
    st.plotly_chart(fig)


#vendas

#evolucao do faturamento no ano selecionado
def fig_evolucao_faturamento(df, data):
    df_evolucao_faturamento = df.sort_values('Data')
    df_evolucao_faturamento['Mês'] = df_evolucao_faturamento['Data'].dt.strftime('%m')
    df_evolucao_faturamento = df_evolucao_faturamento[df_evolucao_faturamento['Situação do Pagamento'] == 'Realizado']
    df_evolucao_faturamento = df_evolucao_faturamento.groupby('Mês')['Faturamento (R$)'].sum().reset_index()
    fig = px.line(
        data_frame=df_evolucao_faturamento, 
        x='Mês', 
        y='Faturamento (R$)',
        text=df_evolucao_faturamento['Faturamento (R$)'].apply(lambda x: f'R${utils.formata_valor(x)}'),
        hover_name=df_evolucao_faturamento['Mês'].map(meses)
    )
    fig.update_layout(
        title=f'Evolução do Faturamento em {data.year}',
        yaxis_showticklabels=False,
        xaxis_tickmode='array', 
        xaxis_tickvals = list(meses.keys()),  
        xaxis_ticktext = list(meses.values())
    )
    fig.update_traces(
        textposition='top center',
        hovertemplate='Data: %{hovertext}<br>Faturamento: %{text}'
    )
    st.plotly_chart(fig)
    

#faturamento por cliente no ano selecionado
def fig_faturamento_por_cliente(df, data):
    df_faturamento_por_cliente = df[df['Situação do Pagamento'] == 'Realizado']
    df_faturamento_por_cliente = df_faturamento_por_cliente.groupby('Nome')['Faturamento (R$)'].sum().reset_index()
    df_faturamento_por_cliente = df_faturamento_por_cliente.sort_values('Faturamento (R$)', ascending=False).head()
    df_faturamento_por_cliente['Faturamento (R$)'] = df_faturamento_por_cliente['Faturamento (R$)'].astype('float64')
    df_faturamento_por_cliente = df_faturamento_por_cliente.rename(columns={'Nome':'Cliente'})
    fig = px.bar(
        data_frame=df_faturamento_por_cliente, 
        x='Cliente', 
        y='Faturamento (R$)',
        text=df_faturamento_por_cliente['Faturamento (R$)'].apply(lambda x: f'R${utils.formata_valor(x)}'),
        hover_name='Cliente'
    )
    fig.update_layout(
        title=f'Top 5 Clientes em {data.year}',
        xaxis_type='category',
        yaxis_showticklabels=False,
    )
    fig.update_traces(
        textposition='outside',
        hovertemplate='Cliente: %{hovertext}<br>Faturamento: %{text}'
    )
    st.plotly_chart(fig)


#evolução do faturamento por produto no ano selecionado
def fig_evolucao_faturamento_por_produto(df, data, produtos):
    df_faturamento_por_produto = df.sort_values('Data')
    df_faturamento_por_produto['Mês'] = df_faturamento_por_produto['Data'].dt.strftime('%m')
    df_faturamento_por_produto['Faturamento (R$)'] = df_faturamento_por_produto['Preço Unitário (R$)'].astype(float) * df_faturamento_por_produto['Quantidade']
    df_faturamento_por_produto = df_faturamento_por_produto.groupby(['Mês', 'Nome'])['Faturamento (R$)'].sum().reset_index().sort_values('Mês')
    df_faturamento_por_produto = df_faturamento_por_produto[df_faturamento_por_produto['Nome'].isin(produtos)]
    st.dataframe(df_faturamento_por_produto)
    fig = px.line(
        data_frame=df_faturamento_por_produto, 
        x='Mês', 
        y='Faturamento (R$)',
        text=df_faturamento_por_produto['Faturamento (R$)'].apply(lambda x: f'R${utils.formata_valor(x)}'),
        hover_name='Nome',
        color='Nome',
    )
    fig.update_layout(
        title=f'Evolução do Faturamento por Produto em {data.year}',
        yaxis_showticklabels=False,
        xaxis_tickmode='array', 
        xaxis_tickvals = list(meses.keys()),  
        xaxis_ticktext = list(meses.values())
    )
    fig.update_traces(
        textposition='top center',
        hovertemplate='Faturamento: %{text}<br>Data: %{x}'
    )
    st.plotly_chart(fig)
    

#estoque

#estoque por produto no ano selecionado
def fig_estoque_por_produto(df, data):
    df_estoque_por_produto = df
    df_estoque_por_produto = df_estoque_por_produto.groupby('Nome')['Custo (R$)'].sum().reset_index()
    df_estoque_por_produto = df_estoque_por_produto.sort_values('Custo (R$)', ascending=False).head()
    df_estoque_por_produto['Despesa (R$)'] = df_estoque_por_produto['Custo (R$)'].astype('float64')
    df_estoque_por_produto = df_estoque_por_produto.rename(columns={'Nome':'Cliente'})
    fig = px.bar(
        data_frame=df_estoque_por_produto, 
        x='Cliente', 
        y='Despesa (R$)',
        text=df_estoque_por_produto['Despesa (R$)'].apply(lambda x: f'R${utils.formata_valor(x)}'),
        color='Despesa (R$)',
        hover_name='Cliente',
    )
    fig.update_layout(
        title=f'Top 5 Clientes em {data.year}',
        yaxis_showticklabels=False,
    )
    fig.update_traces(
        textposition='outside',
        hovertemplate='Cliente: %{hovertext}<br>Despesa: %{text}'
    )
    st.plotly_chart(fig)