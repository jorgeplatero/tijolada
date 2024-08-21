import streamlit as st
import services.database as db
import models.models as models


#consultas
def select_clientes():
    db.cursor.execute('SELECT * FROM cliente')
    clientes = []
    for row in db.cursor.fetchall():
        clientes.append(
            models.Cliente(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
        )
    return clientes


def select_fornecedores():
    db.cursor.execute('SELECT * FROM fornecedor')
    fornecedores = []
    for row in db.cursor.fetchall():
        fornecedores.append(
            models.Fornecedor(row[0], row[1], row[2], row[3], row[4], row[5])
        )
    return fornecedores


def select_produtos():
    db.cursor.execute('SELECT * FROM produto')
    produtos = []
    for row in db.cursor.fetchall():
        produtos.append(
            models.Fornecedor(row[0], row[1], row[2])
        )
    return produtos


def select_estoques():
    db.cursor.execute('SELECT * FROM estoque')
    estoques = []
    for row in db.cursor.fetchall():
        estoques.append(
            models.Fornecedor(row[0], row[1], row[2])
        )
    return estoques


def select_vendas():
    db.cursor.execute('SELECT * FROM venda')
    vendas = []
    for row in db.cursor.fetchall():
        vendas.append(
            models.Venda(
                    row[0], row[1], row[2], row[3], row[4], row[5],
                    row[6], row[7], row[8], row[9]
                )
        )
    return vendas


def select_compras():
    db.cursor.execute('SELECT * FROM compra')
    compras = []
    for row in db.cursor.fetchall():
        compras.append(
            models.Compra(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6]
                )
        )
    return compras


#inserts
def insert_clientes(cliente):
    try:
        count = db.cursor.execute(
            f"""
                INSERT INTO cliente (nome_cliente, tipo_cliente, cpf_cnpj_cliente, endereco_cliente, bairro_cliente, telefone_cliente, referencia_cliente, situacao_cliente)
                VALUES ('{cliente.nome_cliente}', {cliente.tipo_cliente}, '{cliente.cpf_cnpj_cliente}', '{cliente.endereco_cliente}', '{cliente.bairro_cliente}', {cliente.telefone_cliente}, '{cliente.referencia_cliente}', '{cliente.situacao_cliente}');
            """
        )
        db.conn.commit()
        st.success('Cliente inserido!')
    except Exception as e:
        st.write(f'Erro durante inserção: {e}')
        

def insert_fornecedores(fornecedor):
    try:
        count = db.cursor.execute(
            f"""
                INSERT INTO fornecedor (nome_fornecedor, tipo_fornecedor, cnpj_fornecedor, endereco_fornecedor, bairro_fornecedor, telefone_fornecedor, referencia_fornecedor, situacao_fornecedor)
                VALUES ('{fornecedor.nome_fornecedor}', '{fornecedor.cnpj_fornecedor}', '{fornecedor.endereco_fornecedor}', '{fornecedor.bairro_fornecedor}', '{fornecedor.telefone_fornecedor}');
            """
        )
        db.conn.commit()
        st.success('Fornecedor inserido!')
    except Exception as e:
        st.write(f'Erro durante inserção: {e}')