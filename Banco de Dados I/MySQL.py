
%pip install mysql-connector-python



# ## Abrindo conexão com o banco de dados
# 
# Utilizando a biblioteca mysql-connector-python, iremos realizar a conexão com o banco de dados previamente criado


import mysql.connector

# Configuração da conexão com o MySQL
config = {
    'user': 'root',
    'password': '123456',
    'host': 'localhost',
    'database': 'nota_fiscal',
    'raise_on_warnings': True
}
conexao = mysql.connector.connect(**config)

# Criar um objeto cursor para interagir com o banco de dados
cursor = conexao.cursor()

print(f"""
{40*'*'}
CONEXÃO COM O BANCO DE DADOS INICIADA
{40*'*'}
""")


# ## Inserindo dados nas tabelas


# Nesta etapa, vamos criar variáveis com as inserções via comando SQL


sql_inserir_dados_clientes = '''
INSERT INTO nota_fiscal.clientes 
(id, nome_completo, razao_social, cpf, cnpj, data_nascimento, email, telefone, cep, logradouro, numero, complemento, bairro, municipio, uf)
VALUES
(1, 'João Silva', NULL, '12345678901', NULL, '1990-05-15', 'joao.silva@email.com', '1234567890', '12345678', 'Rua Principal', '123', 'Apto 101', 'Centro', 'Cidade A', 'SP'),
(2, NULL, 'Oliveira ME', NULL, '98765432000112', '1985-08-22', 'maria.oliveira@email.com', '9876543210', '87654321', 'Avenida Secundária', '456', 'CASA E DECORAÇÃO 202', 'Bairro Norte', 'Cidade B', 'RJ'),
(3, NULL, 'Pereira & Cia', NULL, '12345678901234', '1978-03-10', 'carlos.pereira@email.com', '1122134455', '54321098', 'Travessa da Esquina', '789', 'Sala 303', 'Bairro Sul', 'Cidade C', 'MG'),
(4, 'Ana Souza', NULL, '45678901234', NULL, '1982-11-28', 'ana.souza@email.com', '987654321', '54321098', 'Rua das Flores', '789', 'Bloco 2, Ap 405', 'Jardim Primavera', 'Cidade D', 'SP'),
(5, 'José Oliveira', NULL, '78901234567', NULL, '1975-07-14', 'jose.oliveira@email.com', '1122334155', '12345678', 'Avenida Principal', '4567', 'CASA E DECORAÇÃO 102', 'Centro', 'Cidade E', 'RJ'),
(6, NULL, 'Santos Construções', NULL, '98765432000134', '1990-02-20', 'mariana.santos@email.com', '9980776655', '87654321', 'Rua do Comércio', '321', 'Sala 201', 'Bairro Comercial', 'Cidade F', 'MG'),
(7, NULL, 'Lima & Associados', NULL, '12345678900234', '1988-09-03', 'fernanda.lima@email.com', '1122334451', '12345678', 'Rua das Árvores', '987', 'Apto 301', 'Jardim das Flores', 'Cidade G', 'SP'),
(8, 'Gabriel Costa', NULL, '34567890122', NULL, '1973-12-18', 'gabriel.costa@email.com', '9988776605', '87654321', 'Avenida Central', '654', 'CASA E DECORAÇÃO 405', 'Centro', 'Cidade H', 'RJ'),
(9, 'Isabela Rocha', NULL, '56789012345', NULL, '1995-04-25', 'isabela.rocha@email.com', '1122334425', '54321098', 'Travessa dos Campos', '543', 'Sala 102', 'Bairro Novo', 'Cidade I', 'MG'),
(10, NULL, 'Almeida Construções', NULL, '87654321012345', '1980-07-31', 'lucas.almeida@email.com', '9988776611', '87654321', 'Rua das Montanhas', '876', 'CASA E DECORAÇÃO 203', 'Bairro Residencial', 'Cidade J', 'SP'),
(11, 'Patrícia Nunes', NULL, '98765430921', NULL, '1989-11-14', 'patricia.nunes@email.com', '1122334450', '12345678', 'Avenida dos Lagos', '1234', 'Apto 504', 'Lagoa Azul', 'Cidade K', 'RJ'),
(12, NULL, 'Santos & Filhos', '1098765444', NULL, '1972-06-08', 'rafaela.santos@email.com', '9988006235', '54321098', 'Travessa das Pedras', '876', 'CASA E DECORAÇÃO 102', 'Bairro Pedregulho', 'Cidade L', 'MG'),
(13, NULL, 'Lima Incorporações', NULL, '98765432000234', '1998-03-22', 'sergio.lima@email.com', '1122334495', '87654321', 'Rua do Progresso', '543', 'Sala 201', 'Bairro Industrial', 'Cidade M', 'SP'),
(14, 'Vanessa Costa', NULL, '34567890123', NULL, '1985-08-05', 'vanessa.costa@email.com', '9988776600', '12345678', 'Avenida da Praia', '654', 'CASA E DECORAÇÃO 405', 'Praia Grande', 'Cidade N', 'RJ'),
(15, 'William Oliveira', NULL, '56789012355', NULL, '1977-02-10', 'william.oliveira@email.com', '1122934455', '54321098', 'Travessa das Oliveiras', '543', 'Sala 102', 'Bairro das Oliveiras', 'Cidade O', 'MG'),
(16, NULL, 'Almeida & Filhos', NULL, '87654321000545', '1993-05-18', 'camila.almeida@email.com', '9988773655', '87654321', 'Rua das Flores', '876', 'CASA E DECORAÇÃO 203', 'Bairro Florido', 'Cidade P', 'SP'),
(17, 'Denis Nunes', NULL, '98765432109', NULL, '1976-11-30', 'denis.nunes@email.com', '1122334457', '12345678', 'Avenida Central', '1234', 'Apto 504', 'Centro', 'Cidade Q', 'RJ'),
(18, 'Elaine Santos', NULL, '10987654321', NULL, '1990-04-15', 'elaine.santos@email.com', '9988336656', '54321098', 'Travessa dos Campos', '543', 'Sala 102', 'Bairro dos Campos', 'Cidade R', 'MG'),
(19, NULL, 'Lima Empreendimentos', NULL, '98765432101234', '1982-02-28', 'felipe.lima@email.com', '1122334455', '87654321', 'Rua da Liberdade', '543', 'Sala 201', 'Bairro Liberdade', 'Cidade S', 'SP'),
(20, 'Gisele Costa', NULL, '34567890124', NULL, '1974-09-10', 'gisele.costa@email.com', '9988776005', '12345678', 'Avenida dos Girassóis', '654', 'CASA E DECORAÇÃO 405', 'Jardim das Flores', 'Cidade T', 'RJ');
'''


