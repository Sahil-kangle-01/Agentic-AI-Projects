from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

doc = TextLoader("data.txt", encoding="utf-8").load()
splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
chunks = splitter.split_documents(doc)
print("Number of chunks:", len(chunks))
for i, chunk in enumerate(chunks):
    print("\nChunk", i + 1)
    print(chunk.page_content)
