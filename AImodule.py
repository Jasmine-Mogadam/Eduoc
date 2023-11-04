import openai
import os

import sys
import chromadb

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('OPENAI_API_KEY')


def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]

messages =  [  
{'role':'system', 'content':'You are a Teacher Assistant for a Computer Science class that evaluates and grades C++ Homework assignments turned in by students.'},    
{'role':'user', 'content':'tell me a joke'},   
  ]

"""
Prompting Principles¶
Principle 1: Write clear and specific instructions
Principle 2: Give the model time to “think”
Tactics
Tactic 1: Use delimiters to clearly indicate distinct parts of the input
Delimiters can be anything like: ```, "".", < >, <tag> </tag>, :
"""

text = f"""
You should express what you want a model to do by \ 
providing instructions that are as clear and \ 
specific as you can possibly make them. \ 
This will guide the model towards the desired output, \ 
and reduce the chances of receiving irrelevant \ 
or incorrect responses. Don't confuse writing a \ 
clear prompt with writing a short prompt. \ 
In many cases, longer prompts provide more clarity \ 
and context for the model, which can lead to \ 
more detailed and relevant outputs.
"""
prompt = f"""
Summarize the text delimited by triple backticks \ 
into a single sentence.
```{text}```
"""
response = get_completion_from_messages(messages, temperature=0)
print(response)





"""
You can either set it as the OPENAI_API_KEY environment variable before using the library:

 !export OPENAI_API_KEY='sk-...'
Or, set openai.api_key to its value:

import openai
openai.api_key = "sk-..."
A note about the backslash
In the course, we are using a backslash \ to make the text fit on the screen without inserting newline '\n' characters.
GPT-3 isn't really affected whether you insert newline characters or not. But when working with LLMs in general, you may consider whether newline characters in your prompt may affect the model's performance.
"""



Load Python libraries to view HTML
from IPython.display import display, HTML
display(HTML(response))







import constants
from langchain.document_loaders import TextLoader
#from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = constants.APIKEY

#https://github.com/jerryjliu/llama_index
from llama_index import VectorStoreIndex, SimpleDirectoryReader

#https://www.youtube.com/watch?v=9AXP7tCI9PI


query = sys.argv[1]




loader = TextLoader('data.txt')
#for a directory instead of file
#loader = DirectoryLoader(".", glob="*.txt")
index = VectorstoreIndexCreator().from_loaders([loader])


print(index.query(query, llm=ChatOpenAI()))







load_pdf() 

chunkify_pdf() 
    #takes in a pdf file and returns a list of strings


embed_chunks() 



LLM_API_CALL() 
    

