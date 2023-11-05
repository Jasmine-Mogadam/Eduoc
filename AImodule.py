from PyPDF2 import PdfReader
from dotenv import load_dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.embeddings import CohereEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS
import constants
import cohereconstant
import cohere
#from langchain.prompts import PromptTemplate
#from langchain.chains import Cohere
#from langchain.chains import OpenAI

from langchain.chains.question_answering import load_qa_chain
#from langchain.
from langchain.llms import Cohere

#code partially sourced from: https://www.youtube.com/watch?v=TLf90ipMzfE
import os

osTrackCohere = True


if not osTrackCohere:
    os.environ["OPENAI_API_KEY"] = constants.APIKEY


#create rerouter, if PDF do this, otherwise use text reader
reader = PdfReader("C:\\Users\\FBITinfoilprotection\\Desktop\\chatgptexperiments\\langchain\\JeffreyEdwards.pdf")

raw_text = ''
for i, page in enumerate(reader.pages):
    text = page.extract_text()
    if text:
        raw_text += text

raw_text[:100]
# potential problem is if pdf is decoded


text_splitter = CharacterTextSplitter(
    separator = "\n",
    chunk_size = 1000,
    chunk_overlap = 200,
    length_function = len,
)
texts = text_splitter.split_text(raw_text)

if(osTrackCohere):
    embeddings = CohereEmbeddings(cohere_api_key=cohereconstant.APIKEY)
else:
    embeddings = OpenAIEmbeddings()
    
#takes text chunks and finds corresponding embeddings
docsearch = FAISS.from_texts(texts, embeddings)





chain = load_qa_chain(Cohere(cohere_api_key=cohereconstant.APIKEY), chain_type="stuff")

query = "who is the person featured in this document?"
docs = docsearch.similarity_search(query)
print(chain.run(input_documents=docs, question=query))





#read documentation, put it on top of mind before coding


def load_pdf() 

def chunkify_pdf() 
    #takes in a pdf file and returns a list of strings
    #needs to autocreate number of chunks according to text size

    return chunks_object_array, num_chunks

def embed_chunks(chunks_object_array, num_chunks) 
    #create as many embeddings according to chunks


def LLM_API_CALL() 
    
#vector search fails when not enough information concerning query
#need to handle validation check to handle fail cases
#also rejection case by USEr to flush out bad responses or queries

def chat_interface()

def chat_history()

def reroute_info_to_doc()
    #toggle what messages user wants doctor to see
    #reroutes information


#options to consider
    #1. overhead tracking of consent, multilevel consent on metadata to certain data
    #2. info passed through chatpgt that has metadata consent or clearance levels needs to perserve it accross information exchange
    #constitutional ai

