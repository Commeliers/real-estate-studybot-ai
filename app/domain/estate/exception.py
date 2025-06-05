from app.error.code import RealEstateAnswerCreateFail, NotRealEstateQuestion
from app.error.handler import BaseCustomException

# 부동산 질문에 대한 답변 생성 자체가 실패했을 때 던질 예외 (503)
class RealEstateAnswerCreateFailException(BaseCustomException):
    def __init__(self):
        super().__init__(
            is_success=False,
            http_status=RealEstateAnswerCreateFail.HTTP_STATUS.value,
            code=RealEstateAnswerCreateFail.CODE.value,
            message=RealEstateAnswerCreateFail.MESSAGE.value
        )

# LLM 분류 검사에서 걸러진 질문에 대한 예외 (400)
class NotRealEstateQuestionException(BaseCustomException):
    def __init__(self):
        super().__init__(
            is_success=False,
            http_status=NotRealEstateQuestion.HTTP_STATUS.value,
            code=NotRealEstateQuestion.CODE.value,
            message=NotRealEstateQuestion.MESSAGE.value
        )