from flask import Flask, g
import sqlite3
from config import DATABASE_PATH

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(arg=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    with app.open_resource("database\\schema.sql", mode="r") as f:
        db.executescript(f.read())
    db.commit()

app = Flask(__name__)

app.teardown_appcontext(close_db)

@app.route("/init")
def init():
    init_db()
    return "DB initialized."

@app.route("/")
def home():
    return ""

if __name__ == "__main__":
    app.run(debug=True)