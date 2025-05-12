from langchain_core.messages import HumanMessage

from app.config.model import study_model
from app.domain.estate.exception import RealEstateAnswerCreateFailException
from app.domain.estate.schema.dto import RealEstateResponse
from app.domain.estate.template import study_prompt


structured_model = study_model.with_structured_output(RealEstateResponse)
chain = study_prompt | structured_model

def create_real_estate_response(question: str) -> RealEstateResponse:
    return chain.invoke({
        "content": HumanMessage(content=question)
    })


def execute(question: str) -> RealEstateResponse:
    try:
        return create_real_estate_response(question)
    except Exception:
        raise RealEstateAnswerCreateFailException