sql_inserir_dados_produtos = '''
INSERT INTO nota_fiscal.produtos 
(id, nome, codigo_barras, categoria, preco, saldo_estoque, unidade_comercial, observacao, ativo)
VALUES
(1, 'Cadeira de Escritório', '1234567890123', 'CASA E DECORAÇÃO', 199.99, 50, 'UN', 'Cadeira ergonômica com suporte lombar', 1),
(2, 'Smartphone Modelo X', '9876543210987', 'ELETRÔNICOS', 799.99, 30, 'UN', 'Tela AMOLED, câmera de alta resolução', 1),
(3, 'Geladeira Frost Free', '4567890123456', 'ELETRODOMÉSTICOS', 1499.99, 20, 'UN', 'Duplex, eficiente em consumo de energia', 1),
(4, 'Livro: "Aventuras Fantásticas"', '1111222233334', 'LIVROS E ENTRETENIMENTO', 29.99, 100, 'UN', 'Best-seller de ficção científica', 1),
(5, 'Sapato Social Masculino', '5555666677778', 'MODA', 89.99, 80, 'PR', 'Couro legítimo, elegante para ocasiões especiais', 1),
(6, 'Kit de Maquiagem', '8765432109876', 'SAÚDE E BELEZA', 49.99, 120, 'UN', 'Paleta de sombras, batons e pincéis', 1),
(7, 'Ferro de Passar a Vapor', '5432109876543', 'ELETRODOMÉSTICOS', 69.99, 60, 'UN', 'Compacto e eficiente para passar roupas', 1),
(8, 'Câmera de Segurança IP', '1234543212345', 'ELETRÔNICOS', 129.99, 40, 'UN', 'Monitoramento remoto por aplicativo', 1),
(9, 'Livro: "História Antiga"', '5555444433332', 'LIVROS E ENTRETENIMENTO', 24.99, 150, 'UN', 'Exploração de civilizações antigas', 1),
(10, 'Camiseta Casual', '9876543210001', 'MODA', 19.99, 200, 'UN', 'Algodão confortável, disponível em diversas cores', 1),
(11, 'Secador de Cabelo Profissional', '2222111122221', 'SAÚDE E BELEZA', 79.99, 50, 'UN', 'Potente e com múltiplas velocidades', 1),
(12, 'Panela Elétrica de Arroz', '3333222211110', 'ELETRODOMÉSTICOS', 59.99, 70, 'UN', 'Prepara arroz de forma prática e rápida', 1),
(13, 'Livro: "Mistérios do Universo"', '1111222233335', 'LIVROS E ENTRETENIMENTO', 34.99, 90, 'UN', 'Exploração do cosmos e fenômenos cósmicos', 1),
(14, 'Tênis Esportivo', '5555666677779', 'MODA', 59.99, 110, 'PR', 'Design moderno e confortável para atividades físicas', 1),
(15, 'Kit de Maquiagem Profissional', '8765432109877', 'SAÚDE E BELEZA', 99.99, 30, 'UN', 'Paleta completa para maquiadores profissionais', 1),
(16, 'Aspirador de Pó Portátil', '5432109876544', 'ELETRODOMÉSTICOS', 89.99, 45, 'UN', 'Compacto e eficiente para a limpeza diária', 1),
(17, 'Smartwatch Fitness', '1234543212346', 'ELETRÔNICOS', 149.99, 25, 'UN', 'Monitora atividades físicas e saúde', 1),
(18, 'Livro: "A Arte da Cozinha"', '5555444433333', 'LIVROS E ENTRETENIMENTO', 44.99, 80, 'UN', 'Receitas e técnicas culinárias', 1),
(19, 'Bolsa Feminina Elegante', '9876543210002', 'MODA', 39.99, 100, 'UN', 'Design sofisticado e espaçoso', 1),
(20, 'Secador de Cabelo Compacto', '2222111122222', 'SAÚDE E BELEZA', 49.99, 60, 'UN', 'Leve e ideal para viagens', 1),
(21, 'Ferro de Passar a Vapor', '5432109876545', 'ELETRODOMÉSTICOS', 79.99, 40, 'UN', 'Com base antiaderente', 1),
(22, 'Caixa de Som Bluetooth', '1234543212347', 'ELETRÔNICOS', 109.99, 35, 'UN', 'Conexão sem fio para dispositivos móveis', 1),
(23, 'Livro: "Aventuras Submarinas"', '5555444433334', 'LIVROS E ENTRETENIMENTO', 29.99, 120, 'UN', 'Exploração dos oceanos e vida marinha', 1),
(24, 'Sandália Feminina', '9876543210003', 'MODA', 29.99, 150, 'PR', 'Confortável e elegante para o dia a dia', 1),
(25, 'Chapinha para Cabelo', '2222111122223', 'SAÚDE E BELEZA', 69.99, 50, 'UN', 'Placas de cerâmica para alisamento perfeito', 1),
(26, 'Cafeteira Elétrica', '5432109876546', 'ELETRODOMÉSTICOS', 89.99, 30, 'UN', 'Prepara café rapidamente', 1),
(27, 'Livro: "Viagens pelo Mundo"', '5555444433335', 'LIVROS E ENTRETENIMENTO', 39.99, 80, 'UN', 'Relatos de viagens ao redor do globo', 1),
(28, 'Mochila Esportiva', '9876543210004', 'MODA', 49.99, 60, 'UN', 'Ideal para atividades ao ar livre', 1),
(29, 'Barbeador Elétrico', '2222111122224', 'SAÚDE E BELEZA', 59.99, 40, 'UN', 'Preciso e fácil de usar', 1),
(30, 'Liquidificador Potente', '5432109876547', 'ELETRODOMÉSTICOS', 99.99, 20, 'UN', 'Prepara sucos e vitaminas', 1);
'''


