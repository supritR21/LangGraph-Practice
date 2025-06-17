import os
from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.messages import AnyMessage
from langchain_core.runnables import RunnableConfig
from langgraph.prebuilt.chat_agent_executor import AgentState
from pydantic import BaseModel

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def get_weather(city: str) -> str:  
    """Get weather for a given city."""
    return f"It's always sunny in {city}."

class WeatherResponse(BaseModel):
    answer: str

model = ChatGroq(
    model_name="llama3-70b-8192",  # Updated to currently supported model
    groq_api_key=GROQ_API_KEY,
    temperature=0.7,
)

agent = create_react_agent(
    model=model,
    tools=[get_weather],
    response_format=WeatherResponse
)

# Run the agent
messages = [
    {"role": "system", "content": "You are a helpful weather assistant. Use the provided get_weather tool to check weather conditions."},
    {"role": "user", "content": "what is the weather in Patna?"}
]

response = agent.invoke(
    {
        "messages": messages
    },
    {"configurable": {"temperature": 0.7}}
)

print(response["output"])