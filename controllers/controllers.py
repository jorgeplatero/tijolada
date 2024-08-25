import streamlit as st
import services.database as db
import models.models as models
import re

#consultas
#---------------------------------------------------------------

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

def select_clientes():
    db.cursor.execute('SELECT * FROM cliente')
    clientes = []
    for row in db.cursor.fetchall():
        clientes.append(
            models.Cliente(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]
                )
        )
    return clientes

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
        st.success('Venda inserida!')
    except db.erro as e:
        db.conn.rollback()
        delete_vendas(venda_produto.venda_id_venda) 
        st.error(f'{re.search(r"Quantidade.+insuficiente!", str(e)).group()}')


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
        st.success('Compra inserida!')
    except Exception as e:
        db.conn.rollback()
        delete_compras(compra_produto.compra_id_compra)
        st.error(f'Erro durante inserção: {e}')

#deletes
        
def delete_compras(id_compra):
    try:
        db.cursor.execute(
            f"""
                DELETE FROM compra WHERE ID_compra = {id_compra};
            """
        )
        db.conn.commit()
    except Exception as e:
        st.write(f'Erro durante exclusão: {e}')
        db.conn.rollback()
        

def delete_vendas(id_venda):
    try:
        db.cursor.execute(
            f"""
                DELETE FROM venda WHERE ID_venda = {id_venda};
            """
        )
        db.conn.commit()
    except Exception as e:
        st.write(f'Erro durante exclusão: {e}')
        db.conn.rollback()
        
#updates
#---------------------------------------------------------------
        
#fornecedores
def update_fornecedores(fornecedor):
    try:
        db.cursor.execute(
            f"""
                UPDATE fornecedor SET 
                    nome_fornecedor = '{fornecedor.nome_fornecedor}',  
                    cnpj_fornecedor = '{fornecedor.cnpj_fornecedor}', 
                    endereco_fornecedor = '{fornecedor.endereco_fornecedor}', 
                    bairro_fornecedor = '{fornecedor.bairro_fornecedor}', 
                    telefone_fornecedor = '{fornecedor.telefone_fornecedor}'
                WHERE 
                    ID_fornecedor = '{fornecedor.id_fornecedor}';
            """
        )
        db.conn.commit()
    except Exception as e:
        st.write(f'Erro durante inserção: {e}')
        db.conn.rollback()


#produtos
def update_produtos(produto):
    try:
        db.cursor.execute(
            f"""
                UPDATE produto SET 
                    nome_produto = '{produto.nome_produto}',  
                    unidade_medida_produto = '{produto.unidade_medida_produto}'
                WHERE 
                    ID_produto = '{produto.id_produto}';
            """
        )
        db.conn.commit()
    except Exception as e:
        st.write(f'Erro durante inserção: {e}')
        db.conn.rollback()


#clientes
def update_clientes(cliente):
    try:
        db.cursor.execute(
            f"""
                UPDATE cliente SET 
                    nome_cliente = '{cliente.nome_cliente}', 
                    tipo_cliente = '{cliente.tipo_cliente}', 
                    cpf_cnpj_cliente = '{cliente.cpf_cnpj_cliente}', 
                    endereco_cliente = '{cliente.endereco_cliente}', 
                    bairro_cliente = '{cliente.bairro_cliente}', 
                    telefone_cliente = '{cliente.telefone_cliente}', 
                    referencia_cliente = '{cliente.referencia_cliente}', 
                    situacao_cliente  = '{cliente.situacao_cliente}'
                WHERE 
                    ID_cliente = '{cliente.id_cliente}';
            """
        )
        db.conn.commit()
    except Exception as e:
        st.write(f'Erro durante inserção: {e}')
        db.conn.rollback()
        

#compra
def update_compras(compra):
    try:
        db.cursor.execute(
            f"""
                UPDATE compra SET 
                    data_compra = '{compra.data_compra}', 
                    fornecedor_ID_fornecedor = '{compra.fornecedor_id_fornecedor}', 
                    produto_ID_produto = '{compra.produto_id_produto}', 
                    preco_total_compra = '{compra.preco_total_compra}', 
                    forma_pagamento_compra = '{compra.forma_pagamento_compra}', 
                    situacao_pagamento_compra = '{compra.situacao_pagamento_compra}', 
                    situacao_entrega_compra  = '{compra.situacao_entrega_compra}'
                WHERE 
                    ID_compra = '{compra.id_compra}';
            """
        )
        db.conn.commit()
    except Exception as e:
        st.write(f'Erro durante inserção: {e}')
        db.conn.rollback()
        

def update_compras_produtos(compra_produto):
    try:
        db.cursor.execute(
            f"""
                UPDATE compra_produto SET 
                    compra_ID_compra = '{compra_produto.compra_id_compra}', 
                    produto_ID_produto = '{compra_produto.produto_id_produto}', 
                    preco_unitario_produto_compra = '{compra_produto.preco_unitario_produto_compra}', 
                    quantidade_produto_compra = '{compra_produto.quantidade_produto_compra}'
                WHERE 
                    ID_compra_produto = '{compra_produto.id_compra_produto}';
            """
        )
        db.conn.commit()
    except Exception as e:
        st.write(f'Erro durante inserção: {e}')
        db.conn.rollback()
        

#venda
def update_vendas(venda):
    try:
        db.cursor.execute(
            f"""
                UPDATE venda SET 
                    data_venda = '{venda.data_venda}', 
                    cliente_ID_cliente = '{venda.cliente_id_cliente}', 
                    endereco_entrega_venda = '{venda.endereco_entrega_venda}', 
                    bairro_entrega_venda = '{venda.bairro_entrega_venda}', 
                    observacoes_venda = '{venda.observacoes_venda}', 
                    preco_total_venda = '{venda.preco_total_venda}', 
                    situacao_pagamento_venda  = '{venda.situacao_pagamento_venda}',
                    situacao_entrega_venda  = '{venda.situacao_entrega_venda}',
                    forma_pagamento_venda  = '{venda.forma_pagamento_venda}'
                WHERE 
                    ID_venda = '{venda.id_venda}';
            """
        )
        db.conn.commit()
    except Exception as e:
        st.write(f'Erro durante inserção: {e}')
        db.conn.rollback()
        

def update_vendas_produtos(venda_produto):
    try:
        db.cursor.execute(
            f"""
                UPDATE venda_produto SET 
                    venda_ID_venda = '{venda_produto.venda_id_venda}', 
                    produto_ID_produto = '{venda_produto.produto_id_produto}', 
                    preco_unitario_produto_venda = '{venda_produto.preco_unitario_produto_venda}', 
                    quantidade_produto_venda = '{venda_produto.quantidade_produto_venda}'
                WHERE 
                    ID_venda_produto = '{venda_produto.id_venda_produto}';
            """
        )
        db.conn.commit()
    except Exception as e:
        st.write(f'Erro durante inserção: {e}')
        db.conn.rollback()