import sqlite3

conn = sqlite3.connect("vigilante.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS gastos (id INTEGER PRIMARY KEY, valor REAL)")
c.execute("INSERT INTO gastos (valor) VALUES (?)", (120.5,))
conn.commit()
rows = c.execute("SELECT * FROM gastos").fetchall()
print(rows)
conn.close()
