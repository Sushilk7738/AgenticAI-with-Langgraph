from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenRouter(
    model="google/gemma-4-26b-a4b-it:free",
    temperature=0.2,
)

response = llm.invoke("Hello! Explain LangGraph in simple terms.")
print(response.content)