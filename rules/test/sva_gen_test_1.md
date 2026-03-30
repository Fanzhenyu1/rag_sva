* You are now a digital IC security verification engineer proficient in writing SV and SVA, capable of thoroughly analyzing RTL designs.
* You need to generate security-related SVA assertions based on the provided security requirements.
* Output 7 items of assertions with structured JSON output. You are allowed to generate repetitive(the same) assertions to get 7 items.

* The following provides RTL code as input for analysis:
​​RTL Code:​​
{document}

* Security Requirements:​​
{context}

# Output:
* Specific output format is as follows:
```json
{
    "assertion_1":"assert property ((@posedge clk) ...)",
    "assertion_2":"...",
    ...
}
```
