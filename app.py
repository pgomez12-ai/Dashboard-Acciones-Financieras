import streamlit as st
import yfinance as yf

# Configuración del título de la app
st.title("Trading de Acciones")

# Selección de acción
ticker = st.text_input("Ingresa el ticker de la acción (ejemplo: AAPL, TSLA)")

if ticker:
    # Obtención de datos con yfinance
    data = yf.download(ticker, period="1d", interval="1m")
    st.write(f"Datos de {ticker}:", data.tail())
    
    # Gráfico de la acción
    st.line_chart(data['Close'])
