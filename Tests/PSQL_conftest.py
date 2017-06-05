import psycopg2 
from addok import hooks 
import addok-psql-store
from addok.config import config

def psqlTest_configure():
	config.DOCUMENT_STORE_PYPATH = 'addok-psql-store.PSQLStore'
	config.PG_CONFIG = 'dbname=addok user=addok host=localhost password=addok'
	config.PG_TABLE = 'addok'
	
	hooks.register(addok-psql-store)
	
def createTableTest(psqlTest_configure):
	with psycopg2.connect(**psqlTest_configure) as con:
		with con.cursor() as cur:
			cur.execute("CREATE TABLE test;")
			
	

	

	

