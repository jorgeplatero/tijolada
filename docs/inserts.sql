--fornecedores
----------------------------------------------------------------
INSERT INTO fornecedor 
    (nome_fornecedor, cnpj_fornecedor, endereco_fornecedor, bairro_fornecedor, telefone_fornecedor)
VALUES 
    ('Cimentos São Paulo', '12.345.678/0001-90', 'Avenida Brasil, 123', 'Centro', '(11) 9999-9999'),
    ('Tintas Colorarte', '23.456.789/0001-00', 'Rua das Flores, 456', 'Jardim das Flores', '(11) 8888-8888'),
    ('Madeiras do Vale', '34.567.890/0001-10', 'Rua dos Pinheiros, 789', 'Vila Leopoldina', '(11) 7777-7777'),
    ('Telhas do Brasil', '45.678.901/0001-20', 'Avenida dos Estados, 1011', 'Mooca', '(11) 6666-6666'),
    ('Ferramentas Ideal', '56.789.012/0001-30', 'Rua da Liberdade, 1213', 'Liberdade', '(11) 5555-5555'),
    ('Elétrica Silva', '67.890.123/0001-40', 'Rua da Paz, 1415', 'Vila Mariana', '(11) 4444-4444'),
    ('Tubos e Canos S.A.', '78.901.234/0001-50', 'Avenida Paulista, 1617', 'Consolação', '(11) 3333-3333'),
    ('Gesso e Divisórias LTDA', '89.012.345/0001-60', 'Rua da Independência, 1819', 'Ipiranga', '(11) 2222-2222'),
    ('Vidros & Espelhos', '90.123.456/0001-70', 'Avenida Rio Branco, 2021', 'Centro', '(11) 1111-1111'),
    ('Pedras e Granitos Brasil', '01.234.567/0001-80', 'Rua do Comércio, 2223', 'Sé', '(11) 0000-0123'),
    ('Tijolos S.A.', '04.334.571/0001-73', 'Rua do Sol, 123', 'Brás', '(11) 0000-0000'),
    ('Revestimentos Nova Fronteira', '10.201.545/0001-01', 'Rua da Lua, 243', 'Guilhermina', '(11) 1248-0000');

--produtos
----------------------------------------------------------------
INSERT INTO produto (nome_produto, unidade_medida_produto) 
VALUES
    ('Pedra para Pavimentação', 'm²'),
    ('Tijolo Ecológico', 'un'),
    ('Caixa d´água', 'l'),
    ('Torneira', 'un'),
    ('Pia', 'un'),
    ('Vasos Sanitários', 'un'),
    ('Ralo', 'un'),
    ('Tinta Epóxi', 'lata'),
    ('Verniz', 'lata'),
    ('Cola para Madeira', 'kg'),
    ('Massa para Juntas', 'kg'),
    ('Selante', 'un'),
    ('Esquadria de Alumínio', 'm²'),
    ('Porta de Madeira', 'un'),
    ('Janela de Madeira', 'un'),
    ('Tinta para Madeira', 'lata'),
    ('Manta Térmica', 'm²'),
    ('Isolamento Acústico', 'm²'),
    ('Fita Veda Frio', 'm'),
    ('Cimento Cola', 'kg'),
    ('Rejunte', 'kg'),
    ('Escada de Alumínio', 'un'),
    ('Andaime', 'un'),
    ('Betoneira', 'un'),
    ('Carrinho de Mão', 'un'),
    ('Serra Circular', 'un'),
    ('Furadeira', 'un'),
    ('Lixadeira', 'un'),
    ('Chave de Fenda', 'un'),
    ('Chave de Boca', 'un'),
    ('Alicate', 'un'),
    ('Martelo', 'un'),
    ('Nível', 'un'),
    ('Trena', 'un'),
    ('Mangueira', 'm'),
    ('Conexão para Mangueira', 'un'),
    ('Bomba d´água', 'un'),
    ('Caixa de Luz', 'un'),
    ('Disjuntor', 'un'),
    ('Fio de Cobre', 'm'),
    ('Fio de Alumínio', 'm'),
    ('Luminária', 'un'),
    ('Chuveiro', 'un'),
    ('Torneira para Banheiro', 'un'),
    ('Torneira para Cozinha', 'un'),
    ('Caixa de Gordura', 'un'),
    ('Sifão', 'un'),
    ('Registro de Água', 'un'),
    ('Caixa de Passagem', 'un'),
    ('Ducha', 'un'),
    ('Caixa de Correio', 'un'),
    ('Cerca de Arame', 'm'),
    ('Cerca de Tela', 'm'),
    ('Portão de Alumínio', 'un'),
    ('Portão de Ferro', 'un'),
    ('Grade de Proteção', 'm'),
    ('Piso de Madeira', 'm²'),
    ('Piso de Vinil', 'm²'),
    ('Piso Laminado', 'm²'),
    ('Tapete', 'm²'),
    ('Cortina', 'm²'),
    ('Rodapé', 'm'),
    ('Moldura', 'm'),
    ('Varanda', 'm²'),
    ('Tijolo de Vidro', 'un'),
    ('Massa para Reboco', 'kg'),
    ('Massa para Assentamento', 'kg'),
    ('Cola para Azulejo', 'kg');

