import openai
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") # Configurazione OpenAI API Key

# Configurazione chiave Gemini

def comunicazione_gpt4(prompt):
    response = openai.Completion.create(
        model = "gpt-4",
        prompt = prompt,
        max_tokens = 150,
        temperature = 0.7
    )
    risposta = response.choices[0].text.strip()
    return risposta

def comunicazione_gemini1_5(prompt):
    # Implementare
    # Implementare
    # Implementare
    # Implementare
    return risposta

def comunicazione_gemini2_0(prompt):
    # Implementare
    # Implementare
    # Implementare
    # Implementare
    return risposta