sql_inserir_dados_fornecedores = '''
INSERT INTO nota_fiscal.fornecedores 
(id, razao_social, cnpj, email, telefone, cep, logradouro, numero, complemento, bairro, municipio, uf, observacao, ativo)
VALUES
(1, 'NORDESTE IND COM ART METAIS LTDA', '12345678000100', 'nordeste@email.com', '1122334400', '12345678', 'Rua Principal', '123', 'Apto 101', 'Centro', 'Cidade A', 'SP', 'Especializado em eletrônicos', 1),
(2, 'RECIFE IPUTINGA', '98765432100012', 'iputinga@outlook.com.br', '9988776655', '87654321', 'Avenida Secundária', '456', 'CASA E DECORAÇÃO 202', 'Bairro Norte', 'Cidade B', 'RJ', 'Fornecimento de moda masculina', 1),
(3, 'Louças Brasil LTDA', '12345678901234', 'loucas@gmail.com', '1122334455', '54321098', 'Travessa da Esquina', '789', 'Sala 303', 'Bairro Sul', 'Cidade C', 'MG', 'Atende diversos segmentos', 1),
(4, 'Adilson Batista dos Santos Comércio e Serviços LTDA', '45678901234567', 'comercio@outlook.com', '9876543210', '54321098', 'Rua das Flores', '789', 'Bloco 2, Ap 405', 'Jardim Primavera', 'Cidade D', 'SP', 'Especializado em produtos de decoração', 1),
(5, 'J.P Indústria LTDA', '78901234567890', 'jp@jp.com.br', '1122334155', '12345678', 'Avenida Principal', '4567', 'CASA E DECORAÇÃO 102', 'Centro', 'Cidade E', 'RJ', 'Fornecimento de eletrônicos de última geração', 1),
(6, 'IABC Indústria de Cosméticos LTDA', '10987654321098', 'contato@iabc.com', '9980776655', '87654321', 'Rua do Comércio', '321', 'Sala 201', 'Bairro Comercial', 'Cidade F', 'MG', 'Produtos variados para comércio', 1),
(7, 'Mundial Acessórios e Variedades.', '12345678900234', 'suporte@mudial.com', '1122334451', '12345678', 'Rua das Árvores', '987', 'Apto 301', 'Jardim das Flores', 'Cidade G', 'SP', 'Fornecimento de móveis para escritório', 1),
(8, 'G L de Almeida Comércio e Indústria', '34567890122222', 'contato@gl.com', '9988776605', '87654321', 'Avenida Central', '654', 'CASA E DECORAÇÃO 405', 'Centro', 'Cidade H', 'RJ', 'Produtos variados para o mercado', 1),
(9, 'Esplanada Indústria e Comércio S/A', '56789012345098', 'esplanada@hotmail.com', '1122334425', '54321098', 'Travessa dos Campos', '543', 'Sala 102', 'Bairro Novo', 'Cidade I', 'MG', 'Fornecimento de produtos diversos', 1),
(10, 'KELVIA LOPES PEREIRA DE ARAUJO', '87654321011111', 'kelvia@gmail.com', '9988776611', '87654321', 'Rua das Montanhas', '876', 'CASA E DECORAÇÃO 203', 'Bairro Residencial', 'Cidade J', 'SP', 'Especializado em produtos para construção', 1);
'''


