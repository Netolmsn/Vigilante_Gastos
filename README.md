# 🕵️ Vigilante de Gastos

Um sistema inteligente de **monitoramento de despesas em tempo real**, com **detecção de anomalias**, **painel interativo** e **envio de eventos**, desenvolvido com **FastAPI**, **Streamlit** e **Machine Learning**.

---

## 🚀 Visão Geral

O **Vigilante de Gastos** tem como objetivo ajudar usuários e empresas a identificar **gastos anormais ou suspeitos**.  
Ele funciona em 3 partes principais:

1. **🧠 Backend (API - FastAPI)**  
   Responsável por receber eventos de gastos, processá-los, calcular _scores de anomalia_ e armazenar os resultados.

2. **📊 Dashboard (Streamlit)**  
   Interface interativa que exibe métricas, gráficos, histórico e anomalias detectadas em tempo real.

3. **💸 Envio de Despesas (Streamlit App)**  
   Aplicativo auxiliar que permite inserir manualmente novos gastos (ou simular dados) para alimentar o sistema.

---

## 🧩 Estrutura do Projeto

vigilante_streaming/
│
├── app.py # Servidor FastAPI principal (API)
├── dashboard.py # Dashboard em Streamlit
├── streamlit_app.py # Envio manual de gastos
│
├── models/ # (Opcional) Modelos ML e funções de predição
├── data/ # Dados salvos (sqlite ou csv)
│
├── README.md # Este arquivo
└── requirements.txt # Dependências do projeto

yaml
Copiar código

---

## ⚙️ Instalação

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seuusuario/vigilante_streaming.git
cd vigilante_streaming
2️⃣ Criar ambiente virtual (opcional, mas recomendado)
bash
Copiar código
python -m venv venv
Ativar:

Windows (PowerShell ou Git Bash):

bash
Copiar código
venv\Scripts\activate
Linux / macOS:

bash
Copiar código
source venv/bin/activate
3️⃣ Instalar dependências
bash
Copiar código
pip install fastapi uvicorn streamlit pandas scikit-learn passlib bcrypt pyjwt
🧠 Como Executar o Projeto
O sistema é composto por três componentes que devem ser executados em terminais separados. Siga a ordem abaixo para ver o streaming em ação.

1️⃣ Rodar o Servidor FastAPI (API)
Este é o backend responsável pela lógica e detecção de anomalias.

Bash
uvicorn app:app --reload
💡 Servidor rodando em: http://127.0.0.1:8000

2️⃣ Rodar a Simulação de Eventos (demo.py)
Em um segundo terminal, execute este script. Ele começará a enviar eventos de gastos simulados para a API a cada 2 segundos, alimentando o sistema.

Bash
python demo.py

3️⃣ Rodar o Dashboard (Painel Principal)
Em um terceiro terminal, inicie o painel de visualização.

Bash
streamlit run dashboard.py
📊 Acesse o Dashboard em: http://localhost:8501

💸 (Opcional) App de Envio Manual
Se quiser enviar despesas manualmente, use o streamlit_app.py em um quarto terminal.

Bash
streamlit run streamlit_app.py

📈 Funcionalidades Principais
✅ Detecção de anomalias em gastos usando aprendizado de máquina
✅ Painel interativo com métricas, gráficos e histórico
✅ Autenticação de usuários (opcional, via JWT)
✅ Registro manual e automático de despesas
✅ Visualização de últimas anomalias detectadas
✅ Interface moderna e responsiva

📦 Tecnologias Utilizadas
Tecnologia	Função
🧠 FastAPI	Backend / API
📊 Streamlit	Dashboard e app de envio
📈 Pandas	Manipulação de dados
🤖 Scikit-Learn	Modelo de detecção de anomalias
🔐 Passlib + JWT	Autenticação (opcional)

🧰 Endpoints da API (principais)
Método	Rota	Descrição
POST	/event	Envia um novo evento de gasto
GET	/events	Retorna todos os eventos registrados
POST	/token	Gera token de autenticação (opcional)

```
