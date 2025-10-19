# 🕵️ Vigilante de Gastos

**Vigilante de Gastos** é um sistema de monitoramento financeiro inteligente que identifica **anomalias em despesas pessoais ou corporativas** em tempo real.  
Ele combina **um backend em FastAPI**, **um dashboard em Streamlit** e **scripts de simulação de eventos**, oferecendo uma visão completa do comportamento financeiro.

---

## 🚀 Funcionalidades Principais

- 📊 **Dashboard interativo (Streamlit)**

  - Exibe métricas de gastos, gráficos e alertas de anomalias.
  - Visualização de histórico e despesas recentes.
  - Design moderno com sidebar escura e interface clara e fluida.

- ⚙️ **API (FastAPI)**

  - Recebe e armazena eventos de despesas.
  - Identifica anomalias (valores fora do padrão).
  - Pode funcionar com ou sem autenticação JWT.

- 🤖 **Simulador de eventos (Python)**
  - Envia automaticamente gastos aleatórios para a API.
  - Permite testar o sistema de detecção de anomalias em tempo real.

---

## 🧩 Estrutura do Projeto

vigilante-de-gastos/
│
├── backend/
│ ├── main.py # API FastAPI (eventos e autenticação)
│ ├── database.db # Banco SQLite (gerado automaticamente)
│ ├── requirements.txt # Dependências do backend
│
├── dashboard/
│ ├── app.py # Interface Streamlit (frontend)
│ ├── README.md # Este arquivo
│
├── simulator/
│ └── send_events.py # Script para envio automático de eventos
│
└── README.md

## 🏗️ Arquitetura

```text
[Simulador de Eventos] → [API FastAPI] → [Banco de Dados SQLite] → [Dashboard Streamlit]

⚙️ Instalação
1️⃣ Clone o repositório
git clone https://github.com/seuusuario/vigilante-de-gastos.git
cd vigilante-de-gastos

2️⃣ Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

3️⃣ Instale as dependências
Backend:
cd backend
pip install -r requirements.txt

Dashboard:
cd ../dashboard
pip install streamlit pandas requests

Simulador:
cd ../simulator
pip install requests

▶️ Execução
🧠 1. Inicie a API FastAPI
cd backend
uvicorn main:app --reload


API rodará em:
👉 http://127.0.0.1:8000

💸 2. Execute o simulador de eventos
cd simulator
python send_events.py


O script começará a enviar despesas automaticamente para a API.

📊 3. Abra o dashboard Streamlit
cd dashboard
streamlit run app.py
```
