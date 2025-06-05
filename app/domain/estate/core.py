from langchain_core.messages import HumanMessage

from app.config.model import study_model
from app.domain.estate.exception import RealEstateAnswerCreateFailException, NotRealEstateQuestionException
from app.domain.estate.schema.dto import RealEstateResponse
from app.domain.estate.template import study_prompt
from app.domain.estate.classifier import classify_real_estate

# LangChain 구조화된 모델 (Pydantic 검증 포함)
structured_model = study_model.with_structured_output(RealEstateResponse)
chain = study_prompt | structured_model

# 실제 LangChain 체인을 호출해 RealEstateResponse를 반환
def create_real_estate_response(question: str) -> RealEstateResponse:
    try:
        # 내부적으로 Pydantic 검증까지 통과하여 RealEstateResponse 인스턴스 반환
        return chain.invoke({ "content": HumanMessage(content=question) })
    except Exception:
        # 스키마가 일치하지 않으면 503 에러
        raise RealEstateAnswerCreateFailException()

# 분류기로 필터링하여 부동산 질문인지 확인 후, 최종적으로 LangChain 체인을 호출하여 응답을 생성하는 메서드
def execute(question: str) -> RealEstateResponse:
    # 분류기 기반 검사 - Flase면 예외 발생
    is_real = classify_real_estate(question)
    if not is_real:
        raise NotRealEstateQuestionException()

    # 최종 모델 호출
    try:
        return create_real_estate_response(question)
    except NotRealEstateQuestionException:
        raise
    except Exception:
        raise RealEstateAnswerCreateFailException()