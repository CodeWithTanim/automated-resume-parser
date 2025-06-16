# app/database.py

import sqlite3
from flask import g

DATABASE = 'resumes.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def init_db(app):
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS resumes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT,
                phone TEXT,
                skills TEXT
            )
        ''')
        db.commit()

    @app.teardown_appcontext
    def close_connection(exception):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()

def insert_resume_data(data):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        INSERT INTO resumes (name, email, phone, skills)
        VALUES (?, ?, ?, ?)
    ''', (
        data.get('name'),
        data.get('email'),
        data.get('phone'),
        ', '.join(data.get('skills'))
    ))
    db.commit()