--clientes
----------------------------------------------------------------
INSERT INTO 
    cliente (nome_cliente, tipo_cliente, cpf_cnpj_cliente, endereco_cliente, bairro_cliente, telefone_cliente, referencia_cliente, situacao_cliente)
VALUES 
    ('João da Silva', 'Pessoa Física', '123.456.789-10', 'Rua A, 123', 'Centro', '(11) 9999-9999', 'Ao lado do monotrilho', 'Adimplente'),
    ('Construtora Alpha', 'Pessoa Jurídica', '12.345.678/0001-90', 'Avenida B, 456', 'Jardim', '(11) 8888-8888', 'Em frente ao banco', 'Adimplente'),
    ('Maria Souza', 'Pessoa Física', '987.654.321-20', 'Rua C, 789', 'Vila', '(11) 7777-7777', 'Em frente ao posto de combustível', 'Adimplente'),
    ('Arquitetura & Design', 'Pessoa Jurídica', '23.456.789/0001-00', 'Avenida D, 1011', 'Centro', '(11) 6666-6666', 'Ao lado do shopping', 'Adimplente'),
    ('Pedro Oliveira', 'Pessoa Física', '111.222.333-44', 'Rua E, 1213', 'Vila', '(11) 5555-5555', 'Em frente ao mercado', 'Inadimplente'),
    ('Decor & Design', 'Pessoa Jurídica', '34.567.890/0001-10', 'Avenida F, 1415', 'Jardim', '(11) 4444-4444', 'Esquina com a Avenida E', 'Adimplente'),
    ('Ana Santos', 'Pessoa Física', '789.456.123-50', 'Rua G, 1617', 'Centro', '(11) 3333-3333', 'Em frente à praça', 'Adimplente'),
    ('Manutenção Ideal', 'Pessoa Jurídica', '45.678.901/0001-20', 'Avenida H, 1819', 'Vila', '(11) 2222-2222', 'Portão azul', 'Adimplente'),
    ('Carlos Silva', 'Pessoa Física', '901.234.567-60', 'Rua I, 2021', 'Centro', '(11) 1111-1111', 'Muro laranja', 'Inadimplente'),
    ('Reform & Design', 'Pessoa Jurídica', '56.789.012/0001-30', 'Avenida J, 2223', 'Jardim', '(11) 0000-0000', 'Em frente à delegacia', 'Adimplente'),
    ('Bruna Pereira', 'Pessoa Física', '456.789.012-34', 'Rua K, 1234', 'Vila', '(11) 9876-5432', 'Casa verde', 'Adimplente'),
    ('Construções Silva', 'Pessoa Jurídica', '56.789.012/0001-40', 'Avenida L, 1456', 'Centro', '(11) 7654-3210', 'Ao lado do terminal B', 'Adimplente'),
    ('Ricardo Santos', 'Pessoa Física', '101.101.101-11', 'Rua M, 1678', 'Vila', '(11) 8765-4321', 'Rua da padaria', 'Adimplente'),
    ('Jardim & Paisagem', 'Pessoa Jurídica', '67.890.123/0001-50', 'Avenida N, 1890', 'Jardim', '(11) 9876-5432', 'Próximo ao bicicletário', 'Adimplente'),
    ('Fernanda Oliveira', 'Pessoa Física', '202.202.202-22', 'Rua O, 2012', 'Vila', '(11) 8765-4321', 'Portão cinza', 'Adimplente'),
    ('Gabriel Costa', 'Pessoa Física', '303.303.303-33', 'Rua Q, 2456', 'Vila', '(11) 7654-3210', 'Vizinho ao mercadinho A', 'Inadimplente'),
    ('Laura Silva', 'Pessoa Física', '404.404.404-44', 'Rua S, 2890', 'Vila', '(11) 9876-5432', 'Casa da esquina', 'Adimplente'),
    ('Caio Reformas & Manutenção', 'Pessoa Jurídica', '90.123.456/0001-80', 'Avenida T, 3012', 'Centro', '(11) 7654-3210', 'Portão baixo', 'Adimplente'),
    ('Rosana Cardozo', 'Pessoa Física', '123.456.789.12', 'Rua Reino Encantado, 666', 'Vila dos Sete Anões', '(11) 92345-6789', 'Ao lado da casa do Zangão', 'Adimplente'),
    ('Maroca Paper', 'Pessoa Jurídica', '44.848.013/0001-90', 'Avenida Reino Encantado, 666', 'Vila da Rainha Má', '(11) 2345-6789', 'De frente para a macieira', 'Inadimplente');

