import sqlite3
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

conn = sqlite3.connect("vigilante.db")
c = conn.cursor()

username = input("Novo usuário (username): ")
password = input("Password: ")

hashed_password = pwd_context.hash(password)

try:
    c.execute("INSERT INTO users (username, hashed_password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    print(f"✅ Usuário '{username}' criado com sucesso!")
except sqlite3.IntegrityError:
    print(f"⚠️ Usuário '{username}' já existe — escolha outro nome.")

conn.close()
