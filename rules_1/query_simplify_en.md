# 1. Task Description:
* You are now a digital IC security verification engineer, you need analyze the provided RTL code to create a concise query.
  * Analyze the design to determine the design name and what type of circuit design it is.
  * Identify the key signals in the design, providing a simple description of their functions, explain the functions implemented by the circuit.
* Output the analysis results in txt format within 500 tokens.

# 2. Input: RTL design
{document}

# 3. Output: Concise Query
* The specific format and the content to be included are as follows:
```txt
<Design Name> is a circuit design that implements... functions, containing key signals..., which serve the purposes of... respectively.
Based on the above information, retrieve possible threat models, security related test points and security properties, etc.
```
