# 1. Task Description:
* You need to summarize the key content from the provided context document to create a concise query.
  * Analyze the context document to determine the design name and what type of circuit design it is.
  * Briefly analyze and identify the key signals in the design, providing a simple description of their functions.
  * Based on this circuit design, briefly explain the functions implemented by the circuit.
* Output the analysis results in txt format, keeping the output within 500 tokens, for subsequent use as a query to retrieve information from a vector database.

# 2. Input: Context Document
* The context document provided below serves as input for analysis.
  ${document}

# 3. Output: Concise Query
* Output: Present the output in txt format.
* The specific format and the content to be included are as follows:
```txt
<Design Name> is a circuit design that implements... functions, containing key signals..., which serve the purposes of... respectively.
Based on the above information, retrieve possible threat models, security vulnerabilities, security assets, or security propertys, etc.
```
