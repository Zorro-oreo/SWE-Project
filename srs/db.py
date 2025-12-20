import sqlite3
from flask import g
from srs.config import DATABASE_PATH

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(arg=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()