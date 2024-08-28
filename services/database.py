import psycopg2 as ps


conn = ps.connect(
    dbname = 'tijolada',
    user ='xxxxxxxx',
    password = 'xxxxxxxx',
    host = 'localhost',
    port = '5432' 
)
cursor = conn.cursor()
erro = ps.Error