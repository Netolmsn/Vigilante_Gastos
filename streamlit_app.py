import streamlit as st
import pandas as pd
import sqlite3
import time
from datetime import datetime

DB_PATH = "vigilante.db"
st.set_page_config(page_title="Vigilante de Gastos", layout="wide")
st.title("🕵️ Vigilante de Gastos em Streaming")

def load_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM gastos ORDER BY id DESC LIMIT 200", conn)
    conn.close()
    if not df.empty:
        df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df

placeholder = st.empty()
while True:
    with placeholder.container():
        df = load_data()
        if df.empty:
            st.info("Nenhum gasto registrado ainda. Aguarde o demo enviar dados...")
        else:
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Total de registros", len(df))
            with col2:
                st.metric("Última atualização", datetime.now().strftime("%H:%M:%S"))
            st.subheader("📈 Gastos recentes")
            st.dataframe(df[["timestamp", "valor", "categoria", "score", "alerta", "explicacao"]])
            st.line_chart(df.set_index("timestamp")[["valor"]])
        time.sleep(3)
