from fastapi import APIRouter, HTTPException
from reverse_turing.rag_service import RAGService

router = APIRouter()
rag_service = RAGService()


@router.get("/retrieve")
async def retrieve_documents(query: str, top_n: int = 5):
    try:
        results = rag_service.retrieve(query, top_n)
        return {"query": query, "results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
