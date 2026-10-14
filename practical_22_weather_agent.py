import requests
from langchain_ollama import OllamaLLM

city = input("Enter city: ")
url = f"https://wttr.in/{city}?format=j1"
response = requests.get(url, timeout=20)
response.raise_for_status()
data = response.json()
current = data["current_condition"][0]
temp = current["temp_C"]
weather = current["weatherDesc"][0]["value"]
llm = OllamaLLM(model="llama3.2", temperature=0.4)
prompt = f"""
You are a weather assistant.
City: {city}
Weather: {weather}
Temperature: {temp}°C
Give simple advice to a person visiting this city.
"""
print(llm.invoke(prompt))
