# 👩‍💻 EDAna – Agente Autônomo de Análise de Dados

Este projeto foi desenvolvido por Amanda Praça como parte da atividade extra da disciplina de Agentes Autônomos (I2A2 2025). O objetivo é criar um agente inteligente e generativo capaz de realizar análises exploratórias de dados (E.D.A.) de forma automatizada, respondendo perguntas e gerando gráficos com base em arquivos CSV fornecidos pelo usuário.

---

## 🔹 Nome do agente

**EDAna** – sua especialista em análise exploratória de dados.

---

## 🚀 Funcionalidades

- Upload de qualquer arquivo CSV
- Interface interativa via Streamlit
- Respostas automáticas a perguntas como:
- Quais são os tipos de dados?
- Quais variáveis estão correlacionadas?
- Existem valores atípicos?
- Qual é a conclusão final?
- Geração de gráficos como histogramas, boxplots e dispersões
- Registro das análises realizadas em memória
- Conclusões automáticas com base nas interações
- Estilo visual personalizado (azul petróleo + dourado)
- Mensagens animadas com `st.toast()`
- Rodapé com assinatura da autora

---

## 🔹 Componentes principais

- **Interface Streamlit**: permite upload de arquivos CSV e entrada de perguntas pelo usuário.
- **Análise automatizada com pandas, seaborn e matplotlib**: o agente gera estatísticas descritivas, gráficos e resumos dos dados.
- **Integração com LLM Gemini**: a LLM é acionada automaticamente para interpretar os dados e responder perguntas com base no conteúdo do CSV.
- **Prompt estruturado**: o agente envia à LLM um resumo técnico dos dados, garantindo que as respostas sejam baseadas exclusivamente nas informações disponíveis.
- **Memória local**: o agente registra perguntas e respostas anteriores, permitindo que construa conclusões e evite chamadas repetidas à API.
- **Segurança**: a chave da API do Gemini é armazenada em arquivo `.env`, ocultada do código-fonte e do repositório público.

---

## 🔹 Funcionamento

1. O usuário acessa o agente via link público  
2. Faz upload de um arquivo CSV ou seleciona um já disponível  
3. Digita uma pergunta livre sobre os dados  
4. O agente processa o CSV, gera um resumo técnico e envia à LLM  
5. A resposta é exibida na interface, podendo incluir gráficos gerados com código Python  
6. As análises são registradas em memória, permitindo que o agente construa conclusões ao longo da interação

Essa abordagem garante que o agente seja **autônomo, generativo e confiável**, respondendo com base nos dados e sem intervenção manual. A LLM está integrada ao código e opera como parte do agente, conforme exigido pela atividade.

---

## 📦 Tecnologias utilizadas

- Python 3
- Streamlit
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Gemini API (via `llm_utils.py`)
- dotenv

---

## 🛠 Como executar localmente

```bash
git clone https://github.com/amandapraca/EDAna.git
cd EDAna
pip install -r requirements.txt
streamlit run app.py

⚠️ Certifique-se de criar um arquivo .env com sua chave da API Gemini:
GEMINI_API_KEY=your_key_here


Amanda, aqui está o seu novo README completíssimo — profissional, acolhedor e com o toque especial da EDAna 💙

📘 README.md — Repositório EDAna
# 👩‍💻 EDAna – Agente Autônomo de Análise de Dados

Este projeto foi desenvolvido por Amanda Praça como parte da atividade extra da disciplina de Agentes Autônomos (I2A2 2025). O objetivo é criar um agente inteligente e generativo capaz de realizar análises exploratórias de dados (E.D.A.) de forma automatizada, respondendo perguntas e gerando gráficos com base em arquivos CSV fornecidos pelo usuário.

---

## 🔹 Nome do agente

**EDAna** – sua especialista em análise exploratória de dados.

---

## 🚀 Funcionalidades

- Upload de qualquer arquivo CSV
- Interface interativa via Streamlit
- Respostas automáticas a perguntas como:
  - Quais são os tipos de dados?
  - Quais variáveis estão correlacionadas?
  - Existem valores atípicos?
  - Qual é a conclusão final?
- Geração de gráficos como histogramas, boxplots e dispersões
- Registro das análises realizadas em memória
- Conclusões automáticas com base nas interações
- Estilo visual personalizado (azul petróleo + dourado)
- Mensagens animadas com `st.toast()`
- Rodapé com assinatura da autora

---

## 🔹 Componentes principais

- **Interface Streamlit**: permite upload de arquivos CSV e entrada de perguntas pelo usuário.
- **Análise automatizada com pandas, seaborn e matplotlib**: o agente gera estatísticas descritivas, gráficos e resumos dos dados.
- **Integração com LLM Gemini**: a LLM é acionada automaticamente para interpretar os dados e responder perguntas com base no conteúdo do CSV.
- **Prompt estruturado**: o agente envia à LLM um resumo técnico dos dados, garantindo que as respostas sejam baseadas exclusivamente nas informações disponíveis.
- **Memória local**: o agente registra perguntas e respostas anteriores, permitindo que construa conclusões e evite chamadas repetidas à API.
- **Segurança**: a chave da API do Gemini é armazenada em arquivo `.env`, ocultada do código-fonte e do repositório público.

---

## 🔹 Funcionamento

1. O usuário acessa o agente via link público  
2. Faz upload de um arquivo CSV ou seleciona um já disponível  
3. Digita uma pergunta livre sobre os dados  
4. O agente processa o CSV, gera um resumo técnico e envia à LLM  
5. A resposta é exibida na interface, podendo incluir gráficos gerados com código Python  
6. As análises são registradas em memória, permitindo que o agente construa conclusões ao longo da interação

Essa abordagem garante que o agente seja **autônomo, generativo e confiável**, respondendo com base nos dados e sem intervenção manual. A LLM está integrada ao código e opera como parte do agente, conforme exigido pela atividade.

---

## 📦 Tecnologias utilizadas

- Python 3
- Streamlit
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Gemini API (via `llm_utils.py`)
- dotenv

---

## 🛠 Como executar localmente

```bash
git clone https://github.com/amandapraca/EDAna.git
cd EDAna
pip install -r requirements.txt
streamlit run app.py


