from flask import Flask, g
import sqlite3
from config import DATABASE_PATH
from controllers.user_controller import user_bp

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(arg=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()

app = Flask(__name__)

app.teardown_appcontext(close_db)

app.register_blueprint(user_bp)

@app.route("/")
def home():
    return ""

if __name__ == "__main__":
    app.run(debug=True)