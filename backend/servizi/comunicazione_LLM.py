import openai

openai.api_key = "API_KEY" # Configurazione OpenAI API Key

def comunicazione_gpt(prompt):
    response = openai.Completion.create(
        model = "gpt-4",
        prompt = prompt,
        max_tokens = 100,
        temperature = 0.7
    )
    output = response.choices[0].text.strip()
    return output