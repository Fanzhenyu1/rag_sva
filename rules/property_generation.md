# Input: Design File & Security Specification
Given the source design file and the corresponded comments as follows:
{document}
Given the security specification corresponded to the design:
{test_points}

# Task Description:
You are required to complete the following tasks:
1. Based on the provided security specification and the RTL design, translating the description information in the specification into security assertions.
2. Output 7 items of security assertions in json format. You are allowed to generate the same assertion.

# Output: Security Assertions
* Specific output format is as follows, do not give the reasoning process.
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