sql_inserir_dados_pedidos = '''
INSERT INTO nota_fiscal.pedidos 
(id, clientes_id, data_compra, status, valor_total, frete, tipo_pagamento, descricao)
VALUES
(1, 1, '2023-01-15', 'PROCESSANDO PAGAMENTO', 150.00, 10.00, 'BOLETO', 'Pedido em andamento'),
(2, 2, '2023-02-20', 'CANCELADO', 300.50, 15.00, 'CARTÃO DE CRÉDITO', 'Pagamento não autorizado'),
(3, 3, '2023-03-10', 'PREPARANDO PEDIDO', 75.99, 8.50, 'PIX', 'Pedido em preparação'),
(4, 4, '2023-04-05', 'ENVIADO', 200.25, 12.00, 'CARTÃO DE CRÉDITO', 'Pedido enviado para entrega'),
(5, 5, '2023-05-12', 'ENTREGUE', 450.80, 20.00, 'PIX', 'Pedido entregue com sucesso'),
(6, 16, '2023-06-18', 'PROCESSANDO PAGAMENTO', 80.50, 9.00, 'BOLETO', 'Aguardando confirmação de pagamento'),
(7, 7, '2023-07-23', 'PREPARANDO PEDIDO', 120.75, 15.00, 'CARTÃO DE CRÉDITO', 'Pedido em preparação'),
(8, 8, '2023-08-30', 'ENVIADO', 600.00, 25.00, 'PIX', 'Pedido enviado para entrega'),
(9, 1, '2023-09-05', 'PROCESSANDO PAGAMENTO', 90.20, 10.00, 'BOLETO', 'Aguardando confirmação de pagamento'),
(10, 20, '2023-10-08', 'PREPARANDO PEDIDO', 180.75, 18.00, 'CARTÃO DE CRÉDITO', 'Pedido em preparação'),
(11, 1, '2023-11-15', 'CANCELADO', 100.00, 10.00, 'CARTÃO DE CRÉDITO', 'Pagamento não autorizado'),
(12, 2, '2023-11-20', 'CANCELADO', 300.50, 15.00, 'CARTÃO DE CRÉDITO', 'Pagamento não autorizado'),
(13, 3, '2023-03-10', 'PREPARANDO PEDIDO', 200.75, 18.00, 'CARTÃO DE CRÉDITO', 'Pedido em preparação'),
(14, 4, '2023-12-05', 'ENVIADO', 200.25, 12.00, 'CARTÃO DE CRÉDITO', 'Pedido enviado para entrega'),
(15, 15, '2023-12-12', 'ENTREGUE', 450.80, 20.00, 'PIX', 'Pedido entregue com sucesso'),
(16, 6, '2023-06-18', 'PROCESSANDO PAGAMENTO', 80.50, 9.00, 'BOLETO', 'Aguardando confirmação de pagamento'),
(17, 7, '2023-07-23', 'PREPARANDO PEDIDO', 120.75, 15.00, 'CARTÃO DE CRÉDITO', 'Pedido em preparação'),
(18, 8, '2023-08-30', 'ENVIADO', 600.00, 25.00, 'PIX', 'Pedido enviado para entrega'),
(19, 9, '2023-09-05', 'PROCESSANDO PAGAMENTO', 90.20, 10.00, 'BOLETO', 'Aguardando confirmação de pagamento'),
(20, 10, '2023-10-08', 'PREPARANDO PEDIDO', 180.75, 18.00, 'CARTÃO DE CRÉDITO', 'Pedido em preparação');
'''