--compras
----------------------------------------------------------------
INSERT INTO compra (fornecedor_ID_fornecedor, situacao_pagamento_compra, situacao_entrega_compra, forma_pagamento_compra, data_compra) 
VALUES
    (1, 'Não realizado', 'Não realizada', 'Crédito', '2023-01-15 10:30:00'),
    (2, 'Realizado', 'Realizada', 'Débito', '2023-02-28 15:45:00'),
    (3, 'Não realizado', 'Realizada', 'Dinheiro', '2023-03-10 18:12:00'),
    (4, 'Realizado', 'Não realizada', 'PIX', '2023-04-05 09:00:00'),
    (5, 'Realizado', 'Realizada', 'Crédito', '2023-05-20 11:35:00'),
    (6, 'Não realizado', 'Não realizada', 'Débito', '2023-06-12 17:20:00'),
    (7, 'Realizado', 'Realizada', 'Dinheiro', '2023-07-08 13:50:00'),
    (8, 'Não realizado', 'Não realizada', 'PIX', '2023-08-25 20:05:00'),
    (9, 'Realizado', 'Realizada', 'Crédito', '2023-09-18 08:40:00'),
    (10, 'Não realizado', 'Não realizada', 'Débito', '2023-10-03 16:22:00'),
    (11, 'Realizado', 'Realizada', 'Dinheiro', '2023-11-16 19:10:00'),
    (12, 'Não realizado', 'Não realizada', 'PIX', '2023-12-01 12:00:00'),
    (1, 'Realizado', 'Realizada', 'Crédito', '2024-01-09 14:55:00'),
    (2, 'Não realizado', 'Não realizada', 'Débito', '2024-02-14 07:30:00'),
    (3, 'Realizado', 'Não realizada', 'Dinheiro', '2024-03-05 21:15:00'),
    (4, 'Não realizado', 'Realizada', 'PIX', '2024-04-22 10:48:00'),
    (5, 'Não realizado', 'Não realizada', 'Crédito', '2024-05-08 12:20:00'),
    (6, 'Realizado', 'Realizada', 'Débito', '2024-06-29 18:00:00'),
    (7, 'Não realizado', 'Não realizada', 'Dinheiro', '2024-07-17 15:35:00'),
    (8, 'Realizado', 'Realizada', 'PIX', '2024-08-03 09:50:00'),
    (9, 'Realizado', 'Não realizada', 'Crédito', '2024-09-11 13:10:00'),
    (10, 'Não realizado', 'Realizada', 'Débito', '2024-10-27 16:45:00'),
    (11, 'Não realizado', 'Não realizada', 'Dinheiro', '2024-11-13 11:25:00'),
    (12, 'Realizado', 'Realizada', 'PIX', '2024-12-05 19:00:00'),
    (1, 'Não realizado', 'Não realizada', 'Crédito', '2023-01-22 08:15:00'),
    (2, 'Realizado', 'Realizada', 'Débito', '2023-02-11 17:05:00'),
    (3, 'Não realizado', 'Realizada', 'Dinheiro', '2023-03-28 12:30:00'),
    (4, 'Realizado', 'Não realizada', 'PIX', '2023-04-18 14:40:00'),
    (5, 'Realizado', 'Realizada', 'Crédito', '2023-05-06 20:25:00'),
    (6, 'Não realizado', 'Não realizada', 'Débito', '2023-06-25 10:10:00'),
    (7, 'Realizado', 'Realizada', 'Dinheiro', '2023-07-14 16:55:00'),
    (8, 'Não realizado', 'Não realizada', 'PIX', '2023-08-09 13:30:00'),
    (9, 'Realizado', 'Realizada', 'Crédito', '2023-09-02 09:20:00'),
    (10, 'Não realizado', 'Não realizada', 'Débito', '2023-10-19 18:10:00'),
    (11, 'Realizado', 'Realizada', 'Dinheiro', '2023-11-07 15:00:00'),
    (12, 'Não realizado', 'Não realizada', 'PIX', '2023-12-24 22:45:00'),
    (1, 'Realizado', 'Realizada', 'Crédito', '2024-01-01 00:01:00'),
    (2, 'Não realizado', 'Não realizada', 'Débito', '2024-02-05 12:55:00'),
    (3, 'Realizado', 'Não realizada', 'Dinheiro', '2024-03-20 10:30:00'),
    (4, 'Não realizado', 'Realizada', 'PIX', '2024-04-10 16:15:00'),
    (5, 'Não realizado', 'Não realizada', 'Crédito', '2024-05-26 14:00:00'),
    (6, 'Realizado', 'Realizada', 'Débito', '2024-06-16 19:30:00'),
    (7, 'Não realizado', 'Não realizada', 'Dinheiro', '2024-07-04 17:20:00'),
    (8, 'Realizado', 'Realizada', 'PIX', '2024-08-21 11:55:00'),
    (9, 'Realizado', 'Não realizada', 'Crédito', '2024-09-08 15:45:00'),
    (10, 'Não realizado', 'Realizada', 'Débito', '2024-10-23 20:00:00'),
    (11, 'Não realizado', 'Não realizada', 'Dinheiro', '2024-11-10 13:10:00'),
    (12, 'Realizado', 'Realizada', 'PIX', '2024-12-17 18:30:00');

