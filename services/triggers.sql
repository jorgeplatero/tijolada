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

--trigger para atualizar o preço unitário do produto em uma venda
CREATE OR REPLACE FUNCTION calcular_preco_unitario_venda()
RETURNS TRIGGER AS $$
BEGIN
    -- Calcula o preço unitário de venda com 20% de markup
    NEW.preco_unitario_produto_venda := (
        SELECT cp.preco_unitario_produto_compra * 1.20
        FROM compra_produto cp
        JOIN compra c ON cp.compra_ID_compra = c.ID_compra
        WHERE cp.produto_ID_produto = NEW.produto_ID_produto
        ORDER BY c.data_compra DESC
        LIMIT 1
    );
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER trg_atualizar_preco_unitario_venda
BEFORE INSERT ON venda_produto
FOR EACH ROW
EXECUTE PROCEDURE calcular_preco_unitario_venda();

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

CREATE OR REPLACE TRIGGER trg_atualizar_estoque_compra
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

CREATE OR REPLACE TRIGGER trg_atualizar_estoque_venda
AFTER INSERT ON venda_produto
FOR EACH ROW
EXECUTE FUNCTION atualizar_estoque_venda();