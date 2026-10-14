from langchain_ollama import OllamaLLM

low = OllamaLLM(model="llama3.2", temperature=0.1)
high = OllamaLLM(model="llama3.2", temperature=1.0)
prompt = "Write a creative sentence about Artificial Intelligence."
print("LOW TEMPERATURE:")
print(low.invoke(prompt))
print("\nHIGH TEMPERATURE:")
print(high.invoke(prompt))
