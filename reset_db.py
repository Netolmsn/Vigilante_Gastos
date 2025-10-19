import sqlite3
from passlib.context import CryptContext
import os

DB_PATH = "vigilante.db"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ================================================
# 1️⃣ Apaga o banco antigo (se existir)
# ================================================
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)
    print("🗑️ Banco de dados antigo removido.")

# ================================================
# 2️⃣ Cria o novo banco e tabelas
# ================================================
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

# Tabela de usuários
c.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    hashed_password TEXT NOT NULL
)
""")

# Tabela de gastos
c.execute("""
CREATE TABLE gastos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    valor REAL,
    categoria TEXT,
    score REAL,
    alerta INTEGER,
    explicacao TEXT
)
""")

print("✅ Tabelas criadas com sucesso.")

# ================================================
# 3️⃣ Cria usuário padrão
# ================================================
username = "teste123"
password = "1234"
hashed_password = pwd_context.hash(password)

c.execute("INSERT INTO users (username, hashed_password) VALUES (?, ?)", (username, hashed_password))
conn.commit()
conn.close()

print(f"👤 Usuário criado com sucesso:\n   Usuário: {username}\n   Senha: {password}")
print("🏁 Banco pronto para uso. Agora rode:\n   uvicorn app:app --reload\n   python demo.py")
