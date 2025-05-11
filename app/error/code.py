from enum import Enum
from starlette import status

class InternalServerError(Enum):
    HTTP_STATUS = status.HTTP_500_INTERNAL_SERVER_ERROR
    CODE = 500
    MESSAGE = "서버 오류가 발생했습니다."

class BadRequest(Enum):
    HTTP_STATUS = status.HTTP_400_BAD_REQUEST
    CODE = 400
    MESSAGE = "잘못된 요청입니다."

class Unauthorized(Enum):
    HTTP_STATUS = status.HTTP_401_UNAUTHORIZED
    CODE = 401
    MESSAGE = "인증이 필요합니다."

class Forbidden(Enum):
    HTTP_STATUS = status.HTTP_403_FORBIDDEN
    CODE = 403
    MESSAGE = "권한이 없습니다."

class NotFound(Enum):
    HTTP_STATUS = status.HTTP_404_NOT_FOUND
    CODE = 404
    MESSAGE = "요청하신 리소스를 찾을 수 없습니다."

class Conflict(Enum):
    HTTP_STATUS = status.HTTP_409_CONFLICT
    CODE = 409
    MESSAGE = "리소스 충돌이 발생했습니다."

class ValidationFailure(Enum):
    HTTP_STATUS = status.HTTP_422_UNPROCESSABLE_ENTITY
    CODE = 422
    MESSAGE = "유효성 검사에 실패했습니다."

class TooManyRequests(Enum):
    HTTP_STATUS = status.HTTP_429_TOO_MANY_REQUESTS
    CODE = 429
    MESSAGE = "요청이 너무 많습니다. 잠시 후 다시 시도해주세요."

class ServiceUnavailable(Enum):
    HTTP_STATUS = status.HTTP_503_SERVICE_UNAVAILABLE
    CODE = 503
    MESSAGE = "서비스를 일시적으로 사용할 수 없습니다."

class GatewayTimeout(Enum):
    HTTP_STATUS = status.HTTP_504_GATEWAY_TIMEOUT
    CODE = 504
    MESSAGE = "게이트웨이 응답이 없습니다."
