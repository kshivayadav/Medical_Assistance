from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.llm_service import get_medical_response
import uuid
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Medical Assistant API with Memory",
    version="1.0.0"
)

class QueryRequest(BaseModel):
    question: str
    session_id: str | None = None

class QueryResponse(BaseModel):
    answer: str
    session_id: str



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ask", response_model=QueryResponse)
async def ask_question(request: QueryRequest):

    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    session_id = request.session_id or str(uuid.uuid4())

    try:
        answer = get_medical_response(request.question, session_id)
        return QueryResponse(answer=answer, session_id=session_id)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
def health():
    return {"status": "API running with conversation memory"}




