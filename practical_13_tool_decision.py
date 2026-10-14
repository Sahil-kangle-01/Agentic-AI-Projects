from langchain_core.tools import tool
from langchain_ollama import OllamaLLM

@tool
def difficulty(experience: int) -> str:
    """Select interview difficulty based on years of experience."""
    if experience < 2:
        return "Easy"
    return "Advanced"

llm = OllamaLLM(model="llama3.2", temperature=0.3)
years = int(input("Years of experience: "))
level = difficulty.invoke({"experience": years})
prompt = f"""
Generate 3 interview questions.
Difficulty: {level}
Include answers.
"""
result = llm.invoke(prompt)
print("\nDifficulty:", level)
print("\nQuestions:")
print(result)
