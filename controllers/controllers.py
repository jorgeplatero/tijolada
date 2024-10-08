import streamlit as st
import services.database as db
import models.models as models
import modules.utils_module as utils
import warnings
warnings.filterwarnings('ignore')


#consultas
#---------------------------------------------------------------

#fornecedores
def select_fornecedores():
    db.cursor.execute('SELECT * FROM fornecedor')
    fornecedores = []
    for row in db.cursor.fetchall():
        fornecedores.append(
            models.Fornecedor(row[0], row[1], row[2], row[3], row[4], row[5])
        )
    return fornecedores


#fornecedor selecionado
def select_fornecedor_selecionado(id_fornecedor):
    db.cursor.execute(f'SELECT * FROM fornecedor WHERE id_fornecedor = {id_fornecedor}')
    row = db.cursor.fetchone()
    if row:
        return models.Fornecedor(
            row[0], row[1], row[2], row[3], row[4], row[5]
        )
    else:
        return None


#produtos
def select_produtos():
    db.cursor.execute('SELECT * FROM produto')
    produtos = []
    for row in db.cursor.fetchall():
        produtos.append(
            models.Produto(row[0], row[1], row[2])
        )
    return produtos


#produto selecionado
def select_produto_selecionado(id_produto):
    db.cursor.execute(f'SELECT * FROM produto WHERE id_produto = {id_produto}')
    row = db.cursor.fetchone()
    if row:
        return models.Produto(
            row[0], row[1], row[2]
        )
    else:
        return None


#estoque
def select_estoques():
    db.cursor.execute('SELECT * FROM estoque')
    estoques = []
    for row in db.cursor.fetchall():
        estoques.append(
            models.Estoque(row[0], row[1], row[2])
        )
    return estoques


#vendas
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


#venda selecionada
def select_venda_selecionada(id_venda):
    db.cursor.execute(f'SELECT * FROM venda WHERE id_venda = {id_venda}')
    row = db.cursor.fetchone()
    if row:
        return models.Venda(
            row[0], row[1], row[2], row[3], row[4], row[5],
            row[6], row[7], row[8], row[9]
        )
    else:
        return None
    

#itens de venda
def select_vendas_produtos():
    db.cursor.execute('SELECT * FROM venda_produto')
    vendas_produtos = []
    for row in db.cursor.fetchall():
        vendas_produtos.append(
            models.VendaProduto(
                    row[0], row[1], row[2], row[3], row[4]
                )
        )
    return vendas_produtos


#item de venda selecionado
def select_vendas_produtos_selecionado(id_venda_produto):
    db.cursor.execute(f'SELECT * FROM venda_produto WHERE id_venda_produto = {id_venda_produto}')
    row = db.cursor.fetchone()
    if row:
        return models.VendaProduto(
            row[0], row[1], row[2], row[3], row[4]
        )
    else:
        return None
    

#compras
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


#compra selecionada
def select_compra_selecionada(id_compra):
    db.cursor.execute(f'SELECT * FROM compra WHERE id_compra = {id_compra}')
    row = db.cursor.fetchone()
    if row:
        return models.Compra(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6]
        )
    else:
        return None
    

#itens de compra
def select_compras_produtos():
    db.cursor.execute('SELECT * FROM compra_produto')
    compras_produtos = []
    for row in db.cursor.fetchall():
        compras_produtos.append(
            models.CompraProduto(
                    row[0], row[1], row[2], row[3], row[4]
                )
        )
    return compras_produtos


#item de compra selecionado
def select_compras_produtos_selecionado(id_compra_produto):
    db.cursor.execute(f'SELECT * FROM compra_produto WHERE id_compra_produto = {id_compra_produto}')
    row = db.cursor.fetchone()
    if row:
        return models.CompraProduto(
            row[0], row[1], row[2], row[3], row[4]
        )
    else:
        return None
    

#clientes
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


