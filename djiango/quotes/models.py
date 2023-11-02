import psycopg2
from mongoengine import connect
#StringField, ListField, ReferenceField, DateTimeField
from django.contrib.auth.models import AbstractUser
from django.db import models

connect('cluster0', host='mongodb+srv://vikkimrrr7:VikaVikaGo78@cluster0.kvolsxm.mongodb.net/')

import psycopg2

db_params = {
    'dbname': 'postgres',
    'user': 'vikkimrrr77',
    'password': 'VikaVikaGo78',
    'host': 'localhost',
    'port': '5432'
}

connection = None

try:
    connection = psycopg2.connect(**db_params)
    print("Підключено до бази даних PostgreSQL")

    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print(f"Версія PostgreSQL: {record[0]}")

except (Exception, psycopg2.Error) as error:
    print(f"Помилка підключення до бази даних: {error}")

finally:
    if connection:
        cursor.close()
        connection.close()
        print("З'єднання закрито")

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Quote(models.Model):
    text = models.TextField()
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE)

    def __str(self):
        return self.text[:50]

class CustomUser(AbstractUser):
    pass
