from PyPDF2 import PdfReader
from dotenv import load_dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.embeddings import CohereEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS
#import constants
#import cohereconstant
import cohere
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from langchain.chains.question_answering import load_qa_chain
#from langchain.
from langchain.llms import Cohere

#code partially sourced from: https://www.youtube.com/watch?v=TLf90ipMzfE
import os



#TO DO
#
#
#  1.  add prompt engineering
#
#
#  2.  add validation
#
#
#  3. make sure its
#
#
#
#  4.  can you add voice functionality?  with play.ht?


APIKEY = "uMMJCaKxLNlvfKkkX2bUnNpm3nwazk6EeYfMWCxT"

def pdf_or_text_chat(mode, query, pdf):

    osTrackCohere = True

    if(mode=="pdf"):
        #pdf chat mode

        #create rerouter, if PDF do this, otherwise use text reader
        reader = PdfReader(pdf)

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
            embeddings = CohereEmbeddings(cohere_api_key=APIKEY)
        else:
            embeddings = OpenAIEmbeddings()
            
        #takes text chunks and finds corresponding embeddings
        docsearch = FAISS.from_texts(texts, embeddings)


        chain = load_qa_chain(Cohere(cohere_api_key=APIKEY), chain_type="stuff")

        #query = "who is the person featured in this document?"
        docs = docsearch.similarity_search(query)
        print(chain.run(input_documents=docs, question=query))
        #REDO PRINT, YOU DONT NEED PRINT EXCEPT FOR DEBUGGING

    if mode=="text":   
        #normal single prompt chat mode
        question = query
        template = """QUESTION: {question}

        #Answer: Let's think step by step."""

        prompt = PromptTemplate(template=template, input_variables=["question"])

        llm = Cohere(cohere_api_key=APIKEY)

        llm_chain = LLMChain(prompt=prompt, llm=llm)


        print(llm_chain.run(question))

    return ValueError("mode must be pdf or text")



if __name__ == "__main__":
    pdf_or_text_chat("pdf", "who is the person featured in this document?", "C:\\Users\\FBITinfoilprotection\\Desktop\\chatgptexperiments\\langchain\\JeffreyEdwards.pdf")
