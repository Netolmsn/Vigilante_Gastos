from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.security import OAuth2PasswordRequestForm   # 🔒 Desativado
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
from passlib.context import CryptContext                  # 🔒 Desativado
import sqlite3
import jwt                                                 # 🔒 Desativado
from sklearn.ensemble import IsolationForest
import numpy as np

# =========================================
# Configurações básicas
# =========================================
# SECRET_KEY = "segredo-super-seguro"                       # 🔒 Desativado
# ALGORITHM = "HS256"                                       # 🔒 Desativado
DB_PATH = "vigilante.db"

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")   # 🔒 Desativado

app = FastAPI(title="🕵️ Vigilante de Gastos - API (Sem autenticação)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================================
# Modelos Pydantic
# =========================================
class Gasto(BaseModel):
    valor: float
    categoria: str

class GastoProcessado(BaseModel):
    timestamp: str
    valor: float
    categoria: str
    score: float
    alerta: int
    explicacao: str

# =========================================
# Banco de Dados
# =========================================
def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# =========================================
# 🔒 Autenticação (comentada)
# =========================================
"""
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user(username: str):
    conn = get_db_connection()
    user = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
    conn.close()
    return user

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user["hashed_password"]):
        return False
    return True

def create_access_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password

    if not authenticate_user(username, password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    token = create_access_token({"sub": username})
    return {"access_token": token, "token_type": "bearer"}
"""

# =========================================
# Modelo de Anomalia (Isolation Forest)
# =========================================
model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
trained = False

def train_model_if_needed():
    global trained
    if trained:
        return

    conn = get_db_connection()
    data = conn.execute("SELECT valor FROM gastos").fetchall()
    conn.close()
    if len(data) > 5:
        X = np.array([d["valor"] for d in data]).reshape(-1, 1)
        model.fit(X)
        trained = True

# =========================================
# Funções principais
# =========================================
def save_event_db(e: GastoProcessado):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("""
        INSERT INTO gastos (timestamp, valor, categoria, score, alerta, explicacao)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (e.timestamp, e.valor, e.categoria, e.score, e.alerta, e.explicacao))
    conn.commit()
    conn.close()

def process_event(valor, categoria):
    train_model_if_needed()
    X = np.array([[valor]])
    score = float(model.decision_function(X)[0]) if trained else 0.0
    pred = int(model.predict(X)[0]) if trained else 1
    alerta = 1 if pred == -1 else 0
    explicacao = "Anomalia detectada!" if alerta else "Gasto normal"
    return GastoProcessado(
        timestamp=datetime.now().isoformat(),
        valor=valor,
        categoria=categoria,
        score=score,
        alerta=alerta,
        explicacao=explicacao
    )

# =========================================
# Rotas
# =========================================
@app.post("/event")
def post_event(gasto: Gasto):
    try:
        processed = process_event(gasto.valor, gasto.categoria)
        save_event_db(processed)
        return {"status": "ok", "data": processed.dict()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/events")
def get_events():
    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM gastos ORDER BY id DESC LIMIT 200").fetchall()
    conn.close()
    return [dict(r) for r in rows]

@app.get("/")
def root():
    return {"msg": "API Vigilante de Gastos ativa 🚀 (sem autenticação)"}
