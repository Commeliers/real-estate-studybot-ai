import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

load_dotenv()

AZURE_OPENAI_API_KEY          = os.getenv("OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT         = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_TYPE             = os.getenv("OPENAI_API_TYPE")
AZURE_OPENAI_API_VERSION      = os.getenv("OPENAI_API_VERSION")
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

chat_client = AzureChatOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    openai_api_type=AZURE_OPENAI_TYPE,
    openai_api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
    deployment_name=AZURE_OPENAI_CHAT_DEPLOYMENT_NAME,
    temperature=0.0,    # 결정적(deterministic) 결과
    max_tokens=5        # “부동산” 또는 “비부동산”만 반환
)

REAL_ESTATE_LABEL = "부동산"
NON_REAL_ESTATE_LABEL = "비부동산"

def classify_real_estate(question: str) -> bool:
    """
    AzureChatOpenAI를 사용해 '부동산 관련 질문' 여부를 판단합니다.
    - 부동산과 연관 있다면 “부동산”만, 아니면 “비부동산”만 반환하도록 유도
    - 반환값이 REAL_ESTATE_LABEL("부동산")이면 True, 그렇지 않으면 False
    """
    
    # 분류용 프롬프트 정의
    messages = [
        SystemMessage(content=(
            "당신은 한국어 부동산 도메인 분류기입니다.\n"
            "아래 예시를 보고, 질문이 부동산과 조금이라도 관련 있으면 “부동산”만, "
            "관련 없으면 “비부동산”만 반환하세요.\n"
            "예시1) “아파트 전세와 월세의 차이가 뭐예요?” → 부동산\n"
            "예시2) “축구 경기 언제야?” → 비부동산\n"
            "예시3) “부동산 중개수수료 비율이 어떻게 되나요?” → 부동산\n"
            "예시4) “오늘 점심 메뉴 추천해줘” → 비부동산\n"
        )),
        HumanMessage(content=question)
    ]

    try:
        response = chat_client(messages)
        reply = response.content.strip()

        # 터미널 로그(디버깅) 출력
        print(f"[Classifier] question={question!r} -> reply={reply!r}")
        return (reply == REAL_ESTATE_LABEL)
    except Exception as e:
        # 분류 호출 중 에러 발생 시 안전하게 False 처리
        print(f"[Classifier] error: {e}")
        return False