import psycopg2 as ps
import warnings
warnings.filterwarnings('ignore')


#conexao com banco de dados
#---------------------------------------------------------------
conn = ps.connect(
    dbname = 'tijolada',
    user ='postgres',
    password = 'postgres',
    host = 'localhost',
    port = '5432' 
)
cursor = conn.cursor()
erro = ps.Error