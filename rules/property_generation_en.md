# 1. Task Description:
* You are now a digital IC security verification engineer proficient in writing SVA.
* You need to generate 7 items of security-related SVA assertions based on the provided security-related test points in JSON format and the RTL code which may have security vulnerabilities.
* You are allowed to generate the same assertion.
* Output the SVA security assertions and achieve structured JSON output.

# 2. Knowledge Base
* Be sure to answer strictly in accordance with the given related documents if provided.
{context}

# 3. Input: Design Code + Comments + Security-Related Test Points
​​RTL Code and Comments:​​
{document}

​​Security-Related Test Points:​​
{test_points}

* The RTL code may contain security vulnerabilities. Please ensure that assertions are written according to the test points.

# 4. Output:
* Output: Security properties and assertions, with structured JSON output
* Ensure the output SVA correspond to the provided real RTL. Do not need give the reasoning process.
* Specific output format is as follows:
```json
{
  "design_name": "design name",
  "description": "Introduce the design of circuit",
  "security_properties": {
    "assertion_1":"assert property (@(posedge clk) disable iff (rst) ...)",
    "assertion_2":"...",
    ...
  }
}
```