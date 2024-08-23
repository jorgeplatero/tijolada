class Cliente:
    def __init__(
            self, id_cliente, nome_cliente, tipo_cliente, cpf_cnpj_cliente, endereco_cliente,
            bairro_cliente, telefone_cliente, referencia_cliente, situacao_cliente
        ):
        self.id_cliente = id_cliente
        self.nome_cliente = nome_cliente
        self.tipo_cliente = tipo_cliente
        self.cpf_cnpj_cliente = cpf_cnpj_cliente
        self.endereco_cliente = endereco_cliente
        self.bairro_cliente = bairro_cliente
        self.telefone_cliente = telefone_cliente
        self.referencia_cliente = referencia_cliente
        self.situacao_cliente = situacao_cliente


class Fornecedor:
    def __init__(
            self, id_fornecedor, nome_fornecedor, cnpj_fornecedor, endereco_fornecedor, 
            bairro_fornecedor, telefone_fornecedor
        ):
        self.id_fornecedor = id_fornecedor
        self.nome_fornecedor = nome_fornecedor
        self.cnpj_fornecedor = cnpj_fornecedor
        self.endereco_fornecedor = endereco_fornecedor
        self.bairro_fornecedor = bairro_fornecedor
        self.telefone_fornecedor = telefone_fornecedor


class Produto:
    def __init__(
            self, id_produto, nome_produto, unidade_medida_produto
        ):
        self.id_produto = id_produto
        self.nome_produto = nome_produto
        self.unidade_medida_produto = unidade_medida_produto
        

class Estoque:
    def __init__(
            self, id_estoque, produto_id_produto, quantidade_estoque
        ):
        self.id_estoque = id_estoque
        self.produto_id_produto = produto_id_produto
        self.quantidade_estoque = quantidade_estoque

class Compra:
    def __init__(
            self, id_compra, data_compra, fornecedor_id_fornecedor, produto_id_produto, preco_total_compra, 
            situacao_pagamento_compra, situacao_entrega_compra, forma_pagamento_compra
        ):
        self.id_compra = id_compra
        self.data_compra = data_compra
        self.fornecedor_id_fornecedor = fornecedor_id_fornecedor
        self.produto_id_produto = produto_id_produto
        self.preco_total_compra = preco_total_compra
        self.situacao_pagamento_compra = situacao_pagamento_compra
        self.situacao_entrega_compra = situacao_entrega_compra
        self.forma_pagamento_compra = forma_pagamento_compra
        

class CompraProduto:
    def __init__(
            self, id_compra_produto, compra_id_compra, produto_id_produto, preco_unitario_produto_compra, 
            quantidade_produto_compra
        ):
        self.id_compra_produto = id_compra_produto
        self.compra_id_compra = compra_id_compra
        self.produto_id_produto = produto_id_produto
        self.preco_unitario_produto_compra = preco_unitario_produto_compra
        self.quantidade_produto_compra = quantidade_produto_compra
        
class Venda:
    def __init__(
            self, id_venda, data_venda, cliente_id_cliente, endereco_entrega_venda, 
            bairro_entrega_venda, observacoes_venda, preco_total_venda, situacao_pagamento_venda,
            situacao_entrega_venda, forma_pagamento_venda
        ):
        self.id_venda = id_venda
        self.data_venda = data_venda
        self.cliente_id_cliente = cliente_id_cliente
        self.endereco_entrega_venda = endereco_entrega_venda
        self.bairro_entrega_venda = bairro_entrega_venda
        self.observacoes_venda = observacoes_venda
        self.preco_total_venda = preco_total_venda
        self.situacao_pagamento_venda = situacao_pagamento_venda
        self.situacao_entrega_venda = situacao_entrega_venda
        self.forma_pagamento_venda = forma_pagamento_venda
        

class VendaProduto:
    def __init__(
            self, id_venda_produto, venda_id_venda, produto_id_produto, 
            preco_unitario_produto_venda, quantidade_produto_venda
        ):
        self.id_venda_produto = id_venda_produto
        self.venda_id_venda = venda_id_venda
        self.produto_id_produto = produto_id_produto
        self.preco_unitario_produto_venda = preco_unitario_produto_venda
        self.quantidade_produto_venda = quantidade_produto_venda