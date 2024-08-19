import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser


from typing import List

from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes


load_dotenv()

parser = StrOutputParser()

model = ChatOpenAI(model="gpt-4", api_key=os.environ["OPENAI_API_KEY"])


system_template = "Translate the following from {from_lang} into {to_lang}"
text = "Merhaba Dünya!"
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

chain = prompt_template | model | parser
translation = chain.invoke( {"from_lang": "Turkish", "to_lang": "Italian", "text": text  })
print(translation)


# 4. App definition
app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces",
)

# 5. Adding chain route

add_routes(
    app,
    chain,
    path="/chain",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)