--itens de compra
----------------------------------------------------------------
INSERT INTO compra_produto (compra_ID_compra, produto_ID_produto, preco_unitario_produto_compra, quantidade_produto_compra) 
VALUES
    (1, 3, 10.99, 120),
    (2, 15, 15.99, 100),
    (3, 27, 20.99, 80),
    (4, 41, 25.99, 150),
    (5, 53, 30.99, 180),
    (6, 65, 35.99, 160),
    (7, 8, 40.99, 90),
    (8, 20, 45.99, 140),
    (9, 32, 50.99, 130),
    (10, 44, 55.99, 70),
    (11, 56, 60.99, 110),
    (12, 68, 65.99, 170),
    (13, 1, 70.99, 190),
    (14, 13, 75.99, 100),
    (15, 25, 80.99, 80),
    (16, 37, 85.99, 120),
    (17, 49, 90.99, 160),
    (18, 61, 95.99, 140),
    (19, 2, 100.99, 180),
    (20, 14, 105.99, 130),
    (21, 26, 110.99, 70),
    (22, 38, 115.99, 110),
    (23, 50, 120.99, 150),
    (24, 62, 125.99, 190),
    (25, 4, 130.99, 170),
    (26, 16, 135.99, 90),
    (27, 28, 140.99, 100),
    (28, 40, 145.99, 120),
    (29, 52, 150.99, 160),
    (30, 64, 155.99, 180),
    (31, 6, 160.99, 110),
    (32, 18, 165.99, 80),
    (33, 30, 170.99, 130),
    (34, 42, 175.99, 140),
    (35, 54, 180.99, 190),
    (36, 66, 185.99, 150),
    (37, 7, 190.99, 170),
    (38, 19, 195.99, 90),
    (39, 31, 200.99, 100),
    (40, 43, 205.99, 120),
    (41, 55, 210.99, 160),
    (42, 67, 215.99, 180),
    (43, 9, 220.99, 110),
    (44, 21, 225.99, 80),
    (45, 33, 230.99, 130),
    (46, 45, 235.99, 140),
    (47, 57, 240.99, 190),
    (48, 68, 245.99, 150),
    (1, 50, 255.99, 100),
    (2, 10, 55.99, 140),
    (3, 22, 115.99, 180),
    (4, 34, 175.99, 120),
    (5, 46, 235.99, 160),
    (6, 58, 295.99, 180),
    (7, 50, 255.99, 100),
    (8, 10, 55.99, 140),
    (9, 22, 115.99, 180),
    (10, 34, 175.99, 120),
    (11, 46, 235.99, 160),
    (12, 58, 295.99, 180),
    (13, 50, 255.99, 100),
    (14, 10, 55.99, 140),
    (15, 22, 115.99, 180),
    (16, 34, 175.99, 120),
    (17, 46, 235.99, 160),
    (18, 58, 295.99, 180),
    (19, 50, 255.99, 100),
    (20, 10, 55.99, 140),
    (21, 22, 115.99, 180),
    (22, 34, 175.99, 120),
    (23, 46, 235.99, 160),
    (24, 58, 295.99, 180),
    (25, 50, 255.99, 100),
    (26, 10, 55.99, 140),
    (27, 22, 115.99, 180),
    (28, 34, 175.99, 120),
    (29, 46, 235.99, 160),
    (30, 58, 295.99, 180),
    (31, 50, 255.99, 100),
    (32, 10, 55.99, 140),
    (33, 22, 115.99, 180),
    (34, 34, 175.99, 120),
    (35, 46, 235.99, 160),
    (36, 58, 295.99, 180),
    (37, 50, 255.99, 100),
    (38, 10, 55.99, 140),
    (39, 22, 115.99, 180),
    (40, 34, 175.99, 120),
    (41, 46, 235.99, 160),
    (42, 58, 295.99, 180),
    (43, 50, 255.99, 100),
    (44, 10, 55.99, 140),
    (45, 22, 115.99, 180),
    (46, 34, 175.99, 120),
    (47, 46, 235.99, 160),
    (48, 58, 295.99, 180);


