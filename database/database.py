import psycopg2
def connection():
    connection = psycopg2.connect(
        user="postgres",
        password="admin",
        host="localhost",
        port="5432",
        database="employe_json")
    return connection


#hello niteen sir