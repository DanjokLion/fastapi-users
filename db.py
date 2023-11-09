from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

class Database():
    def __init__(self):
        self.engine('sqlite://app/database.db')
        self.__initialise_db()

    def __initialise_db(self):
        with self.engine.connect() as conn:
            conn.execute(text('CREATE TABLE IF NOT EXIST reviews (name VARCHAR(60), message TEXT)'))
            conn.execute(text('CREATE TABLE IF NOT EXIST users (name VARCHAR(60), email TEXT, age INTEGER, is_subscribed BOOLEAN)'))

    def add_feedback(self, name, message):
        with self.engine.connect() as conn:
            conn.execute(text('INSERT INTO reviews (name, message) VALUES (:n, :m)'), {'n': name, 'm': message})
            conn.commit()

    def get_all_reviews(self):
        with self.engine.connect() as conn:
            return conn.execute(text('SELECT name, message FROM reviews')).all()
        
    def add_user(self, usr_model):
        with self.engine.connect() as conn:
            conn.execute(text('INSERT INTO users (name, email, age, is_subscribed) VALUES(:name, :email, :age, :is_subscribed)'), usr_model.__dict__)
            conn.commit()

    def get_all_users(self):
        with self.engine.connect() as conn:
            users = conn.execute(text('SELECT * FROM users')).all()
        attrs = ('name', 'email', 'age', 'is_subscribed')
        return [dict(zip(attrs, u)) for u in users]