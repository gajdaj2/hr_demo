import PyPDF2
import chromadb
import os

import openai
from chromadb.utils import embedding_functions
from langchain.text_splitter import RecursiveCharacterTextSplitter

from pdf_read import get_text_from_pdf

os.environ['OPENAI_API_KEY'] = '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'

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,
                                               chunk_overlap=100)

client = chromadb.PersistentClient(path="chroma.db")
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key="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",
    model_name="text-embedding-ada-002"
)

# collection = client.create_collection(name="resumes", embedding_function=openai_ef)
collection = client.get_collection(name="resumes")
files = ['1.pdf', '2.pdf', '3.pdf']

# for file in files:
#     collection.add(documents=[get_text_from_pdf(file) for file in files],
#                    metadatas=[{"source": file} for file in files],
#                    ids=[file for file in files])

result = collection.query(query_texts=["What this persons know about Java ? "], n_results=4)

print("1 kandydat")
print(result['documents'][0][0])

print("2 kandydat")
print(result['documents'][0][1])

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": "You are HR assistant "
        },
        {
            "role": "user",
            "content": "Your job is analysis of resumes bellow.\nCheck this points:\n1. What they know about Java from 1-100 \n2. What they know about Docker from 1-100\n 3. What they know about Git from 1-100 \n 4. Sum points and give score to best candidate with best score label 'Best candidate' and other 'Other'\n 5. Give explanation why this candidate is best of this job in max 200 tokens'  \nIn result generate only csv file in format like bellow don't genereate anything else \n : Candidate;Git [%];Java [%];Docker [%];Classification;Explanation" +
                       str(result['documents'][0])
        }
    ],
    temperature=1,
    max_tokens=2000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

import csv
print(response["choices"][0]["message"]["content"])

data = response["choices"][0]["message"]["content"]

with open('dane3.csv', 'w', newline='', encoding='utf-8') as file:
    file.write(data)