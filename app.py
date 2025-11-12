import os
import psycopg2
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        db_url = os.environ["DATABASE_URL"]
        conn = psycopg2.connect(db_url)
        return "Conexiune reușită la PostgreSQL!"
    except Exception as e:
        return f"Eroare la conectare: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)