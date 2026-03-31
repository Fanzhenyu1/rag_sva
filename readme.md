# 使用方法说明

## 项目文件说明

- benchmarks：测试源文件，包含设计与复现实现所需的安全信息等
- lib_data：搭建硬件安全知识数据库的资源文件
- RAG：断言生成系统的主要实现代码
- recycle_bin：可废弃
- rules：三阶段LLM推理链的prompt & 复现实现所用的一阶段prompt
- rules_1：预处理采用的prompt & RAG系统的query搭建prompt
- temp: 执行流程的生成结果 & 中间结果
- test: 集成流程执行的可执行文件，包含naive-RAG/hyb-RAG可选调用，3阶推理/1阶推理可选

## 代码执行准备

- python环境准备
requirements.txt提供了本研究使用python的相关依赖
推荐python版本，3.12.7
可以使用如下指令安装依赖
```bash
pip install -r requirements.txt
```

- LLM-key配置
本研究主要使用deepseek以及openai相关模型的API
deepseek的API-KEY通过添加环境变量"DEEPSEEK_API_KEY"进行配置
openai的API-KEY可通过添加环境变量"OPENAI_API_KEY"或在.env文件中进行配置

- 其他相关配置
RAG混合检索需要准备milvus向量数据库，否则使用默认的bge-small-en-v1.5实现常规检索

## 代码执行

1. 进入test文件夹
执行以下指令
```bash
cd ./test
```

2. 执行engine.py文件
执行以下指令
```bash
python engine.py -b 1 -d 0 -r 1
```
其中-b参数表示是否进行benchmark基准测试，-d参数表征设计命名，以便生成对应设计的相关结果，-r参数表征是否采用RAG
文件内可以设置采用简单RAG或者混合检索RAG，以及是否使用3-stage推理
当采用一阶推理以及混合检索RAG时，会生成answer_property_all_h.txt文件至目标文件夹./temp/bm_temp/0/

以下给出相关代码执行结果
```json
{
  "design_name": "lock_reg",
  "description": "A register lock module with data input/output, read enable (r_en), write enable (w_en), lock signal, clock, and reset. The register stores data_in when w_en is high and reset is low. The lock signal is present but not functionally connected in the given RTL, indicating a potential security flaw.",
  "security_properties": {
    "assertion_1": "assert property (@(posedge clk) disable iff (rst) lock |-> $stable(data));",
    "assertion_2": "assert property (@(posedge clk) disable iff (rst) (lock && w_en) |-> (data == $past(data)));",
    "assertion_3": "assert property (@(posedge clk) disable iff (rst) (lock && w_en) |-> (data_in == $past(data_in)));",
    "assertion_4": "assert property (@(posedge clk) disable iff (rst) (lock && w_en) |-> (data_out == $past(data_out)));",
    "assertion_5": "assert property (@(posedge clk) disable iff (rst) (lock && w_en) |-> (data == $past(data, 1)));",
    "assertion_6": "assert property (@(posedge clk) disable iff (rst) (lock && w_en) |-> (data_in == $past(data_in, 1)));",
    "assertion_7": "assert property (@(posedge clk) disable iff (rst) (lock && w_en) |-> (data_out == $past(data_out, 1)));"
  }
}
```

