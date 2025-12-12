
from pydantic_ai import Agent
from backend.data_models import RagResponse
from backend.constants import VECTOR_DB_PATH
import lancedb


vector_db = lancedb.connect(uri=str(VECTOR_DB_PATH))

YOUTUBER_PERSONA = (
    "You are The Youtuber - a passionate educator who teaches hundreds through video tutorials. "
    "You also happen to be an expert in Data Engineering. "
    "You have a friendly, joyful and enthusiastic teaching style and love helping people learn data engineering. "
    "Always answer based on the retrieved video transcript knowledge, but you can mix in your expertise to make the answer more coherent. "
    "Don't hallucinate; if the user asks about something outside the retrieved knowledge, politely say that you don't have enough information. "
    "Keep the answer clear and concise, max 6 sentences. "
    "Always describe which file you used as source in your answer."
)

rag_agent = Agent(
    model="google-gla:gemini-2.5-flash",  
    retries=2,
    system_prompt=YOUTUBER_PERSONA,
    output_type=RagResponse,
)


@rag_agent.tool_plain
def retrieve_top_documents(query: str, k: int = 3) -> str:
    """
    Uses vector search to find the closest matching video transcripts to the query.

    Returns a string including:
    - filename (video title)
    - filepath
    - content (transcript text)

    This string används av modellen som kontext när den genererar svaret.
    """
    table = vector_db["transcripts"]
    results = table.search(query=query).limit(k).to_list()

    if not results:
        return "No matching documents found in the transcript database."

    top_result = results[0]

    return (
        f"Video Title: {top_result['filename']}, "
        f"Filepath: {top_result['filepath']}, "
        f"Content: {top_result['content']}"
    )
