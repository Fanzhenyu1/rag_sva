import pymupdf4llm
from pathlib import Path

# input_file = "E://mylife_yanjiu//project//rag_sva//lib_data//RadixCWEGuide_0821V2-.pdf"
input_file = "E://mylife_yanjiu//project//AssertLLM//spec//aes.pdf"

def pymupdf4llm_convert(input_file: str):
    # Using pymupdf4llm to Extract PDF content as Markdown
    md_text = pymupdf4llm.to_markdown(doc=input_file, 
                                    # pages=[8,9,10,11,12],
                                    )
    # Path("../lib_data/output.md").write_bytes(md_text.encode())
    Path("../lib_data/spec/aes_spec.md").write_bytes(md_text.encode())
    print("Markdown saved to aes_spec.md")
    return 0

if __name__ == "__main__":
    pymupdf4llm_convert(input_file)