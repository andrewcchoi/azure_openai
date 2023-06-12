import os
import openai
import tiktoken

from dotenv import load_dotenv

load_dotenv()

openai.api_type = "azure"
openai.api_version = os.getenv("AZURE_OPENAI_VERSION_GPT")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")  # Your Azure OpenAI resource's endpoint value .
openai.api_key = os.getenv("AZURE_OPENAI_KEY")
engine_openai = os.getenv("AZURE_OPENAI_ENGINE")
temp = float(os.getenv("TEMPERATURE"))
model = os.getenv("AZURE_OPENAI_MODEL")

system_message = {"role": "system", "content": "You are a helpful assistant."}
max_response_tokens = int(os.getenv("MAX_RESPONSE_TOKENS")) # 250
token_limit= int(os.getenv("TOKEN_LIMIT")) # 4096
conversation=[]
conversation.append(system_message)

def num_tokens_from_messages(messages, model=model):
    encoding = tiktoken.encoding_for_model(model)
    num_tokens = 0
    for message in messages:
        num_tokens += 4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":  # if there's a name, the role is omitted
                num_tokens += -1  # role is always required and always 1 token
    num_tokens += 2  # every reply is primed with <im_start>assistant
    return num_tokens

try:
    print("Start typing")
    while(True):
        user_input = input("")     
        conversation.append({"role": "user", "content": user_input})
        conv_history_tokens = num_tokens_from_messages(conversation)

        while (conv_history_tokens+max_response_tokens >= token_limit):
            del conversation[1] 
            conv_history_tokens = num_tokens_from_messages(conversation)
            
        response = openai.ChatCompletion.create(
            engine=engine_openai, # The deployment name you chose when you deployed the ChatGPT or GPT-4 model.
            messages = conversation,
            temperature=temp,
            max_tokens=max_response_tokens,
        )

        conversation.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
        print("\n" + response['choices'][0]['message']['content'] + "\n")

except KeyboardInterrupt as ke:
    print("Chat Closed")

except Exception as e:
    print(e)
