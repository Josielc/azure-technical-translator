import os
import uuid
import requests
from dotenv import load_dotenv

load_dotenv()

AZURE_KEY = os.getenv("AZURE_TRANSLATOR_KEY")
AZURE_ENDPOINT = os.getenv("AZURE_TRANSLATOR_ENDPOINT").rstrip("/")
AZURE_REGION = os.getenv("AZURE_TRANSLATOR_REGION")

def translate_text(text, to_lang="pt"):
    url = f"{AZURE_ENDPOINT}/translate"
    params = {"api-version": "3.0", "to": to_lang}

    headers = {
        "Ocp-Apim-Subscription-Key": AZURE_KEY,
        "Ocp-Apim-Subscription-Region": AZURE_REGION,
        "Content-type": "application/json",
        "X-ClientTraceId": str(uuid.uuid4()),
    }

    body = [{"text": text}]
    r = requests.post(url, params=params, headers=headers, json=body)
    r.raise_for_status()
    return r.json()[0]["translations"][0]["text"]
