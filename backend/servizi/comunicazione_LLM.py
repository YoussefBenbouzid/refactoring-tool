import openai
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") # Configurazione OpenAI API Key

def comunicazione_gpt(prompt):
    response = openai.Completion.create(
        model = "gpt-4",
        prompt = prompt,
        max_tokens = 150,
        temperature = 0.7
    )
    output = response.choices[0].text.strip()
    return output