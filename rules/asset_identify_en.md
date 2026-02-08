# 1. Task Description:
* You need to analyze the RTL designs and Knowledge Base provided to identify the threat model that corresponds to the design.
* Please get Threat Model strictly based on the information provided in the knowledge base.

# 2. Knowledge Base
{context}

# 3. Input: Design Code + Comment
* The design code and comments provided below serves as input for analysis:
{document}

* The RTL code may contain security vulnerabilities. Please ensure that Threat Model are written according to the design.

# 4. Output: Security-Critical Threat Model
* Do not need give the reasoning process.
* The format is as follows:
```json
{
  "threat_model": {
    "TM_001":
    {
      "description": "Description of security threat model 1",
      "related_signal": "signal_a"
    },
    ...
  }
}
```

# 5. Example 
* The threat model' description you can refer to the following example:
"The register lock fails to lock register when lock function is enabled. The lock register can be modified when the lock signal is on."

