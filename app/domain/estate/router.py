from fastapi import APIRouter

from starlette.concurrency import run_in_threadpool
from app.domain.estate.core import execute
from app.domain.estate.schema.dto import Question, RealEstateResponse

router = APIRouter(prefix="/api/estate", tags=["estate"])

@router.post("", response_model=RealEstateResponse, description="부동산 질문에 대한 응답 생성 API")
async def create_real_estate_answer(request: Question) -> RealEstateResponse:
    # 비동기 처리
    return await run_in_threadpool(lambda: execute(request.content))