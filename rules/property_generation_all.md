# 1. Task Description:
* You are now a digital IC security verification engineer proficient in writing SVA.
* You need to generate 7 items of security-related SVA assertions based on the RTL code provided and security information in the knowledge base. You are allowed to generate the same assertion.
* Output the security assertions and achieve structured JSON output.

# 2. Knowledge Base
* Be sure to answer strictly in accordance with the followed security related documents.
{context}

# 3. Input: RTL code
{document}

# 4. Output:
* Ensure the output SVA is consistent with the provided RTL code. Do not give the reasoning process.
* The output format is as follows:
```json
{
  "design_name": "design name",
  "description": "Introduce the design of circuit",
  "security_properties": {
    "assertion_1":"assert property (@(posedge clk) disable iff (rst) ...);",
    "assertion_2":"...",
    ...
  }
}
```
