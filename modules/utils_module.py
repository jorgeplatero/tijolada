import streamlit as st
import controllers.controllers as controllers
import time
import warnings
warnings.filterwarnings('ignore')


#formatacoes
#---------------------------------------------------------------

#valores
def formata_valor(valor, prefixo = ''):
    for unidade in ['', 'mil']:
        if valor < 1000:
            return f'{prefixo} {valor:.2f} {unidade}'
        valor /= 1000
    return f'{prefixo} {valor:.2f} milhões'

#estilos
#---------------------------------------------------------------

#estoque
def estiliza_celula_estoque(nivel):
    color = '#FF6347' if nivel == 'Sem Estoque' else '#3CB371' if nivel == 'Alto' else '#4682B4' if nivel == 'Médio' else '#FFFF00'
    return f'background-color: {color}; color: black; font-weight: bold'


#calculos
#---------------------------------------------------------------

#nivel do estoque
def categoriza_quantidade_estoque(qtd):
    if 1 <= qtd <= 10:
        return 'Baixo'  
    elif 10 <= qtd <= 100:
        return 'Médio'  
    elif qtd >= 100:
        return 'Alto'
    else:
        return 'Sem Estoque'


#mensagens
#---------------------------------------------------------------

#valores
def mensagem_sucesso(mensagem):
    st.success(f'{mensagem}!')
    time.sleep(1)


def mensagem_erro(mensagem):
    st.error(f'{mensagem}')
    time.sleep(5)


#consultas
#---------------------------------------------------------------

#clientes
def consulta_clientes():
    clientes = []
    try:
        for item in controllers.select_clientes():
            clientes.append(
                [
                    item.id_cliente, item.nome_cliente, item.tipo_cliente, item.cpf_cnpj_cliente,
                    item.endereco_cliente, item.bairro_cliente, item.telefone_cliente, 
                    item.referencia_cliente, item.situacao_cliente
                ]
            )
    except Exception as e:
            st.error(f'Erro durante consulta: {e}')
    return clientes


#fornecedores
def consulta_fornecedores():
    fornecedores = []
    try:
        for item in controllers.select_fornecedores():
            fornecedores.append(
                [
                    item.id_fornecedor, item.nome_fornecedor, item.cnpj_fornecedor,
                    item.endereco_fornecedor, item.bairro_fornecedor, item.telefone_fornecedor
                ]
            )
    except Exception as e:
            st.error(f'Erro durante consulta: {e}')
    return fornecedores


#produtos
def consulta_produtos():
    produtos = []
    try:
        for item in controllers.select_produtos():
            produtos.append([item.id_produto, item.nome_produto, item.unidade_medida_produto])
    except Exception as e:
            st.error(f'Erro durante consulta: {e}')
    return produtos


#compras
def consulta_compras():
    compras = []
    try:
        for item in controllers.select_compras():
            compras.append(
                [
                    item.id_compra, item.data_compra, item.fornecedor_id_fornecedor, item.preco_total_compra, 
                    item.situacao_pagamento_compra, item.situacao_entrega_compra, item.forma_pagamento_compra
                ]
            )
    except Exception as e:
            st.error(f'Erro durante consulta: {e}')
    return compras


#itens de compras
def consulta_compras_produtos():
    compras_produtos = []
    try:
        for item in controllers.select_compras_produtos():
            compras_produtos.append(
                [
                    item.id_compra_produto, item.compra_id_compra, item.produto_id_produto, 
                    item.preco_unitario_produto_compra, item.quantidade_produto_compra
                ]
            )
    except Exception as e:
            st.error(f'Erro durante consulta: {e}')
    return compras_produtos


#vendas
def consulta_vendas():
    vendas = []
    try:
        for item in controllers.select_vendas():
            vendas.append(
                [
                    item.id_venda, item.data_venda, item.cliente_id_cliente,
                    item.endereco_entrega_venda, item.bairro_entrega_venda, item.observacoes_venda,
                    item.preco_total_venda, item.situacao_pagamento_venda, item.situacao_entrega_venda,
                    item.forma_pagamento_venda
                ]
            )
    except Exception as e:
            st.error(f'Erro durante consulta: {e}')
    return vendas


#itens de vendas
def consulta_vendas_produtos():
    vendas_produtos = []
    try:
        for item in controllers.select_vendas_produtos():
            vendas_produtos.append(
                [
                    item.id_venda_produto, item.venda_id_venda, item.produto_id_produto, 
                    item.preco_unitario_produto_venda, item.quantidade_produto_venda
                ]
            )
    except Exception as e:
            st.error(f'Erro durante consulta: {e}')
    return vendas_produtos


#estoque
def consulta_estoques():
    estoques = []
    try:
        for item in controllers.select_estoques():
            estoques.append(
                [
                    item.id_estoque, item.produto_id_produto, item.quantidade_estoque
                ]
            )
    except Exception as e:
            st.error(f'Erro durante consulta: {e}')
    return estoques