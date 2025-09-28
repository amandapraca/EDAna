import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

from dotenv import load_dotenv
import os
import google.generativeai as genai

# Configuração da chave da API Gemini
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Memória do agente
memoria_analises = []

# Carregar o CSV
nome_arquivo = input("📁 Qual é o nome do arquivo CSV que você quer analisar? (ex: aluguel.csv): ")

try:
    df = pd.read_csv(nome_arquivo, sep=None, engine="python", encoding="utf-8", on_bad_lines="skip")
    df.columns = df.columns.str.strip()
except Exception as e:
    print(f"❌ Erro ao ler o arquivo: {e}")
    exit()

# Corrigir se o CSV estiver mal formatado
if len(df.columns) == 1:
    print("⚠️ CSV parece estar mal formatado. Tentando corrigir...")
    cabecalho = df.columns[0].split(",")
    dados = df[df.columns[0]].str.split(",", expand=True)
    dados.columns = [col.strip() for col in cabecalho]
    if dados.iloc[0].equals(pd.Series(cabecalho)):
        dados = dados.drop(index=0).reset_index(drop=True)
    dados = dados.apply(pd.to_numeric, errors='coerce')
    df = dados
    df.columns = df.columns.str.strip()
    print("✅ CSV reconstruído com sucesso!")

# Informações iniciais
print("Colunas do CSV:", df.columns.tolist())
print("Tipos de dados:", df.dtypes)
print("Arquivo CSV carregado com sucesso!")
print("Número de linhas no arquivo:", len(df))

# Funções analíticas
def tipos_de_dados():
    memoria_analises.append("Analisou os tipos de dados.")
    return df.dtypes

def distribuicoes():
    memoria_analises.append("Analisou distribuições das variáveis.")
    df.hist(figsize=(20, 15), bins=50)
    plt.tight_layout()
    plt.show()
    return "Distribuições exibidas com sucesso."

def intervalo():
    memoria_analises.append("Calculou intervalo de valores.")
    intervalo = df.describe().loc[["min", "max"]]
    print(intervalo)
    return "Intervalo de valores exibido no terminal."

def tendencia_central():
    memoria_analises.append("Calculou média e mediana.")
    media = df.mean()
    mediana = df.median()
    print("Médias:\n", media)
    print("\nMedianas:\n", mediana)
    return "Média e mediana exibidas no terminal."

def variabilidade():
    memoria_analises.append("Calculou desvio padrão e variância.")
    desvio = df.std()
    variancia = df.var()
    print("Desvios padrão:\n", desvio)
    print("\nVariâncias:\n", variancia)
    return "Desvio padrão e variância exibidos no terminal."

def detectar_outliers():
    memoria_analises.append("Detectou outliers usando z-score.")
    z_scores = np.abs((df - df.mean()) / df.std())
    outliers = (z_scores > 3).sum()
    print("Outliers por coluna:\n", outliers)
    return "Outliers detectados e exibidos no terminal."

def analisar_correlacoes():
    memoria_analises.append("Analisou correlações entre variáveis.")
    plt.figure(figsize=(15, 12))
    sns.heatmap(df.corr(), cmap="coolwarm", annot=False)
    plt.title("Mapa de Correlação")
    plt.tight_layout()
    plt.show()
    return "Mapa de correlação exibido com sucesso."

def padroes_temporais():
    memoria_analises.append("Analisou padrões temporais.")
    if "Time" not in df.columns:
        return "Coluna 'Time' não encontrada."
    plt.figure(figsize=(10, 6))
    plt.plot(df["Time"], df["Amount"], alpha=0.5)
    plt.title("Padrões Temporais de Transações")
    plt.xlabel("Tempo")
    plt.ylabel("Valor da Transação")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    return "Padrões temporais exibidos com sucesso."