sql_inserir_dados_notas_fiscais = '''
INSERT INTO nota_fiscal.notas_fiscais 
(id, pedidos_id, modelo, serie, numero, chave_acesso, data_emissao, observaçao) -- OBSERVAÇÃO COM Ç
VALUES
(1, 1, '55', '1', '0001234',   '45678901234568890123456', '2023-01-15 08:30:00', 'Nota fiscal em processamento'),
(2, 2, '55', '1', '0005678',   '56789012345678902234567', '2023-02-20 09:45:00', 'Nota fiscal CANCELADA'),
(3, 3, '55', '1', '0009123',   '67890123456789012345677', '2023-03-10 10:15:00', 'Nota fiscal em processamento'),
(4, 4, '55', '1', '0012567',   '78901234567890123456799', '2023-04-05 11:30:00', 'Nota fiscal enviada para transporte'),
(5, 5, '55', '1', '0016012',   '89012345678901233567890', '2023-05-12 12:45:00', 'Nota fiscal entregue ao cliente'),
(6, 6, '55', '1', '0019456',   '90123456789012345778901', '2023-06-18 14:00:00', 'Nota fiscal em processamento'),
(7, 7, '55', '1', '0022901',   '01234567890723456789012', '2023-07-23 15:15:00', 'Nota fiscal a caminho da entrega'),
(8, 8, '55', '1', '0026345',   '12345678901234567890123', '2023-08-30 16:30:00', 'Nota fiscal entregue ao transportador'),
(9, 9, '55', '1', '0029790',   '23456789012345678901234', '2023-09-05 17:45:00', 'Nota fiscal processada em processamento'),
(10, 10, '55', '1', '0033234', '34567890123456789012345', '2023-10-08 19:00:00', 'Nota fiscal processada com sucesso'),
(11, 11, '55', '1', '0036679', '45678901234567890123456', '2023-11-15 08:30:00', 'Nota fiscal cancelada'),
(12, 12, '55', '1', '0040123', '56989012345678901234567', '2023-11-20 09:45:00', 'Nota fiscal cancelada'),
(13, 13, '55', '1', '0043567', '27890123456789012345678', '2023-03-10 10:15:00', 'Nota fiscal em processamento'),
(14, 14, '55', '1', '0047012', '78901234567890123456789', '2023-12-05 11:30:00', 'Nota fiscal enviada para transporte'),
(15, 15, '55', '1', '0050456', '89012340678921234567890', '2023-12-12 12:45:00', 'Nota fiscal entregue ao cliente'),
(16, 16, '55', '1', '0053901', '90123456789022345678901', '2023-06-18 14:00:00', 'Nota fiscal processada com sucesso'),
(17, 17, '55', '1', '0057345', '01234562890123452789012', '2023-07-23 15:15:00', 'Nota fiscal a caminho da entrega'),
(18, 18, '55', '1', '0060790', '12345672901234567890123', '2023-08-30 16:30:00', 'Nota fiscal entregue ao transportador'),
(19, 19, '55', '1', '0064234', '23456789012345278901234', '2023-09-05 17:45:00', 'Nota fiscal em processamento'),
(20, 20, '55', '1', '0067679', '34567890123456289012345', '2023-10-08 19:00:00', 'Nota fiscal processada com sucesso');
'''


