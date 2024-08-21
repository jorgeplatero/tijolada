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