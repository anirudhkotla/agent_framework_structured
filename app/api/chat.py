from fastapi import APIRouter
from app.models.schemas import ChatRequest
from app.orchestrator.orchestrator import run_orchestrator


router = APIRouter()


@router.post("/chat")
async def chat(req: ChatRequest):
    return await run_orchestrator(req.message)