.
├── backend/
│   ├── data_models.py      # LanceDB-modeller (Transcript, Prompt, RagResponse)
│   ├── rag.py              # RAG-agent, persona och retrieval-logik
│   └── constans.py         # DATA_PATH och VECTOR_PATH
│
├── frontend/
│   └── app.py              # Streamlit-chatgränssnitt
│
├── api.py                  # FastAPI-backend, exponerar /rag/query
├── ingestion.py            # Skapar LanceDB-tabell från data/*.md (Task 0)
│
├── data/                   # YouTube-transkript i markdown-format
├── knowledge_base/         # Genereras automatiskt av ingestion (LanceDB)
│
├── .env                    # API-nycklar (GOOGLE_API_KEY)
├── pyproject.toml / uv.lock
└── README.md
🔧 Förutsättningar
Python 3.10+

uv (rekommenderat av kursen)

En API-nyckel (t.ex. GOOGLE_API_KEY)

Skapa en .env i projektroten:

ini
Kopiera kod
GOOGLE_API_KEY=din_nyckel_här
🚀 Så kör du projektet
1️⃣ Kör ingestion (Task 0)
Bygger vektorbasen:

bash
Kopiera kod
uv run python ingestion.py
2️⃣ Starta FastAPI-backend (Task 2)
bash
Kopiera kod
uvicorn api:app --reload
Öppna:

http://127.0.0.1:8000

http://127.0.0.1:8000/docs

3️⃣ Starta Streamlit-chatten (Task 2)
bash
Kopiera kod
streamlit run frontend/app.py
🧠 Arkitekturdiagram
arduino
Kopiera kod
┌────────────────────────┐
│ Markdown-transkript (.md)
└───────────┬────────────┘
            │ ingestion.py
            ▼
┌────────────────────────┐
│   LanceDB embeddings   │
└───────────┬────────────┘
            │ vector search
            ▼
┌────────────────────────┐
│   RAG-agent (PydanticAI)
│   + persona + retrieval │
└───────────┬────────────┘
            │ /rag/query
            ▼
┌────────────────────────┐
│     FastAPI backend    │
└───────────┬────────────┘
            │ HTTP POST
            ▼
┌────────────────────────┐
│   Streamlit frontend   │
└────────────────────────┘