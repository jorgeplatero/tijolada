import psycopg2 as ps


conn = ps.connect(
    dbname = 'loja_materiais_construcao',
    user ='postgres',
    password = 'postgres',
    host = 'localhost',
    port = '5432' 
)
cursor = conn.cursor()
erro = ps.Error