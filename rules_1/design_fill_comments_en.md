# 1.Task Description:
- You are now a digital IC engineer. You need to analyze the RTL design and SPEC to add comments for RTL module.
- You are required to complete the following tasks:
  - 1. Analyze the specification/design code to identify the key components, such as interfaces, signals, behaviors, etc.
  - 2. Add comments for RTL design, including design features, descriptions of key signals or registers, descriptions of logical or sequential behaviors, etc.
- Output the comment information for RTL design in JSON format.

# 2.Input: Design Code / SPEC Documentation
- The design code / SPEC documentation provided below serves as input for analysis:
{document}

# 3.Output: Design Analysis Results
- Output: Output the results in JSON format.
- The specific format and output content are as follows:
```json
{
  "design_name": "Module Name",  
  "comment_info": "Information about the design's function and feature",  
  "comment_signal": [  
    {  
      "signal_name": "Key Signal/Register Name 1 in the module",  
      "signal_description": "Commentary information about the signal/register's functionality, etc."  
    },  
    ...  
  ],  
  "comment_logic": [  
    {  
      "logic_name": "Name of key logical/sequential behavior 1 in the module",  
      "logic_description": "Commentary information about the module's key logical/sequential behaviors, etc.",  
      "related_signals": ["Related Signal/Register Name 1", "Related Signal/Register Name 2", ...]  
    },  
    ...  
  ]
}
```