--venda
----------------------------------------------------------------
INSERT INTO venda (cliente_ID_cliente, endereco_entrega_venda, bairro_entrega_venda, observacoes_venda, situacao_pagamento_venda, situacao_entrega_venda, forma_pagamento_venda, data_venda) 
VALUES
    (1, 'Rua A, 123', 'Centro', 'Entregar para João, ligar antes de entregar', 'Realizado', 'Realizada', 'Crédito', '2023-01-15 10:00:00'),
    (2, 'Avenida B, 456', 'Jardim', 'Chamar a Maria para receber', 'Realizado', 'Realizada', 'Débito', '2024-03-20 15:30:00'),
    (3, 'Rua C, 789', 'Vila', 'Deixar na portaria', 'Não realizado', 'Não realizada', 'Dinheiro', '2023-07-05 09:15:00'),
    (4, 'Avenida D, 1011', 'Centro', 'Ligar para confirmar o endereço antes da entrega', 'Realizado', 'Realizada', 'PIX', '2024-01-10 11:45:00'),
    (5, 'Rua E, 1213', 'Jardim', 'Entregar para o porteiro', 'Não realizado', 'Não realizada', 'Crédito', '2023-09-28 16:00:00'),
    (6, 'Avenida F, 1415', 'Vila', 'Chamar para confirmar o recebimento', 'Realizado', 'Realizada', 'Débito', '2024-05-12 14:30:00'),
    (7, 'Rua G, 1617', 'Centro', 'Deixar na portaria com o porteiro', 'Não realizado', 'Não realizada', 'Dinheiro', '2023-11-18 10:00:00'),
    (8, 'Avenida H, 1819', 'Jardim', 'Entregar para o Sr. Carlos', 'Realizado', 'Realizada', 'PIX', '2024-02-25 17:15:00'),
    (9, 'Rua I, 2021', 'Vila', 'Ligar para confirmar o horário da entrega', 'Não realizado', 'Não realizada', 'Crédito', '2023-06-03 13:30:00'),
    (10, 'Avenida J, 2223', 'Centro', 'Deixar na portaria', 'Realizado', 'Realizada', 'Débito', '2024-04-08 11:00:00'),
    (11, 'Rua K, 2425', 'Jardim', 'Entregar para a Sra. Ana', 'Não realizado', 'Não realizada', 'Dinheiro', '2023-08-12 16:45:00'),
    (12, 'Avenida L, 2627', 'Vila', 'Chamar antes de entregar', 'Realizado', 'Realizada', 'PIX', '2024-06-15 15:15:00'),
    (13, 'Rua M, 2829', 'Centro', 'Deixar na portaria com o porteiro', 'Não realizado', 'Não realizada', 'Crédito', '2023-10-22 10:30:00'),
    (14, 'Avenida N, 3031', 'Jardim', 'Entregar para o Sr. José', 'Realizado', 'Realizada', 'Débito', '2024-03-01 13:00:00'),
    (15, 'Rua O, 3233', 'Vila', 'Ligar para confirmar o endereço da entrega', 'Não realizado', 'Não realizada', 'Dinheiro', '2023-12-09 17:00:00'),
    (16, 'Avenida P, 3435', 'Centro', 'Deixar na portaria', 'Realizado', 'Realizada', 'PIX', '2024-04-28 11:30:00'),
    (17, 'Rua Q, 3637', 'Jardim', 'Entregar para a Sra. Maria', 'Não realizado', 'Não realizada', 'Crédito', '2023-05-17 15:45:00'),
    (18, 'Avenida R, 3839', 'Vila', 'Chamar antes de entregar', 'Realizado', 'Realizada', 'Débito', '2024-02-12 14:15:00'),
    (19, 'Rua S, 4041', 'Centro', 'Deixar na portaria com o porteiro', 'Não realizado', 'Não realizada', 'Dinheiro', '2023-04-01 10:15:00'),
    (20, 'Avenida T, 4243', 'Jardim', 'Entregar para o Sr. Pedro', 'Realizado', 'Realizada', 'PIX', '2024-06-05 17:30:00'),
    (1, 'Rua A, 123', 'Centro', 'Entregar para João, ligar antes de entregar', 'Realizado', 'Realizada', 'Débito', '2023-02-22 12:00:00'),
    (2, 'Avenida B, 456', 'Jardim', 'Chamar a Maria para receber', 'Não realizado', 'Não realizada', 'Crédito', '2024-04-10 10:30:00'),
    (3, 'Rua C, 789', 'Vila', 'Deixar na portaria', 'Realizado', 'Realizada', 'Dinheiro', '2023-08-15 17:45:00'),
    (4, 'Avenida D, 1011', 'Centro', 'Ligar para confirmar o endereço antes da entrega', 'Não realizado', 'Não realizada', 'PIX', '2024-02-05 14:00:00'),
    (5, 'Rua E, 1213', 'Jardim', 'Entregar para o porteiro', 'Realizado', 'Realizada', 'Crédito', '2023-11-03 11:15:00'),
    (6, 'Avenida F, 1415', 'Vila', 'Chamar para confirmar o recebimento', 'Não realizado', 'Não realizada', 'Débito', '2024-03-28 16:30:00'),
    (7, 'Rua G, 1617', 'Centro', 'Deixar na portaria com o porteiro', 'Realizado', 'Realizada', 'Dinheiro', '2023-05-20 10:45:00'),
    (8, 'Avenida H, 1819', 'Jardim', 'Entregar para o Sr. Carlos', 'Não realizado', 'Não realizada', 'PIX', '2024-05-18 13:00:00'),
    (9, 'Rua I, 2021', 'Vila', 'Ligar para confirmar o horário da entrega', 'Realizado', 'Realizada', 'Crédito', '2023-09-10 14:15:00'),
    (10, 'Avenida J, 2223', 'Centro', 'Deixar na portaria', 'Não realizado', 'Não realizada', 'Débito', '2024-01-25 12:30:00'),
    (11, 'Rua K, 2425', 'Jardim', 'Entregar para a Sra. Ana', 'Realizado', 'Realizada', 'Dinheiro', '2023-12-22 16:00:00'),
    (12, 'Avenida L, 2627', 'Vila', 'Chamar antes de entregar', 'Não realizado', 'Não realizada', 'PIX', '2024-04-12 15:45:00'),
    (13, 'Rua M, 2829', 'Centro', 'Deixar na portaria com o porteiro', 'Realizado', 'Realizada', 'Crédito', '2023-07-08 11:30:00'),
    (14, 'Avenida N, 3031', 'Jardim', 'Entregar para o Sr. José', 'Não realizado', 'Não realizada', 'Débito', '2024-06-01 14:00:00'),
    (15, 'Rua O, 3233', 'Vila', 'Ligar para confirmar o endereço da entrega', 'Realizado', 'Realizada', 'Dinheiro', '2023-10-12 17:15:00'),
    (16, 'Avenida P, 3435', 'Centro', 'Deixar na portaria', 'Não realizado', 'Não realizada', 'PIX', '2024-03-10 10:45:00'),
    (17, 'Rua Q, 3637', 'Jardim', 'Entregar para a Sra. Maria', 'Realizado', 'Realizada', 'Crédito', '2023-06-05 15:00:00'),
    (18, 'Avenida R, 3839', 'Vila', 'Chamar antes de entregar', 'Não realizado', 'Não realizada', 'Débito', '2024-05-02 13:30:00'),
    (19, 'Rua S, 4041', 'Centro', 'Deixar na portaria com o porteiro', 'Realizado', 'Realizada', 'Dinheiro', '2023-03-18 11:00:00'),
    (20, 'Avenida T, 4243', 'Jardim', 'Entregar para o Sr. Pedro', 'Não realizado', 'Não realizada', 'PIX', '2024-04-20 17:00:00'),
    (1, 'Rua A, 123', 'Centro', 'Entregar para João, ligar antes de entregar', 'Realizado', 'Realizada', 'Crédito', '2023-01-15 10:00:00'),
    (2, 'Avenida B, 456', 'Jardim', 'Chamar a Maria para receber', 'Realizado', 'Realizada', 'Débito', '2024-03-20 15:30:00'),
    (3, 'Rua C, 789', 'Vila', 'Deixar na portaria', 'Não realizado', 'Não realizada', 'Dinheiro', '2023-07-05 09:15:00'),
    (4, 'Avenida D, 1011', 'Centro', 'Ligar para confirmar o endereço antes da entrega', 'Realizado', 'Realizada', 'PIX', '2024-01-10 11:45:00'),
    (5, 'Rua E, 1213', 'Jardim', 'Entregar para o porteiro', 'Não realizado', 'Não realizada', 'Crédito', '2023-09-28 16:00:00'),
    (6, 'Avenida F, 1415', 'Vila', 'Chamar para confirmar o recebimento', 'Realizado', 'Realizada', 'Débito', '2024-05-12 14:30:00'),
    (7, 'Rua G, 1617', 'Centro', 'Deixar na portaria com o porteiro', 'Não realizado', 'Não realizada', 'Dinheiro', '2023-11-18 10:00:00'),
    (8, 'Avenida H, 1819', 'Jardim', 'Entregar para o Sr. Carlos', 'Realizado', 'Realizada', 'PIX', '2024-02-25 17:15:00'),
    (9, 'Rua I, 2021', 'Vila', 'Ligar para confirmar o horário da entrega', 'Não realizado', 'Não realizada', 'Crédito', '2023-06-03 13:30:00'),
    (10, 'Avenida J, 2223', 'Centro', 'Deixar na portaria', 'Realizado', 'Realizada', 'Débito', '2024-04-08 11:00:00'),
    (11, 'Rua K, 2425', 'Jardim', 'Entregar para a Sra. Ana', 'Não realizado', 'Não realizada', 'Dinheiro', '2023-08-12 16:45:00'),
    (12, 'Avenida L, 2627', 'Vila', 'Chamar antes de entregar', 'Realizado', 'Realizada', 'PIX', '2024-06-15 15:15:00'),
    (13, 'Rua M, 2829', 'Centro', 'Deixar na portaria com o porteiro', 'Não realizado', 'Não realizada', 'Crédito', '2023-10-22 10:30:00'),
    (14, 'Avenida N, 3031', 'Jardim', 'Entregar para o Sr. José', 'Realizado', 'Realizada', 'Débito', '2024-03-01 13:00:00'),
    (15, 'Rua O, 3233', 'Vila', 'Ligar para confirmar o endereço da entrega', 'Não realizado', 'Não realizada', 'Dinheiro', '2023-12-09 17:00:00'),
    (16, 'Avenida P, 3435', 'Centro', 'Deixar na portaria', 'Realizado', 'Realizada', 'PIX', '2024-04-28 11:30:00'),
    (17, 'Rua Q, 3637', 'Jardim', 'Entregar para a Sra. Maria', 'Não realizado', 'Não realizada', 'Crédito', '2023-05-17 15:45:00'),
    (18, 'Avenida R, 3839', 'Vila', 'Chamar antes de entregar', 'Realizado', 'Realizada', 'Débito', '2024-02-12 14:15:00'),
    (19, 'Rua S, 4041', 'Centro', 'Deixar na portaria com o porteiro', 'Não realizado', 'Não realizada', 'Dinheiro', '2023-04-01 10:15:00'),
    (20, 'Avenida T, 4243', 'Jardim', 'Entregar para o Sr. Pedro', 'Realizado', 'Realizada', 'PIX', '2024-06-05 17:30:00'),
    (1, 'Rua A, 123', 'Centro', 'Entregar para João, ligar antes de entregar', 'Realizado', 'Realizada', 'Crédito', '2023-01-21 10:00:00'),
    (2, 'Avenida B, 456', 'Jardim', 'Chamar a Maria para receber', 'Realizado', 'Realizada', 'Débito', '2024-03-27 15:30:00'),
    (3, 'Rua C, 789', 'Vila', 'Deixar na portaria', 'Não realizado', 'Não realizada', 'Dinheiro', '2023-07-05 09:15:00'),
    (4, 'Avenida D, 1011', 'Centro', 'Ligar para confirmar o endereço antes da entrega', 'Realizado', 'Realizada', 'PIX', '2024-01-18 11:45:00'),
    (5, 'Rua E, 1213', 'Jardim', 'Entregar para o porteiro', 'Não realizado', 'Não realizada', 'Crédito', '2023-09-29 16:00:00'),
    (6, 'Avenida F, 1415', 'Vila', 'Chamar para confirmar o recebimento', 'Realizado', 'Realizada', 'Débito', '2024-05-16 14:30:00'),
    (7, 'Rua G, 1617', 'Centro', 'Deixar na portaria com o porteiro', 'Não realizado', 'Não realizada', 'Dinheiro', '2023-11-20 10:00:00'),
    (8, 'Avenida H, 1819', 'Jardim', 'Entregar para o Sr. Carlos', 'Realizado', 'Realizada', 'PIX', '2024-02-25 17:15:00'),
    (9, 'Rua I, 2021', 'Vila', 'Ligar para confirmar o horário da entrega', 'Não realizado', 'Não realizada', 'Crédito', '2023-06-05 13:30:00'),
    (10, 'Avenida J, 2223', 'Centro', 'Deixar na portaria', 'Realizado', 'Realizada', 'Débito', '2024-04-10 11:00:00'),
    (11, 'Rua K, 2425', 'Jardim', 'Entregar para a Sra. Ana', 'Não realizado', 'Não realizada', 'Dinheiro', '2023-08-17 16:45:00'),
    (12, 'Avenida L, 2627', 'Vila', 'Chamar antes de entregar', 'Realizado', 'Realizada', 'PIX', '2024-06-19 15:15:00'),
    (13, 'Rua M, 2829', 'Centro', 'Deixar na portaria com o porteiro', 'Não realizado', 'Não realizada', 'Crédito', '2023-10-29 10:30:00'),
    (14, 'Avenida N, 3031', 'Jardim', 'Entregar para o Sr. José', 'Realizado', 'Realizada', 'Débito', '2024-03-30 13:00:00'),
    (15, 'Rua O, 3233', 'Vila', 'Ligar para confirmar o endereço da entrega', 'Não realizado', 'Não realizada', 'Dinheiro', '2023-12-11 17:00:00'),
    (16, 'Avenida P, 3435', 'Centro', 'Deixar na portaria', 'Realizado', 'Realizada', 'PIX', '2024-04-29 11:30:00'),
    (17, 'Rua Q, 3637', 'Jardim', 'Entregar para a Sra. Maria', 'Não realizado', 'Não realizada', 'Crédito', '2023-05-22 15:45:00'),
    (18, 'Avenida R, 3839', 'Vila', 'Chamar antes de entregar', 'Realizado', 'Realizada', 'Débito', '2024-02-24 14:15:00'),
    (19, 'Rua S, 4041', 'Centro', 'Deixar na portaria com o porteiro', 'Não realizado', 'Não realizada', 'Dinheiro', '2023-04-29 10:15:00'),
    (20, 'Avenida T, 4243', 'Jardim', 'Entregar para o Sr. Pedro', 'Realizado', 'Realizada', 'PIX', '2024-06-14 17:30:00');

