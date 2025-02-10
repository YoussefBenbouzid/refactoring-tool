import os
import time
from google.cloud import aiplatform
from google.oauth2 import service_account
from vertexai.preview.generative_models import GenerativeModel
from google.api_core.exceptions import ResourceExhausted
from dotenv import load_dotenv
from openai import AzureOpenAI

# Configurazione Gemini
configs = [("service_account.json", "innovation-place", "us-central1")]
def init_model(service_account_path, project, region, model_name):
    credentials = service_account.Credentials.from_service_account_file(service_account_path)
    aiplatform.init(
        credentials=credentials,
        project=project,         
        location=region          
    )
    model = GenerativeModel(model_name)
    return model

# Configurazione OpenAI
load_dotenv()
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-08-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)
deployment_name = os.getenv("DEPLOYMENT_NAME")

# Chiamata a Gemini 1.5
def comunicazione_gemini_1_5(prompt: str):
    model = init_model(configs[0][0], configs[0][1], configs[0][2], "gemini-1.5-pro-001")
    try:
        return model.generate_content([prompt]).candidates[0].content.parts[0]._raw_part.text
    except ResourceExhausted:
        print(f"\n! - Gemini 1.5: limitazione delle richieste superata. Si prega di attendere un minuto.")
        time.sleep(60)
        return model.generate_content([prompt]).candidates[0].content.parts[0]._raw_part.text
    except Exception as e:
        print(f"\n! - Gemini 1.5: eccezione ({e}).")

# Chiamata a Gemini 2.0
def comunicazione_gemini_2_0(prompt: str):
    model = init_model(configs[0][0], configs[0][1], configs[0][2], "gemini-2.0-flash-exp")
    try:
        return model.generate_content([prompt]).candidates[0].content.parts[0]._raw_part.text
    except ResourceExhausted:
        print(f"\n! - Gemini 2.0: limitazione delle richieste superata. Si prega di attendere un minuto.")
        time.sleep(60)
        return model.generate_content([prompt]).candidates[0].content.parts[0]._raw_part.text
    except Exception as e:
        print(f"\n! - Gemini 2.0: eccezione ({e}).")

# Chiamata a GPT-4
def comunicazione_gpt_4(prompt):
    response = client.chat.completions.create(
        model=deployment_name,
        messages=[{"role": "user", "content": prompt}],
        temperature=1.0
    )
    risposta = response.choices[0].message.content
    return risposta