⚠️ Certifique-se de criar um arquivo .env com sua chave da API Gemini:
GEMINI_API_KEY=your_key_here

🌐 Acesso online
Você pode acessar o agente diretamente pelo link abaixo:
🔗 https://agente-eda-amanda.streamlit.app
⏳ A página pode levar alguns segundos para carregar. Aguarde até que a interface esteja visível antes de interagir.

Amanda, aqui está o seu novo README completíssimo — profissional, acolhedor e com o toque especial da EDAna 💙

📘 README.md — Repositório EDAna
# 👩‍💻 EDAna – Agente Autônomo de Análise de Dados

Este projeto foi desenvolvido por Amanda Praça como parte da atividade extra da disciplina de Agentes Autônomos (I2A2 2025). O objetivo é criar um agente inteligente e generativo capaz de realizar análises exploratórias de dados (E.D.A.) de forma automatizada, respondendo perguntas e gerando gráficos com base em arquivos CSV fornecidos pelo usuário.

---

## 🔹 Nome do agente

**EDAna** – sua especialista em análise exploratória de dados.

---

## 🚀 Funcionalidades

- Upload de qualquer arquivo CSV
- Interface interativa via Streamlit
- Respostas automáticas a perguntas como:
  - Quais são os tipos de dados?
  - Quais variáveis estão correlacionadas?
  - Existem valores atípicos?
  - Qual é a conclusão final?
- Geração de gráficos como histogramas, boxplots e dispersões
- Registro das análises realizadas em memória
- Conclusões automáticas com base nas interações
- Estilo visual personalizado (azul petróleo + dourado)
- Mensagens animadas com `st.toast()`
- Rodapé com assinatura da autora

---

## 🔹 Componentes principais

- **Interface Streamlit**: permite upload de arquivos CSV e entrada de perguntas pelo usuário.
- **Análise automatizada com pandas, seaborn e matplotlib**: o agente gera estatísticas descritivas, gráficos e resumos dos dados.
- **Integração com LLM Gemini**: a LLM é acionada automaticamente para interpretar os dados e responder perguntas com base no conteúdo do CSV.
- **Prompt estruturado**: o agente envia à LLM um resumo técnico dos dados, garantindo que as respostas sejam baseadas exclusivamente nas informações disponíveis.
- **Memória local**: o agente registra perguntas e respostas anteriores, permitindo que construa conclusões e evite chamadas repetidas à API.
- **Segurança**: a chave da API do Gemini é armazenada em arquivo `.env`, ocultada do código-fonte e do repositório público.

---

## 🔹 Funcionamento

1. O usuário acessa o agente via link público  
2. Faz upload de um arquivo CSV ou seleciona um já disponível  
3. Digita uma pergunta livre sobre os dados  
4. O agente processa o CSV, gera um resumo técnico e envia à LLM  
5. A resposta é exibida na interface, podendo incluir gráficos gerados com código Python  
6. As análises são registradas em memória, permitindo que o agente construa conclusões ao longo da interação

Essa abordagem garante que o agente seja **autônomo, generativo e confiável**, respondendo com base nos dados e sem intervenção manual. A LLM está integrada ao código e opera como parte do agente, conforme exigido pela atividade.

