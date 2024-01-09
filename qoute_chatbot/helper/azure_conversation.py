# import openai

# from config import config

# openai.api_key = config.OPENAI_API_KEY


# def azure_chat_completion(messages: list) -> str:
#     try:
#         response = openai.chat.completions.create(messages=messages)
#         return response['choices'][0]['message']['content']
#     except:
#         return config.ERROR_MESSAGE
