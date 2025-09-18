# 面向SVA生成的Prompt制定规则（安全相关）

## 1. prompt相关方法
### 1.1 角色赋予
- 明确Agent担任的角色
```
"你是一名数字IC安全验证工程师，熟悉形式化验证流程，并掌握SVA编写"
```

### 1.2 结构化设计prompt
- 使用XML标签来构造
```XML
<instructions>
具体任务，目的，要求等："编写SVA断言，语法正确，符合SPEC规范"
</instructions>

<context>
上下文信息：SPEC规范
</context>

<examples>
上下文示例
</examples>

<formatting>
期望输出的格式要求
</formatting>
```
- 使用markdown，json等为代表的半结构化文档
```markdown
# 1.任务描述:
...
## 1.2 具体要求：
- 
...
# 2.示例：
...
# 3.输出格式：
...
```

### 1.3 思维链（CoT）引入
- 明确任务划分，分步完成具体任务
- SVA生成任务可被划分为：
  - 安全资产识别与信号映射
  - 测试点提取
  - 硬件安全属性与断言编写

### 1.4 少样本提示（few-shot）
- 提供回答示范

### 1.5 结构化输出答案
- 输出答案时，使用结构化输出，如XML、JSON等

### 1.6 内容限定关键提示
- 限制大模型输出，避免幻觉
```
"如果所提供的信息不足以回答问题，请明确告知“根据现有信息，我无法回答这个问题”。切勿编造答案。"
```

### 1.7 添加内容分割标记
- 将提示词和变量{documents}分开
- 确保提示词模板中变量${documents}只出现一次
```markdown
# 知识库
请记住以下材料，它们可能对回答问题有帮助。

${documents}
```

## 2. SVA生成任务划分

### 2.1 安全资产识别
- 输入：SPEC文档，RTL设计
- 输出：安全资产json型数据格式
- 分析SPEC文档，提取安全关键信号/资产，并于实际RTL设计中的信号进行匹配
- 生成json型数据格式，以供后续作为上下文使用

```json
{
  "SPEC_name": "SPEC命名",  
  "description": "描述SPEC的内容",
  "security_assets": [
    {
      "id": "ASSET_001",
      "description": "安全资产1的描述/安全关键信号a的描述",
      "related_signal": "signal_a" 
    },
    {
      "id": "ASSET_002",
      "description": "安全资产2的描述/安全关键信号b的描述",
      "related_signal": "signal_b"
    }
    ...
  ] 
}
```

### 2.2 SPEC分析与安全测试点提取
- 输入：SPEC文档，安全资产
- 输出：测试点json型数据格式
**具体要求**
- 分析SPEC文档，提取测试点
- 生成json型数据格式，以供后续作为上下文使用

```json
{
  "spec_name": "SPEC命名",
  "description": "描述SPEC的内容",
  "test_points": [
    {
      "id": "TP_001",
      "description": "测试点1的描述",
      "related_signals": ["signal_a", "signal_b"]
    },
    {
      "id": "TP_002",
      "description": "测试点2的描述",
      "related_signals": ["signal_c", "signal_d"]
    }
    ...
  ]
}
```

### 2.3 SVA安全断言生成
- 输入：测试点json型数据格式，RTL代码
- 输出：json型数据格式的安全属性与SVA断言
**具体要求**
- 根据测试点json型数据格式，生成SVA安全断言
- 对于无法生成安全属性以及相应断言的测试点，需在json型数据格式中"description"标注，且sva字段标注为"null"
- 输出带SVA安全断言的RTL代码，且实现json的结构化输出
```json
[ {
    "module1": "module1_name",
    "security_properties": [
      {
        "test_point_id": "TP_001",
        "description": "测试点1的描述",
        "property":"property property_name; ... end property",
        "sva": "SVA for TP_001"
      },
      {
        "test_point_id": "TP_002",
        "description": "测试点2的描述",
        "property":"property property_name; ... end property",
        "sva": "SVA for TP_002"
      }
      ...
    ]
  },
  {},
  ...
]

```

## 3. 具体prompt设计

### 3.1 安全资产识别
- 使用LLM，对SPEC文档或者直接对RTL设计进行分析，提取安全关键信号/资产，并与实际RTL设计中的信号进行匹配

