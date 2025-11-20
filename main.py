from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from tools import search_tool, wiki_tool, save_tool
import os

load_dotenv()

print("=== AGENTE DE INVESTIGACIÓN (Groq - Llama 3.3) ===\n")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2,
)

prompt = ChatPromptTemplate.from_messages([
    ("system",
     "Responde SIEMPRE en español. "
     "Si lo necesitas, puedes usar herramientas. "
     "Devuelve un texto normal, bien redactado."),
    ("human", "{input}")
])

tools = [search_tool, wiki_tool, save_tool]
llm_with_tools = llm.bind_tools(tools)

chain = prompt | llm_with_tools

query = input("¿Sobre qué tema quieres investigar? ")

try:
    result = chain.invoke({"input": query})
    print("\nRESPUESTA:\n")
    print(result.content if hasattr(result, "content") else result)

except Exception as e:
    print("⚠ ERROR:\n", e)
