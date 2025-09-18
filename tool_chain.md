# Tool Chain
## 1.document conversion tools

### 1.1 PDF-Markdown Converter
- [MinerU](https://github.com/opendatalab/mineru)
  - 优势：开源，PDF识别效果出色
  - 缺点：社区提交较多bug，部署可能存在复杂的环境依赖问题
  - 相关教程：
    [快速开始](https://opendatalab.github.io/MinerU/zh/)
    [多格式文件转Markdown实战](https://blog.csdn.net/2401_85325726/article/details/149031296)
    [国产PDF智能提取神器：MinerU项目安装运行实践](https://zhuanlan.zhihu.com/p/22501660011)

- [PyMuPDF4LLM](https://pymupdf.cn/en/latest/pymupdf4llm/index.html)
  - 优势：开源，容易部署，使用简单
  - 缺点：PDF识别效果可能不如MinerU
  - 相关教程：
    [高级RAG：使用PyMuPDF4LLM解析PDF的图片和表格](https://juejin.cn/post/7443801946538803226)

## 2. Markdown Loader
- [UnstructuredFileLoader](https://js.langchain.ac.cn/docs/integrations/document_loaders/)
  - 优势：Langchain框架集成，开源易于使用，支持多格式文本载入
  - 缺点：
  - 相关教程：
    [轻松解析多格式文档：使用UnstructuredLoader的完整指南](https://juejin.cn/post/7437347202479456308)
    [LangChain:万能的非结构化文档载入详解](https://zhuanlan.zhihu.com/p/624812261)

## 3. Text Splitter
- [RecursiveCharacterTextSplitter](https://python.langchain.ac.cn/docs/how_to/recursive_text_splitter/)
  - 优势：Langchain框架集成，开源
  - 缺点：
  - 相关教程：
    [LangChain的文本分割大师：RecursiveCharacterTextSplitter全方位解析](https://jishuzhan.net/article/1951439144651108354)
    [深入理解RecursiveCharacterTextSplitter](https://blog.csdn.net/engchina/article/details/143318366)

## 4. Embedding Model
- "BAAI/bge-small-en-v1.5"
  - 优势：使用的RAG项目中自带的向量数据库，参数量很小，33.4M，适合快速部署
  - 缺点：嵌入效果一般。后续考虑部署更大模型
- "Qwen3"
![本地路径](E://mylife_yanjiu//project//rag_sva//picture//embedding_model_rank.png)

## 5. Vector Database