```markdown
# 1.任务描述：
- 你现在是一名数字IC安全验证工程师，熟悉掌握SPEC文档的理解，可以充分分析RTL设计，对于数字IC的验证工作有足够的经验，对于硬件安全领域的知识有一定了解。
- 你需要识别出SPEC文档或者RTL设计中所涉及的安全关键信号/资产。
- 在缺少SPEC文档情况下，可以在知识库中寻找相关资料作为SPEC，但需与实际RTL设计中的信号进行匹配。
- 输出json型数据格式，以供后续作为上下文使用。

# 2.输入：设计代码/SPEC文档
- 以下提供设计代码/SPEC文档，作为输入以进行分析
${document}

# 3.输出：安全资产
- 输出：安全资产json型数据格式
- 具体格式如下：
```json
{
  "SPEC_name": "SPEC命名",  
  "description": "描述SPEC的内容",
  "security_assets": [
    {
      "id": "ASSET_001",
      "description": "安全资产1的描述/安全关键信号a的描述",
      "related_signal": "signal_a" 
    },
    {
      "id": "ASSET_002",
      "description": "安全资产2的描述/安全关键信号b的描述",
      "related_signal": "signal_b"
    }
    ...
  ] 
}
```endjson

# 4.知识库
- 请记住以下材料，它们可能对回答问题有帮助。
- 当在知识库中未找到相关知识时，则不采用知识库中的材料。
${context}
```

### 3.2 SPEC分析与安全测试点提取
- 在提供安全资产json数据的基础上，继续分析SPEC文档或者RTL设计，分析安全资产的相关行为，提取安全相关的测试点。

```markdown
# 1.任务描述：
- 你现在是一名数字IC安全验证工程师，熟悉掌握SPEC文档的理解，可以充分分析RTL设计，对于数字IC的验证工作有足够的经验，对于硬件安全领域的知识有一定了解。
- 你需要根据提供的json型数据的安全资产，并结合SPEC文档或者RTL设计，完成安全相关的测试点提取工作。
- 在缺少SPEC文档情况下，可以在知识库中寻找相关资料作为SPEC，但需与实际RTL设计中的信号进行匹配。
- 输出json型数据格式，以供后续作为上下文使用。

# 2.输入：设计代码/SPEC文档，安全资产json型数据格式
- 以下提供设计代码/SPEC文档，json型数据的安全资产，作为输入以进行分析
${document}
${security_assets}

# 3.输出：安全相关测试点
- 输出：json型数据格式的安全相关测试点
- 具体格式如下：
```json
{
  "spec_name": "SPEC命名",
  "description": "描述SPEC的内容",
  "test_points": [
    {
      "id": "TP_001",
      "description": "测试点1的描述",
      "related_signals": ["signal_a", "signal_b"]
    },
    {
      "id": "TP_002",
      "description": "测试点2的描述",
      "related_signals": ["signal_c", "signal_d"]
    }
    ...
  ]
}
```endjson

# 4.知识库
- 请记住以下材料，它们可能对回答问题有帮助。
- 当在知识库中未找到相关知识时，则不采用知识库中的材料。
${context}
```

### 3.3 SVA安全属性与断言生成
- 根据提供的测试点json型数据格式，结合RTL代码，采用SVA方式，生成安全属性以及安全断言。

```markdown
# 1.任务描述：
- 你现在是一名数字IC安全验证工程师，熟悉掌握SV以及SVA的编写，可以充分分析RTL设计，将测试点转化为可验证的属性以及断言，对于硬件安全领域的知识有一定了解。
- 你需要根据提供的json型数据的安全相关测试点，结合RTL代码，完成安全相关的SVA断言生成工作。
- 对于无法生成安全属性以及相应断言的测试点，需在json型数据格式中"description"标注，且sva字段标注为"null"
- 输出带SVA安全断言的RTL代码，且实现json的结构化输出。

# 2.输入：RTL代码，安全相关测试点
- 以下提供RTL代码，json型数据的安全相关测试点，作为输入以进行分析
${document}
${test_points}

# 3.输出：安全相关的属性以及SVA
- 输出：安全属性以及断言，且实现json的结构化输出
- 保证输出的安全属性或者SVA与提供的真实RTL中的module对应
- 具体输出格式如下：
```json
[ {
    "module1": "module1_name",
    "security_properties": [
      {
        "test_point_id": "TP_001",
        "description": "测试点1的描述",
        "property":"property property_name; ... end property",
        "sva": "SVA for TP_001"
      },
      {
        "test_point_id": "TP_002",
        "description": "测试点2的描述",
        "property":"property property_name; ... end property",
        "sva": "SVA for TP_002"
      }
      ...
    ]
  },
  {},
  ...
]
```endjson

# 4.知识库
- 请记住以下材料，它们可能对回答问题有帮助。
- 当在知识库中未找到相关知识时，则不采用知识库中的材料。
${context}
```

## 4. 示例
- 以UART设计为例,文件路径：e:\mylife_yanjiu\project\AssertLLM
- 提供SPEC文档，以及RTL代码

