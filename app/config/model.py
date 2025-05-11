import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# 환경 변수 로드
load_dotenv()

# AzureOpenAI 클라이언트 초기화
client = AzureOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    api_version=os.getenv("OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)

# Azure 포털에서 생성한 배포 이름(deployment name)
DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")