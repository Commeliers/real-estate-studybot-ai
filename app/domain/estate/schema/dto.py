from typing import List
from pydantic import BaseModel, Field


class RealEstateResponse(BaseModel):
    concept: str = Field(..., description="핵심 개념에 대한 간결한 설명")
    example: str = Field(..., description="실생활 예시 설명")
    follow_up: List[str] = Field(..., description="추가로 해볼 만한 질문 목록")

class Question(BaseModel):
    content: str = Field(..., description="사용자가 입력한 부동산 질문 텍스트")