### 4.1 安全资产识别
```json
{
"SPEC_name": "UART_to_Bus_Core_Specifications",
"description": "UART to Bus IP core specifications enabling access to an internal 16-bit address and 8-bit data bus via UART interface. Supports text mode (ASCII-based) and binary mode (efficient binary protocol) commands for read/write operations, including buffered access with address auto-increment. Core includes UART transceiver modules (receive and transmit), baud rate generator, and command parser. Verified via test benches for both protocols, with synthesis results provided for multiple FPGA families.",
"security_assets": [
{
"id": "ASSET_001",
"description": "UART serial input signal (ser_in). External attack vector for command injection or data eavesdropping; malicious inputs can bypass parser state machine to execute unauthorized bus operations.",
"related_signal": "ser_in"
},
{
"id": "ASSET_002",
"description": "UART serial output signal (ser_out). Potential data leakage point; sensitive internal bus data transmitted externally could be intercepted if not encrypted.",
"related_signal": "ser_out"
},
{
"id": "ASSET_003",
"description": "Internal address bus (int_address). Controls access to memory locations; unauthorized modifications could target critical registers or sensitive memory regions.",
"related_signal": "int_address"
},
{
"id": "ASSET_004",
"description": "Internal write data bus (int_wr_data). Carries data for write operations; tampering could corrupt firmware or configuration data.",
"related_signal": "int_wr_data"
},
{
"id": "ASSET_005",
"description": "Internal read data bus (int_rd_data). Holds data from read operations; exposure could disclose cryptographic keys or sensitive state information.",
"related_signal": "int_rd_data"
},
{
"id": "ASSET_006",
"description": "Write control signal (int_write). Execution trigger for write operations; glitching or forced activation could lead to data corruption.",
"related_signal": "int_write"
},
{
"id": "ASSET_007",
"description": "Read control signal (int_read). Execution trigger for read operations; unauthorized activation could enable data exfiltration.",
"related_signal": "int_read"
},
{
"id": "ASSET_008",
"description": "Bus request signal (int_req). Arbitration control for bus access; denial-of-service attacks could block legitimate access.",
"related_signal": "int_req"
},
{
"id": "ASSET_009",
"description": "Bus grant signal (int_gnt). Authorization control for bus access; bypassing could allow unprivileged bus operations.",
"related_signal": "int_gnt"
},
{
"id": "ASSET_010",
"description": "Parser state machine (main_sm in uart_parser). Critical control logic; fault injection could disrupt command parsing and enable protocol-level exploits.",
"related_signal": "main_sm"
},
{
"id": "ASSET_011",
"description": "Baud rate configuration registers (baud_freq, baud_limit). Timing parameters; manipulation could desynchronize UART communication and facilitate side-channel attacks.",
"related_signal": "baud_freq, baud_limit"
}
]
}
```

### 4.2 SPEC分析与安全测试点提取
```json
{
  "spec_name": "UART_to_Bus_Core_Specifications",
  "description": "UART to Bus IP core enabling access to internal 16-bit address/8-bit data bus via UART interface. Supports text and binary mode commands for read/write operations with address auto-increment. Core includes UART transceiver, baud generator, and command parser modules.",
  "test_points": [
    {
      "id": "TP_001",
      "description": "验证ser_in端口对恶意命令注入的防护能力：发送非常规字符序列尝试破坏状态机，检查是否触发安全复位机制",
      "related_signals": ["ser_in", "reset", "main_sm"]
    },
    {
      "id": "TP_002",
      "description": "测试ser_out数据泄露防护：在读取敏感寄存器时监控ser_out输出，验证未授权数据是否被过滤",
      "related_signals": ["ser_out", "int_rd_data", "int_address"]
    },
    {
      "id": "TP_003",
      "description": "地址越界访问防护测试：尝试访问保留地址空间(0xFFFF+)，验证是否产生总线错误响应",
      "related_signals": ["int_address", "int_req", "int_gnt"]
    },
    {
      "id": "TP_004",
      "description": "写数据篡改检测：注入故障导致int_wr_data位翻转，验证写入校验机制是否生效",
      "related_signals": ["int_wr_data", "int_write", "int_rd_data"]
    },
    {
      "id": "TP_005",
      "description": "读操作授权验证：在无授权状态下激活int_read，验证核心是否拒绝数据返回",
      "related_signals": ["int_read", "int_rd_data", "int_req"]
    },
    {
      "id": "TP_006",
      "description": "总线仲裁安全测试：同时发起多个总线请求，验证仲裁优先级机制防止DoS攻击",
      "related_signals": ["int_req", "int_gnt", "tx_busy"]
    },
    {
      "id": "TP_007",
      "description": "状态机抗干扰能力测试：在关键状态转换时注入时钟毛刺，验证错误恢复机制",
      "related_signals": ["main_sm", "clock", "reset"]
    },
    {
      "id": "TP_008",
      "description": "波特率配置锁定测试：运行时修改baud_freq/baud_limit，验证配置寄存器写保护机制",
      "related_signals": ["baud_freq", "baud_limit", "ce_16"]
    },
    {
      "id": "TP_009",
      "description": "二进制协议缓冲区溢出防护：发送超长数据包(>256B)，验证长度字段边界检查机制",
      "related_signals": ["rx_data", "bin_byte_count", "new_rx_data"]
    },
    {
      "id": "TP_010",
      "description": "关键信号物理隔离验证：通过布局布线检查，确认安全信号与普通I/O的物理隔离度",
      "related_signals": ["int_gnt", "int_write", "ser_in"]
    }
  ]
}
```