--itens de venda
----------------------------------------------------------------
INSERT INTO venda_produto (venda_ID_venda, produto_ID_produto, quantidade_produto_venda) 
VALUES
    (1, 1, 3),
    (2, 2, 5),
    (3, 3, 2),
    (4, 4, 1),
    (5, 5, 4),
    (6, 6, 7),
    (7, 7, 6),
    (8, 8, 3),
    (9, 9, 2),
    (10, 10, 5),
    (11, 11, 4),
    (12, 12, 6),
    (13, 13, 1),
    (14, 14, 7),
    (15, 15, 3),
    (16, 16, 2),
    (17, 17, 5),
    (18, 18, 4),
    (19, 19, 6),
    (20, 20, 1),
    (21, 21, 7),
    (22, 22, 3),
    (23, 23, 2),
    (24, 24, 5),
    (25, 25, 4),
    (26, 26, 6),
    (27, 27, 1),
    (28, 28, 7),
    (29, 29, 3),
    (30, 30, 2),
    (31, 31, 5),
    (32, 32, 4),
    (33, 33, 6),
    (34, 34, 1),
    (35, 35, 7),
    (36, 36, 3),
    (37, 37, 2),
    (38, 38, 5),
    (39, 39, 4),
    (40, 40, 6),
    (41, 41, 1),
    (42, 42, 7),
    (43, 43, 3),
    (44, 44, 2),
    (45, 45, 5),
    (46, 46, 4),
    (47, 47, 6),
    (48, 48, 1),
    (49, 49, 7),
    (50, 50, 3),
    (51, 51, 2),
    (52, 52, 5),
    (53, 53, 4),
    (54, 54, 6),
    (55, 55, 1),
    (56, 56, 7),
    (57, 57, 3),
    (58, 58, 2),
    (59, 59, 5),
    (60, 60, 4),
    (61, 61, 6),
    (62, 62, 1),
    (63, 63, 7),
    (64, 64, 3),
    (65, 65, 2),
    (66, 66, 5),
    (67, 67, 4),
    (68, 68, 6),
    (69, 1, 8),
    (70, 2, 2),
    (71, 3, 4),
    (72, 4, 9),
    (73, 5, 6),
    (74, 6, 1),
    (75, 7, 7),
    (76, 8, 3),
    (77, 9, 5),
    (78, 10, 2),
    (79, 11, 1),
    (80, 12, 10),
    (1, 13, 9),
    (2, 14, 4),
    (3, 15, 7),
    (4, 16, 5),
    (5, 17, 3),
    (6, 18, 6),
    (7, 19, 2),
    (8, 20, 8),
    (9, 21, 4),
    (10, 22, 1),
    (11, 23, 9),
    (12, 24, 2),
    (13, 25, 7),
    (14, 26, 3),
    (15, 27, 5),
    (16, 28, 4),
    (17, 29, 6),
    (18, 30, 9),
    (19, 31, 8),
    (20, 32, 2),
    (21, 33, 3),
    (22, 34, 1),
    (23, 35, 10),
    (24, 36, 7),
    (25, 37, 5),
    (26, 38, 9),
    (27, 39, 2),
    (28, 40, 6),
    (29, 41, 4),
    (30, 42, 8),
    (31, 43, 7),
    (32, 44, 1),
    (33, 45, 3),
    (34, 46, 2),
    (35, 47, 9),
    (36, 48, 4),
    (37, 49, 5),
    (38, 50, 6),
    (39, 51, 8),
    (40, 52, 3),
    (41, 53, 7),
    (42, 54, 1),
    (43, 55, 9),
    (44, 56, 2),
    (45, 57, 4),
    (46, 58, 3),
    (47, 59, 8),
    (48, 60, 6),
    (49, 61, 1),
    (50, 62, 2),
    (51, 63, 7),
    (52, 64, 9),
    (53, 65, 3),
    (54, 66, 4),
    (55, 67, 8),
    (56, 68, 5),
    (57, 1, 2),
    (58, 2, 3),
    (59, 3, 8),
    (60, 4, 7),
    (61, 5, 1),
    (62, 6, 9),
    (63, 7, 4),
    (64, 8, 6),
    (65, 9, 5),
    (66, 10, 8),
    (67, 11, 2),
    (68, 12, 7),
    (69, 13, 6),
    (70, 14, 1),
    (71, 15, 3),
    (72, 16, 9),
    (73, 17, 5),
    (74, 18, 7),
    (75, 19, 1),
    (76, 20, 4),
    (77, 21, 6),
    (78, 22, 2),
    (79, 23, 9),
    (80, 24, 3);