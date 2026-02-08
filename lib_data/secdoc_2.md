## Vul_A_0001: Register Lock Failure
### Description
* Design Description: 
Register Lock module related. 
* Threat Model:
The register lock fails to lock register when lock function is enabled. Improper clearing of the lock bit or improper lock function implementation enables malicious software to modify critical registers.
* Security Requirement:
The lock register cannot be modified when the lock signal is on.

### Example: Register Lock Failure
* Example:
A simple register lock module. The expected security behavior is, at every positive edge of clock, the value of the data register is same as its value in the previous clock cycle if the value of the lock signal in the previous clock cycle is 1.
* Related CWE:
CWE-1233: Improper Hardware Lock Protection for Security Sensitive Controls.

## Vul_A_0002: Improper Traffic Controller Function
### Description
* Design Description: 
A simple traffic controller.
* Threat Model:
Traffic controller skips yellow before going red when walk button is pressed on green.
* Security Requirement:
Traffic changes should from red -> green -> yellow -> red. If a pedestrian presses walk button, traffic should stop for 4 cycles.

### Example: Improper Traffic Controller Function
* Example:
A simple traffic controller. The expected security behavior is, at every positive edge of clock, if the value of the signal register is RED, then the value of the signal register in the previous clock cycle is either RED or YELLOW.
* Related CWE:
CWE-1245: Improper Finite State Machines (FSMs) in Hardware Logic.

## Vul_A_0003: JTAG Has Improper Password Lock Function
### Description
* Design Description: 
A JTAG module is locked with a password by default. When the password is entered incorrectly, the JTAG interface is locked. 
* Threat Model:
The lock function is not implemented correctly, allowing attackers to write to locked JTAG.
* Security Requirement:
The JTAG interface should be locked with a password and the lock function should be implemented correctly, attackers should not be able to write to locked JTAG.

### Example: JTAG Has Improper Password Lock Function
* Example:
JTAG module in cva6 processor. The expected security behavior is, at every positive edge of clock, the value of the dmi_req_valid signal is 0 if the value of the pass_check signal is 0.
* Related CWE:
CWE-1324: Sensitive Information Accessible by Physical Probing of JTAG Interface.

## Vul_A_0004: Improper Access Control Implementation
### Description
* Design Description: 
Access control bus.
* Threat Model:
When access to the peripheral, the access control bus grants it access to other peripherals illegally.
* Security Requirement:
The access control should be implemented correctly, the privilege level cannot be maliciously modified.

### Example: Improper Access Control Implementation
* Example:
at every positive edge of clock, for each of the PRIV_TYPES number of privilege arrays in the acc_ctrl_c matrix, the value of each of the NB_PERIPHERALS number of peripherals is same as the corresponding bit in the acc_ctrl array where the value for the ith privilege type of the jth peripheral is stored in the (j*PRIV_TYPES + i)th bit.
* Related CWE:
CWE-1317: Missing Security Checks in Fabric Bridge

## Vul_A_0005: AES Security-critical data are visible externally
### Description
* Design Description: 
AES accelerator. Internal register of AES are visible externally.
* Threat Model:
Incorrect implementation of AES enables attackers to illegally extract information from security-critical data such as key registers, cipher text in AES.
* Security Requirement:
the cipher text cannot be read until encryption is done.

### Example: AES Security-critical data are visible externally
* Example:
AES accelerator. The expected security behavior is, at every positive edge of clock, the value of the rdata signal is 0 if the value of ct_valid signal is 0 and the value of the address is greater than or equal to 12 and less than or equal to 15 and the value of the en signal is 1.
* Related CWE:
CWE-1303: Non Transparent Sharing of Microarchitectural Resources.

## Vul_A_0006: AES Secret Keys Not Cleared When Entering Debug Mode
### Description
* Design Description: 
AES accelerator. Secret keys are not cleared when entering debug mode.
* Threat Model:
The challenge response authorization is not applying to all debug accesses thus giving an attacker access to some security sensitive registers, such as AES keys.
* Security Requirement:
the key is cleared if the debug mode is entered.

### Example: AES Secret Keys Not Cleared When Entering Debug Mode
* Example:
AES accelerator. The expected security behavior is, at every positive edge of clock, the value of the key_big2 signal is 0 if the value of the debug_mode_i signal is 1 in the current clock cycle and 0 in the past clock cycle.
* Related CWE:
CWE-1244: Improper Access to Sensitive Information Using Debug and Test Interfaces.

