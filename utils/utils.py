import streamlit as st
import controllers.controllers as controllers
import models.models as models


#consultas
#---------------------------------------------------------------

#clientes
def consulta_clientes():
    clientes = []
    for item in controllers.select_clientes():
        clientes.append(
            [
                item.id_cliente, item.nome_cliente, item.tipo_cliente, item.cpf_cnpj_cliente,
                item.endereco_cliente, item.bairro_cliente, item.telefone_cliente, 
                item.referencia_cliente, item.situacao_cliente
            ]
        )
    return clientes


#fornecedores
def consulta_fornecedores():
    fornecedores = []
    for item in controllers.select_fornecedores():
        fornecedores.append(
            [
                item.id_fornecedor, item.nome_fornecedor, item.cnpj_fornecedor,
                item.endereco_fornecedor, item.bairro_fornecedor, item.telefone_fornecedor
            ]
        )
    return fornecedores


#produtos
def consulta_produtos():
    produtos = []
    for item in controllers.select_produtos():
        produtos.append([item.id_produto, item.nome_produto, item.unidade_medida_produto])
    return produtos


#produtos
def consulta_estoques():
    estoques = []
    for item in controllers.select_estoques():
        estoques.append([item.id_estoque, item.produto_id_produto, item.quantidade_estoque])
    return estoques


#vendas
def consulta_vendas():
    vendas = []
    for item in controllers.select_vendas():
        vendas.append(
            [
                item.id_venda, item.data_venda, item.cliente_id_cliente,
                item.endereco_entrega_venda, item.bairro_entrega_venda, item.observacoes_venda,
                item.preco_total_venda, item.situacao_pagamento_venda, item.situacao_entrega_venda,
                item.forma_pagamento_venda
            ]
        )
    return vendas


#compras
def consulta_compras():
    compras = []
    for item in controllers.select_compras():
        compras.append(
            [
                item.id_compra, item.data_compra, item.fornecedor_id_fornecedor,
                item.preco_total_compra, item.situacao_pagamento_compra, item.situacao_entrega_compra,
                item.forma_pagamento_compra
            ]
        )
    return compras

#inserts
#---------------------------------------------------------------

#clientes
def insert_clientes():
    with st.form(key='insert_clientes'):
        col1, col2 = st.columns([.6, .4])
        with col1:
            input_nome_cliente = st.text_input(label='Nome')
        with col2:
            input_telefone_cliente = st.text_input(label='Telefone')
        input_tipo_pessoa = st.selectbox(label='Tipo', options=['Pessoa Jurídica', 'Pessoa Física'])
        input_cpf_cnpj_cliente = st.text_input(label='CPF/CNPJ')
        col1, col2 = st.columns([.6, .4])
        with col1:
            input_endereco_cliente = st.text_input(label='Endereço')
        with col2:
            input_bairro_cliente = st.text_input(label='Bairro')
        input_referencia_cliente = st.text_input(label='Referência')
        input_situacao_cliente = st.selectbox(label='Situação', options=['Inadimplente', 'Adimplente'])
        input_button_submit = st.form_submit_button('Inserir')
    
    if input_tipo_pessoa == 'Pessoa Jurídica':
        input_tipo_cliente = False
    else:
        input_tipo_cliente = True

    if input_situacao_cliente == 'Inadimplente':
        input_situacao_cliente = False
    else:
        input_situacao_cliente = True

    if input_button_submit:
        controllers.insert_clientes(
            models.Cliente(0, input_nome_cliente, input_tipo_cliente, input_cpf_cnpj_cliente, input_endereco_cliente, input_bairro_cliente, input_telefone_cliente, input_referencia_cliente, input_situacao_cliente)
        )
    else:
        pass


#fornecedores
def insert_fornecedores():
    with st.form(key='insert_fornecedores'):
        col1, col2 = st.columns([.6, .4])
        with col1:
            input_nome_fornecedor = st.text_input(label='Nome')
        with col2:
            input_telefone_fornecedor = st.text_input(label='Telefone')
        input_cnpj_fornecedor = st.text_input(label='CPF/CNPJ')
        col1, col2 = st.columns([.6, .4])
        with col1:
            input_endereco_fornecedor = st.text_input(label='Endereço')
        with col2:
            input_bairro_fornecedor = st.text_input(label='Bairro')
        input_button_submit = st.form_submit_button('Inserir')
    

    if input_button_submit:
        controllers.insert_fornecedores(
            models.Fornecedor(0, input_nome_fornecedor, input_cnpj_fornecedor, input_endereco_fornecedor, input_bairro_fornecedor, input_telefone_fornecedor)
        )
    else:
        pass