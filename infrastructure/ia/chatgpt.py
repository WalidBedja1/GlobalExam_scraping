# Client GPT : dialogue avec OpenAI

import openai
from config import GPT_API_KEY, GPT_CONVERSATION_ID


class ChatGPTClient:
    def __init__(self):
        openai.api_key = GPT_API_KEY

    def ask(self, statement, options):
        # Formate le prompt en fonction de la question
        prompt = f"Question : {statement}\nOptions : {options}\nRéponds de manière concise."

        # Appelle l'API ChatGPT (ou utilisation d’une conversation existante)
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            conversation_id=GPT_CONVERSATION_ID  # si utilisé
        )

        return response.choices[0].message["content"]
