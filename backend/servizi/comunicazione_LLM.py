import openai
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") # Configurazione OpenAI API Key

# Configurazione chiave Gemini

# Configurazione chiamata Gemini 1.5
def comunicazione_gemini1_5(prompt):
    # Implementare
    # Implementare
    # Implementare
    # Implementare
    return risposta

# Configurazione chiamata Gemini 2.0
def comunicazione_gemini2_0(prompt):
    # Implementare
    # Implementare
    # Implementare
    # Implementare
    return risposta

# Configurazione chiamata GPT-4
def comunicazione_gpt4(prompt):
    response = openai.Completion.create(
        model = "gpt-4",
        prompt = prompt,
        max_tokens = 150,
        temperature = 0.7
    )
    risposta = response.choices[0].text.strip()
    return risposta