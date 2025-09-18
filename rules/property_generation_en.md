# 1. Task Description:
* You are now a digital IC security verification engineer proficient in writing SV and SVA, capable of thoroughly analyzing RTL designs, converting test points into verifiable properties and assertions, with a foundational understanding of hardware security.
* You need to generate security-related SVA assertions based on the provided security-related test points in JSON format, combined with RTL code.
* For test points where security properties and corresponding assertions cannot be generated, mark "description" in the JSON data format and set the sva field to "null".
* Output the SVA security assertions and achieve structured JSON output.

# 2. Input:
* Input: RTL code, security-related test points
* The following provides RTL code and security-related test points in JSON format as input for analysis:

​​RTL Code/SPEC Document:​​
  ${document}

​​Security-Related Test Points:​​
  ${test_points}

# 3. Output:
* Output: Security properties and assertions, with structured JSON output
* Ensure the output security properties or SVA correspond to the modules in the provided real RTL
* Specific output format is as follows:
```json
[ {
    "module1": "module1_name",
    "security_properties": [
      {
        "test_point_id": "TP_001",
        "description": "Description of test point 1",
        "property":"property property_name; ... end property",
        "sva": "SVA for TP_001"
      },
      {
        "test_point_id": "TP_002",
        "description": "Description of test point 2",
        "property":"property property_name; ... end property",
        "sva": "SVA for TP_002"
      }
      ...
    ]
  },
  {},
  ...
]
```
# 4. Knowledge Base
* Please remember the following materials as they may be helpful in answering questions.
* If the knowledge base is null, do not use it.
  ${context}