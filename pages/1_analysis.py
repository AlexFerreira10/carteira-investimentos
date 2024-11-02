import yfinance as yf
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd  # Importação adicionada

# Configuração da página do Streamlit
st.set_page_config(page_title="Análises de Investimentos", layout="wide")

# Título e Descrição
st.title("Análises de Investimentos")
st.write("""
Nesta seção, você poderá visualizar análises detalhadas de ações, incluindo preço, volume negociado, histórico de dividendos, volatilidade e correlação entre as ações selecionadas.
""")
st.divider()

# Seleção de ações e download dos dados
tickers = ["PETR4.SA", "WEGE3.SA"]
data = {ticker: yf.Ticker(ticker).history(period="6mo") for ticker in tickers}
dividend_data = {ticker: yf.Ticker(ticker).dividends for ticker in tickers}

# Carregar informações qualitativas
qualitative_data = {}
for ticker in tickers:
    ticker_info = yf.Ticker(ticker).info
    qualitative_data[ticker] = {
        "Indústria": ticker_info.get("industry", "N/A"),
        "Funcionários": ticker_info.get("fullTimeEmployees", "N/A")
    }

# Limpeza e Tratamento dos Dados
for ticker, df in data.items():
    df.dropna(inplace=True)
    df['Daily Return'] = df['Close'].pct_change()
    df['20 Day MA'] = df['Close'].rolling(window=20).mean()
    df['30 Day Volatility'] = df['Daily Return'].rolling(window=30).std()

# Análise de Correlação
daily_returns = pd.DataFrame({ticker: df['Daily Return'] for ticker, df in data.items()})
correlation_matrix = daily_returns.corr()

# Visualizações no Streamlit com Plotly
for ticker in tickers:
    st.subheader(f"Análise para {ticker}")

    # Gráfico de Preço de Fechamento e Média Móvel
    st.write("### Preço de Fechamento e Média Móvel")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data[ticker].index, y=data[ticker]['Close'], mode='lines', name="Fechamento", line=dict(color="blue")))
    fig.add_trace(go.Scatter(x=data[ticker].index, y=data[ticker]['20 Day MA'], mode='lines', name="Média Móvel 20 dias", line=dict(color="orange", dash="dash")))
    fig.update_layout(title=f"Preço de Fechamento e Média Móvel - {ticker}", xaxis_title="Data", yaxis_title="Preço (R$)")
    st.plotly_chart(fig)

    # Gráfico de Volume
    st.write("### Volume Negociado")
    fig = px.bar(data[ticker], x=data[ticker].index, y="Volume", labels={'Volume': 'Volume'}, title=f"Volume Negociado - {ticker}")
    st.plotly_chart(fig)

    # Gráfico de Volatilidade
    st.write("### Volatilidade")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data[ticker].index, y=data[ticker]['30 Day Volatility'], mode='lines', name="Volatilidade 30 dias", line=dict(color="red")))
    fig.update_layout(title=f"Volatilidade ao longo do Tempo - {ticker}", xaxis_title="Data", yaxis_title="Volatilidade")
    st.plotly_chart(fig)

# Mapa de Calor da Correlação entre as Ações
st.subheader("Matriz de Correlação entre as Ações")
fig = px.imshow(correlation_matrix, text_auto=True, aspect="auto",
                color_continuous_scale="RdBu", title="Matriz de Correlação entre Ações")
st.plotly_chart(fig, use_container_width=True)


# Seção de Conceitos Matemáticos e Financeiros
st.title("Conceitos Matemáticos e Financeiros")
st.write("""
## 1. Preço de Fechamento
O preço de fechamento é o último preço ao qual uma ação foi negociada durante um período de negociação.

## 2. Volume Diário
Refere-se à quantidade total de ações que foram compradas e vendidas em dia
""")

st.write("""
## 3. Média Móvel
A média móvel suaviza as flutuações de dados e é calculada como:
""")
st.latex(r"""
\text{Média Móvel 20 dias} = \frac{\sum_{i=0}^{19} \text{Preço de Fechamento}_i}{20}
""")
st.write("""
## 4. Volatilidade
A volatilidade é uma medida da dispersão dos retornos de uma ação, calculada como o desvio padrão dos retornos diários:
""")
st.latex(r"""
\text{Desvio Padrão} = \sqrt{\frac{\sum_{i=1}^{N} (R_i - \bar{R})^2}{N}}
""")
st.write("""
## 5. Correlação
A correlação mede a relação entre os retornos de diferentes ações e varia de -1 a 1.

## 6. Gráficos e Visualizações
- **Gráficos de Preço**: Mostram a evolução dos preços de fechamento.
- **Gráficos de Volume**: Mostram a quantidade de ações negociadas.
- **Gráficos de Volatilidade**: Mostram a variação da volatilidade ao longo do tempo.
- **Matriz de Correlação**: Visualiza como as ações se correlacionam entre si.
""")