### 4.3 SVA安全属性与断言生成
```json
[
  {
    "module": "uart_parser",
    "security_properties": [
      {
        "test_point_id": "TP_001",
        "description": "验证ser_in端口对恶意命令注入的防护能力",
        "property": "property illegal_cmd_recovery;\n  @(posedge clock) disable iff (reset)\n  (main_sm == `MAIN_IDLE) && new_rx_data && \n  !(rx_data inside {8'h00, `CHAR_R_UP, `CHAR_r_LO, `CHAR_W_UP, `CHAR_w_LO, `CHAR_CR, `CHAR_LF}) |=> \n  ##[1:10] (main_sm == `MAIN_EOL) ##[1:5] (main_sm == `MAIN_IDLE);\nend property",
        "sva": "assert property (illegal_cmd_recovery);"
      },
      {
        "test_point_id": "TP_002",
        "description": "测试ser_out数据泄露防护",
        "property": "null",
        "sva": "null"
      },
      {
        "test_point_id": "TP_005",
        "description": "读操作授权验证",
        "property": "property read_authorization;\n  @(posedge clock) disable iff (reset)\n  int_read |-> (int_req && int_gnt);\nend property",
        "sva": "assert property (read_authorization);"
      },
      {
        "test_point_id": "TP_007",
        "description": "状态机抗干扰能力测试",
        "property": "null",
        "sva": "null"
      },
      {
        "test_point_id": "TP_009",
        "description": "二进制协议缓冲区溢出防护",
        "property": "property buffer_overflow_protection;\n  @(posedge clock) disable iff (reset)\n  (main_sm == `MAIN_BIN_DATA) && (bin_byte_count == 8'h01) && new_rx_data |=> \n  ##1 (main_sm == `MAIN_IDLE);\nend property",
        "sva": "assert property (buffer_overflow_protection);"
      }
    ]
  },
  {
    "module": "uart2bus_top",
    "security_properties": [
      {
        "test_point_id": "TP_003",
        "description": "地址越界访问防护测试",
        "property": "property address_boundary_check;\n  @(posedge clock) disable iff (reset)\n  (int_address > 16'hFFFF) |-> !(int_req || int_write || int_read);\nend property",
        "sva": "assert property (address_boundary_check);"
      }
    ]
  },
  {
    "module": "baud_gen",
    "security_properties": [
      {
        "test_point_id": "TP_008",
        "description": "波特率配置锁定测试",
        "property": "property baud_config_lock;\n  @(posedge clock) disable iff (reset)\n  $stable(baud_freq) and $stable(baud_limit);\nend property",
        "sva": "assert property (baud_config_lock);"
      }
    ]
  },
  {
    "module": "global",
    "security_properties": [
      {
        "test_point_id": "TP_004",
        "description": "写数据篡改检测",
        "property": "null",
        "sva": "null"
      },
      {
        "test_point_id": "TP_006",
        "description": "总线仲裁安全测试",
        "property": "property bus_arbitration_safety;\n  @(posedge clock) disable iff (reset)\n  int_req |=> ##[1:10] int_gnt or ##[1:10] !int_req;\nend property",
        "sva": "assert property (bus_arbitration_safety);"
      },
      {
        "test_point_id": "TP_010",
        "description": "关键信号物理隔离验证",
        "property": "null",
        "sva": "null"
      }
    ]
  }
]
```

### 4.4 问题讨论
- 明显发现生成的安全属性或者断言没有很好的对应module，并不存在global模块，需在提示中进行加强。

## 5. 安全断言生成方法优化
## 5.1 添加功能SPEC分析总结-安全需求映射
1. 针对已有的功能SPEC，或者源代码通过LLM进行分析总结，包含电路实现的基本功能（不需要RAG）
2. 通过第一步得到的总结，作为上下文，改写query，对安全漏洞数据库进行检索，找到相关的安全需求，与可能的威胁模型，形成安全SPEC（借助RAG）
3. 根据原设计与得到的安全SPEC，生成安全属性以及安全断言