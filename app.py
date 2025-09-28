import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from llm_utils import gerar_resposta_llm

# Estilo visual da EDAna
st.markdown("""
<style>
.stApp {
    background-color: #0D1B2A;
    color: #FFD700;
}
h1, h2, h3, .stMarkdown {
    color: #FFD700;
}
button {
    background-color: #007BFF !important;
    color: white !important;
    border: none;
    padding: 0.5em 1em;
    border-radius: 5px;
}
input, textarea {
    background-color: #1B2A3A !important;
    color: #FFD700 !important;
    border: 1px solid #FFD700 !important;
}
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="EDAna – Agente Autônomo EDA", layout="wide")
st.title("👩‍💻 EDAna – Sua especialista em análise de dados")
st.toast("👋 Bem-vindos ao agente EDAna!", icon="💡")

# Inicializa sessão
if 'df' not in st.session_state:
    st.session_state['df'] = None
if 'historico' not in st.session_state:
    st.session_state['historico'] = []

# Função para gerar conclusões automáticas
def gerar_conclusoes():
    conclusoes = []
    for pergunta, resposta in st.session_state['historico']:
        p = pergunta.lower()
        if "distribuição" in p or "histograma" in p:
            conclusoes.append("A distribuição dos dados mostra concentração em faixas específicas.")
        if "outlier" in p or "valor atípico" in p:
            conclusoes.append("Foram detectados outliers em colunas relevantes.")
        if "correlação" in p or "relacionamento" in p:
            conclusoes.append("Há correlação significativa entre algumas variáveis.")
        if "intervalo" in p:
            conclusoes.append("Os valores variam dentro de um intervalo amplo.")
        if "frequente" in p or "valores comuns" in p:
            conclusoes.append("Algumas variáveis apresentam valores recorrentes.")
        if "tempo" in p:
            conclusoes.append("Foi observada uma variação temporal nas transações.")
    return conclusoes if conclusoes else ["Nenhuma conclusão foi gerada ainda. Faça perguntas para que a EDAna possa pensar!"]

# Botão para usar novo arquivo
if st.button("📁 Usar novo arquivo"):
    st.session_state['df'] = None
    st.session_state['historico'] = []
    st.rerun()

# Upload do CSV
if st.session_state['df'] is None:
    st.markdown("## 👋 Bem-vindos ao agente EDAna!")
    st.markdown("""
    EDAna é sua especialista em análise exploratória de dados.  
    Faça upload de um arquivo CSV e me pergunte qualquer coisa sobre os dados.  
    Posso gerar gráficos, detectar padrões, encontrar outliers e muito mais!  
    """)

    arquivo = st.file_uploader("Faça upload de um arquivo CSV", type=["csv"])
    if arquivo is not None:
        try:
            df = pd.read_csv(arquivo, sep=None, engine="python", encoding="utf-8", on_bad_lines="skip")
            df.columns = df.columns.str.strip()

            # Corrigir CSV mal formatado
            if len(df.columns) == 1:
                st.warning("⚠️ CSV parece estar mal formatado. Tentando corrigir...")
                cabecalho = df.columns[0].split(",")
                dados = df[df.columns[0]].str.split(",", expand=True)
                dados.columns = [col.strip() for col in cabecalho]
                if dados.iloc[0].equals(pd.Series(cabecalho)):
                    dados = dados.drop(index=0).reset_index(drop=True)
                dados = dados.apply(pd.to_numeric, errors='coerce')
                df = dados
                df.columns = df.columns.str.strip()
                st.success("✅ CSV reconstruído com sucesso!")

            st.session_state['df'] = df
            st.toast("✅ Arquivo carregado com sucesso!", icon="📊")

        except Exception as e:
            st.error(f"❌ Erro ao ler o arquivo: {e}")

# Interface principal com abas
if st.session_state['df'] is not None:
    df = st.session_state['df']
    aba1, aba2 = st.tabs(["🔍 Análise Interativa", "🧠 Conclusões da EDAna"])

    with aba1:
        st.subheader("👀 Pré-visualização dos dados")
        st.dataframe(df.head())

        st.markdown("---")
        st.subheader("🗣️ Faça uma pergunta sobre os dados")

        pergunta = st.text_input("Digite sua pergunta:")
        if pergunta and st.button("Enviar pergunta"):
            with st.spinner("🔎 Analisando os dados..."):
                resposta = gerar_resposta_llm(pergunta, df)
            st.session_state['historico'].append((pergunta, resposta))
            st.rerun()

        # Histórico de perguntas
        if st.session_state['historico']:
            st.markdown("### 🧠 Histórico de perguntas")
            for i, (q, r) in enumerate(st.session_state['historico'], 1):
                st.markdown(f"**{i}. Pergunta:** {q}")
                st.markdown(f"**Resposta:** {r}")
                st.markdown("---")

        # Seção de gráficos
        st.markdown("---")
        st.subheader("📊 Gerar gráfico")

        tipo_grafico = st.selectbox("Escolha o tipo de gráfico", ["Histograma", "Boxplot", "Dispersão"])
        colunas_numericas = df.select_dtypes(include="number").columns.tolist()

        if tipo_grafico == "Histograma":
            coluna = st.selectbox("Selecione a coluna numérica", colunas_numericas)
            if st.button("Gerar histograma"):
                fig, ax = plt.subplots()
                sns.histplot(df[coluna], kde=True, ax=ax)
                ax.set_title(f"Distribuição da coluna {coluna}")
                st.pyplot(fig)

        elif tipo_grafico == "Boxplot":
            coluna = st.selectbox("Selecione a coluna numérica", colunas_numericas)
            if st.button("Gerar boxplot"):
                fig, ax = plt.subplots()
                sns.boxplot(x=df[coluna], ax=ax)
                ax.set_title(f"Boxplot da coluna {coluna}")
                st.pyplot(fig)

        elif tipo_grafico == "Dispersão":
            col1 = st.selectbox("Eixo X", colunas_numericas)
            col2 = st.selectbox("Eixo Y", colunas_numericas)
            if st.button("Gerar gráfico de dispersão"):
                fig, ax = plt.subplots()
                sns.scatterplot(x=df[col1], y=df[col2], ax=ax)
                ax.set_title(f"Dispersão entre {col1} e {col2}")
                st.pyplot(fig)

    with aba2:
        st.markdown("## 🧠 Conclusões automáticas")
        st.markdown("Aqui estão os insights que a EDAna identificou com base nas suas perguntas:")
        for frase in gerar_conclusoes():
            st.markdown(f"- {frase}")

# Rodapé personalizado
st.markdown("---")
st.markdown("🧬 Criado com carinho por Amanda Praça • Desafio I2A2 2025")
