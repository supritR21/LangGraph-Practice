import os
import time
from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from langchain_core.language_models import FakeListChatModel
from typing import Union, Dict, Any

# Load env vars
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Define weather tool with more varied responses
def get_weather(city: str) -> str:
    """Get the current weather for a given city.
    
    Args:
        city: The city to get weather for.
        
    Returns:
        A string describing the weather with realistic variations.
    """
    weather_scenarios = [
        f"The weather in {city} is 75°F (24°C) and sunny with a gentle breeze.",
        f"In {city}, it's currently 82°F (28°C) with partly cloudy skies.",
        f"{city} is experiencing 68°F (20°C) with light rain showers.",
        f"Currently in {city}: 90°F (32°C) and humid with a chance of thunderstorms."
    ]
    return weather_scenarios[hash(city) % len(weather_scenarios)]

def create_model() -> Union[ChatGroq, FakeListChatModel]:
    """Create the chat model with proper fallback handling"""
    if not GROQ_API_KEY:
        print("⚠️ No Groq API key found, using mock model")
        return FakeListChatModel(responses=["Mock weather response"])
    
    available_models = ["llama3-70b-8192", "mixtral-8x7b-32768"]
    
    for model_name in available_models:
        try:
            model = ChatGroq(
                model_name=model_name,
                groq_api_key=GROQ_API_KEY,
                temperature=0.7,
            )
            # Test the model with a simple request
            test_response = model.invoke("Hello")
            print(f"✅ Successfully connected to Groq model: {model_name}")
            return model
        except Exception as e:
            print(f"⚠️ Could not initialize {model_name}: {str(e)}")
            continue
    
    print("⚠️ All Groq models failed, falling back to mock model")
    return FakeListChatModel(responses=["Mock weather response"])

def extract_final_response(response: Dict[str, Any]) -> str:
    """Extract the clean final response from the agent's output"""
    messages = response.get('messages', [])
    for msg in reversed(messages):
        if msg.type == "ai" and msg.content:
            return msg.content
    return "Sorry, I couldn't generate a response."

# Create model with proper fallback
model = create_model()

# Create agent
agent = create_react_agent(
    model=model,
    tools=[get_weather],
    prompt="You are a helpful weather assistant. Provide concise weather information when asked.",
)

def ask_agent(question: str) -> str:
    """Ask the agent with proper error handling and clean output"""
    try:
        start_time = time.time()
        response = agent.invoke(
            {"messages": [{"role": "user", "content": question}]}
        )
        processing_time = time.time() - start_time
        
        final_response = extract_final_response(response)
        return f"{final_response} (Response time: {processing_time:.2f}s)"
        
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    questions = [
        "What's the weather in Kolkata?",
        "Can you tell me the weather conditions in Mumbai?",
        "How's the weather looking in Delhi today?"
    ]
    
    print("\n🌦️ Weather Assistant 🌤️")
    print("----------------------")
    
    for question in questions:
        print(f"\nQuestion: {question}")
        response = ask_agent(question)
        print(f"Response: {response}")
        time.sleep(0.5)  # Small delay between requests