## Vul_A_0007: Privileged CSR register can be accessed by unprivileged user
### Description
* Design Description: 
CSR controller of the processor.
* Threat Model:
Incorrect implementation of the CSR controller allows attackers access to privileged CSRs.
* Security Requirement:
When accessing CSR from a lower than required privilege level, the privilege violation should be triggered.

### Example: Privileged CSR register can be accessed by unprivileged user
* Example:
CSR controller of the processor. The expected security behavior is, at every positive edge of clock, the value of the privilege_violation signal is 1 if any bit of the priv_lvl_o signal is 0 while the corresponding bit of the priv_lvl signal is 1 and the value of the csr_op_i signal is among the four values CSR_WRITE, CSR_SET, CSR_CLEAR, CSR_READ.
* Related CWE:
CWE-1261: Improper Handling of Single Event Upsets

## Vul_A_0008: Register lock has incorrect default values
### Description
* Design Description: 
Register lock.
* Threat Model:
Register locks are configured with incorrect default values at reset.
* Security Requirement:
The register lock should be configured with correct default values at reset.

### Example: Register lock has incorrect default values
* Example:
Register lock. The expected security behavior is, at every positive edge of clock, all the BIT_WIDTH number of bits of each of the NO_WORDS number of elements in the reglk_mem array are set to 1 if the value of the rst signal in the previous clock cycle is 1.
* Related CWE:
CWE-276: Incorrect Default Permissions.

## Vul_A_0009: ADC Wakeup Timer Incorrectly Configured at Reset
### Description
* Design Description: 
ADC controller.
* Threat Model:
Incorrect implementation of the Wakeup timer in ADC controller allows attackers to bypass the wakeup timer.
* Security Requirement:
The ADC wakeup timer should be configured with correct values at reset.

### Example: ADC Wakeup Timer Incorrectly Configured at Reset
* Example:
ADC controller. The expected security behavior is, at every positive edge of clock other than when the rst_i signal is 0, the value of the wakeup_timer_cnt_q signal is 0 in the next clock cycle if the value of the cfg_fsm_rst_i signal in this clock cycle is 1.
* Related CWE:
CWE-1221: Incorrect Register Defaults or Module Parameters.

## Vul_A_0010: The system failed to reset as required
### Description
* Design Description: 
Reset manager.
* Threat Model:
Reset does not follow fall even after maximum clock cycles of input trigger.
* Security Requirement:
Reset should follow fall of input signal within a given range of clock cycles unless input is asserted again.

### Example: The system failed to reset as required
* Example:
Reset manager. The expected security behavior is, at every positive edge of clock other than when the rst_i signal is 1, if the por_n_i signal falls, then in a minimum of MIN_CYCLES clock cycles and a maximum of MAX_CYCLES clock cycles, the value of the por_n_i signal should become 1 or the value of the rst_por_aon_n signal should become 0.
* Related CWE:
CWE-1206

## Vul_A_0011: Measure the time encryption takes can obtain security-critical information
### Description
* Design Description: 
AES encryption engine. The encryption time varies under different key lengths. Side-channel vulnerability.
* Threat Model:
By measuring the time encryption takes, an attacker can obtain information about which key was used. 
* Security Requirement:
Different configurations of security sensitive operations should all take the same amount of time to avoid leaking information that can be used in a timing side channel attack.

### Example: Measure the time encryption takes can obtain security-critical information
* Example:
AES encryption engine. The expected security behavior is, When different lengths of encryption keys are used, the number of clock cycles from the initial stage to the completion of encryption is consistent.
* Related CWE:
CWE-203: Observable Discrepancy. 

## Vul_A_0012: Sensitive Information in HRoT Local SRAM Not Removed Before Reuse
### Description
* Design Description: 
SoC Level. Hardware Root of Trust (HRoT) local SRAM, TMCU, etc.
* Threat Model:
Bugs or malice in parts of the system external to the HRoT-local SRAM that may obtain privileged information from uncleared privileged regions after a mode-switch.
* Security Requirement:
Information from the range [PRIV_END_ADDR : PRIV_START_ADDR] must not leave the SRAM once zeroization has been triggered unless the range is zeroized, the tmcu is in privileged mode, or zeroization has not been requested. 

### Example: Sensitive Information in HRoT Local SRAM Not Removed Before Reuse
* Example:
SoC Level. Hardware Root of Trust (HRoT) local SRAM, TMCU, etc. The expected security behavior is, In the hardware root of trust, data residing in the privileged address space of the local SRAM (ranging from PRIV_START_ADDR to PRIV_END_ADDR) is strictly prohibited from being exposed to external interfaces. Access to this privileged data is permitted only under two specific conditions: first, when the system is operating in privileged mode—indicated by tmcu.CSR.priv_mode being set to true, which signifies the execution of trusted high-privilege software; and second, during a zeroization procedure—when tmcu.CSR.zeroize_status equals 0, typically indicating that the system is actively performing a security erasure operation. Under all other circumstances, data leakage from the privileged memory region is blocked.
* Related CWE:
CWE-226: Sensitive Information in Resource Not Removed Before Reuse.