def valores_frequentes():
    memoria_analises.append("Analisou os valores mais frequentes.")
    frequencias = {}
    for coluna in df.columns:
        if df[coluna].nunique() > 50:
            continue
        contagem = df[coluna].value_counts().head(5)
        frequencias[coluna] = contagem
    if not frequencias:
        return "Nenhuma coluna com valores repetidos suficientes para análise."
    for coluna, contagem in frequencias.items():
        print(f"\nColuna: {coluna}")
        print(contagem)
    return "Valores frequentes exibidos no terminal."

def gerar_clusters():
    memoria_analises.append("Gerou clusters com KMeans.")
    colunas_numericas = df.select_dtypes(include=["int64", "float64"])
    if colunas_numericas.shape[1] < 2:
        return "Não há colunas numéricas suficientes para gerar clusters."
    scaler = StandardScaler()
    dados_padronizados = scaler.fit_transform(colunas_numericas)
    kmeans = KMeans(n_clusters=3, random_state=42)
    clusters = kmeans.fit_predict(dados_padronizados)
    df["Cluster"] = clusters
    plt.figure(figsize=(10, 6))
    plt.scatter(dados_padronizados[:, 0], dados_padronizados[:, 1], c=clusters, cmap="viridis", alpha=0.6)
    plt.title("Visualização dos Clusters (KMeans)")
    plt.xlabel("Variável 1 (padronizada)")
    plt.ylabel("Variável 2 (padronizada)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    return "Clusters gerados e visualizados com sucesso."

def graficos_correlacionados():
    memoria_analises.append("Gerou gráficos de dispersão entre variáveis correlacionadas.")
    correlacoes = df.corr().abs()
    pares_correlacionados = []
    for i in range(len(correlacoes.columns)):
        for j in range(i + 1, len(correlacoes.columns)):
            var1 = correlacoes.columns[i]
            var2 = correlacoes.columns[j]
            if correlacoes.loc[var1, var2] > 0.8:
                pares_correlacionados.append((var1, var2))
    if not pares_correlacionados:
        return "Nenhum par de variáveis com correlação forte foi encontrado."
    for var1, var2 in pares_correlacionados[:3]:
        plt.figure(figsize=(8, 6))
        plt.scatter(df[var1], df[var2], alpha=0.5)
        plt.title(f"Dispersão entre {var1} e {var2}")
        plt.xlabel(var1)
        plt.ylabel(var2)
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    return f"Foram exibidos {len(pares_correlacionados[:3])} gráficos de dispersão com correlação forte."

def conclusao_final():
    if not memoria_analises:
        return "Nenhuma análise foi realizada ainda."
    print("\nResumo das análises realizadas:")
    for item in memoria_analises:
        print(f"- {item}")
    return f"Foram realizadas {len(memoria_analises)} análises. O resumo foi exibido no terminal."

# Função principal de resposta
def responder_pergunta(pergunta):
    pergunta = pergunta.lower()
    if "tipo" in pergunta or "dados" in pergunta:
        return tipos_de_dados()
    elif "distribuição" in pergunta or "histograma" in pergunta:
        return distribuicoes()
    elif "intervalo" in pergunta:
        return intervalo()
    elif "média" in pergunta or "mediana" in pergunta:
        return tendencia_central()
    elif "desvio" in pergunta or "variância" in pergunta:
        return variabilidade()
    elif "outlier" in pergunta or "valor atípico" in pergunta:
        return detectar_outliers()
    elif "correlação" in pergunta or "relacionamento" in pergunta:
        return analisar_correlacoes()
    elif "tempo" in pergunta or "padrão temporal" in pergunta:
        return padroes_temporais()
    elif "frequente" in pergunta or "repetido" in pergunta or "comum" in pergunta or "valores" in pergunta:
        return valores_frequentes()
    elif "cluster" in pergunta or "agrupamento" in pergunta:
        return gerar_clusters()
    elif "dispersão" in pergunta or "correlacionadas" in pergunta or "gráfico entre variáveis" in pergunta:
        return graficos_correl
