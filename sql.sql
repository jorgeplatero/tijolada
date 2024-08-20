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
    nome_produto VARCHAR(30) UNIQUE NOT NULL,
    unidade_medida_produto VARCHAR(10)
);

--compra
CREATE TABLE compra (
    ID_compra SERIAL PRIMARY KEY,
    data_compra DATE NOT NULL,
    fornecedor_ID_fornecedor INTEGER REFERENCES fornecedor (ID_fornecedor) ON UPDATE CASCADE,
    preco_total_compra MONEY,
    forma_pagamento_compra VARCHAR(50),
    situacao_pagamento_compra BOOLEAN DEFAULT TRUE,
    situacao_entrega_compra BOOLEAN DEFAULT TRUE
);

CREATE TABLE compra_produto (
    ID_compra_produto SERIAL PRIMARY KEY,
    compra_ID_compra INTEGER REFERENCES compra (ID_compra) ON UPDATE CASCADE,
    produto_ID_produto INTEGER REFERENCES produto (ID_produto) ON UPDATE CASCADE,
    preco_unitario_produto_compra MONEY NOT NULL,
    quantidade_produto_compra REAL NOT NULL,
    desconto_produto_compra MONEY DEFAULT 0
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
	tipo_cliente BOOLEAN,
    cpf_cnpj_cliente VARCHAR(18) UNIQUE NOT NULL,
    endereco_cliente VARCHAR(100),
    bairro_cliente VARCHAR(50),
	telefone_cliente VARCHAR(15),
	referencia_cliente VARCHAR(255),
	situacao_cliente VARCHAR(15)
);

--venda
CREATE TABLE venda (
    ID_venda SERIAL PRIMARY KEY,
	data_venda DATE,
    cliente_ID_cliente INTEGER REFERENCES cliente (ID_cliente) ON UPDATE CASCADE,
    endereco_entrega_venda VARCHAR(100),
    bairro_entrega_venda VARCHAR(50),
    observacoes_venda VARCHAR(255),
    preco_total_venda MONEY,
    situacao_pagamento_venda BOOLEAN DEFAULT TRUE,
    situacao_entrega_venda BOOLEAN DEFAULT TRUE,
    forma_pagamento_venda VARCHAR(50)
);

CREATE TABLE venda_produto (
    ID_venda_produto SERIAL PRIMARY KEY,
    venda_ID_venda INTEGER REFERENCES venda (ID_venda) ON UPDATE CASCADE,
    produto_ID_produto INTEGER REFERENCES produto (ID_produto) ON UPDATE CASCADE,
    preco_unitario_produto_venda MONEY NOT NULL,
    quantidade_produto_venda REAL NOT NULL,
    desconto_produto_venda MONEY DEFAULT 0
);

--tabelas dimensão
CREATE TABLE dim_tipo_cliente (
    ID_tipo_cliente INTEGER PRIMARY KEY,
    descricao_tipo_cliente VARCHAR(15) NOT NULL
);

CREATE TABLE dim_situacao_pagamento_venda (
    ID_situacao_pagamento_venda INTEGER PRIMARY KEY,
    descricao_situacao_pagamento_venda VARCHAR(15) NOT NULL
);

CREATE TABLE dim_situacao_entrega_venda (
    ID_situacao_entrega_venda INTEGER PRIMARY KEY,
    descricao_situacao_entrega_venda VARCHAR(15) NOT NULL
);

CREATE TABLE dim_situacao_pagamento_compra (
    ID_situacao_pagamento_compra INTEGER PRIMARY KEY,
    descricao_situacao_pagamento_compra VARCHAR(15) NOT NULL
);

CREATE TABLE dim_situacao_entrega_compra (
    ID_situacao_entrega_compra INTEGER PRIMARY KEY,
    descricao_situacao_entrega_compra VARCHAR(15) NOT NULL
);

