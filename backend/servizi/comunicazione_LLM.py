import os
import openai
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY
genai.configure(api_key=GEMINI_API_KEY)

# Configurazione comunicazione con Gemini 1.5
def comunicazione_gemini1_5(prompt):
    response = genai.ChatCompletion.create(
        model="gemini-1.5",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
        temperature=0.5
    )
    risposta = response["choices"][0]["message"]["content"].strip()
    return risposta

# Configurazione comunicazione con Gemini 2.0
def comunicazione_gemini2_0(prompt):
    response = genai.ChatCompletion.create(
        model="gemini-2.0",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
        temperature=0.5
    )
    risposta = response["choices"][0]["message"]["content"].strip()
    return risposta

# Configurazione comunicazione con GPT-4
def comunicazione_gpt4(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
        temperature=0.5
    )
    risposta = response["choices"][0]["message"]["content"].strip()
    return risposta