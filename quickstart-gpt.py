#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai

from dotenv import load_dotenv

load_dotenv()

openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT") 
openai.api_version = os.getenv("AZURE_OPENAI_VERSION_GPT") 
openai.api_key = os.getenv("AZURE_OPENAI_KEY") 
engine_openai = os.getenv("AZURE_OPENAI_ENGINE")

response = openai.ChatCompletion.create(
    engine=engine_openai, # engine = "deployment_name".
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
        {"role": "user", "content": "Do other Azure Cognitive Services support this too?"}
    ]
)

print(response)
print(response['choices'][0]['message']['content'])