---

## 📦 Tecnologias utilizadas

- Python 3
- Streamlit
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Gemini API (via `llm_utils.py`)
- dotenv

---

## 🛠 Como executar localmente

```bash
git clone https://github.com/amandapraca/EDAna.git
cd EDAna
pip install -r requirements.txt
streamlit run app.py


⚠️ Certifique-se de criar um arquivo .env com sua chave da API Gemini:
GEMINI_API_KEY=your_key_here




🌐 Acesso online
Você pode acessar o agente diretamente pelo link abaixo:
🔗 https://agente-eda-amanda.streamlit.app
⏳ A página pode levar alguns segundos para carregar. Aguarde até que a interface esteja visível antes de interagir.







Amanda, aqui está o seu novo README completíssimo — profissional, acolhedor e com o toque especial da EDAna 💙

📘 README.md — Repositório EDAna
# 👩‍💻 EDAna – Agente Autônomo de Análise de Dados

Este projeto foi desenvolvido por Amanda Praça como parte da atividade extra da disciplina de Agentes Autônomos (I2A2 2025). O objetivo é criar um agente inteligente e generativo capaz de realizar análises exploratórias de dados (E.D.A.) de forma automatizada, respondendo perguntas e gerando gráficos com base em arquivos CSV fornecidos pelo usuário.

---

## 🔹 Nome do agente

**EDAna** – sua especialista em análise exploratória de dados.

---

## 🚀 Funcionalidades

- Upload de qualquer arquivo CSV
- Interface interativa via Streamlit
- Respostas automáticas a perguntas como:
  - Quais são os tipos de dados?
  - Quais variáveis estão correlacionadas?
  - Existem valores atípicos?
  - Qual é a conclusão final?
- Geração de gráficos como histogramas, boxplots e dispersões
- Registro das análises realizadas em memória
- Conclusões automáticas com base nas interações
- Estilo visual personalizado (azul petróleo + dourado)
- Mensagens animadas com `st.toast()`
- Rodapé com assinatura da autora

---

## 🔹 Componentes principais

- **Interface Streamlit**: permite upload de arquivos CSV e entrada de perguntas pelo usuário.
- **Análise automatizada com pandas, seaborn e matplotlib**: o agente gera estatísticas descritivas, gráficos e resumos dos dados.
- **Integração com LLM Gemini**: a LLM é acionada automaticamente para interpretar os dados e responder perguntas com base no conteúdo do CSV.
- **Prompt estruturado**: o agente envia à LLM um resumo técnico dos dados, garantindo que as respostas sejam baseadas exclusivamente nas informações disponíveis.
- **Memória local**: o agente registra perguntas e respostas anteriores, permitindo que construa conclusões e evite chamadas repetidas à API.
- **Segurança**: a chave da API do Gemini é armazenada em arquivo `.env`, ocultada do código-fonte e do repositório público.

---

## 🔹 Funcionamento

1. O usuário acessa o agente via link público  
2. Faz upload de um arquivo CSV ou seleciona um já disponível  
3. Digita uma pergunta livre sobre os dados  
4. O agente processa o CSV, gera um resumo técnico e envia à LLM  
5. A resposta é exibida na interface, podendo incluir gráficos gerados com código Python  
6. As análises são registradas em memória, permitindo que o agente construa conclusões ao longo da interação

Essa abordagem garante que o agente seja **autônomo, generativo e confiável**, respondendo com base nos dados e sem intervenção manual. A LLM está integrada ao código e opera como parte do agente, conforme exigido pela atividade.

---

## 📦 Tecnologias utilizadas

- Python 3
- Streamlit
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Gemini API (via `llm_utils.py`)
- dotenv

---

## 🛠 Como executar localmente

```bash
git clone https://github.com/amandapraca/EDAna.git
cd EDAna
pip install -r requirements.txt
streamlit run app.py


⚠️ Certifique-se de criar um arquivo .env com sua chave da API Gemini:
GEMINI_API_KEY=your_key_here


🌐 Acesso online
Você pode acessar o agente diretamente pelo link abaixo:
🔗 https://agente-eda-amanda.streamlit.app
⏳ A página pode levar alguns segundos para carregar. Aguarde até que a interface esteja visível antes de interagir.

📁 Estrutura do projeto
EDAna/
├── app.py               # Interface principal e lógica de interação
├── llm_utils.py         # Função de integração com a LLM Gemini
├── requirements.txt     # Lista de dependências
├── .env                 # Chave da API (não incluído no repositório público)
└── README.md            # Este arquivo

🧬 Autoria
Criado com carinho por Amanda Praça
Desafio I2A2 – Agentes Autônomos 2025
https://github.com/amandapraca


