import streamlit as st
import controllers.controllers as controllers
import models.models as models


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


def consulta_fornecedores():
    fornecedores = []
    for item in controllers.select_fornecedores():
        fornecedores.append(
            [
                item.id_fornecedores, item.nome_fornecedores, item.cnpj_fornecedores,
                item.endereco_fornecedores, item.bairro_fornecedores, item.telefone_fornecedores
            ]
        )
    return fornecedores


def insert_clientes():
    with st.form(key='insert_clientes'):
        input_nome_cliente = st.text_input(label='Name')
        input_tipo_pessoa_juridica = st.checkbox('Pessoa Jurídica')
        input_tipo_pessoa_fisica = st.checkbox('Pessoa Física')
        input_cpf_cnpj_cliente = st.text_input(label='CPF/CNPJ')
        input_endereco_cliente = st.text_input(label='Endereço')
        input_bairro_cliente = st.text_input(label='Bairro')
        input_telefone_cliente = st.text_input(label='Telefone')
        input_referencia_cliente = st.text_input(label='Referência')
        input_situacao_cliente_inadimplente = st.checkbox('Inadimplente')
        input_situacao_cliente_adimplente = st.checkbox('Adimplente')

        input_button_submit = st.form_submit_button('Inserir')
    if input_button_submit:
        if input_tipo_pessoa_juridica:
            input_tipo_cliente = False
        if input_tipo_pessoa_fisica:
            input_tipo_cliente = True
        if input_situacao_cliente_inadimplente:
            input_situacao_cliente = False
        if input_situacao_cliente_adimplente:
            input_situacao_cliente = True

        controllers.insert_clientes(
            models.Cliente(0, input_nome_cliente, input_tipo_cliente, input_cpf_cnpj_cliente, input_endereco_cliente, input_bairro_cliente, input_telefone_cliente, input_referencia_cliente, input_situacao_cliente)
        )
        st.success('Cliente inserido!')
