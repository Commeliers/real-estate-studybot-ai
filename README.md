# 부동산 스터디 챗봇

`LangChain`, `FastAPI`, `Azure OpenAI`를 사용해 부동산 질문에 대해 답하는 학습용 챗봇입니다. 질문에 대한 적절한 답변을 하도록 프롬프트 엔지니어링과 가드레일 설정을 하였습니다.

---

## 📝 소개

이 프로젝트는 부동산 관련 학습용 챗봇으로, 사용자가 입력한 질문을 `Azure OpenAI(LLM)`에 전달해 “핵심 개념 → 실생활 예시 → 추가 질문” 세 가지 요소를 담은 JSON 응답을 생성합니다. `FastAPI` 서버를 통해 클라이언트와 비동기 통신하며, `LangChain`을 활용해 프롬프트 엔지니어링과 `Pydantic` 검증(가드레일)을 함께 적용하여 안정적으로 동작합니다.

![image](https://github.com/user-attachments/assets/051d3601-dc1e-45a3-af6b-8c84f34f14b8)

![image](https://github.com/user-attachments/assets/aed1a744-015d-454b-ad6d-3088fab8873b)

---

## 💻 실제 구현 화면

<img width="1147" height="644" alt="image" src="https://github.com/user-attachments/assets/4ef1130e-ace8-49b6-ac18-0ae3a61210a0" />

<img width="1146" alt="image" src="https://github.com/user-attachments/assets/fb96c9fa-a1d3-4f89-a830-1d40e204b691" />


---

## 📜 인프라 아키텍처 구성도

### 전체 아키텍처

![homeprotector_아키텍처](https://github.com/user-attachments/assets/4ed3c273-7138-479f-8afb-2bc402dbc15e)

### AI 아키텍처
<img width="221" alt="image" src="https://github.com/user-attachments/assets/49293e23-528b-4f73-a568-bbaf25fa1b9f" />



---


## 🔑 주요 특징

- **LangChain + Azure OpenAI**  
  - `AzureChatOpenAI` 인스턴스를 통해 GPT 모델(gpt-4o-mini 등)을 호출  
  - LangChain의 `with_structured_output(RealEstateResponse)`를 통해 Pydantic 스키마 검증을 자동화  

- **FastAPI 서버**  
  - `POST /api/estate` 엔드포인트에 JSON `{ "content": "<질문>" }` 형식으로 요청  
  - 비동기로 모델 호출
  - 커스텀 예외 처리 

- **Prompt‐level 가드레일**  
  - `SystemPrompt`에서 질문에 대한 응답을 JSON 형태로 출력하도록 프롬프트 엔지니어링
  - 비부동산 질문 시 `부동산 관련 질문이 아닙니다. 부동산과 관련된 질문을 해주세요. 😁`로 거절  

- **LLM‐기반 분류기**  
  - `LLM` 분류 모델을 통해 질문이 부동산 관련인지 판단
  - 부동산 관련 질문이 아니면 거절
  - “부동산 키워드가 포함되어도, 문맥상 부동산이 아니면” 거절  

- **Pydantic 스키마 검증 (Output Validation)**  
  - 모델 응답 문자열을 `parse_raw()`로 검증하여 “키 누락”이나 “잘못된 형식” 발생 시 503 예외 처리  
  - 필요 시 추가 내용 검증(부동산 키워드 포함 여부 등) 삽입 가능  

- **Error Handling & Logging**  
  - 모델 호출 실패, 파싱 오류, 가드레일 위반 등 모든 예외 상황을 로깅해 원인 분석 및 가드레일 강화에 활용  
  - FastAPI의 `add_exception_handler`로 `BaseCustomException` 등록  

---

## ⚙️ 디렉터리 구조
```
real-estate-studybot-ai/
├─ app/
│   ├─ config/
│   │   └─ model.py
│   ├─ domain/
│   │   └─ estate/
│   │       ├─ core.py
│   │       ├─ classifier.py
│   │       ├─ exception.py
│   │       ├─ prompt.py
│   │       ├─ router.py
│   │       └─ schema/
│   │           └─ dto.py
│   ├─ error/
│   │   ├─ code.py
│   │   └─ handler.py
│   └─ main.py
├─ .env
└─ README.md

```

## ▶️ 서버 실행
```
# 실행
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# 운영 환경 백그라운드 실행
nohup uvicorn app.main:app --host 0.0.0.0 --port 8000 > uvicorn.log 2>&1 &
```

## 📚 라이브러리 설치
```
pip install fastapi uvicorn python-dotenv openai pydantic langchain-openai langchain-core langchain
```
