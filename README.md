# Azure Technical Translator

Projeto de tradução automática de artigos técnicos utilizando Azure AI Translator, com foco em:

- Precisão terminológica
- Controle de glossário técnico
- Tradução de conteúdo web
- Execução via linha de comando (CLI)

---

## 🚀 Tecnologias Utilizadas

- Python 3.14
- Azure AI Translator
- FastAPI
- Requests
- Glossário técnico customizado

---

## 📦 Estrutura do Projeto

azure-technical-translator/
│
├── app.py # API (FastAPI)
├── cli.py # Interface via linha de comando
├── translator.py # Integração com Azure Translator
├── glossary.py # Controle de termos técnicos
├── glossary.json # Base de termos personalizados
├── article_fetcher.py # Captura texto de artigos web
├── requirements.txt
├── .env.example
└── examples/


---

## 🔑 Configuração

Crie um arquivo `.env` com:

AZURE_TRANSLATOR_KEY=your_key_here
AZURE_TRANSLATOR_ENDPOINT=https://api.cognitive.microsofttranslator.com/
AZURE_TRANSLATOR_REGION=eastus2


---

## ▶️ Como Executar

Instalar dependências:

```bash
pip install -r requirements.txt

Traduzir texto:
python cli.py --text "Hello world"

Traduzir artigo por URL:
python cli.py --url "https://example.com/article" --to pt
