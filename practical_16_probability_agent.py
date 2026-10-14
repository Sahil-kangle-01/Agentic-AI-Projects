from langchain_ollama import OllamaLLM

# Educational probability/decision-making demonstration only; not medical advice.
symptom_probability = {"mild": 0.2, "moderate": 0.5, "severe": 0.9}
severity = input("Severity (mild/moderate/severe): ").lower()
if severity not in symptom_probability:
    raise ValueError("Enter mild, moderate, or severe.")
risk = symptom_probability[severity]
if risk > 0.7:
    action = "Seek professional medical attention"
else:
    action = "Monitor symptoms"
llm = OllamaLLM(model="llama3.2", temperature=0.2)
result = llm.invoke(f"Explain this recommendation in simple words:\n{action}")
print("\nRisk:", risk)
print("Recommendation:", action)
print("\nExplanation:")
print(result)
