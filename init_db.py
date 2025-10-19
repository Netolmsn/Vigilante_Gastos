import sqlite3

DB_PATH = "vigilante.db"

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    hashed_password TEXT NOT NULL
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS gastos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT NOT NULL,
    valor REAL NOT NULL,
    categoria TEXT NOT NULL,
    score REAL,
    alerta INTEGER,
    explicacao TEXT
)
""")

conn.commit()
conn.close()

print("✅ Banco de dados 'vigilante.db' inicializado com sucesso!")
