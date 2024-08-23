import streamlit as st
import services.database as db
import models.models as models


#consultas
#---------------------------------------------------------------

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
            models.Produto(row[0], row[1], row[2])
        )
    return produtos


def select_estoques():
    db.cursor.execute('SELECT * FROM estoque')
    estoques = []
    for row in db.cursor.fetchall():
        estoques.append(
            models.Estoque(row[0], row[1], row[2])
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
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
                )
        )
    return compras


#inserts
#---------------------------------------------------------------

#clientes
def insert_clientes(cliente):
    try:
        db.cursor.execute(
            f"""
                INSERT INTO cliente (nome_cliente, tipo_cliente, cpf_cnpj_cliente, endereco_cliente, bairro_cliente, telefone_cliente, referencia_cliente, situacao_cliente)
                VALUES ('{cliente.nome_cliente}', '{cliente.tipo_cliente}', '{cliente.cpf_cnpj_cliente}', '{cliente.endereco_cliente}', '{cliente.bairro_cliente}', {cliente.telefone_cliente}, '{cliente.referencia_cliente}', '{cliente.situacao_cliente}');
            """
        )
        db.conn.commit()
    except Exception as e:
        st.write(f'Erro durante inserção: {e}')
        db.conn.rollback()

        
#fornecedores
def insert_fornecedores(fornecedor):
    try:
        db.cursor.execute(
            f"""
                INSERT INTO fornecedor (nome_fornecedor, cnpj_fornecedor, endereco_fornecedor, bairro_fornecedor, telefone_fornecedor)
                VALUES ('{fornecedor.nome_fornecedor}', '{fornecedor.cnpj_fornecedor}', '{fornecedor.endereco_fornecedor}', '{fornecedor.bairro_fornecedor}', '{fornecedor.telefone_fornecedor}');
            """
        )
        db.conn.commit()
    except Exception as e:
        st.write(f'Erro durante inserção: {e}')
        db.conn.rollback()
        

#produtos
def insert_produtos(produto):
    try:
        db.cursor.execute(
            f"""
                INSERT INTO produto (nome_produto, unidade_medida_produto)
                VALUES ('{produto.nome_produto}', '{produto.unidade_medida_produto}');
            """
        )
        db.conn.commit()
    except Exception as e:
        st.write(f'Erro durante inserção: {e}')
        db.conn.rollback()

#vendas
def insert_vendas(venda):
    try:
        db.cursor.execute(
            f"""
                INSERT INTO venda (cliente_ID_cliente, endereco_entrega_venda, bairro_entrega_venda, observacoes_venda,
                situacao_pagamento_venda, situacao_entrega_venda, forma_pagamento_venda)
                VALUES ('{venda.cliente_id_cliente}', '{venda.endereco_entrega_venda}', '{venda.bairro_entrega_venda}', 
                '{venda.observacoes_venda}', '{venda.situacao_pagamento_venda}', '{venda.situacao_entrega_venda}',
                '{venda.forma_pagamento_venda}');
            """
        )
        db.conn.commit()
    except Exception as e:
        st.write(f'Erro durante inserção: {e}')
        db.conn.rollback()
    db.cursor.execute(f'SELECT LASTVAL()')
    return db.cursor.fetchone()[0]


#produtos venda
def insert_produtos_vendas(venda_produto):
    try:
        db.cursor.execute(
            f"""
                INSERT INTO venda_produto (venda_ID_venda, produto_ID_produto, preco_unitario_produto_venda, 
                quantidade_produto_venda)
                VALUES ('{venda_produto.venda_id_venda}', '{venda_produto.produto_id_produto}', '{venda_produto.preco_unitario_produto_venda}',
                '{venda_produto.quantidade_produto_venda}');
            """
        )
        db.conn.commit()
    except Exception as e:
        st.write(f'Erro durante inserção: {e}')
        db.conn.rollback()


#compras
def insert_compras(compra):
    try:
        db.cursor.execute(
            f"""
                INSERT INTO compra (fornecedor_ID_fornecedor, produto_ID_produto, situacao_pagamento_compra, 
                situacao_entrega_compra, forma_pagamento_compra)
                VALUES ('{compra.fornecedor_id_fornecedor}', '{compra.produto_id_produto}', '{compra.situacao_pagamento_compra}', 
                '{compra.situacao_entrega_compra}', '{compra.forma_pagamento_compra}');
            """
        )
        db.conn.commit()
    except Exception as e:
        st.write(f'Erro durante inserção: {e}')
        db.conn.rollback()
    db.cursor.execute(f'SELECT LASTVAL()')
    return db.cursor.fetchone()[0]


#produtos compra
def insert_produtos_compras(compra_produto):
    try:
        db.cursor.execute(
            f"""
                INSERT INTO compra_produto (compra_ID_compra, produto_ID_produto, preco_unitario_produto_compra, 
                quantidade_produto_compra)
                VALUES ('{compra_produto.compra_id_compra}', '{compra_produto.produto_id_produto}', 
                '{compra_produto.preco_unitario_produto_compra}', '{compra_produto.quantidade_produto_compra}');
            """
        )
        db.conn.commit()
    except Exception as e:
        st.write(f'Erro durante inserção: {e}')
        db.conn.rollback()