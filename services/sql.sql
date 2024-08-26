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
    data_compra DATE DEFAULT CURRENT_DATE,
    fornecedor_ID_fornecedor INTEGER REFERENCES fornecedor (ID_fornecedor) ON UPDATE CASCADE,
    preco_total_compra MONEY,
    forma_pagamento_compra VARCHAR(50),
    situacao_pagamento_compra VARCHAR(50),
    situacao_entrega_compra VARCHAR(50)
);

CREATE TABLE compra_produto (
    ID_compra_produto SERIAL PRIMARY KEY,
    compra_ID_compra INTEGER REFERENCES compra (ID_compra) ON UPDATE CASCADE,
    produto_ID_produto INTEGER REFERENCES produto (ID_produto) ON UPDATE CASCADE,
    preco_unitario_produto_compra MONEY NOT NULL,
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
	data_venda DATE DEFAULT CURRENT_DATE,
    cliente_ID_cliente INTEGER REFERENCES cliente (ID_cliente) ON UPDATE CASCADE,
    endereco_entrega_venda VARCHAR(100),
    bairro_entrega_venda VARCHAR(50),
    observacoes_venda VARCHAR(255),
    preco_total_venda MONEY,
    situacao_pagamento_venda VARCHAR(50),
    situacao_entrega_venda VARCHAR(50),
    forma_pagamento_venda VARCHAR(50)
);

CREATE TABLE venda_produto (
    ID_venda_produto SERIAL PRIMARY KEY,
    venda_ID_venda INTEGER REFERENCES venda (ID_venda) ON UPDATE CASCADE,
    produto_ID_produto INTEGER REFERENCES produto (ID_produto) ON UPDATE CASCADE,
    preco_unitario_produto_venda MONEY,
    quantidade_produto_venda REAL NOT NULL
);

--triggers

--venda

--trigger para atualizar preço total de uma venda
CREATE OR REPLACE FUNCTION calcular_preco_total_venda()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE venda SET preco_total_venda = (
        SELECT SUM(vp.preco_unitario_produto_venda * vp.quantidade_produto_venda)
        FROM venda_produto vp
        WHERE vp.venda_ID_venda = NEW.venda_ID_venda
    )
    WHERE ID_venda = NEW.venda_ID_venda;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER trg_calcular_preco_total_venda
AFTER INSERT OR UPDATE OR DELETE ON venda_produto
FOR EACH ROW EXECUTE PROCEDURE calcular_preco_total_venda();

--compra

--trigger para atualizar preço total de uma compra
CREATE OR REPLACE FUNCTION calcular_preco_total_compra()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE compra SET preco_total_compra = (
        SELECT SUM(cp.preco_unitario_produto_compra * cp.quantidade_produto_compra)
        FROM compra_produto cp
        WHERE cp.compra_ID_compra = NEW.compra_ID_compra
    )
    WHERE ID_compra = NEW.compra_ID_compra;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER trg_calcular_preco_total_compra
AFTER INSERT OR UPDATE OR DELETE ON compra_produto
FOR EACH ROW EXECUTE PROCEDURE calcular_preco_total_compra();

--estoque

--trigger para inserir um novo produto no estoque após uma compra inédita
CREATE OR REPLACE FUNCTION atualizar_estoque_compra()
RETURNS TRIGGER AS $$
BEGIN
    -- Verifica se o produto já existe no estoque
    IF EXISTS (SELECT 1 FROM estoque WHERE produto_ID_produto = NEW.produto_ID_produto) THEN
        -- Atualiza a quantidade em estoque
        UPDATE estoque
        SET quantidade_estoque = quantidade_estoque + NEW.quantidade_produto_compra
        WHERE produto_ID_produto = NEW.produto_ID_produto;
    ELSE
        -- Insere um novo registro no estoque
        INSERT INTO estoque (produto_ID_produto, quantidade_estoque)
        VALUES (NEW.produto_ID_produto, NEW.quantidade_produto_compra);
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER atualizar_estoque_compra
AFTER INSERT ON compra_produto
FOR EACH ROW
EXECUTE FUNCTION atualizar_estoque_compra();

--trigger para atualizar o estoque após uma venda
CREATE OR REPLACE FUNCTION atualizar_estoque_venda() RETURNS TRIGGER AS $$
BEGIN
    -- Verifica se a nova quantidade em estoque não ficará negativa
    IF (SELECT quantidade_estoque FROM estoque WHERE produto_ID_produto = NEW.produto_ID_produto) - NEW.quantidade_produto_venda < 0 THEN
        RAISE EXCEPTION 'Quantidade em estoque insuficiente!';
    END IF;

    -- Atualiza a quantidade em estoque
    UPDATE estoque
    SET quantidade_estoque = quantidade_estoque - NEW.quantidade_produto_venda
    WHERE produto_ID_produto = NEW.produto_ID_produto;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER atualizar_estoque_venda
AFTER INSERT ON venda_produto
FOR EACH ROW
EXECUTE FUNCTION atualizar_estoque_venda();