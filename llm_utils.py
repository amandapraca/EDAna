import os
import pandas as pd
from dotenv import load_dotenv
import google.generativeai as genai

# Carrega a chave da API do .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Função para gerar resumo dos dados
def gerar_resumo_dos_dados(df: pd.DataFrame) -> str:
    colunas_numericas = df.select_dtypes(include="number")

    resumo = f"""
Colunas e tipos:
{df.dtypes.to_string()}

Estatísticas descritivas:
{colunas_numericas.describe().to_string()}

Correlação entre variáveis:
{colunas_numericas.corr().to_string()}
"""
    return resumo

# Função principal que chama a LLM via SDK Gemini
def gerar_resposta_llm(pergunta: str, df: pd.DataFrame) -> str:
    try:
        model = genai.GenerativeModel("gemini-pro-latest")
        resumo_dados = gerar_resumo_dos_dados(df)

        prompt = f"""
Você é um agente autônomo de análise de dados. Seu papel é responder perguntas com base nos dados abaixo, que foram extraídos de um arquivo CSV.

Regras:
- Responda com base exclusivamente nos dados.
- Não invente informações.
- Se não for possível responder, diga: "Os dados não permitem responder essa pergunta."
- Seja técnico, claro e completo.
- Use exemplos, estatísticas e comparações quando necessário.

Resumo dos dados:
{resumo_dados}

Pergunta:
{pergunta}
"""

        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"❌ Erro ao gerar resposta: {e}"