3. 断言检查
断言检查依赖questasim检查工具，以及[LLMs_for_HW_Assertions](https://github.com/seth-lab-tamu/LLMs_for_HW_Assertions)提供的完整benchmark仿真环境
以下给出相应tcl脚本以执行断言检查，文件目录需要按需修改
```tcl
vlib work
vmap work work

vlog -sv -cover bst ../src/dut_buggy.sv
vlog -sv -cover bst ./assertion_buggy.sv
vlog -sv -cover bst ../tb/tb.sv

vdir tb

vsim -voptargs="+acc" -assertdebug -coverage work.tb

run -all
quit -sim
```

4. 断言仿真结果
以下给出相关的断言通过questasim进行仿真的结果
```log
# do sim.do
# ** Warning: (vlib-34) Library already exists at "work".
# QuestaSim-64 vmap 10.7c Lib Mapping Utility 2018.08 Aug 18 2018
# vmap work work 
# Modifying modelsim.ini
# QuestaSim-64 vlog 10.7c Compiler 2018.08 Aug 18 2018
# Start time: 11:02:02 on Nov 26,2025
# vlog -sv -cover bst ../src/dut_buggy.sv 
# -- Compiling module lock_reg
# 
# Top level modules:
# 	lock_reg
# End time: 11:02:02 on Nov 26,2025, Elapsed time: 0:00:00
# Errors: 0, Warnings: 0
# QuestaSim-64 vlog 10.7c Compiler 2018.08 Aug 18 2018
# Start time: 11:02:02 on Nov 26,2025
# vlog -sv -cover bst ./assertion_buggy.sv 
# -- Compiling module v_dut_buggy
# 
# Top level modules:
# 	v_dut_buggy
# End time: 11:02:02 on Nov 26,2025, Elapsed time: 0:00:00
# Errors: 0, Warnings: 0
# QuestaSim-64 vlog 10.7c Compiler 2018.08 Aug 18 2018
# Start time: 11:02:02 on Nov 26,2025
# vlog -sv -cover bst ../tb/tb.sv 
# -- Compiling module tb
# 
# Top level modules:
# 	tb
# End time: 11:02:02 on Nov 26,2025, Elapsed time: 0:00:00
# Errors: 0, Warnings: 0
# Library vendor : Model Technology
# Maximum unnamed designs : 3
# MODULE tb
# vsim -voptargs=""+acc"" -assertdebug -coverage work.tb 
# Start time: 11:02:02 on Nov 26,2025
# ** Note: (vsim-8009) Loading existing optimized design _opt
# //  Questa Sim-64
# //  Version 10.7c win64 Aug 18 2018
# //
# //  Copyright 1991-2018 Mentor Graphics Corporation
# //  All Rights Reserved.
# //
# //  QuestaSim and its associated documentation contain trade
# //  secrets and commercial or financial information that are the property of
# //  Mentor Graphics Corporation and are privileged, confidential,
# //  and exempt from disclosure under the Freedom of Information Act,
# //  5 U.S.C. Section 552. Furthermore, this information
# //  is prohibited from disclosure under the Trade Secrets Act,
# //  18 U.S.C. Section 1905.
# //
# Loading sv_std.std
# Loading work.tb(fast)
# Loading work.lock_reg(fast)
# Loading work.v_dut_buggy(fast)
# ** Error: Assertion failed: data changed while lock is on
#    Time: 25 ns Started: 25 ns  Scope: tb.lock_reg_u.i_bind_dut_buggy File: ./assertion_buggy.sv Line: 23 Expr: data==$past(data)
# ** Error: Assertion failed: data changed while lock is on
#    Time: 105 ns Started: 105 ns  Scope: tb.lock_reg_u.i_bind_dut_buggy File: ./assertion_buggy.sv Line: 23 Expr: data==$past(data)
# ** Error: Assertion failed: data changed while lock is on
#    Time: 175 ns Started: 175 ns  Scope: tb.lock_reg_u.i_bind_dut_buggy File: ./assertion_buggy.sv Line: 23 Expr: data==$past(data)
# ** Error: Assertion failed: data changed while lock is on
#    Time: 255 ns Started: 255 ns  Scope: tb.lock_reg_u.i_bind_dut_buggy File: ./assertion_buggy.sv Line: 23 Expr: data==$past(data)
# ** Error: Assertion failed: data changed while lock is on
#    Time: 295 ns Started: 295 ns  Scope: tb.lock_reg_u.i_bind_dut_buggy File: ./assertion_buggy.sv Line: 23 Expr: data==$past(data)
# ** Error: Assertion failed: data changed while lock is on
#    Time: 385 ns Started: 385 ns  Scope: tb.lock_reg_u.i_bind_dut_buggy File: ./assertion_buggy.sv Line: 23 Expr: data==$past(data)
# ** Error: Assertion failed: data changed while lock is on
#    Time: 405 ns Started: 405 ns  Scope: tb.lock_reg_u.i_bind_dut_buggy File: ./assertion_buggy.sv Line: 23 Expr: data==$past(data)
# ** Error: Assertion failed: data changed while lock is on
#    Time: 525 ns Started: 525 ns  Scope: tb.lock_reg_u.i_bind_dut_buggy File: ./assertion_buggy.sv Line: 23 Expr: data==$past(data)
# ** Error: Assertion failed: data changed while lock is on
#    Time: 645 ns Started: 645 ns  Scope: tb.lock_reg_u.i_bind_dut_buggy File: ./assertion_buggy.sv Line: 23 Expr: data==$past(data)
# ** Error: Assertion failed: data changed while lock is on
#    Time: 705 ns Started: 705 ns  Scope: tb.lock_reg_u.i_bind_dut_buggy File: ./assertion_buggy.sv Line: 23 Expr: data==$past(data)
# ** Error: Assertion failed: data changed while lock is on
#    Time: 725 ns Started: 725 ns  Scope: tb.lock_reg_u.i_bind_dut_buggy File: ./assertion_buggy.sv Line: 23 Expr: data==$past(data)
# ** Error: Assertion failed: data changed while lock is on
#    Time: 765 ns Started: 765 ns  Scope: tb.lock_reg_u.i_bind_dut_buggy File: ./assertion_buggy.sv Line: 23 Expr: data==$past(data)
# ** Error: Assertion failed: data changed while lock is on
#    Time: 775 ns Started: 775 ns  Scope: tb.lock_reg_u.i_bind_dut_buggy File: ./assertion_buggy.sv Line: 23 Expr: data==$past(data)
# ** Error: Assertion failed: data changed while lock is on
#    Time: 785 ns Started: 785 ns  Scope: tb.lock_reg_u.i_bind_dut_buggy File: ./assertion_buggy.sv Line: 23 Expr: data==$past(data)
# ** Error: Assertion failed: data changed while lock is on
#    Time: 925 ns Started: 925 ns  Scope: tb.lock_reg_u.i_bind_dut_buggy File: ./assertion_buggy.sv Line: 23 Expr: data==$past(data)
# ** Error: Assertion failed: data changed while lock is on
#    Time: 935 ns Started: 935 ns  Scope: tb.lock_reg_u.i_bind_dut_buggy File: ./assertion_buggy.sv Line: 23 Expr: data==$past(data)
# ** Error: Assertion failed: data changed while lock is on
#    Time: 955 ns Started: 955 ns  Scope: tb.lock_reg_u.i_bind_dut_buggy File: ./assertion_buggy.sv Line: 23 Expr: data==$past(data)
# ** Note: $finish    : ../tb/tb.sv(56)
#    Time: 1005 ns  Iteration: 0  Instance: /tb
# End time: 11:02:03 on Nov 26,2025, Elapsed time: 0:00:01
# Errors: 17, Warnings: 0
```