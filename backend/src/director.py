import psycopg2

conn = psycopg2.connect(dbname = 'imdb_development', user = 'akintola')
cursor = conn.cursor()

def find_all_attributes():
    statement = (""" 
                      SELECT * FROM directors 
                      JOIN movie_directors ON directors.id = movie_directors.director_id
                      JOIN movies ON movies.id = movie_directors.movie_id
                      WHERE movies.title = 'The Martian';
    """)
    cursor.execute(statement)
    return cursor.fetchall()

def average_runtime():
    statement = ("""
                    SELECT AVG(runtime) FROM movies
                    JOIN movie_directors ON movie_directors.movie_id = movies.id
                    JOIN directors ON movie_directors.director_id = directors.id
                    WHERE directors.name = 'Steven Soderbergh';
    """)
    cursor.execute(statement)
    return cursor.fetchall()

def top_3_runtime(): 
    statement = (""" 
                SELECT directors.name, AVG(movies.runtime) FROM movies 
                JOIN movie_directors ON movie_directors.movie_id = movies.id
                JOIN directors ON movie_directors.director_id = directors.id
                GROUP BY directors.name
                HAVING COUNT(*) > 3
                ORDER BY AVG(movies.runtime) DESC
                LIMIT 3;
    """)
    cursor.execute(statement)
    return cursor.fetchall()

class Director():
    __table__ = 'directors'
    columns = [id, name]
    
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def first_name(self):
        
