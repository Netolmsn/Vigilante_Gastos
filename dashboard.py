import streamlit as st
import pandas as pd
import requests
from datetime import datetime

# ====================================================
# CONFIGURAÇÕES GERAIS
# ====================================================
API_URL = "http://127.0.0.1:8000"
st.set_page_config(page_title="Vigilante de Gastos", layout="wide")

# ====================================================
# CSS - Sidebar dark elegante + container otimizado
# ====================================================
st.markdown("""
<style>
/* Sidebar dark elegante */
section[data-testid="stSidebar"] {
    background-color: #1E1E2F !important;
    color: white !important;
}

/* Ícones e textos brancos no menu lateral */
section[data-testid="stSidebar"] .stRadio label {
    color: white !important;
    font-weight: 600;
    font-size: 16px;
}

/* Cabeçalhos no menu lateral */
section[data-testid="stSidebar"] .stMarkdown {
    color: white !important;
}

/* Fundo principal */
.main {
    background-color: #FAFAFA;
}

/* Títulos */
h1, h2, h3 {
    color: #222;
}

/* ======= Container com espaçamento padrão ======= */
div.block-container {
    max-width: 1600px !important;
    padding-left: 3rem !important;
    padding-right: 3rem !important;
    margin-top: 3rem !important; /* restaurado */
    padding-top: 1rem !important;
}

/* Tabelas mais legíveis */
[data-testid="stDataFrame"] {
    background-color: white !important;
    border-radius: 8px !important;
    box-shadow: 0 0 8px rgba(0,0,0,0.05);
}
</style>
""", unsafe_allow_html=True)

# ====================================================
# MENU LATERAL COM ÍCONES
# ====================================================
menu = st.sidebar.radio(
    "📋 Navegação",
    [
        "🏠 Dashboard",
        "⚙️ Configurações",
        "🔑 Login (futuro)"
    ],
    index=0,
)

st.sidebar.markdown("---")
st.sidebar.markdown("🕵️ **Vigilante de Gastos**")

# ====================================================
# 🔒 ABA DE LOGIN (DESATIVADA)
# ====================================================
if menu == "🔑 Login (futuro)":
    st.title("🔐 Login (futuro)")
    st.info("Esta aba será ativada quando a autenticação estiver implementada.")
    """
    # Exemplo futuro de login:
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        st.write("Função de autenticação será adicionada aqui.")
    """
    st.stop()

# ====================================================
# FUNÇÃO PARA OBTER EVENTOS DA API
# ====================================================
def get_events():
    try:
        r = requests.get(f"{API_URL}/events")
        if r.status_code == 200:
            df = pd.DataFrame(r.json())
            if not df.empty:
                df["timestamp"] = pd.to_datetime(df["timestamp"])
            return df
        else:
            st.error(f"Erro ao buscar dados: {r.text}")
            return pd.DataFrame()
    except Exception as e:
        st.error(f"Erro ao conectar à API: {e}")
        return pd.DataFrame()

# ====================================================
# DASHBOARD PRINCIPAL
# ====================================================
if menu == "🏠 Dashboard":
    st.title("📊 Vigilante de Gastos - Painel Principal")

    df = get_events()
    if df.empty:
        st.info("Nenhum gasto registrado ainda.")
        st.stop()

    # ======================
    # Métricas superiores
    # ======================
    col1, col2, col3 = st.columns(3)

    total_anomalias = df["alerta"].sum()
    score_medio = round(df["score"].mean(), 2)
    ultima_atualizacao = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with col1:
        st.metric("🚨 Anomalias Detectadas", total_anomalias)
    with col2:
        st.metric("📈 Score Médio", score_medio)
    with col3:
        st.metric("🕒 Última Atualização", ultima_atualizacao)

    st.markdown("---")

    # ======================
    # Gráfico + Última Anomalia
    # ======================
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("💸 Gastos ao Longo do Tempo")
        st.line_chart(df.set_index("timestamp")[["valor"]])

    with col2:
        st.subheader("🚨 Última Anomalia Detectada")
        ultimo_alerta = df[df["alerta"] == 1].sort_values("timestamp", ascending=False).head(1)
        if not ultimo_alerta.empty:
            row = ultimo_alerta.iloc[0]
            st.error(f"**Categoria:** {row['categoria']}  \n**Valor:** R$ {row['valor']:.2f}")
            st.write(f"**Explicação:** {row['explicacao']}")
            st.progress(int(row['score']))
        else:
            st.success("Nenhuma anomalia recente detectada ✅")

    # ======================
    # Histórico de Despesas
    # ======================
    st.markdown("### 📋 Histórico de Despesas")
    st.dataframe(
        df[["timestamp", "categoria", "valor", "score", "alerta", "explicacao"]],
        use_container_width=True,
        height=350,
    )

    st.markdown("---")

    # ======================
    # Despesas Recentes
    # ======================
    st.subheader("🧾 Despesas Recentes")
    recentes = df.sort_values("timestamp", ascending=False).head(5)
    st.table(
        recentes[["timestamp", "categoria", "valor"]]
        .rename(columns={
            "timestamp": "Data",
            "categoria": "Categoria",
            "valor": "Valor (R$)"
        })
    )

# ====================================================
# ABA DE CONFIGURAÇÕES
# ====================================================
elif menu == "⚙️ Configurações":
    st.title("⚙️ Configurações")
    st.info("Aqui você poderá ajustar opções futuras, como notificações e limites de alerta.")