## Vul_A_0013:  access the cipher text before all rounds have completed
### Description
* Design Description: 
Encryption Module. AES module.
* Threat Model:
A mistake in the implementation of the AES algorithm allows a malicious actor to access the cipher text before all rounds have completed. 
* Security Requirement:
No information about the data in the cipher should flow to the output until all rounds are completed.

### Example: access the cipher text before all rounds have completed
* Example:
Encryption Module. AES module. The expected security behavior is, The output of the AES substitution box (sbox_data_o) is forbidden from directly influencing the primary data output of the AES module (data_o). However, this prohibition has one specific exception: This direct information flow is only permitted during the very last round of the encryption/decryption process, precisely when the current round counter (round_i) equals the total defined number of rounds (NUM_ROUNDS).
* Related CWE: 
CWE-325: Missing Cryptographic Step.

## Vul_A_0014:  The incorrect implementation of FSM leads to unexpected errors
### Description
* Design Description: 
FSM of Program Interrupt controller module in processor core.
* Threat Model:
Core0 implements an error handler using the programmable interrupt controller module core0.pic. The module contains an FSM that that may transition into a state that is intended to triple fault, the core0 CPU and reset the device.
* Security Requirement:
Core0.pic.fsm must not enter the triple fault-triggering state unless authorization flags associate with the privilege level are set i.e. the CPU is running privileged code.

### Example: The incorrect implementation of FSM leads to unexpected errors
* Example:
FSM of Program Interrupt controller module in processor core. The expected security behavior is, core0.pic.fsm must not enter the triple fault-triggering state unless authorization flags associate with the privilege level are set i.e. the CPU is running privileged code.
* Related CWE: 
CWE-440: Expected Behavior Violation.

## Vul_A_0015: Untrusted processor be able to access data in the HRoT SRAM
### Description
* Design Description: 
SoC Level. Hardware Root of Trust (HRoT) local SRAM, DMA module, etc.
* Threat Model:
The Core0 processor is running software at the lowest privilege level and the security access policy prevents it from accessing any data in the HRoT.SRAM memory. The access policy allow the DMA to read and write data in the HRoT.SRAM memory. An untrusted agent running code on the Core0 processor can access data in the HRoT SRAM by programming the DMA so that it appears that the DMA is the source of the transaction.
* Security Requirement:
The untrusted processor must not be able to access data in the HRoT SRAM.

### Example: Untrusted processor be able to access data in the HRoT SRAM
* Example:
SoC Level. Hardware Root of Trust (HRoT) local SRAM, DMA module, etc. The expected security behavior is, the data in SRAM of HRoT must not flow to the untrusted processor. The access to the HRoT SRAM is controlled by the DMA module, but the DMA module should ensure that the data in the SRAM is not exposed to the untrusted processor.
* Related CWE: 
CWE-441: Unintended Proxy or Intermediary ('Confused Deputy').

## Vul_A_0016: not properly isolate shared resources between trusted and untrusted agents
### Description
* Design Description: 
SoC Level. Hardware Root of Trust (HRoT) local SRAM, untrusted processor core, hrot_iface etc.
* Threat Model:
we assume that the threat is from malicious software in the untrusted domain. We assume this software has access to the core{0-N} memory map and can be running at any privilege level on the untrusted cores. The capability of this threat in this example is communication to and from the mailbox region of SRAM modulated by the hrot_iface.
* Security Requirement:
Information must not enter or exit the shared region of SRAM through hrot_iface when in secure or privileged mode. 

### Example: not properly isolate shared resources between trusted and untrusted agents
* Example:
SoC Level. Hardware Root of Trust (HRoT) local SRAM, untrusted processor core, hrot_iface etc. The expected security behavior is, The privileged range in the SRAM model is bounded by SHARED_START_ADDR and SHARED_END_ADDR. The values for SHARED_END_ADDR and SHARED_START_ADDR are constants provided by the user. Data in this privileged range is only allowed to flow to the external interface of the hardware trust root (hrot_iface) when the system is currently in privileged mode (srm.csr.priv_mode is true). In non-privileged mode, data is prohibited from flowing out. Data input from the external interface of the hardware trust root can be written to this privileged range SRAM at any time, but there is a key exception: when the system is in privileged mode, such input data is strictly prohibited from being written.
* Related CWE: 
CWE-1189: Improper Isolation of Shared Resources on System on-a-Chip (SoC)