#cliente selecionado
def select_cliente_selecionado(id_cliente):
    db.cursor.execute(f'SELECT * FROM cliente WHERE id_cliente = {id_cliente}')
    row = db.cursor.fetchone()
    if row:
        return models.Cliente(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]
        )
    else:
        return None


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
        utils.mensagem_sucesso('Cliente inserido')
    except Exception as e:
        utils.mensagem_erro(e)
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
        utils.mensagem_sucesso('Fornecedor inserido')
    except Exception as e:
        utils.mensagem_erro(e)
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
        utils.mensagem_sucesso('Produto inserido')
    except Exception as e:
        utils.mensagem_erro(e)
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
        db.cursor.execute(f'SELECT LASTVAL()')
        return db.cursor.fetchone()[0]
    except Exception as e:
        utils.mensagem_erro(e)
        db.conn.rollback()


#itens de venda
def insert_produtos_vendas(id_venda, df_venda_produto):
    try:
        data_venda_produtos = [(id_venda, row[0], row[1]) for _, row in df_venda_produto.iterrows()]
        db.cursor.executemany(
            """
            INSERT INTO venda_produto (venda_ID_venda, produto_ID_produto, quantidade_produto_venda)
            VALUES (%s, %s, %s)
            """,
            data_venda_produtos
        )
        db.conn.commit()
        utils.mensagem_sucesso('Venda inserida')
    except db.erro as e:
        utils.mensagem_erro(e)
        db.conn.rollback()
        delete_vendas(id_venda)


#compras
def insert_compras(compra):
    try:
        db.cursor.execute(
            f"""
                INSERT INTO compra (fornecedor_ID_fornecedor, situacao_pagamento_compra, 
                situacao_entrega_compra, forma_pagamento_compra)
                VALUES ('{compra.fornecedor_id_fornecedor}', '{compra.situacao_pagamento_compra}', 
                '{compra.situacao_entrega_compra}', '{compra.forma_pagamento_compra}');
            """
        )
        db.conn.commit()
        db.cursor.execute(f'SELECT LASTVAL()')
        return db.cursor.fetchone()[0]
    except Exception as e:
        utils.mensagem_erro(e)
        db.conn.rollback()


#itens de compra
def insert_produtos_compras(id_compra, df_compra_produto):
    try:
        df_compra_produto = [(id_compra, row[0], row[1], row[2]) for _, row in df_compra_produto.iterrows()]
        db.cursor.executemany(
            """
            INSERT INTO compra_produto (compra_ID_compra, produto_ID_produto, preco_unitario_produto_compra, 
            quantidade_produto_compra)
            VALUES (%s, %s, %s, %s)
            """,
            df_compra_produto
        )
        db.conn.commit()
        utils.mensagem_sucesso('Compra inserida')
    except Exception as e:
        utils.mensagem_erro(e)
        db.conn.rollback()
        delete_compras(id_compra)


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
        utils.mensagem_sucesso('Fornecedor atualizado')
    except Exception as e:
        utils.mensagem_erro(e)
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
        utils.mensagem_sucesso('Produto atualizado')
    except Exception as e:
        utils.mensagem_erro(e)
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
        utils.mensagem_sucesso('Cliente atualizado')
    except Exception as e:
        utils.mensagem_erro(e)
        db.conn.rollback()
        

#compra
def update_compras(compra):
    try:
        db.cursor.execute(
            f"""
                UPDATE compra SET  
                    fornecedor_ID_fornecedor = '{compra.fornecedor_id_fornecedor}', 
                    forma_pagamento_compra = '{compra.forma_pagamento_compra}', 
                    situacao_pagamento_compra = '{compra.situacao_pagamento_compra}', 
                    situacao_entrega_compra  = '{compra.situacao_entrega_compra}'
                WHERE 
                    ID_compra = '{compra.id_compra}';
            """
        )
        db.conn.commit()
        utils.mensagem_sucesso('Compra atualizada')
    except Exception as e:
        utils.mensagem_erro(e)
        db.conn.rollback()
        

