@echo off
title Vigilante de Gastos - Inicialização
color 0A
echo ================================================
echo      🕵️ INICIANDO O VIGILANTE DE GASTOS
echo ================================================
echo.

REM --- Ativar ambiente virtual (se estiver usando) ---
REM call venv\Scripts\activate

echo 🚀 Iniciando servidor FastAPI...
start cmd /k "uvicorn app:app --reload"

timeout /t 5 /nobreak >nul

echo 📊 Iniciando Dashboard (Streamlit)...
start cmd /k "streamlit run dashboard.py"

timeout /t 3 /nobreak >nul

echo 💸 Iniciando aplicativo de envio manual...
start cmd /k "streamlit run streamlit_app.py"

echo.
echo ✅ Todos os serviços foram iniciados!
echo -----------------------------------------------
echo 🌐 API:          http://127.0.0.1:8000
echo 📊 Dashboard:    http://localhost:8501
echo 💸 Envio App:    http://localhost:8502 (aprox.)
echo -----------------------------------------------
pause
