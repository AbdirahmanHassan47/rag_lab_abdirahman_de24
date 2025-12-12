
from backend.constants import VECTOR_DB_PATH, DATA_PATH
from backend.data_models import Transcript
import lancedb
from pathlib import Path
import time


def setup_vector_db(path: Path):
    """Skapar (om nödvändigt) en LanceDB-databas och en 'transcripts'-tabell."""
    path = Path(path)
    path.mkdir(exist_ok=True, parents=True)

    print(f"[INFO] Connecting to LanceDB at: {path}")

    vector_db = lancedb.connect(uri=str(path))
   
    vector_db.create_table("transcripts", schema=Transcript, exist_ok=True)

    return vector_db


def ingest_docs_to_vector_db(table):
    """Läser alla .md-filer i DATA_PATH och lägger in dem i LanceDB."""
    files = sorted(DATA_PATH.glob("*.md"))

    if not files:
        print(f"[WARNING] No .md files found in DATA_PATH: {DATA_PATH}")
        return

    print(f"[INFO] Found {len(files)} markdown files to ingest...\n")

    for filepath in files:
        print(f"[INFO] Ingesting: {filepath.name}")

        content = filepath.read_text(encoding="utf-8")
        doc_id = filepath.stem

       
        table.delete(f"doc_id = '{doc_id}'")

        table.add(
            [
                {
                    "doc_id": doc_id,
                    "filepath": str(filepath),
                    "filename": filepath.stem,
                    "content": content,
                }
            ]
        )

        print(f"[OK] Added doc_id={doc_id}")
        time.sleep(0.1)  # liten paus om du vill undvika rate limits / load

    print("\n[INFO] Ingestion complete!")


if __name__ == "__main__":
    vdb = setup_vector_db(VECTOR_DB_PATH)
    ingest_docs_to_vector_db(vdb["transcripts"])
