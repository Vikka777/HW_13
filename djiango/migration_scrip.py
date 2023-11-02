import pymongo
import psycopg2

def connect_to_mongodb():
    client = pymongo.MongoClient("mongodb://localhost:5432/")
    db = client["Postgres"]
    return db

def connect_to_postgresql():
    conn = psycopg2.connect(
        database="Postgres",
        user="vikkimrrr7",
        password="VikaVikaGo78",
        host="localhost",
        port="5432"
    )
    return conn

def migrate_data():
    mongodb = connect_to_mongodb()
    postgresql = connect_to_postgresql()

    mongodb_data = mongodb["quotes"].find()

    cursor = postgresql.cursor()
    for data in mongodb_data:
        text = data["text"]
        author = data["author"]

        # Виконати INSERT запит у таблицю PostgreSQL (приклад для таблиці "myapp_quote")
        cursor.execute("INSERT INTO mysite_quote (text, author_id) VALUES (%s, %s)",
                       (text, author))

    postgresql.commit()
    cursor.close()

if __name__ == "__main__":
    migrate_data()