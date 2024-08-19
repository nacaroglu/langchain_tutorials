import os
from dotenv import load_dotenv
from langchain.llms import Replicate

load_dotenv()

llm = Replicate(
    model="meta/meta-llama-3-8b-instruct",
    model_kwargs={"temperature": 0.75, "max_length": 500, "top_p": 1},
)
prompt = """
User: Can you descibe power of Turkiye in 2050?
Assistant:
"""

result = llm(prompt)

print(result)
