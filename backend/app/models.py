# /backend/app/models.py
from pydantic import BaseModel

class AbstractInput(BaseModel):
    title: str
    text: str

class AnalysisResult(BaseModel):
    is_ai_generated: bool
    average_similarity: float
    message: str