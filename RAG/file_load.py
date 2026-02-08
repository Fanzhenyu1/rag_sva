import os
from langchain_community.document_loaders import UnstructuredFileLoader
from langchain.schema import Document

def load_file(file_path: str):
    """
    Load a file using UnstructuredFileLoader from langchain_community.

    Args:
        file_path (str): The path to the file to be loaded.

    Returns:
        List[Document]: A list of Document objects loaded from the file.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    # loader = UnstructuredFileLoader(file_path,mode="elements",autodetect_encoding=True)
    # documents = loader.load()
    # pass
    # print(f"#### Document loaded from {file_path} has been finished. ####")

    # return documents
    # 直接读取整个文件内容，构造单个 Document，延后到 doc_chunk 中进行切分

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()
    document = Document(page_content=text, metadata={"source": file_path})
    print(f"#### Document loaded from {file_path} has been finished. ####")
    pass
    return [document]

def load_files(file_paths: list[str]):
    """
    Load multiple files using UnstructuredFileLoader from langchain_community.

    Args:
        file_paths (List[str]): A list of paths to the files to be loaded.

    Returns:
        List[Documents]: A list of Document objects loaded from the files.
    """
    all_documents = []
    for file_path in file_paths:
        docs = load_file(file_path)
        all_documents.extend(docs)

    return all_documents

if __name__ == "__main__":
    dir_path = "e:/mylife_yanjiu/project/rag_sva/source_document"
    file_paths = [
        os.path.join(dir_path, f)
        for f in os.listdir(dir_path)
        if os.path.isfile(os.path.join(dir_path, f))
    ]
    load_files(file_paths)