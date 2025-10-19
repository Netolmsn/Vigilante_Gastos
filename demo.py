import requests
import time
import random
from datetime import datetime

API_URL = "http://127.0.0.1:8000"

# =========================================
# 🔒 Autenticação (comentada)
# =========================================
"""
USERNAME = "teste123"
PASSWORD = "1234"

def get_token(username, password):
    '''Obtém o token de autenticação da API'''
    print("🔑 Obtendo token...")
    r = requests.post(f"{API_URL}/token", data={"username": username, "password": password})
    if r.status_code != 200:
        print(f"❌ Erro ao autenticar: {r.text}")
        return None
    print("✅ Token obtido com sucesso!\n")
    return r.json()["access_token"]
"""

# =========================================
# Envio de eventos (sem autenticação)
# =========================================
def send_event(valor, categoria):
    data = {"valor": valor, "categoria": categoria}
    # headers = {"Authorization": f"Bearer {token}"}  # 🔒 Desativado
    try:
        r = requests.post(f"{API_URL}/event", json=data)  # sem autenticação
        if r.status_code == 200:
            print(f"✅ Enviado: {valor:.2f} ({categoria})")
        else:
            print(f"⚠️ Erro: {r.status_code} -> {r.text}")
    except Exception as e:
        print(f"❌ Falha de conexão: {e}")

# =========================================
# Loop principal
# =========================================
def main():
    print("🚀 Iniciando envio de eventos para Vigilante de Gastos (sem autenticação)...")

    # 🔒 Código de autenticação comentado
    """
    token = get_token(USERNAME, PASSWORD)
    if not token:
        print("❌ Encerrando execução: falha ao autenticar.")
        return

    headers = {"Authorization": f"Bearer {token}"}
    test_response = requests.get(f"{API_URL}/events", headers=headers)
    if test_response.status_code == 401:
        print("❌ Token inválido — verifique usuário e senha.")
        return
    else:
        print("🔒 Token válido! Enviando eventos...\n")
    """

    categorias = ["mercado", "lazer", "transporte", "contas", "investimento"]
    while True:
        valor = round(random.uniform(10, 500), 2)
        categoria = random.choice(categorias)
        send_event(valor, categoria)
        time.sleep(2)

if __name__ == "__main__":
    main()
