--tabelas

--fornecedor
CREATE TABLE fornecedor (
    ID_fornecedor SERIAL PRIMARY KEY,
    nome_fornecedor VARCHAR(100) UNIQUE NOT NULL,
    cnpj_fornecedor VARCHAR(18) UNIQUE NOT NULL,
    endereco_fornecedor VARCHAR(100),
    bairro_fornecedor VARCHAR(50),
    telefone_fornecedor VARCHAR(15)
);

--produto
CREATE TABLE produto (
    ID_produto SERIAL PRIMARY KEY,
    nome_produto VARCHAR(255) UNIQUE NOT NULL,
    unidade_medida_produto VARCHAR(10)
);

--compra
CREATE TABLE compra (
    ID_compra SERIAL PRIMARY KEY,
    data_compra TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    fornecedor_ID_fornecedor INTEGER REFERENCES fornecedor (ID_fornecedor) ON UPDATE CASCADE,
    preco_total_compra DECIMAL,
    situacao_pagamento_compra VARCHAR(50),
    situacao_entrega_compra VARCHAR(50),
    forma_pagamento_compra VARCHAR(50)
);

CREATE TABLE compra_produto (
    ID_compra_produto SERIAL PRIMARY KEY,
    compra_ID_compra INTEGER REFERENCES compra (ID_compra) ON UPDATE CASCADE,
    produto_ID_produto INTEGER REFERENCES produto (ID_produto) ON UPDATE CASCADE,
    preco_unitario_produto_compra DECIMAL NOT NULL,
    quantidade_produto_compra REAL NOT NULL
);

--estoque
CREATE TABLE estoque (
    ID_estoque SERIAL PRIMARY KEY,
    produto_ID_produto INTEGER REFERENCES produto (ID_produto) ON UPDATE CASCADE,
    quantidade_estoque REAL NOT NULL
);

--cliente
CREATE TABLE cliente (
    ID_cliente SERIAL PRIMARY KEY,
    nome_cliente VARCHAR(100) UNIQUE NOT NULL,
	tipo_cliente VARCHAR(50),
    cpf_cnpj_cliente VARCHAR(18) UNIQUE NOT NULL,
    endereco_cliente VARCHAR(100),
    bairro_cliente VARCHAR(50),
	telefone_cliente VARCHAR(15),
	referencia_cliente VARCHAR(255),
	situacao_cliente VARCHAR(50)
);

--venda
CREATE TABLE venda (
    ID_venda SERIAL PRIMARY KEY,
	data_venda TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
    cliente_ID_cliente INTEGER REFERENCES cliente (ID_cliente) ON UPDATE CASCADE,
    endereco_entrega_venda VARCHAR(100),
    bairro_entrega_venda VARCHAR(50),
    observacoes_venda VARCHAR(255),
    preco_total_venda DECIMAL,
    situacao_pagamento_venda VARCHAR(50),
    situacao_entrega_venda VARCHAR(50),
    forma_pagamento_venda VARCHAR(50)
);

CREATE TABLE venda_produto (
    ID_venda_produto SERIAL PRIMARY KEY,
    venda_ID_venda INTEGER REFERENCES venda (ID_venda) ON UPDATE CASCADE,
    produto_ID_produto INTEGER REFERENCES produto (ID_produto) ON UPDATE CASCADE,
    preco_unitario_produto_venda DECIMAL,
    quantidade_produto_venda REAL NOT NULL
);