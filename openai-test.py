from openai import OpenAI
import os

client = OpenAI()
client.api_key = os.environ.get("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")
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
# client = OpenAI(
#   api_key=os.environ.get("CUSTOM_ENV_NAME"),
# )