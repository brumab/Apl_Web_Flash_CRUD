import pymysql
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DB"),
        port=int(os.getenv("MYSQL_PORT", 3306)),
        cursorclass=pymysql.cursors.DictCursor
    )

mysql = MySQL(app)

# =========================
# Inicialização segura (Flask 3)
# =========================
db_initialized = False

def create_table():
    cur = mysql.connection.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL
        )
    """)
    mysql.connection.commit()
    cur.close()

@app.before_request
def init_db():
    global db_initialized
    if not db_initialized:
        try:
            create_table()
            db_initialized = True
        except Exception as e:
            print("Erro ao inicializar banco:", e)

# =========================
# Rotas
# =========================
@app.route("/test-db")
def test_db():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT 1")
        cur.close()
        return "✅ Conectado ao MySQL Aiven com sucesso"
    except Exception as e:
        return f"❌ Erro MySQL: {e}"

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students ORDER BY id DESC")
    students = cur.fetchall()
    cur.close()
    return render_template('index.html', students=students)

@app.route('/inserir', methods=['POST'])
def inserir():
    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO students (name, email, phone) VALUES (%s, %s, %s)",
        (request.form['name'], request.form['email'], request.form['phone'])
    )
    mysql.connection.commit()
    cur.close()
    flash("Aluno cadastrado com sucesso!")
    return redirect(url_for('index'))

@app.route('/atualizar', methods=['POST'])
def atualizar():
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE students
        SET name=%s, email=%s, phone=%s
        WHERE id=%s
    """, (
        request.form['name'],
        request.form['email'],
        request.form['phone'],
        request.form['id']
    ))
    mysql.connection.commit()
    cur.close()
    flash("Aluno atualizado com sucesso!")
    return redirect(url_for('index'))

@app.route('/excluir/<int:id_dado>', methods=['POST'])
def excluir(id_dado):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", (id_dado,))
    mysql.connection.commit()
    cur.close()
    flash("Aluno excluído com sucesso!")
    return redirect(url_for('index'))
