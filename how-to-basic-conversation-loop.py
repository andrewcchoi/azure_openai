import os
import openai

from dotenv import load_dotenv

load_dotenv()

openai.api_type = "azure"
openai.api_version = os.getenv("AZURE_OPENAI_VERSION_GPT") 
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")  # Your Azure OpenAI resource's endpoint value .
openai.api_key = os.getenv("AZURE_OPENAI_KEY")
engine_openai = os.getenv("AZURE_OPENAI_ENGINE")

conversation=[{"role": "system", "content": "You are a helpful assistant."}]

try:
    print("Start typing")
    while(True):
        user_input = input()      
        conversation.append({"role": "user", "content": user_input})

        response = openai.ChatCompletion.create(
            engine=engine_openai, # The deployment name you chose when you deployed the ChatGPT or GPT-4 model.
            messages = conversation
        )

        conversation.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
        print("\n" + response['choices'][0]['message']['content'] + "\n")

except KeyboardInterrupt as ke:
    print("Chat Closed")

except Exception as e:
    print(e)
