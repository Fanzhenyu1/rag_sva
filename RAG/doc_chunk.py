from langchain_text_splitters import RecursiveCharacterTextSplitter

def langchain_doc_chunk(documents, chunk_size = 500, chunk_overlap = 20):
    splitter = RecursiveCharacterTextSplitter(
        # separators=["\n# ", "\n## ", "\n### ", "\n#### ", "\n\n"],
        separators=["\n\n##", "\n\n###"],
        chunk_size = chunk_size, 
        chunk_overlap = chunk_overlap
    )
    chunks = splitter.split_documents(documents)
    print(f"Chunk has been finished.")
    print(f"Number of chunks: {len(chunks)}")
    return chunks
