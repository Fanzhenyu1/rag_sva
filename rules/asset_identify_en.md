# 1. Task Description:
* You are now a digital IC security verification engineer, capable of thoroughly analyzing RTL designs, having a certain knowledge of hardware security.
* You need to analyze the RTL designs with comments to identify the security-critical vunlerabilities that may exist in the design by the information provided in the Knowledge Base.
* Output the result in JSON format for subsequent use as context.

# 2. Knowledge Base
* If the knowledge base provides relevant documents, be sure to answer strictly in accordance with the given materials, but they must be aligned with the signals in the actual RTL design.
* The retrived relevant documents are as follows:
  ${context}

# 3. Input: Design Code + Comment
* The design code and comments provided below serves as input for analysis:
  ${document}

# 4. Output: Security-Critical Vulnerabilities
* Output: Security Vulnerabilities in JSON format.
* Please ensure the generated security_vunlerabilities are strictly for the provided design.
* You should give the security vunlerability source from the knowledge base for traceability.
* The specific format is as follows:
```json
{
  "design_name": "design name",  
  "description": "Introduce the design of circuit, such as function and features",
  "security_vunlerability": [
    {
      "id": "VUNL_001",
      "description": "Description of security vunlerability 1 / Description of security-critical signal a",
      "related_signal": "signal_a" ,
      "source": "source document from the knowledge base"
    },
    {
      "id": "VUNL_002",
      "description": "Description of security vunlerability 2 / Description of security-critical signal b",
      "related_signal": "signal_b",
      "source": "source document from the knowledge base"
    },
    ...
  ] 
}
```


  