from langchain_openai import AzureChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# .env 파일에서 값 읽기
AZURE_OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_TYPE = os.getenv("OPENAI_API_TYPE")
AZURE_OPENAI_API_VERSION = os.getenv("OPENAI_API_VERSION")
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

# AzureChatOpenAI 인스턴스 생성
study_model = AzureChatOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    openai_api_type=AZURE_OPENAI_TYPE,
    openai_api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
    deployment_name=AZURE_OPENAI_CHAT_DEPLOYMENT_NAME,
    temperature=0.1,
)