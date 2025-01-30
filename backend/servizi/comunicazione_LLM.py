from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
import google.generativeai as genai

client = OpenAI()

# Impostazione chiavi API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# Configurazione comunicazione con Gemini 1.5
def comunicazione_gemini_1_5(prompt):
    response = genai.chat.completions.create(
        model="gemini-1.5",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=0.5
    )
    risposta = response["choices"][0]["message"]["content"].strip()
    return risposta

# Configurazione comunicazione con Gemini 2.0
def comunicazione_gemini_2_0(prompt):
    response = genai.chat.completions.create(
        model="gemini-2.0",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=0.5
    )
    risposta = response["choices"][0]["message"]["content"].strip()
    return risposta

# Configurazione comunicazione con GPT-4
def comunicazione_gpt_4(prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=0.5
    )
    risposta = response["choices"][0]["message"]["content"].strip()
    return risposta