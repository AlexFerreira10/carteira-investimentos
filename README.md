# Agregador de Investimentos

Este projeto é uma aplicação interativa desenvolvida com **Python**, com foco em análise e recomendação de ações. O objetivo é ajudar investidores como João Silva a tomar decisões informadas ao montar sua carteira de investimentos.

## Funcionalidades Principais

### 📊 Análise de Investimentos
- **Preço de Fechamento** e **Média Móvel de 20 dias**.
- **Volume de Negociação** ao longo do tempo.
- **Volatilidade** de 30 dias.
- **Correlação** entre as ações.

### 🔎 Insights e Feedback
- Recomendações baseadas no perfil do investidor.
- Pontos fortes e fracos das ações analisadas.
- Estratégias para diversificação e mitigação de riscos.

---

## Cenário do Cliente

### Perfil do Cliente
- **Nome:** João Silva  
- **Idade:** 40 anos  
- **Perfil de risco:** Baixo  
- **Objetivo:** Crescimento de capital com estabilidade.  
- **Horizonte de investimento:** Médio a longo prazo (5 a 10 anos).  
- **Preferência:** Empresas consolidadas com crescimento no preço das ações.

### Ações em Análise
1. **PETR4.SA (Petrobras)**
2. **WEGE3.SA (WEG)**

---

## Análises Financeiras

### 📈 Preço de Fechamento e Média Móvel
Visualiza a evolução do preço de fechamento ao longo do tempo com a média móvel para suavizar variações de curto prazo.

### 📊 Volume de Negociação
Mostra a quantidade de ações negociadas diariamente, refletindo a liquidez.

### 🔀 Volatilidade
Apresenta a variação do preço das ações, calculada com base nos retornos diários.

### 🔗 Matriz de Correlação
Análise da relação entre os retornos das ações para identificar sinergias e riscos.

---

## Recomendações

### Para PETR4.SA (Petrobras)
- **Alta volatilidade**, ideal para investidores que aceitam oscilações.
- **Alta liquidez**, facilitando a venda em curto prazo.
- **Para João:** Requer monitoramento frequente devido ao perfil conservador.

### Para WEGE3.SA (WEG)
- **Estabilidade** com menor volatilidade.
- **Consistência no crescimento**, alinhado ao objetivo de longo prazo.
- **Recomendação:** Ideal para o perfil de João, priorizando estabilidade.

---

## Conceitos Financeiros

### Média Móvel
Suaviza flutuações de curto prazo:
$$ \text{Média Móvel 20 dias} = \frac{\sum_{i=0}^{19} \text{Preço de Fechamento}_{t-i}}{20} $$

### Volatilidade
Medida do desvio padrão dos retornos diários:
$$ \sigma = \sqrt{\frac{\sum_{i=1}^{N} (R_i - \bar{R})^2}{N}} $$

### Retorno Esperado
A média dos retornos diários de um ativo:
$$ \bar{R} = \frac{\sum_{i=1}^{N} R_i}{N} $$

---

## Tecnologias Utilizadas

- **Python**
- **Streamlit** para a interface interativa.
- **Plotly** para visualizações gráficas.
- **yFinance** para consulta de dados de ações.
- **Pandas** para manipulação de dados financeiros.

---

## Executando o Projeto

1. Clone este repositório:
   ```bash
   git clone git@github.com:AlexFerreira10/carteira-investimentos.git

2. Instale as Dependências:

3. Execute a aplicação:
   ```bash
   streamlit run app.py

---

## ✍️ Considerações Finais

- **Autor:** Douglas Alexsander Ferreira Corrêa 
- **LinkedIn:** https://www.linkedin.com/in/alexferreira92/


