import streamlit as st

# Configuração da página de Insights e Feedback
st.set_page_config(page_title="Insights e Feedback", layout="wide")

# Título da Página
st.title("Insights e Feedback para o Cliente")
st.write("""
Nesta seção, apresentamos os principais insights e recomendações para ajudar João a tomar uma decisão mais informada sobre suas opções de investimento.
""")
st.divider()

# Introdução aos Insights
st.header("Insights Gerais sobre as Ações")
st.write("""
**Análise Geral:**  
Com base nos dados dos últimos 6 meses, foram observadas as seguintes características nas ações selecionadas:
- **PETR4.SA (Petrobras)** apresenta alta volatilidade, o que implica em maiores variações de preço a curto prazo. Ideal para quem aceita oscilações.
- **WEGE3.SA (WEG)** exibe uma tendência mais estável, com menores flutuações, alinhando-se ao perfil de risco baixo de João.
""")
st.divider()

# Insights Específicos por Ação
st.subheader("Análise Específica para Cada Ação")

# Insights para PETR4.SA
st.write("### PETR4.SA (Petrobras)")
st.write("""
- **Crescimento Potencial:** Os dados indicam uma baixa recente, porém a volatilidade é elevada.  
- **Volume de Negociação:** Alta frequência de negociação, sugerindo alta liquidez, o que é vantajoso em cenários de venda rápida.  
- **Recomendação:** **Para João, que tem um perfil de risco baixo**, essa ação necessitaria um melhor acompanhamento do mercado e considerar a diversificação para reduzir riscos.
""")
st.divider()

# Insights para WEGE3.SA
st.write("### WEGE3.SA (WEG)")
st.write("""
- **Estabilidade:** Menor volatilidade, oferecendo uma linha de crescimento consistente e estável.  
- **Volume de Negociação:** Estável, com menos variações diárias, sugerindo um bom equilíbrio de entrada e saída de capital.  
- **Recomendação:** **Esta ação pode ser ideal para João** dado seu perfil conservador, pois apresenta crescimento moderado e estabilidade, alinhando-se ao objetivo de longo prazo.
""")
st.divider()

# Feedback e Recomendações para o Cliente
st.header("Feedback e Recomendações")
st.write("""
Com base nas análises, recomendamos o seguinte para João:
- **Diversificação**: Considerar um mix de ambas as ações (PETR4 e WEGE3) para balancear risco e crescimento.
- **Monitoramento de Volatilidade**: Revisar regularmente a volatilidade de PETR4 para identificar momentos de alta instabilidade, alinhando com o perfil de João.
- **Foco em Empresas Estáveis**: Priorizar WEGE3 e ações similares, dado que o objetivo de João é o crescimento com estabilidade.
""")