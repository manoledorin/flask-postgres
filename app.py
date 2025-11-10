from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        conn = psycopg2.connect(
            host="db",
            database="devopsdb",
            user="devopsuser",
            password="devopspass"
        )
        return "Conexiune reușită la PostgreSQL!"
    except Exception as e:
        return f"Eroare la conectare: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)