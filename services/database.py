import psycopg2 as ps


conn = ps.connect(
    dbname = 'building_supply_stock',
    user ='postgres',
    password = 'postgres',
    host = 'localhost',
    port = '5432' 
)
cursor = conn.cursor()