import yfinance as yf
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import plotly.graph_objects as go
import numpy as np

st.title("Regressão Linear")
st.write("Nesta seção, utilizamos a modelegem preditiva, técnica de IA, para prever preços de fechamento de ações.")

# Seleção de ticker
ticker = st.selectbox("Selecione uma ação para análise:", ["PETR4.SA", "WEGE3.SA"])

# Carregar dados históricos
df = yf.Ticker(ticker).history(period="1y")

# Criar a coluna Target para o preço do dia seguinte
df['Target'] = df['Close'].shift(-1)

# Remover valores nulos
df.dropna(inplace=True)

# Criar as features, com as outras estavam dando muito erro
X = df[['Close', 'Volume']].values  # preço de fechamento e o volume como features
y = df['Target'].values  # Preço de fechamento do próximo dia como alvo

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Avaliação
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
st.write(f"Erro Quadrático Médio (MSE): {mse:.2f}")

# Previsão para os próximos 30 dias
future_prices = []
last_price = df['Close'].iloc[-1]

# Previsão baseada no modelo, para os próximos 30 dias
for _ in range(30):
    # O modelo precisa de uma entrada com preço de fechamento e volume para prever
    # Aqui, usamos o último volume como valor constante
    last_volume = df['Volume'].iloc[-1]  # Pegando o último volume
    pred = model.predict([[last_price, last_volume]])  # Usando preço e volume como entrada
    future_prices.append(pred[0])
    last_price = pred[0]  # Atualizando o preço de fechamento para o próximo dia

# Gerar datas futuras
future_dates = pd.date_range(start=df.index[-1], periods=31, freq="B")[1:]
future_df = pd.DataFrame({"Data": future_dates, "Preço Previsto": future_prices})

# Visualizar previsões
fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index, y=df['Close'], name="Histórico"))
fig.add_trace(go.Scatter(x=future_df["Data"], y=future_df["Preço Previsto"], name="Previsão", line=dict(dash="dot")))
fig.update_layout(title="Previsão de Preços", xaxis_title="Data", yaxis_title="Preço")
st.plotly_chart(fig)
