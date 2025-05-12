from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate

from app.domain.estate.prompt import REAL_ESTATE_PROMPT


study_prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(REAL_ESTATE_PROMPT),
        HumanMessagePromptTemplate.from_template("{content}"),
    ]
)