from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from dotenv import load_dotenv
import os
from backend.memory_store import get_session_history
from langchain_groq import ChatGroq


load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

SYSTEM_PROMPT = """
You are an AI-powered Medical Assistant.

You provide evidence-based, structured, and easy-to-understand health information.

You do not diagnose or prescribe.
Include medical disclaimer when appropriate.
Keep responses clear and structured.
"""

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_PROMPT),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{question}")
    ]
)

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile",
    temperature=0.2,
    max_tokens=1024
)

chain = prompt | llm

# memory wrapper
chain_with_memory = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="question",
    history_messages_key="history",
)

def get_medical_response(question: str, session_id: str):
    try:
        response = chain_with_memory.invoke(
            {"question": question},
            config={"configurable": {"session_id": session_id}}
        )
        return response.content
    except Exception as e:
        return "⚠️ AI service temporarily unavailable."