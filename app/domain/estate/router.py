from fastapi import APIRouter

from app.domain.estate.core import execute
from app.domain.estate.schema.dto import Question, RealEstateResponse

router = APIRouter(prefix="/api/estate", tags=["estate"])


@router.post("", response_model=RealEstateResponse, description="부동산 질문에 대한 응답 생성 API")
async def create_real_estate_answer(request: Question) -> RealEstateResponse:
    return execute(request.content)