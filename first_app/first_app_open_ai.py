import os
from dotenv import load_dotenv

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain_experimental.tools import PythonAstREPLTool
from langchain.llms import OpenAI


load_dotenv()


llm = OpenAI(temperature=0., model="gpt-3.5-turbo-instruct")
agent = initialize_agent(
 tools = [PythonAstREPLTool()], 
 llm=llm, 
 agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
 verbose=True
)
agent.run("whats 4 * 4")