#itens de compra
def update_compras_produtos(compra_produto):
    try:
        db.cursor.execute(
            f"""
                UPDATE compra_produto SET  
                    produto_ID_produto = '{compra_produto.produto_id_produto}', 
                    preco_unitario_produto_compra = '{compra_produto.preco_unitario_produto_compra}', 
                    quantidade_produto_compra = '{compra_produto.quantidade_produto_compra}'
                WHERE 
                    ID_compra_produto = '{compra_produto.id_compra_produto}';
            """
        )
        db.conn.commit()
        utils.mensagem_sucesso('Item de compra atualizado')
    except Exception as e:
        utils.mensagem_erro(e)
        db.conn.rollback()
        

#venda
def update_vendas(venda):
    try:
        db.cursor.execute(
            f"""
                UPDATE venda SET 
                    cliente_ID_cliente = '{venda.cliente_id_cliente}', 
                    endereco_entrega_venda = '{venda.endereco_entrega_venda}', 
                    bairro_entrega_venda = '{venda.bairro_entrega_venda}', 
                    observacoes_venda = '{venda.observacoes_venda}', 
                    situacao_pagamento_venda  = '{venda.situacao_pagamento_venda}',
                    situacao_entrega_venda  = '{venda.situacao_entrega_venda}',
                    forma_pagamento_venda  = '{venda.forma_pagamento_venda}'
                WHERE 
                    ID_venda = '{venda.id_venda}';
            """
        )
        db.conn.commit()
        utils.mensagem_sucesso('Venda atualizada')
    except Exception as e:
        utils.mensagem_erro(e)
        db.conn.rollback()
        

#itens de venda
def update_vendas_produtos(venda_produto):
    try:
        db.cursor.execute(
            f"""
                UPDATE venda_produto SET 
                    produto_ID_produto = '{venda_produto.produto_id_produto}', 
                    preco_unitario_produto_venda = '{venda_produto.preco_unitario_produto_venda}', 
                    quantidade_produto_venda = '{venda_produto.quantidade_produto_venda}'
                WHERE 
                    ID_venda_produto = '{venda_produto.id_venda_produto}';
            """
        )
        db.conn.commit()
        utils.mensagem_sucesso('Item de venda atualizado')
    except Exception as e:
        utils.mensagem_erro(e)
        db.conn.rollback()


#deletes
#---------------------------------------------------------------
        
#compras
def delete_compras(id_compra):
    try:
        db.cursor.execute(
            f"""
                DELETE FROM compra WHERE ID_compra = {id_compra};
            """
        )
        db.conn.commit()
        utils.mensagem_sucesso('Compra excluída')
    except Exception as e:
        utils.mensagem_erro(e)
        db.conn.rollback()


#itens de compra
def delete_compras_produtos(id_compra_produto):
    try:
        db.cursor.execute(
            f"""
                DELETE FROM compra_produto WHERE ID_compra_produto = {id_compra_produto};
            """
        )
        db.conn.commit()
        utils.mensagem_sucesso('Item de compra excluído')
    except Exception as e:
        utils.mensagem_erro(e)
        db.conn.rollback()


#vendas
def delete_vendas(id_venda):
    try:
        db.cursor.execute(
            f"""
                DELETE FROM venda WHERE ID_venda = {id_venda};
            """
        )
        db.conn.commit()
        utils.mensagem_sucesso('Venda excluída')
    except Exception as e:
        utils.mensagem_erro(e)
        db.conn.rollback()


#itens de venda
def delete_vendas_produtos(id_venda_produto):
    try:
        db.cursor.execute(
            f"""
                DELETE FROM venda_produto WHERE ID_venda_produto = {id_venda_produto};
            """
        )
        db.conn.commit()
        utils.mensagem_sucesso('Item de venda excluído')
    except Exception as e:
        utils.mensagem_erro(e)
        db.conn.rollback()