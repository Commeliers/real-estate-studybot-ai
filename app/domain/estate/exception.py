from app.error.code import RealEstateAnswerCreateFail
from app.error.handler import BaseCustomException


class RealEstateAnswerCreateFailException(BaseCustomException):
    def __init__(self):
        super().__init__(
            is_success=False,
            http_status=RealEstateAnswerCreateFail.HTTP_STATUS.value,
            code=RealEstateAnswerCreateFail.CODE.value,
            message=RealEstateAnswerCreateFail.MESSAGE.value
        )