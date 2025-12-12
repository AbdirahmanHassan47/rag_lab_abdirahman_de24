
from pydantic import BaseModel, Field
from lancedb.embeddings import get_registry
from lancedb.pydantic import LanceModel, Vector
from dotenv import load_dotenv

load_dotenv()


embedding_model = get_registry().get("gemini-text").create(
    name="gemini-embedding-001"
)


EMBEDDING_DIM = 3072


class Transcript(LanceModel):
    doc_id: str
    filepath: str
    filename: str = Field(
        description="Filnamnets 'stem', dvs utan suffix (ex: .md, .txt)."
    )
    
    content: str = embedding_model.SourceField()
    embedding: Vector(EMBEDDING_DIM) = embedding_model.VectorField()


class Prompt(BaseModel):
    prompt: str = Field(description="Användarens fråga till RAG-botten.")


class RagResponse(BaseModel):
    filename: str = Field(
        description="Filnamn (utan suffix) för det transkript som användes."
    )
    filepath: str = Field(
        description="Absolut sökväg till den fil som användes som källa."
    )
    answer: str = Field(
        description="Själva svaret till användaren, baserat på transkriptet."
    )