sql_inserir_dados_pedido_produto = '''
INSERT INTO nota_fiscal.pedidos_produtos 
(pedidos_id, produtos_id, quantidade)
VALUES
(1, 1, 2),
(1, 20, 5),
(1, 11, 2),
(1, 4, 3),
(1, 2, 1),
(2, 3, 3),
(2, 4, 1),
(2, 11, 2),
(2, 10, 1),
(3, 5, 1),
(3, 6, 2),
(4, 7, 1),
(4, 8, 4),
(5, 9, 2),
(5, 10, 1),
(6, 11, 3),
(6, 12, 2),
(7, 13, 1),
(7, 14, 1),
(8, 15, 5),
(8, 16, 3),
(9, 17, 2),
(9, 18, 2),
(10, 19, 1),
(10, 20, 1),
(11, 11, 2),
(11, 2, 1),
(12, 3, 3),
(12, 14, 1),
(13, 5, 1),
(13, 16, 2),
(14, 7, 1),
(14, 18, 4),
(15, 9, 2),
(15, 10, 1),
(16, 11, 3),
(16, 12, 2),
(17, 23, 1),
(17, 14, 1),
(18, 15, 5),
(18, 16, 3),
(19, 17, 2),
(19, 18, 2),
(20, 19, 1),
(20, 20, 1);
'''


sql_inserir_dados_fornecedores_produto = '''
INSERT INTO nota_fiscal.fornecedores_produtos 
(fornecedores_id, produtos_id, quantidade)
VALUES
(1, 1, 100),
(2, 2, 50),
(3, 3, 200),
(4, 4, 30),
(5, 5, 80),
(6, 6, 150),
(7, 7, 40),
(8, 8, 70),
(9, 9, 120),
(10, 10, 60),
(1, 11, 100),
(2, 12, 50),
(3, 13, 200),
(4, 14, 30),
(5, 15, 80),
(6, 16, 150),
(7, 17, 40),
(8, 18, 70),
(9, 19, 120),
(10, 20, 60),
(1, 20, 100),
(2, 21, 50),
(3, 22, 200),
(4, 23, 30),
(5, 24, 80),
(6, 25, 150),
(7, 26, 40),
(8, 27, 70),
(9, 28, 120),
(10, 30, 60);
'''


# ### Executando das inserções SQL
# 
# Vamos criar um dicionário contendo todos os códigos SQL para insersão de dados nas tabelas do banco.
# 
# Iremos parsear pelo dicionário utilizando a função 'items()' que retorna uma lista de tuplas onde cada tupla também terá uma chave e valor que poderá ser iterada pelo 'for'.
# 
# Executando a função `execute()` no cursor, conseguimos instanciar o objeto que executa os comandos SQL, e utilizando a função `commit()` na conexão, iremos executar de fato a instrução SQL.


SQL = {
'CLIENTES':sql_inserir_dados_clientes,
'PRODUTOS':sql_inserir_dados_produtos,
'FORNECEDORES':sql_inserir_dados_fornecedores,
'PEDIDOS':sql_inserir_dados_pedidos,
'FISCAIS':sql_inserir_dados_notas_fiscais,
'FORNECEDORES_PRODUTOS':sql_inserir_dados_fornecedores_produto,
'PEDIDO_PRODUTO':sql_inserir_dados_pedido_produto
}

for tabela, sql in SQL.items():
    try:
        cursor.execute(sql)
        conexao.commit()
        print(f"DADOS DE {tabela} INSERIDOS COM SUCESSO")
        
    except Exception as e:
        print(f"Erro ao inserir dados em {tabela}: {e}")

print(40 * '*')
print("TODOS OS DADOS INSERIDOS COM SUCESSO")
print(40 * '*')



# ## Consultando os dados das tabelas
# 
# Diferente das edições ao banco de dados onde usamos a função "commit()", para as consultas, utilizaremos "fetchall()" para leitura do banco


