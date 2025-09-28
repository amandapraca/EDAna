 Código do agente com interface web

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title="Agente EDA", layout="wide")
st.title("🧠 Agente Autônomo de E.D.A.")

memoria_analises = []

uploaded_file = st.file_uploader("📁 Faça upload do arquivo CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.success("✅ Arquivo carregado com sucesso!")
    st.write("Colunas:", df.columns.tolist())
    st.write("Número de linhas:", len(df))

    pergunta = st.text_input("💬 Faça uma pergunta sobre os dados")

    def responder_pergunta(pergunta):
        pergunta = pergunta.lower()
        if "tipo" in pergunta or "dados" in pergunta:
            memoria_analises.append("Analisou os tipos de dados.")
            st.write(df.dtypes)
        elif "distribuição" in pergunta:
            memoria_analises.append("Analisou distribuições.")
            fig = plt.figure(figsize=(20, 15))
            df.hist(bins=50)
            st.pyplot(fig)
        elif "correlação" in pergunta:
            memoria_analises.append("Analisou correlações.")
            fig = plt.figure(figsize=(15, 12))
            sns.heatmap(df.corr(), cmap="coolwarm")
            st.pyplot(fig)
        elif "conclusão" in pergunta:
            if not memoria_analises:
                st.write("Nenhuma análise foi realizada ainda.")
            else:
                st.write("Resumo das análises realizadas:")
                for item in memoria_analises:
                    st.write(f"- {item}")
        else:
            st.write("Desculpe, não entendi sua pergunta.")

    if pergunta:
        responder_pergunta(pergunta)
