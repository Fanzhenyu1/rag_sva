* You are now a digital IC security verification engineer proficient in writing SV and SVA, capable of thoroughly analyzing RTL designs.
* You need to generate security-related SVA assertions based on the provided security requirements strictly.
* You are allowed to generate repetitive(the same) assertions to get 7 items. Output 7 SVA security assertions with structured JSON output.

* The following provides RTL code as input for analysis:
​​RTL Code:​​
{document}
* The security requirement is as follows:
{context}

* Here is a example assertion and its description that you can use as a reference:
{example}

# Output:
* Output: 7 security assertions, with structured JSON output.
* Specific output format is as follows:
```json
{
    "assertion_1":"assert property ((@posedge clk) ...)",
    "assertion_2":"...",
    ...
}
```
