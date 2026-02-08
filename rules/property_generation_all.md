# 1. Task Description:
* You are now a digital IC security verification engineer proficient in writing SVA.
* You need to generate 7 items of security-related SVA assertions step by step. Base on the RTL code provided and Select useful information from the knowledge base to provide the answer.
* You are allowed to generate the same assertion.
* Output the security assertions and achieve structured JSON output.

# 2. Knowledge Base
* Be sure to answer strictly in accordance with the given related documents if provided.
{context}

# 3. Input: RTL code
{document}

# 4. Output:
* Ensure the output SVA is consistent with the provided RTL code.
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
