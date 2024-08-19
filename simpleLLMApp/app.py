import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate




load_dotenv()

parser = StrOutputParser()

model = ChatOpenAI(model="gpt-4", api_key=os.environ["OPENAI_API_KEY"])

'''
messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]

chain = model | parser
translation = chain.invoke(messages)

print(translation)
'''

system_template = "Translate the following from {from_lang} into {to_lang}"
text = "Merhaba Dünya!"
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

chain = prompt_template | model | parser
translation = chain.invoke( {"from_lang": "Turkish", "to_lang": "Italian", "text": text  })
print(translation)