class ConsultasNotasFiscais:
    def __init__(self, conexao, cursor):
        self.conexao = conexao
        self.cursor = cursor

    def _executar_consulta(self, consulta):
        self.cursor.execute(consulta)
        resultado = self.cursor.fetchall()
        for dado in resultado:
            print(dado)

    def consulta_clientes(self):
        print(f'{40*"*"}  {40*"*"} ')
        self._executar_consulta('SELECT * FROM clientes')

    def consulta_pedidos(self):
        print(f'{40*"*"}  {40*"*"} ')
        self._executar_consulta('SELECT * FROM pedidos')

    def consulta_produtos(self):
        print(f'{40*"*"}  {40*"*"} ')
        self._executar_consulta('SELECT * FROM produtos')

    def consulta_notas_fiscais(self):
        print(f'{40*"*"}  {40*"*"} ')
        self._executar_consulta('SELECT * FROM notas_fiscais')

    def consulta_pedidos_produtos(self):
        print(f'{40*"*"}  {40*"*"} ')
        self._executar_consulta('SELECT * FROM pedidos_produtos')

    def consulta_fornecedores_produtos(self):
        print(f'{40*"*"}  {40*"*"} ')
        self._executar_consulta('SELECT * FROM fornecedores_produtos')

    def consulta_fornecedores_ativos(self):
        print(f'{40*"*"} Consultar fornecedores ativos {40*"*"} ')
        self._executar_consulta('SELECT * FROM fornecedores WHERE ativo = 1')

    def consulta_clientes_ativos(self):
        print(f'{40*"*"} Consultar todos os clientes ativos {40*"*"} ')
        self._executar_consulta('''
                                SELECT * 
                                FROM nota_fiscal.clientes 
                                WHERE ativo = 1
                                ''')

    def consulta_estoque_disponivel(self):
        print(f'{40*"*"} Selecionar produtos ativos com estoque disponível {40*"*"} ')
        self._executar_consulta('''
                                SELECT * 
                                FROM produtos 
                                WHERE ativo = 1 
                                AND saldo_estoque > 0
                                ''')

    def consulta_notas_emitidas_data(self):
        print(f'{40*"*"} Selecionar notas fiscais emitidas em uma data específica {40*"*"} ')
        self._executar_consulta('''
                                SELECT * 
                                FROM notas_fiscais 
                                WHERE data_emissao >= "2023-01-01" 
                                AND data_emissao <= "2023-01-31"
                                ''')

    def consulta_valor_de_venda_do_ano(self):
        print(f'{40*"*"} Valor total vendido e entregue em um determinado ano {40*"*"} ')
        self._executar_consulta('''
                                SELECT SUM(valor_total) AS total_vendido
                                FROM nota_fiscal.pedidos
                                WHERE YEAR(data_compra) = 2023 
                                AND status_pedido = "ENTREGUE"
                                ''')

    def consulta_clientes_por_estado(self):
        print(f'{40*"*"} Consulta de todos os clientes de um estado {40*"*"} ')
        self._executar_consulta('''
                                SELECT *
                                FROM nota_fiscal.clientes
                                WHERE uf = "SP"
                                ''')

    def consulta_produtos_por_categoria(self):
        print(f'{40*"*"} Consultar todos os produtos de uma categoria específica {40*"*"} ')
        self._executar_consulta('''
                                SELECT * 
                                FROM nota_fiscal.produtos 
                                WHERE categoria = "ELETRÔNICOS"
                                ''')

    def consulta_pedidos_por_ano(self):
        print(f'{40*"*"} Total de pedidos para o ano de 2023 {40*"*"} ')
        self._executar_consulta('''
                                SELECT COUNT(*) AS total_pedidos
                                FROM nota_fiscal.pedidos
                                WHERE YEAR(data_compra) = 2023
                                ''')

    def consulta_pedidos_entregues_por_mes(self):
        print(f'{40*"*"} Consultar todos os pedidos entregues no último mês {40*"*"} ')
        self._executar_consulta('''
                                SELECT *
                                FROM nota_fiscal.pedidos
                                WHERE status_pedido = "ENTREGUE" 
                                AND data_compra >= CURDATE() - INTERVAL 1 MONTH
                                ''')

    def consulta_compras_por_clientes_id(self):
        print(f'{40*"*"} Calcular o total de compras feitas por um cliente específico {40*"*"} ')
        self._executar_consulta('''
                                SELECT c.nome, c.tipo, COUNT(p.id) AS total_compras
                                FROM nota_fiscal.clientes c
                                JOIN nota_fiscal.pedidos p ON c.id = p.clientes_id
                                GROUP BY c.id
                                ''')

    def consulta_estoque_do_fornecedor(self):
        print(f'{40*"*"} Listar os produtos de um fornecedor específico com suas quantidades em estoque {40*"*"} ')
        self._executar_consulta('''
                                SELECT f.razao_social, fp.produtos_id, pr.nome, pr.saldo_estoque
                                FROM nota_fiscal.fornecedores_produtos fp
                                JOIN nota_fiscal.produtos pr ON fp.produtos_id = pr.id
                                JOIN nota_fiscal.fornecedores f ON fp.fornecedores_id = f.id
                                WHERE fp.fornecedores_id = 1
                                ''')

    def consulta_qnt_tipo_cliente(self):
        print(f'{40*"*"} Quantidade de clientes PF e PJ {40*"*"} ')
        self._executar_consulta('''
                                SELECT c.tipo, COUNT(c.tipo) AS total_clientes
                                FROM nota_fiscal.clientes c
                                JOIN nota_fiscal.pedidos p ON c.id = p.clientes_id
                                GROUP BY c.tipo
                                ''')

    def consulta_total_gasto_por_cliente(self):
        print(f'{40*"*"} Consulta para Obter o Total Gasto por Cliente {40*"*"} ')
        self._executar_consulta('''
                                SELECT
                                    clientes.id AS cliente_id,
                                    clientes.tipo,
                                    clientes.nome AS nome_cliente,
                                    SUM(pedidos.valor_total) AS total_gasto
                                FROM clientes
                                JOIN pedidos ON clientes.id = pedidos.clientes_id
                                GROUP BY cliente_id, nome_cliente
                                ''')

    def consulta_produtos_mais_vendidos(self):
        print(f'{40*"*"} Consulta para Encontrar os Produtos Mais Vendidos {40*"*"} ')
        self._executar_consulta('''
                                SELECT
                                    produtos.nome AS nome_produto,
                                    SUM(pedidos_produtos.quantidade) AS total_vendido
                                FROM produtos
                                JOIN pedidos_produtos ON produtos.id = pedidos_produtos.produtos_id
                                GROUP BY nome_produto
                                ORDER BY total_vendido DESC
                                ''')

    def consulta_media_precos_por_categoria(self):
        print(f'{40*"*"} Consulta para Calcular a Média de Preço dos Produtos por Categoria {40*"*"} ')
        self._executar_consulta('''
                                SELECT categoria, AVG(preco) AS media_preco
                                FROM produtos
                                GROUP BY categoria
                                ''')

    def consulta_cliente_com_maior_gasto_por_periodo(self):
        print(f'{40*"*"} Consulta para Encontrar os Clientes com Maior Valor Gasto em um período {40*"*"} ')
        self._executar_consulta('''
                                SELECT
                                    clientes.id AS cliente_id,
                                    clientes.nome AS nome_cliente,
                                    SUM(pedidos.valor_total) AS total_gasto
                                FROM clientes
                                JOIN pedidos ON clientes.id = pedidos.clientes_id
                                WHERE pedidos.data_compra BETWEEN "2023-01-01" AND "2023-12-31"
                                GROUP BY cliente_id, nome_cliente
                                ORDER BY total_gasto DESC
                                LIMIT 5
                                ''')

    def executar_todas_consultas(self):
        self.consulta_clientes()
        self.consulta_pedidos()
        self.consulta_produtos()
        self.consulta_notas_fiscais()
        self.consulta_pedidos_produtos()
        self.consulta_fornecedores_produtos()
        self.consulta_fornecedores_ativos()
        self.consulta_clientes_ativos()
        self.consulta_estoque_disponivel()
        self.consulta_notas_emitidas_data()
        self.consulta_valor_de_venda_do_ano()
        self.consulta_clientes_por_estado()
        self.consulta_produtos_por_categoria()
        self.consulta_pedidos_por_ano()
        self.consulta_pedidos_entregues_por_mes()
        self.consulta_compras_por_clientes_id()
        self.consulta_estoque_do_fornecedor()
        self.consulta_qnt_tipo_cliente()
        self.consulta_total_gasto_por_cliente()
        self.consulta_produtos_mais_vendidos()
        self.consulta_media_precos_por_categoria()
        self.consulta_cliente_com_maior_gasto_por_periodo()



# Criar uma instância da classe
consultas = ConsultasNotasFiscais(conexao, cursor)

# Executar todas as consultas
consultas.consulta_clientes()


# ## Atualizando dados nas tabelas


sql_atualizacao_clientes = '''
UPDATE nota_fiscal.clientes
SET nome_completo = "MERCADINHO DE JOÃOZINHO"
WHERE id = 1;
'''
cursor.execute(sql_atualizacao_clientes)

resultado = cursor.fetchall()

for dado in resultado:
    print(dado)








# SEMPRE FECHE A CONEXÃO COM O BANCO DE DADOS.

cursor.close()
conexao.close()