## Vul_A_0017: DMA Device Enabled Too Early in Boot Phase
### Description
* Design Description: 
SoC level. Direct Memory Access (DMA) Module. DMA controller. 
* Threat Model:
The untrusted DMA in the SoC example may be enabled by one of the untrusted cores core{0-N} and may access the entire memory range of the SoC before the security configuration is set up by the Hardware Root of Trust (HRoT). An attacker running un-privileged code may set up the dma to read and write protected resources such as sram in the HRoT before the security policy is configured and thus access sensitive data. 
* Security Requirement:
The un-trusted DMA must not be active until the full secure boot sequence is complete. This means data in the dma must not flow out of the dma and data must not flow into the dma until secure boot is complete. 

### Example: DMA Device Enabled Too Early in Boot Phase
* Example:
SoC level. Direct Memory Access (DMA) Module. DMA controller. The expected security behavior is, data must not flow into or out of the dma until boot is complete.
dma.data_reg =/=> dma.$all_outputs unless ( tmcu.csr.boot_stage >= FULL_BOOT )
dma.data_in =/=> dma.data_reg unless ( tmcu.csr.boot_stage >= FULL_BOOT )
* Related CWE: 
CWE-1190: DMA Device Enabled Too Early in Boot Phase

## Vul_A_0018: Exposed Chip Debug and Test Interface With Insufficient or Missing Authorization
### Description
* Design Description: 
debug interface in the HRoT. debug module.
* Threat Model:
Assuming the debug interface in the HRoT is disabled by default and is only enabled when sufficiently authorized e.g., through password protection. A malicious actor can read internal signals in the design through the debug interface if the disabling logic is bypassed.
* Security Requirement:
Information on the internal signals connected to the Trusted Bus(tbus) must not flow to the debug interface outputs unless the debug interface is enabled. 

### Example: Exposed Chip Debug and Test Interface With Insufficient or Missing Authorization
* Example:
debug interface in the HRoT. debug module. The expected security behavior is, Information on the internal signals connected to the Trusted Bus(tbus) must not flow to the debug interface outputs unless the debug interface is enabled. 
tbus.$all_outputs =/=> debug.$all_outputs unless ( debug.enable == ENABLED )
* Related CWE: 
CWE-1191: Exposed Chip Debug and Test Interface With Insufficient or Missing Authorization

## Vul_A_0019: Power-On of Untrusted Execution Core Before Enabling Fabric Access Control
### Description
* Design Description: 
memory and fabric access controls. untrusted firmware.
* Threat Model:
The un-trusted cores core{0-N} fetch instructions from instruction memory in the peripheral IP & memory sub-system and master transactions on the interconnect system. These processors should not be enabled until the interconnect access policy is programmed by the tmcu during the secure boot process. However, Untrusted software executes before interconnect access policy is configured allowing access to the entire SoC memory space including secure areas. 
* Security Requirement:
Untrusted software must not execute i.e. un-trusted cores may not read instruction memory before secure boot process is complete. 

### Example: Power-On of Untrusted Execution Core Before Enabling Fabric Access Control
* Example:
memory and fabric access controls. untrusted firmware. The expected security behavior is, Untrusted software must not execute i.e. un-trusted cores may not read instruction memory before secure boot process is complete. 
imem.idata =/=> core0.idata unless ( tmcu.csr.boot_stage >= FULL_BOOT ) 
* Related CWE: 
CWE-1193: Power-On of Untrusted Execution Core Before Enabling Fabric Access Control

## Vul_A_0020: Failure to Disable Reserved Bits
### Description
* Design Description: 
TMCU. Reserved registers build during the development cycle in tmcu.
* Threat Model:
Features controlled by reserved bits are not properly disabled in the production version of the design allowing an adversary to enable unsupported features which may have negative security consequences. 
* Security Requirement:
All reserved register bits should have no effect on design behavior and reserved register bits should not be writable.

### Example: Failure to Disable Reserved Bits
* Example:
TMCU. Reserved registers build during the development cycle in tmcu. The expected security behavior is,  information in bits in the reserved address range should not have any effect on design behavior, i.e. information should not flow to the output of the memory or register module which holds the information.
tmcu.csr.data_out when (tmcu.addr >= RESERVED_ADDR_START && tmcu.addr <= RESERVED_ADDR_END) =/=> tmcu.$all_outputs 
* Related CWE: 
CWE-1209: Failure to Disable Reserved Bits
