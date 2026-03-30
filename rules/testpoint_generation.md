# Input: Design File & Threat model
Given the source design file and the corresponded comments as follows:
{document}
Given the threat model corresponded to the design:
{security_assets}

# Knowledge Base
{context}

# Task Description:
You are required to complete the following tasks:
1. Based on the provided threat model and the RTL design, write the security specification that match the threat model.
2. You can refer to the examples provided in the knowledge base if the threat model corresponded.
3. Output the security specification in json format.

# Output: Security Specification in JSON format
* The output format is as follows, do not give the reasoning process.
```json
{
    "SP_001": {
      "description": "Description of specification 1",
      "related_signals": ["signal_a", "signal_b"]
    },
    ...
}
```
* The description of specification you can refer to the following example:
"at every positive edge of clock, the value of the r_en signal is same as its value in the previous clock cycle if the value of the w_en signal in the previous clock cycle is 0"