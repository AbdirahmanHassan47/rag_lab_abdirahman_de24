# rag_lab_abdirahman_de24


# 🎬 Youtuber RAG Chatbot – Proof of Concept (DE24)

Detta projekt är ett **RAG-baserat frågesystem** byggt på transkript från en fiktiv YouTube-kanal om data engineering.  
Målet är att skapa en *lärande chatbot* som kan svara på frågor genom att kombinera:

- LanceDB (vektordatabas)
- PydanticAI (RAG-agent + persona)
- FastAPI (backend)
- Streamlit (frontend)

Projektet implementerar **Task 0, 1, 2, 3, 5 och 6** enligt kursens krav för **G-nivå**.  
Detta innebär ett komplett PoC-system som fungerar lokalt end-to-end.



Systemet använder *retrieval augmented generation*:  
1. Hämta relevanta transkript via embeddings  
2. Skicka dessa som kontext till modellen  
3. Generera ett kort, tydligt svar med Youtuberns personlighet  

---

## 📁 Projektstruktur

.
├── backend/
│ ├── constans.py # DATA_PATH, VECTOR_PATH
│ ├── data_models.py # Transcript, Prompt, RagResponse
│ ├── ingestion.py # Ingesta av markdown → LanceDB
│ └── rag.py # RAG-agent + persona + retrieval
│
├── data/ # Markdown-filer (YouTube-transkript)
│
├── knowledge_base/ # Genereras av ingestion (LanceDB)
│
├── api.py # FastAPI-endpoint /rag/query
│
└── frontend/
└── app.py # Streamlit-chatgränssnitt


---

## 🔧 Förutsättningar

- Python 3.10 eller senare  
- uv (rekommenderat av kursen)  
- En API-nyckel för den modell du använder (t.ex. GOOGLE_API_KEY)

Skapa en `.env` i projektroten:


Kör ingestion:

```bash
uv run python backend/ingestion.py


uvicorn api:app --reload


streamlit run frontend/app.py





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
 