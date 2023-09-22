import os

from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()

api_key = os.environ['openai_api_key']

llm = OpenAI(openai_api_key=api_key, temperature=0.5)
