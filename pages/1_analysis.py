import yfinance as yf  
import streamlit as st 
import plotly.express as px 
import plotly.graph_objects as go   
import pandas as pd  

# Configuração da página do Streamlit
st.set_page_config(page_title="Análises de Investimentos", layout="wide")


st.title("Análises de Investimentos")
st.write("""
Nesta seção, você poderá visualizar análises detalhadas de ações, incluindo preço, volume negociado, histórico de dividendos, volatilidade e correlação entre as ações selecionadas.
""")
st.divider()  


tickers = ["PETR4.SA", "WEGE3.SA"]  
# Cria um dicionário com dados históricos das ações dos últimos 6 meses para cada ticker
data = {ticker: yf.Ticker(ticker).history(period="6mo") for ticker in tickers}

# Limpeza e Tratamento dos Dados
for ticker, df in data.items():
    # Remove linhas com valores ausentes (NaN)
    df.dropna(inplace=True)
    # Calcula o retorno diário como a variação percentual do preço de fechamento
    df['Daily Return'] = df['Close'].pct_change()
    # Calcula a média móvel de 20 dias no preço de fechamento
    df['20 Day MA'] = df['Close'].rolling(window=20).mean()
    # Calcula a volatilidade de 30 dias usando o desvio padrão dos retornos diários
    df['30 Day Volatility'] = df['Daily Return'].rolling(window=30).std()

# Análise de Correlação
# Cria um DataFrame com os retornos diários para cada ação
daily_returns = pd.DataFrame({ticker: df['Daily Return'] for ticker, df in data.items()})
# Calcula a matriz de correlação entre os retornos diários das ações
correlation_matrix = daily_returns.corr()

# Visualizações no Streamlit com Plotly
for ticker in tickers:
    st.subheader(f"Análise para {ticker}")

    # Gráfico de Preço de Fechamento e Média Móvel
    st.write("### Preço de Fechamento e Média Móvel")
    fig = go.Figure()
    # Adiciona linha para o preço de fechamento
    fig.add_trace(go.Scatter(x=data[ticker].index, y=data[ticker]['Close'], mode='lines', name="Fechamento", line=dict(color="blue")))
    # Adiciona linha para a média móvel de 20 dias
    fig.add_trace(go.Scatter(x=data[ticker].index, y=data[ticker]['20 Day MA'], mode='lines', name="Média Móvel 20 dias", line=dict(color="orange", dash="dash")))
    # Configura o layout do gráfico
    fig.update_layout(title=f"Preço de Fechamento e Média Móvel - {ticker}", xaxis_title="Data", yaxis_title="Preço (R$)")
    st.plotly_chart(fig)  # Exibe o gráfico no Streamlit

    # Gráfico de Volume
    st.write("### Volume Negociado")
    fig = px.bar(data[ticker], x=data[ticker].index, y="Volume", labels={'Volume': 'Volume'}, title=f"Volume Negociado - {ticker}")
    st.plotly_chart(fig)  

    # Gráfico de Volatilidade
    st.write("### Volatilidade")
    fig = go.Figure()
    # Adiciona linha para a volatilidade de 30 dias
    fig.add_trace(go.Scatter(x=data[ticker].index, y=data[ticker]['30 Day Volatility'], mode='lines', name="Volatilidade 30 dias", line=dict(color="red")))
    # Configura o layout do gráfico
    fig.update_layout(title=f"Volatilidade ao longo do Tempo - {ticker}", xaxis_title="Data", yaxis_title="Volatilidade")
    st.plotly_chart(fig)  

# Mapa de Calor da Correlação entre as Ações
st.subheader("Matriz de Correlação entre as Ações")
# Cria o gráfico de matriz de correlação com mapa de calor
fig = px.imshow(correlation_matrix, text_auto=True, aspect="auto",
                color_continuous_scale="RdBu", title="Matriz de Correlação entre Ações")
st.plotly_chart(fig, use_container_width=True)  

st.title("Conceitos Matemáticos e Financeiros")

st.write("""
## 1. Preço de Fechamento
O preço de fechamento é o último preço ao qual uma ação foi negociada durante um período de negociação.
""")

st.write("""
## 2. Volume Diário
Refere-se à quantidade total de ações que foram compradas e vendidas em um dia.
""")

st.write("""
## 3. Média Móvel
A média móvel suaviza as flutuações de dados e é calculada como:
""")
st.latex(r"""
\text{Média Móvel 20 dias} = \frac{\sum_{i=0}^{19} \text{Preço de Fechamento}_{t-i}}{20}
""")
st.write("""
onde o índice \( t-i \) representa o preço de fechamento nos dias anteriores, e a média móvel de 20 dias utiliza os últimos 20 preços de fechamento.
""")

st.write("""
## 4. Volatilidade
A volatilidade é uma medida da dispersão dos retornos de uma ação, calculada como o desvio padrão dos retornos diários:
""")
st.latex(r"""
\sigma = \sqrt{\frac{\sum_{i=1}^{N} (R_i - \bar{R})^2}{N}}
""")
st.write("""
onde \( R_i \) representa o retorno diário, \( \bar{R} \) é o retorno médio diário, e \( N \) é o número de dias considerados.
""")

st.write("""
## 5. Correlação
A correlação mede a relação entre os retornos de diferentes ações e varia de -1 a 1. A fórmula da correlação entre duas ações \(X\) e \(Y\) é:
""")
st.latex(r"""
\text{Correlação}(X, Y) = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}
""")
st.write("""
onde \( \text{Cov}(X, Y) \) é a covariância entre os retornos de \(X\) e \(Y\), e \( \sigma_X \) e \( \sigma_Y \) são os desvios padrão dos retornos de \(X\) e \(Y\).
""")

st.write("""
## 6. Retorno Esperado
O retorno esperado é a média dos retornos diários de um ativo ao longo de um período. Ele é usado para avaliar o desempenho médio de uma ação e é calculado como:
""")
st.latex(r"""
\bar{R} = \frac{\sum_{i=1}^{N} R_i}{N}
""")
st.write("""
onde \( R_i \) representa o retorno diário e \( N \) é o número de dias considerados.
""")

st.write("""
## 7. Gráficos e Visualizações
- **Gráficos de Preço**: Mostram a evolução dos preços de fechamento.
- **Gráficos de Volume**: Mostram a quantidade de ações negociadas.
- **Gráficos de Volatilidade**: Mostram a variação da volatilidade ao longo do tempo.
- **Matriz de Correlação**: Visualiza como as ações se correlacionam entre si.
""")
