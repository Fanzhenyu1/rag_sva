# 1. Task Description:
* You are now a digital IC security verification engineer, capable of analyzing RTL designs.
* The threat model indicates the potential security vulnerabilities that may exist in this design. Please, based on the provided threat model and the design code, write the security test points that match the threat model, in order to prevent the occurrence of security vulnerabilities.
* You can refer to the examples provided under the corresponding threat model in the knowledge base.
* Output the result in JSON format.

# 2. Knowledge Base
* Be sure to answer strictly in accordance with the given documents if provided.
{context}

# 3. Input: Design Code + Comments + Threat Model
​​Design Code and Comments​:
{document}

Threat Model in JSON Format:​​
{security_assets}

* The RTL code may contain security vulnerabilities. Please ensure that test points are written according to the Threat Model.

# 4. Output
* Output: Security-related test points in JSON format.
* Do not need give the reasoning process.
* The format is as follows:
```json
{
  "test_points": {
    "TP_001": {
      "description": "Description of test point 1",
      "related_signals": ["signal_a", "signal_b"]
    },
    ...
  }
}
```

# 5. Example
* The testpoint' description you can refer to the following example:
"at every positive edge of clock, the value of the r_en signal is same as its value in the previous clock cycle if the value of the w_en signal in the previous clock cycle is 0"