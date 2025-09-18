import os
from langchain_community.document_loaders import UnstructuredFileLoader


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
    
    loader = UnstructuredFileLoader(file_path,mode="elements",autodetect_encoding=True)
    documents = loader.load()
    print(f"#### Document loaded from {file_path} has been finished. ####")

    return documents

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