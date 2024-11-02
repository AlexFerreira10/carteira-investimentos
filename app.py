import streamlit as st

# Configuração da página do Streamlit
st.set_page_config(page_title="Agregador de Investimentos", layout="wide")

# Apresentação
st.title("Carteira de Investimentos de João")
st.write("""
**João está montando uma carteira de ações com foco em crescimento.**  
Ele está em dúvida entre duas ações e então pediu ajuda de um especialista.
""")
st.divider()

# Cenário do Cliente
st.header("Cenário do Cliente")
st.subheader("Perfil do Cliente")
st.write("- **Nome:** João Silva")
st.write("- **Idade:** 40 anos")
st.write("- **Perfil de risco:** Baixo")
st.write("- **Objetivo:** Crescimento de capital com alguma estabilidade e foco em empresas consolidadas")
st.write("- **Horizonte de investimento:** Médio a longo prazo (5 a 10 anos)")
st.write("- **Preferência:** Empresas que apresentam crescimento no preço das ações")

st.subheader("Ações em Análise")
col1, col2 = st.columns(2)
with col1:
    st.write("- **PETR4.SA (Petrobras)**")
    st.write("- **WEGE3.SA (WEG)**")

st.subheader("Análises Esperadas")
st.write("""
- **Análise de Preço e Volume Histórico**
- **Volatilidade e Risco**
- **Correlação entre Ações**
""")

st.divider()