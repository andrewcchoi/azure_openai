import requests
import time
import os

from dotenv import load_dotenv

load_dotenv()

api_base = os.getenv("AZURE_OPENAI_ENDPOINT") 
api_key = os.getenv("AZURE_OPENAI_KEY")
api_version = os.getenv("AZURE_OPENAI_VERSION_DALLE")
url = f"{api_base}openai/images/generations:submit?api-version={api_version}"
headers= { "api-key": api_key, "Content-Type": "application/json" }
body = {
    "prompt": "a multi-colored umbrella on the beach, disposable camera",
    "size": "1024x1024",
    "n": 1
}
submission = requests.post(url, headers=headers, json=body)

operation_location = submission.headers['operation-location']
status = ""
while (status != "succeeded"):
    time.sleep(1)
    response = requests.get(operation_location, headers=headers)
    status = response.json()['status']
image_url = response.json()['result']['data'][0]['url']

print(response)
print(image_url)