CREATE TABLE dim_situacao_cliente (
    ID_situacao_cliente INTEGER PRIMARY KEY,
    descricao_situacao_cliente VARCHAR(15) NOT NULL
);


--inserts tabelas dimensão
INSERT INTO dim_tipo_cliente (ID_tipo_cliente, descricao_tipo_cliente) VALUES
(0, 'Pessoa jurídica'),
(1, 'Pessoa física');

INSERT INTO dim_situacao_pagamento_venda (ID_situacao_pagamento_venda, descricao_situacao_pagamento_venda) VALUES
(0, 'Não realizada'),
(1, 'Realizada');

INSERT INTO dim_situacao_entrega_venda (ID_situacao_entrega_venda, descricao_situacao_entrega_venda) VALUES
(0, 'Não realizada'),
(1, 'Realizada');

INSERT INTO dim_situacao_pagamento_compra (ID_situacao_pagamento_compra, descricao_situacao_pagamento_compra) VALUES
(0, 'Não realizada'),
(1, 'Realizada');

INSERT INTO dim_situacao_entrega_compra (ID_situacao_entrega_compra, descricao_situacao_entrega_compra) VALUES
(0, 'Não realizada'),
(1, 'Realizada');

INSERT INTO dim_situacao_cliente (ID_situacao_cliente, descricao_situacao_cliente) VALUES
(0, 'Inadimplente '),
(1, 'Adimplente');

--triggers

--trigger para atualizar quantidade total de uma venda
CREATE OR REPLACE FUNCTION calcular_preco_total_venda()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE venda SET preco_total_venda = (
        SELECT SUM(p.preco_unitario_produto_venda * vp.quantidade_produto_venda)
        FROM venda_produto vp
        JOIN produto p ON vp.produto_ID_produto = p.ID_produto
        WHERE vp.venda_ID_venda = NEW.ID_venda
    );
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER calcular_preco_total_trigger
AFTER INSERT OR UPDATE OR DELETE ON venda_produto
FOR EACH ROW EXECUTE PROCEDURE calcular_preco_total_venda();

--trigger para atualizar quantidade total de uma compra
CREATE OR REPLACE FUNCTION calcular_preco_total_compra()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE compra SET preco_total_compra = (
        SELECT SUM(p.preco_unitario_produto_compra * cp.quantidade_produto_compra)
        FROM compra_produto cp
        JOIN produto p ON cp.produto_ID_produto = p.ID_produto
        WHERE cp.venda_ID_venda = NEW.ID_venda
    );
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER calcular_preco_total_trigger
AFTER INSERT OR UPDATE OR DELETE ON compra_produto
FOR EACH ROW EXECUTE PROCEDURE calcular_preco_total_compra();

--trigger para atualizar o estoque após uma compra
CREATE OR REPLACE FUNCTION atualizar_estoque_compra()
RETURNS TRIGGER AS $$
BEGIN
    --decrementa a quantidade em estoque para cada produto comprado
    UPDATE estoque
    SET quantidade_estoque = quantidade_estoque + NEW.quantidade_produto_compra
    WHERE produto_ID_produto = NEW.produto_ID_produto;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_compra_produto_estoque
AFTER INSERT OR UPDATE ON compra_produto
FOR EACH ROW
EXECUTE PROCEDURE atualizar_estoque_compra();

--trigger para atualizar o estoque após uma venda
CREATE OR REPLACE FUNCTION atualizar_estoque_venda()
RETURNS TRIGGER AS $$
BEGIN
    --decrementa a quantidade em estoque para cada produto vendido
    UPDATE estoque
    SET quantidade_estoque = quantidade_estoque - NEW.quantidade_produto_venda
    WHERE produto_ID_produto = NEW.produto_ID_produto;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_venda_produto_estoque
AFTER INSERT OR UPDATE ON venda_produto
FOR EACH ROW
EXECUTE PROCEDURE atualizar_estoque_venda();