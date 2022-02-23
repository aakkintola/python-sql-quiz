import psycopg2
from src.director import Director

conn = psycopg2.connect(dbname = 'imdb_development', user = 'akintola')
