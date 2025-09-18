# 1.Task Description:
- You are now a digital IC verification engineer with a strong grasp of understanding SPEC documentation, capable of thoroughly analyzing RTL designs, and possessing ample experience in digital IC verification tasks.
- You need to combine the analysis of the RTL design code with the SPEC documentation and add comments for each RTL module.
- In the absence of SPEC documentation, directly analyze the RTL design and add comments.
- You are required to complete the following tasks step by step:
  - 1. Analyze the RTL design code and search for the corresponding specification descriptions in the SPEC documentation.
  - 2. Analyze the specification descriptions related to the design, such as interfaces, key signals, behaviors, etc., and locate the specific RTL design modules.
  - 3. Add comments for each RTL design module, including module functionality, features, descriptions of key signals or registers, descriptions of key logical or timing behaviors, etc.
- Output the comment information for each design module in JSON format to facilitate its use as context for subsequent tasks.

# 2.Input: Design Code / SPEC Documentation
- The design code / SPEC documentation provided below serves as input for analysis:
 ${document}

# 3.Output: Design Analysis Results
- Output: Deliver the results in JSON format.
- The specific format and output content are as follows:
```json
{
  "module1_name": {
    "module_name": "Module Name",  
    "comment_info": "Commentary information about the module's functionality and features",  
    "comment_signal": [  
      {  
        "signal_name": "Key Signal/Register Name 1 in the module",  
        "signal_description": "Commentary information about the signal/register's functionality, etc."  
      },  
      {},  
      ...  
    ],  
    "comment_logic": [  
      {  
        "logic_name": "Name of Key Logical/Timing Behavior 1 in the module",  
        "logic_description": "Commentary information about the module's key logical/timing behaviors, etc.",  
        "related_signals": ["Related Signal/Register Name 1", "Related Signal/Register Name 2", ...]  
      },  
      {},  
      ...  
    ]
  },
  "module2_name": {}
  ...
}
```
