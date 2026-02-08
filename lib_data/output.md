
## - CWE 1220: Insufficient Granularity of Access Control
### Description
The product implements access controls via a policy or other feature with the intention to disable or restrict accesses (reads and/or writes) to assets in a system from untrusted agents. However, implemented access controls lack required granularity, which renders the control policy too broad because it allows accesses from unauthorized agents to the security-sensitive assets.

### Detection Example
The sram in HRoT has an address range that is readable and writable by un-privileged software, and it has an area that is only readable by un-privileged software. The tbus interconnect enforces access control for slaves on the bus but uses only one bit to control both read and write access. Address 0xA0000000 - 0xA000FFFF is readable and writable by the un-trusted cores core{0-N} and address 0xA0010000 - 0xA001FFFF is only readable by the un-trusted cores core{0-N}

* Threat Model
The security policy access control is not granular enough as it uses one bit to enable both read and write access. This gives write access to an area that should only be readable by un-privileged agents.

* Security Requirement
Access control logic should differentiate between read and write access and to have sufficient address granularity.



## CWE 1221: Incorrect Register Defaults or Module Parameters
### Description
Hardware description language code incorrectly defines register defaults or hardware IP parameters to insecure values.
### Radix Security Rule Template
Information should not flow from/to Asset to/from User-observable signals.

### Detection Example
The otp fuses in the Hardware Root of Trust (HRoT) are readable by untrusted software running on core{0-N} in debug mode only. In non-debug mode they are not accessible to untrusted software.
* Threat Model
The default value of the register bit enabling debug mode is incorrectly set to 1 in the RTL. Hence, allowing untrusted software to read security sensitive data in normal operating mode.
* Security Requirement
Default register values and instantiation parameters which has a security impact needs to be verified against the values specified in the design specification.

From the requirement that the otp fuses should not be readable follows the rule below based on the template. The rule doesn't include the value of the debug mode bit which means the rule will fail if debug mode is incorrectly set to"1".


## - CWE 1223: Race Condition for Write Once Attributes
### Description
A write-once register in hardware design is programmable by an untrusted software component earlier than the trusted software component, resulting in a race condition issue.

Information should not flow from software through the Store signals in the Load Store Units (LSUs) of untrusted CPUs to Write-once registers unless the Write-once values are set i.e. they are have been previously written.


### Detection Example
The interconnect in the untrusted section of the SoC contains write-once registers that define the security access policy for all masters and slaves connected to the interconnect. The access policy registers are programmed by the tmcu during secure boot.

* Threat Model
If there is a race condition and the access control policy registers are programmed by untrusted software before the trusted tmcu can program them during secure boot, a less restrictive access policy may be implemented giving a malicious actor access to security sensitive data.

* Security Requirement
The write-once configuration registers should not be writable by untrusted agents unless the write-once register is set.


## - CWE 1224: Improper Restriction of Write Once Bit Fields
### Description
The hardware design control register "sticky bits" or write-once bit fields are improperly implemented, such that they can be reprogrammed by software.
### Radix Security Rule Template
Information should not flow from software through the Store signals in the LSUs of untrusted CPUs to the State-carrying signals of write-once registers when the writeoncestatus is set


### Detection Example
The interconnect in the untrusted section of the SoC above contains write-once registers that define the security access policy for all the masters and slaves. The access policy registers are programmed by the tmcu during secure boot. Hence they must not be re-written by any of the untrusted CPUs.

* Threat Model
If the write-once registers are implemented incorrectly so that the "written once" state depends on the data written, an attacker running un-privileged code may write one of the write-once registers after secure boot and thus altering the security access policy and potentially elevating its own privilege level.

* Security Requirement
Write-once registers should be truly write-once and the status should not depend on the value written only if the status bit is set.


## CWE 1231: Improper Implementation of Lock Protection Registers
### Description
The product incorrectly implements register lock bit protection features such that protected controls can be programmed even after the lock has been set.
### Radix Security Rule Template
Information should not flow from software through the Protected register data signals to the State-carrying signals of protected registers unless the Protected registers are unlocked.


### Detection Example
The SoC above contains a thermal sensor with a programmable max temperature. Another register tmcu.csr.tempshutdown determines the action to take when the max temperature is reached. If the register is programmed to "1", the SoC is shut down to avoid malfunction or damage. The max temperature register and the tempshutdown register are protected by a lock bit. When trusted firmware sets the lock bit in tmcu.csr.reglock it is not possible to modify the registers. Due to a design bug, the tempshutdown register is not protected by the lock bit.

* Threat Model
Malicious software running on one of the un-trusted cores can potentially do a fault injection attack by disabling the tmcu.csr.temp shutdown register thus allowing the device to overheat to a point where behavior is unpredictable and security features are no longer active.

* Security Requirement
Critical registers which should not be modifiable after configuration, should be protected by a lock mechanism.


## CWE 1232: Improper Lock Behavior After Power State Transition
### Description
Register lock bit protection disables changes to system configuration once the bit is set. Some of the protected registers or lock bits become programmable after power state transitions (e.g., Entry and wake from low power sleep modes) causing the system configuration to be changeable.
### Radix Security Rule Template
Information should not flow from software through the Protected register data signals to the State-carrying signals of protected registers unless the Protected registers are unlocked.


### Detection Example
When the SoC above enters a hibernate power state, the memory in the peripheral IP & memory sub-system is powered down and loses configuration settings. In normal mode, the configuration registers cannot be modified by the un-trusted cores core{0-N} when the tmcu.csr.reglock bit is set. When resuming operations from hibernate mode, the trusted processor tmcu will disable the lock bit and re-configure the memory before leaving the resume state.

* Threat Model
Improper clearing of the lock bit after power state transitions enables malicious software to modify configuration registers.

* Security Requirement
Security critical device configuration registers protected by a lock bit must remain protected when returning to operation after power state transitions.


## CWE 1233: Improper Hardware Lock Protection for Security Sensitive Controls
### Description
The product implements a register lock bit protection feature that permits security sensitive controls to modify the protected configuration.
### Radix Security Rule Template
Signals controllable by untrusted software or agents must not flow to Security-critical Device Configuration memory ranges or registers unless the lock protection mechanism is disabled i.e. the device configuration space must not be modified by un-trusted agents.

### Detection Example
The SoC contains a thermal sensor with a programmable max temperature. Another register tmcu.csr.temp shutdown determines the action to take when the max temperature is reached. If the register is programmed to "1", the SoC is shut down to avoid malfunction or damage. The max temperature register and the temp shutdown register are protected by a lock bit. When trusted firmware sets the lock bit in tmcu.csr.reglock it is not possible to modify the registers. Due to a design bug, the temp shutdown register is not protected by the lock bit. It is also assumed that the lock bit tmcu.csr.reglock remains set during normal operation.

* Threat Model
Malicious software running on one of the un-trusted cores can potentially do a fault injection attack by disabling the tmcu.csr.tempshutdown register thus allowing the device to overheat to a point where behavior is unpredictable and security features are no longer active.

* Security Requirement
Critical registers which should not be modifiable after configuration, should be protected by a lock mechanism. The lock bit should be set during normal operation, i.e. after secure boot is done.



## CWE 1234: Hardware Internal or Debug Modes Allow Override of Locks
### Description
System configuration protection may be bypassed during debug mode.
### Radix Security Rule Template
Information should not flow from un-trusted software through the User-controllable signals to the Security-sensitive configuration locations when the lock bit is set. This rule applies if un-trusted software is never allowed to modify the configuration registers or memory locations when the lock bit is set regardless of other hardware internal, or debug modes being set. If some accesses are allowed, add the (debug mode || scan mode) condition to check specific modes.


### Detection Example
Trusted firmware running on the tmcu configures memory in the peripheral IP & memory subsystem during secure boot. The memory.csr.configuration register is protected by the tmcu.csr.lockbit which is set after configuration is done by the tmcu . When the SoC is in debug or scan mode, the lock bit for the configuration register is overridden.

* Threat Model
If un-trusted software is able to control either the scan or debug mode bits it will override the lock bit for the configuration register so that it can modify the memory configuration.

* Security Requirement
Depending on design intent, there are two different requirements. If overriding the lock bit for the configuration is a design bug or oversight, then configuration should only be writable when the lock bit is not set. If overriding the lock bit for the configuration is intended, then no other way of writing the register should be possible.


## CWE 1240: Use of a Risky Cryptographic Primitive
### Description
This device implements a cryptographic algorithm using a non-standard or unproven cryptographic primitive.


## CWE 1241: Use of Predictable Algorithm in Random Number Generator
### Description
The device uses an algorithm that is predictable and generates a pseudo-random number.


## CWE 1242: Inclusion of Undocumented Features or Chicken Bits
### Description
The device includes chicken bits or undocumented features that can create entry points for unauthorized actors.
### Radix Security Rule Template
Chicken bits should be permanently disabled in production devices or adequate protection should ensure they are not controllable by users. Designers need to document the address range for accessing chicken bits in internal documentation. Depending on system requirements, the chicken bits may or may not be readable registers. If they are readable, additional rules may be required if read access to the bits is restricted.


### Detection Example
The SoC design contains chicken bits in a range of memory in the tmcu.csr. These bits must not be controllable in a production device by un-authorized users. Only trusted software running on the tmcu may write to chicken bits.

* Threat Model
Un-trusted agents being able to control chicken bits may enable features that violate security access policy thus giving the un-trusted agent access to privileged data.

* Security Requirement
Chicken bits should not be controllable in a production device unless done by a trusted agent.


## - CWE 1243: Sensitive Non Volatile Information Not Protected During Debug
### Description
Access to security-sensitive information stored in fuses is not limited during debug.
### Radix Security Rule Template
Information in blown fuses or ROM, Security-sensitive Fuse Values, should not flow to User-accessible signals such as an untrusted debugger when the device is in debug mode.


### Detection Example
Security sensitive information is stored in blown fuses in the otp block and in a section of the rom.mem. During normal operation mode, access control methods prevent untrusted system components from reading this data.

* Threat Model
Data in rom.mem and otp fuses may be visible through the debug interface when the device is in debug mode and normal access control may not be set up. This would give access to sensitive data through an untrusted debugger.

* Security Requirement
Data in rom and otp must not be readable through the debug interface.


## CWE 1244: Improper Access to Sensitive Information Using Debug and Test Interfaces
### Description
The product's physical debug and test interface protection does not block untrusted agents, resulting in unauthorized access to and potentially control of sensitive assets.
### Radix Security Rule Template
Information should not flow from/to the Security-critical signals to/from the User- accessible debug interface unless the debug interface access has been property authenticated.

### Detection Example
A debugger connected to the debug interface needs to provide a correct response to a challenge in order to access internal registers of the Hypothetical SoC, for example registers in the tmcu . If the authorization is successful, the debug.authentication register is set to "1".

* Threat Model
The challenge response authorization is not applying to all debug accesses thus giving an attacker access to some security sensitive registers.

* Security Requirement
There should be no read or write access to security sensitive registers unless the debug agent has been properly authenticated.


## CWE 1245: Improper Finite State Machines (FSMs) in Hardware Logic
### Description
Faulty finite state machines (FSMs) in the hardware logic allow an attacker to put the system in an undefined state, to cause a denial of service (DoS) or gain privileges on the victim's system.
### Radix Security Rule Template
Critical Finite State Machines in the design should not be able to enter undefined states where the behavior is undefined. The Radix Security Rule ensures the FSM next state variable does not flow to the FSM current state variable unless the Next State is a valid state.

### Detection Example
The aes.csr FSM determines read, write or read/write access permissions for registers in the aes module based on source security ID of the initiator of the accesss. The FSM have 4 valid states: IDLE, RD, WR and RDWR. The state is one-hot encoded with 4 state bits for performance reasons which means there are many possible undefined states.

* Threat Model
An attacker may cause the FSM into an undefined state where access permissions are not enforced, allowing access to security sensitive registers.

* Security Requirement
Security sensitive FSMs should not be able to enter undefined states.


## - - CWE 1246: Improper Write Handling in Limited write Non Volatile Memories
### Description
The product does not implement or incorrectly implements wear leveling operations in limited-write non-volatile memories.
### Radix Security Rule Template
Store data from an un-secure processor must not flow to a limited-write Non-volatile memory location if the maximum number of write for that location has been reached. A trusted processor may be allowed to write anyway depending on system design.


### Detection Example
The nvm flash memory implements write leveling to prevent premature failures of the memory. The nvm has a register that defines the maximum number of writes per location. This register is only readable and writable by the secure tmcu processor.

* Threat Model
A malicious actor may be able to bypass the write leveling logic and perform a large number of writes to the same location thus making part of the flash unreliable. This may lead to undefined states in the system where security policies are not enforced or may enable a denial-of-service attack.

* Security Requirement
Non-volatile memory locations should not be writable by un-trusted agents when the maximum number of writes for the location has been reached. 


## CWE 1247: Missing or Improperly Implemented Protection Against Voltage and Clock Glitches
### Description
The device does not contain or contains improperly implemented circuitry or sensors to detect and mitigate voltage and clock glitches and protect sensitive information or software contained on the device.
### Radix Security Rule Template
Radix currently does not cover this CWE, refer to the MITRE website for suggested mitigations.


## CWE 1248: Semiconductor Defects in Hardware Logic with - Security Sensitive Implications
### Description
The security-sensitive hardware module contains semiconductor defects.


## CWE 1251: Mirrored Regions with Different Values
### Description
The product's architecture mirrors regions without ensuring that their contents always stay in sync.
### Radix Security Rule Template
Data in a duplicated resource must not flow to a location that is user accessible while an update of the resource controlling the data is in progress.

### Detection Example
There are 3 processors in the SoC design example, core0, core1 & core2, running user code. For performance reasons, there is one main Memory Management Unit (MMU) and one shadow MMUs. The main MMU handles memory accesses by core0 and the shadow MMU handles memory accesses from core1 & core2. Updates to the main MMU is done by the tmcu and then the main MMU updates the shadow MMU through messages on the interconnect. If the accessible address range for the untrusted cores is updated in the main MMU, there is a time when the three processors may have access to different memory ranges.

* Threat Model
A malicious agent running on core2 may be able to access memory locations outside its allowed range because the shadow MMU does not yet have the same configuration as the main MMU. If core2 can flood the interconnect with traffic and delay the update request, the update to the shadow MMU may be delayed, extending the time available for access.

* Security Requirement
No access to memory through the shadow MMU should be allowed while an update is in progress.


## CWE 1252: CPU Hardware Not Configured to Support Exclusivity of Write and Execute Operations
### Description
The CPU is not configured to provide hardware support for exclusivity of write and execute operations on memory. This allows an attacker to execute data from all of memory.
### Radix Security Rule Template
A processor must not be able to write data in instruction memory and it should only be able to read instructions from instruction memory. Store data in the Load Store Unit (LSU) should not flow to memory location in the instruction address range and data in Memory should not flow to instruction fetch unit in the CPU if the address is outside the address range for instruction memory.


### Detection Example
In this example, the tmcu doesn't have support for write exclusivity and the SoC doesn't have an Memory Protection Unit (MPU) or Memory Management Unit (MMU) to isolate memory regions as execute only. Hence, the tmcu load store unit can write to the entire sram.mem memory and the instruction fetch unit can execute code in the entire sram.mem as well.

* Threat Model
An attacker can write malicious code to memory and later execute the code.

* Security Requirement
If the processor lacks support for write exclusivity, other logic must implement this functionality to prevent writes to instruction memory and instruction fetch from outside instruction memory.



## CWE 1253: Incorrect Selection of Fuse Values
### Description
The logic level used to set a system to a secure state relies on a fuse being unblown. An attacker can set the system to an insecure state merely by blowing the fuse.
### Radix Security Rule Template
A fuse having its blown value and the corresponding security feature being enabled should always hold true. The requirement in this CWE should also be verified during functional verification. The Radix security rule could also be written as a System Verilog Assertion since the condition should always hold true.



### Detection Example
The control word defined by the fuses in otp determine what security related features are enabled in the chip following manufacturing. For example, scan mode is permanently disabled after manufacturing test by blowing the corresponding fuse (the value 1 represents a blown fuse) e.g. bit [0] in otp.fuses.

* Threat Model
If disabling scan mode incorrectly corresponded to fuse value == 0, an attacker could blow the fuse and thus enable scan mode and get access to every register in the design through the JTAG port.

* Security Requirement
A blown one time programmable fuse should always correspond to the most secure, restrictive operating mode of the device



## CWE 1254: Incorrect Comparison Logic Granularity
### Description
The product's comparison logic is performed over a series of steps rather than across the entire string in one operation. If there is a comparison logic failure on one of these steps, the operation may be vulnerable to a timing attack that can result in the interception of the process for nefarious purposes.
### Radix Security Rule Template
The result of a comparison operation must not be visible to an untrusted agent at different latency if the comparison may take a different amount of time to complete depending on the result of the compare.


### Detection Example
The debug unit checks a user-provided password to grant access to a user. The password is 64 bits but the comparison logic is implemented using an 8 bit comparator, checking each byte of the password on consecutive clock cycles. If the password compare fails in the first byte, the fail status signal is asserted and access is denied. If all 8 compares pass, access is granted.

* Threat Model
By measuring the time between request and the fail indication, the timing side channel leaks information about which byte of the password does not match. If you know which byte fails, it is easy to guess the correct password.

* Security Requirement
The compare function should indicate pass / fail after the same amount of time regardless if the fail happened before the last byte.



## - CWE 1255: Comparison Logic is Vulnerable to Power Side Channel Attacks
### Description
A device's real time power consumption may be monitored during security token evaluation and the information gleaned may be used to determine the value of the reference token.


## CWE 1256: Hardware Features Enable Physical Attacks from Software
### Description
Software-controllable device functionality such as power and clock management  permits unauthorized modification of memory or register bits.
### Radix Security Rule Template
Information in the Asset which control physical parameters on chip must be prevented from being written with data from user-accessible signals unless the permission bits are correctly set to the value indicating asset should be writable.


### Detection Example
Security-critical settings for scaling clock frequency and voltage are available in a range of registers bounded by [PRIVENDADDR : PRIVSTARTADDR] in the tmcu.csr module in the HW Root of Trust. These values are writable based on the lockbit register in the same module. The lockbit is only writable by privileged software running on the tmcu.

* Threat Model
We assume that untrusted software running on any of the Core{0-N} processors, (the threat) has access to the input and output ports of the hrotiface. If untrusted software can clear the lockbit or write the clock frequency and voltage registers due to inadequate protection, a fault injection attack could be performed.

* Security Requirement
Information in the address range [ PRIVENDADDR:PRIVSTARTADDR ] must not be writable via hrotiface unless tmcu.csr.lockbit is zero. The tmcu.csr.lock bit must never be writable from the hrotiface interface.



## CWE 1257: Improper Access Control Applied to Mirrored or Aliased Memory Regions
### Description
Aliased or mirrored memory regions in hardware designs may have inconsistent read/write permissions enforced by the hardware. A possible result is that an untrusted agent is blocked from accessing a memory region but is not blocked from accessing the corresponding aliased memory region.
### Radix Security Rule Template
Security sensitive memory mapped registers or memory areas must not flow to signals readable by untrusted agents even if an aliased address is used.


### Detection Example
ROM in the SoC is 64k and it is mapped to address 0x08000000 - 0x0800FFFF . The ROM is security sensitive and is only readable by the tmcu. In order to simplify the address decoding logic, the ROM only decodes the lower 16 address bits and relies on the Memory Protection Unit (MPU) to enforce access control.

* Threat Model
One of the untrusted cores, core{0-N} has read permission from address 0x0400beef. Due to improper access control, the ROM decodes the address as 0xbeef and responds to the read request even though the un-trusted core should not have access to address 0x08000000 and above.

* Security Requirement
No location in ROM should flow to untrusted agents in the system even if the address at the ROM is in the correct range due to memory aliasing.


## CWE 1258: Exposure of Sensitive System Information Due to Uncleared Debug Information
### Description
The hardware does not fully clear security-sensitive values, such as keys and intermediate values in cryptographic operations, when debug mode is entered.
### Radix Security Rule Template
Security sensitive registers must be cleared when a clear request signal is asserted, and their contents must not flow to other locations until the contents has been cleared.


### Detection Example
Keys for AES are stored in internal registers aes.csr.key . These registers are blocked for access by software and other untrusted agents of the SoC. When the design is in debug mode, all registers are accessible through the debug interface. To avoid keys being accessible to unauthorized users, they will be cleared when entering debug mode. The register clear request signal in the template is generated from the debug mode signal in the tmcu. A register in AES indicate that the value is zero.

* Threat Model
If the aes key register is not cleared when entering debug mode, an untrusted debugger can gain access to the keys.

* Security Requirement
The aes key register and other sensitive registers should be cleared when entering debug mode.

## CWE 1259: Improper Restriction of Security Token Assignment
### Description
The System-On-A-Chip (SoC) implements a Security Token mechanism to differentiate what actions are allowed or disallowed when a transaction originates from an entity. However, the Security Tokens are improperly protected.
### Radix Security Rule Template
Security sensitive registers must not be changed unless a write is done by a secure processor or they are set to reset values during chip reset.


### Detection Example
Access to secret registers such as AES key registers is configured in access-policy registers and is determined based on security identifiers. Each agent in the SoC have a security identifier register which is programmed to a unique value by the tmcu during secure boot.

* Threat Model
If one of the untrusted cores, core{0-N} can change its own or another agent's security identifier, the access policy will allow access to registers that would otherwise be protected from this agent.

* Security Requirement
The Security Identifier for an agent should not change unless it is programmed by the tmcu or it is cleared during reset.


## CWE 1260: Improper Handling of Overlap Between Protected Memory Ranges
### Description
The product allows address regions to overlap, which can result in the bypassing of intended memory protection.
### Radix Security Rule Template
Data in a privileged address range in a shared memory (Privileged data signals) must not influence signals readable by untrusted agents. This should always hold true even if the non-privileged address range overlap the privileged address range. Additionally, the privileged address range in shared memory must not be able to be influenced by signals writable by untrusted agents.


### Detection Example
The Hardware Root of Trust (HRoT) local sram is memory mapped in the core{0-N} address space and is also accessible to the tmcu. The address range for privileged memory space is defined in tmcu.csr registers. It is only readable and writable by privileged software. The un-trusted cores, core{0-N} can define an unprivileged area in memory where they have read and write access.

* Threat Model
In this example, we assume that the threat is from malicious software in the untrusted domain. We assume this software has access to the core{0-N} un-privileged memory map and can also change the location of its un-privileged area. If the software running in the untrusted domain can program the un-privileged memory area to overlap with the privileged memory area, this would allow the malicious software to read and write privileged memory.

* Security Requirement
Data in the privileged area of memory must not flow to the hrotiface and data on the hrotiface must not flow to the privileged area of memory regardless of how the nonprivileged address space is  programmed.


## CWE 1261: Improper Handling of Single Event Upsets
### Description
The hardware logic does not effectively handle when single-event upsets (SEUs) occur.
### Radix Security Rule Template
Security sensitive information should not flow to signals readable by untrusted agents when the circuit is in an error state caused by a Single Event Upset. Additionally, security sensitive data must not be able to be influenced by signals writable by untrusted agents when the circuit is in an error state caused by a Single Event Upset.


### Detection Example
The SoC above has logic to detect errors, e.g. parity on memory data or duplicated logic running in lock-step, to detect Single Event Upset (SEU) faults. When an SEU fault is detected, an error bit is set in CSR and software on tmcu tries to recover back to normal operation. During this error state, secure data for example in the SRAM must not be overwritten or be visible to un-trusted cores or on the debug interface.

* Threat Model
In this example, we assume that the threat is from a malicious user either relying on a random event or intentional fault insertion to bring the design into an error state where normal security policies may no longer apply. If malicious software running in the untrusted domain is able to bypass the security policy, this would allow the malicious user to read and write privileged memory. If the malicious user has physical access to the chip, he can try to access secure data through the debug interface which may no longer be protected in an error scenario.

* Security Requirement
Data in the sram memory must not flow to the debug module and data from the debug module must not flow to the memory when an SEU is detected.


## CWE 1262: Register Interface Allows Software Access to Sensitive Data or Security Settings
### Description
Memory-mapped registers provide access to hardware functionality from software and if not properly secured can result in loss of confidentiality and integrity.
### Radix Security Rule Template
Sensitive data should not flow to signals readable by untrusted agents unless a "permitted condition" is true. Additionally, sensitive data must not be able to be influenced by signals writable by untrusted agents.


### Detection Example
Assume that the registers in the HRoT aes core are memory mapped in the core{0-N} address space. All the aes core memory mapped registers have an access control policy specifying read or write access and access by tmcu or core{0-N} . For example, the aes.reg.key register is only readable and writable by tmcu, the aes.reg.datain register is writable but not readable by core{0-N} and the aes.reg.dataout register is only readable when the aes.done bit is set.

* Threat Model
In this example, we assume that the threat is from malicious software running on one of the untrusted processors. It will attempt to read and write all memory mapped registers in the aes address space hoping the access control policy is insufficient. If any access succeeds, information about the key may be obtained.

* Security Requirement
Only the aes.reg.datain register is writable by core{0-N} and only the aes.reg.dataout register is readable by core{0-N} when encryption is done. The aes.dataout register is never writable and the aes.datain register is never readable by core{0-N}.


## CWE 1263: Improper Physical Access Control
### Description
The product is to be designed with access restricted to certain information, but it does not sufficiently protect against an unauthorized actor's ability to access these areas.
### Radix Security Rule Template
Information from/to Physically user-accessible signals must not flow to/from Restricted signals if the physical access protection has been violated. Verification of the physical protection in the manufactured device is beyond the scope of functional verification but Radix rules can stil be used to ensure correct behavior when the physial protection detects a violation.


### Detection Example
The SoC has an anti-tamper detection circuit to detect if the device is de-capped. If the device is de-capped then the memories will be zeroized so no information will be leaked to an attacker. The processors will also halt to avoid leaking any information.

* Threat Model
An attacker may decap the device and probe internal signals to access sensitive data in memories or registers or observe the program running on the embedded processors.

* Security Requirement
When physical tampering is detected e.g. when someone is de-capping the device, the processors should stop and memories should be cleared i.e. zeroized to avoid sensitive data leakage.


## - CWE 1264: Hardware Logic with Insecure De Synchronization between Control and Data Channels
### Description
The hardware logic for error handling and security checks can incorrectly forward data before the security check is complete.
### Radix Security Rule Template
Privileged data shall not flow to the cache if the requestor doesn't have permission to access data or permission check is not completed.


### Detection Example
The tmcu and core{0-N} processors are interconnected through AXI. The security policy (bus firewall) is implemented in an IP block separate from the data routing interconnect. The Hardware Root of Trust (HRoT) processor, tmcu should not be able to share data with the untrusted core{0-N} processors and the bus firewall prevents the untrusted processors from accessing for example rom data in the HRoT.

* Threat Model
If the firewall logic becomes de-synchronized with the data routing an untrusted processor may be able to read privileged data before the security policy is ready and enforced.

* Security Requirement
All privileged data is buffered or blocked by the interconnect until it has determined that the requestor has permission to access the data.



## CWE 1266: Improper Scrubbing of Sensitive Data from Decommissioned Device
### Description
The product does not properly provide a capability for the product administrator to remove sensitive data at the time the product is decommissioned. A scrubbing capability could be missing, insufficient, or incorrect.
### Radix Security Rule Template
Sensitive data to be scrubbed should not flow to the same location when scrubbing has started and is done i.e. sensitive data values are cleared.



### Detection Example
The aes.csr.key register contains sensitive information that needs to be removed after use. This is done by HW setting the key to all zero. The operation is started by the tmcu writing "1" to the aes.csr.dataclear register. The aes.csr.cleardone bit is set to "1" when the clear operation is done. The tmcu will then clear the aes.csr.dataclear bit to complete the operation.

* Threat Model
If the clear is not successful, bits of the key may remain that could leak to unauthorized locations.

* Security Requirement
No information should flow from the key register prior to clearing back to the key register when clearing is done.



## CWE 1267: Policy Uses Obsolete Encoding
### Description
The product uses an obsolete encoding mechanism to implement access controls.
### Radix Security Rule Template
Information from/to Asset-carrying signals in trusted IP must not flow to/from Inputs/Outputs of untrusted IP. Or, Information from/to Asset-carrying signals in trusted IP must not flow to/from Inputs/Outputs of untrusted IP unless it is allowed by up to date access policy.


### Detection Example
The access control block in the hrotiface is being re-used from another design. It is using security tokens to identify the source of the transaction and determine if the access is allowed. The old design only had 2 masters in the untrusted area so only 1 bit was used for the security token. The new SoC has additional masters and the size of the security token is now 4 bits. However, the reused access control is not updated. For example, Core0 is allowed to access the ROM in HRoT but the newly added Core1 is not. The security token for Core0 is 4'b0000 and for Core1 it is 4'b1010 but access control only considers bit [0] so they incorrectly have the same access privilege. The DMA previously was not allowed to write SRAM indicated by bit [0] being 1 but it is now allowed.

* Threat Model
The obsolete access policy may allow an untrusted agent access to secure information.

* Security Requirement
Access policy enforcement must use up to date policy settings and implementations.


## CWE 1268: Policy Privileges are not Assigned Consistently Between Control and Data Agents
### Description
The product's hardware-enforced access control for a particular resource improperly accounts for privilege discrepancies between control and write policies.
### Radix Security Rule Template
Untrusted software through User accessible signals should not flow to any of the critical configuration registers. Sensitive signals, e.g. register values should not flow to User-accessible signals. These rules will flag any confidentiality and integrity violation on the specified signals which may be stricter than the intended access policy. Please review the system design documentation and add exceptions to rules as required.


### Detection Example
All the registers in the aes block are protected by different access policies. For example, the aes.csr.key register is readable and writable by the tmcu only. The aes.csr.status register is readable by a specific master when the aes.csr.control registers is enabled for that specific master.

* Threat Model
A less privileged access policy may override a higher privileged access policy due to incorrect implementation thus allowing access for an untrusted agent to privileged data.

* Security Requirement
Sensitive access controlled signals should adhere to intended access control policy as defined in design specification.



## - CWE 1269: Product Released in Non Release Configuration
### Description
The product released to market is released in pre-production or manufacturing configuration.
### Radix Security Rule Template
Information from/to Asset must not flow to/from User-visible signals unless Manufacturing is not complete.


### Detection Example
The SoC has status registers that aid in debug and development that should not be readable after the device is manufactured. For example, the tmcu.csr.info register should not be readable by any agent after manufacturing. After manufacturing, the fuse otp.manufacturingdone is blown, i.e. set to 1 to indicate that manufacturing is done. A separate post-manufacturing verification step ensuring the fuse is blown is required.

* Threat Model
An untrusted agent is able to read status registers that contain sensitive information in the manufactured device

* Security Requirement
Status registers containing sensitive information should not be readable when the manufacturing done fuse is blown.



## CWE 1270: Generation of Incorrect Security Tokens
### Description
The product implements a Security Token mechanism to differentiate what actions are allowed or disallowed when a transaction originates from an entity. However, the Security Tokens generated in the system are incorrect.
### Radix Security Rule Template
Any access policy register should be set to 0 after system boot i.e. no access to any protected resources. This is likely more restrictive than intended but will report incorrect settings by software. The user should review the design specification and update the rule accordingly.


### Detection Example
Access to secret registers such as AES key registers is configured in access-policy registers and is determined based on security identifiers. Each agent in the SoC has a Security identifier register which is programmed to a unique value by the tmcu during secure boot.

* Threat Model
If the security identifiers are programmed incorrectly an untrusted agent may get access to sensitive data.

* Security Requirement
All security identifies should be programmed to unique values reflecting the access privilege level specified in the design specification for each agent.


## CWE 1271: Uninitialized Value on Reset for Registers Holding Security Settings
### Description
Security-critical logic is not set to a known value on reset.
### Radix Security Rule Template
Security critical control registers should not have unknown values after the device is reset.


### Detection Example
The flip flop implementing the debug.csr.enable register is not connected to reset.

* Threat Model
The debug.csr.enable bit is unknown after reset. In the real chip, it will randomly take the value 0 or 1 meaning the chip may be in debug mode after reset. An attacker can repeatedly reset the chip until debug mode is enabled.

* Security Requirement
All security critical control registers should be set to a known value during reset.


## CWE 1272: Sensitive Information Uncleared Before Debug/Power State Transition
### Description
Sensitive information may leak as a result of a debug or power state transition when information access restrictions change as a result of the transition.
### Radix Security Rule Template
Security critical signals should not flow to User-accessible signals e.g. read by software, unless the device is operating in a privileged operating mode. If the operating mode is changed to "user mode" or "low power mode" the security critical signals should not be accessible.


### Detection Example
When running in privileged mode, the dma will copy security sensitive data from otp.data to registers in the aes. However, it first copies data from otp to sram and then from sram to aes registers. When the device transitions from privileged mode to "user mode" or "low power mode" the data that was moved must not flow outside the Hardware Root of Trust (HRoT).

* Threat Model
When the device transition from one mode to another, sensitive data may remain in registers or memory locations that are readable by un-trusted agents in the new mode and thus leak sensitive data

* Security Requirement
Security sensitive data accessed in one operating mode must not be accessible when transitioning to another operating mode.


## CWE 1273: Device Unlock Credential Sharing
### Description
The credentials necessary for unlocking a device are shared across multiple parties and may expose sensitive information.


## CWE 1274: Insufficient Protections on the Volatile Memory Containing Boot Code
### Description
The protections on the product's non-volatile memory containing boot code are insufficient to prevent the bypassing of secure boot or the execution of an untrusted, boot code chosen by an adversary.
### Radix Security Rule Template
For confidentiality, information must not flow from the boot code storage location (Signals storing boot code) to User-accessible signals. For integrity, information from User-accessible signals must not flow to Signals carrying boot code from User-accessible signals unless Boot is complete.


### Detection Example
As part of the secure boot process in the SoC above, the tmcu fetches bootloader code from non-volatile memory, tnvm and writes it to sram .

* Threat Model
If the device has insufficient protections, an adversary could read the bootloader code from tnvm memory, modify it or replace it and write it to sram before boot is complete and thus have the system boot using malicious code.

* Security Requirement
The memory storing boot code should not be readable by un-trusted agents and the sram storing boot code should not be writable by un-trusted agents until boot is completed.



## CWE 1276: Hardware Child Block Incorrectly Connected to Parent System
### Description
Signals between a hardware IP and the parent system design are incorrectly connected causing security risks.
### Radix Security Rule Template
Information should not flow from/to the Security-critical signals of hardware block to/from User-accessible signals.


### Detection Example
The interconnect in the untrusted sub-system of the SoC uses a security level bit to determine if a transaction is secure or not. core0 is configured as secure and core1 is configured as un-secure by the tmcu at boot time. The nvm memory uses the security level bit to determine if a read transaction is allowed or not. If securitylevel == 0, a read is allowed, if securitylevel == 1, it is not. During implementation the nvm.securitylevel input is incorrectly tied to 0 instead of connected to the corresponding interconnect signal. This means all masters; even un-secure ones will be allowed to read the nvm. 

* Threat Model
Malicious software running on an un-trusted core will be able to access secure data since access control is effectively disabled.

* Security Requirement
Trusted data must not flow to un-trusted agents based on the security level of the master. Use the security level programmed in the destination to detect illegal data flows caused by incorrect connections of the IP.



## CWE 1277: Firmware Not Updateable
### Description
A product's firmware cannot be updated or patched, leaving weaknesses present with no means of repair and the product vulnerable to attack.
### Radix Security Rule Template
Information in User accessible signals must not flow to Sensitive Register locations related to booting from updated firmware. Information from Security sensitive data such as updated firmware must not flow to User accessible signals when booting from updated firmware in an alternative location.



### Detection Example
The tmcu in the Hardware Root of Trust (HRoT) loads firmware from the ROM in the HRoT. The ROM is programmed at manufacturing and cannot be changed. To provide a method to update the firmware, new firmware can be written to the trusted non-volatile memory (tnvm) and a bit set in the tmcu will instruct the tmcu to read firmware from a pre-determined address in tnvm instead.

* Threat Model
An attacker may be able to read the modified firmware and later write back malicious code to the tnvm. The attacker may also clear the control bit in the tnvm so that the device falls back to executing old firmware which may have known security vulnerabilities and thereby enabling further attacks. 

* Security Requirement
The tmcu register controlling firmware location must not be writable from outside the HRoT. The updated firmware must not be readable or writable from outside the HRoT when it is being used by the tmcu.



## CWE 1278: Missing Protection Against Hardware Reverse Engineering Using Integrated Circuit (IC) Imaging Techniques
### Description
Information stored in hardware may be recovered by an attacker with the capability to capture and analyze images of the integrated circuit using techniques such as scanning electron microscopy.


## CWE 1279: Cryptographic Operations are run Before Supporting Units are Ready
### Description
Performing cryptographic operations without ensuring that the supporting inputs are ready to supply valid data may compromise the cryptographic result.
### Radix Security Rule Template
Information should not flow from the Crypto IP outputs to User-accessible signals when the Supporting IP self-test not passed.



### Detection Example
The aes block is using random numbers from an internal True Random Number Generator (TRNG). The TRNG runs a self-test after reset to ensure system integrity. The aes engine must not use the generated random numbers unless the self-test passes. This means no read or write access of the AES block are allowed from untrusted agents outside the Hardware Root of Trust (HRoT) until the TRNG self-test has passed.

* Threat Model
A malicious actor is able read and write data to and from aes before the self-test is completed and has passed and may alter the state of the encryption module or access privileged data.

* Security Requirement
There should be no access to the crypto block by untrusted agents until the integrity of the TRNG is verified.



## CWE 1280: Access Control Check Implemented After Asset is Accessed
### Description
A product's hardware-based access control check occurs after the asset has been accessed.
### Radix Security Rule Template
Information about the Asset must not reach the Asset's point of use unless the Access control check is successful. Note: Finding bad coding styles and missing reset values should be done as part of functional verification.


### Detection Example
Read access to the sram.csr.configuration register is only allowed for the tmcu . Hardware access control checks that the bus master doing the read is valid before the register value is driven to the output.

* Threat Model
If the register value is driven on the bus before the access control check is complete, an un-trusted agent may get access to privileged information.

* Security Requirement
Information in access controlled registers must not be available before the access control check is complete and successful.



## CWE 1281: Sequence of Processor Instructions Leads to Unexpected Behavior
### Description
Specific combinations of processor instructions lead to undesirable behavior such as locking the processor until a hard reset performed.



## - CWE 1282: Assumed Immutable Data is Stored in Writable Memory
### Description
Immutable data, such as a first-stage bootloader, device identifiers, and "write-once" configuration settings are stored in writable memory that can be re-programmed or updated in the field.
### Radix Security Rule Template
Information from User-accessible signals should not affect the Memory storing immutable data.


### Detection Example
In the SoC above, cryptographic hash digests, encryption keys, the first stage bootloader and other trusted data is stored in ROM and one-time programmable fuses. This data is not modifiable after manufacturing. Another case is if the immutable data is stored in sram because the memory type was not defined in the design specification. The immutable data is accessible in the address range [ IMMADDRSTART : IMMADDREND ], defined in the system specification.

* Threat Model
An attacker is able to modify a hash digest stored in what was supposed to be read only memory. Any code the attacker loads after that can be verified as trusted.

* Security Requirement
All immutable code or data should be programmed into ROM or write-once memory that cannot be modified in the field.

The first rule may incorrectly flag a violation since there is no condition checking if data is actually written to the memory as opposed to data flowing to the data input of the memory only. However, any write attempt to immutable data may indicate a security vulnerability. The second rule doesn't specify which physical memory data must not flow to, only the address range that should not be writable.



## CWE 1283: Mutable Attestation or Measurement Reporting Data
### Description
The register contents used for attestation or measurement reporting data to verify boot flow are modifiable by an adversary.
### Radix Security Rule Template
Information from User-accessible signals should not affect the Memory storing attestation and/or measurement data.


### Detection Example
The final hash value calculated on the code during secure boot is written to a register by the tmcu. This value is readable by the un-trusted cores core{0-N} and by the debug interface. It is not writable by any un-trusted agent or debug module. 

* Threat Model
An attacker is able to modify the final hash values due to a design bug so that malicious code that failed verification will now pass and it appears that secure boot passed even though the system is running malicious software

* Security Requirement
Measurement reporting data such as the final hash value should be stored in read only registers or have access protection to prevent modification.


## CWE 1290: Incorrect Decoding of Security Identifiers
### Description
The product implements a decoding mechanism to decode certain bus-transaction signals to security identifiers. If the decoding is implemented incorrectly, then untrusted agents can now gain unauthorized access to the asset.
### Radix Security Rule Template
Information from Untrusted signals must not flow to Security sensitive signals unless the security level of the source is validated independent of the access control logic i.e., the security identifier allows the access.


### Detection Example
The hrotiface access control module only allows access to slaves in the Hardware Root of Trust (HRoT) if the source security identifier matches the access policy defined in the interface. Each master in the untrusted sub-system has a 3-bit security identifier. For example: Core0 is 3'b101 and Core1 is 3'b100. According to the access policy Core0 is allowed to access for example SRAM in the HRoT sub-system but Core1 is  not. The three security identifier bits are out of band inputs to the hrotiface interface. There are less than 4 masters in the untrusted subsystem so the access control module only use the lower 2 bits to determine if the security identifier matches the policy.

* Threat Model
The access control module incorrectly decodes the security identifiers and grant access to untrusted masters.

* Security Requirement
Security identifiers must be correctly decoded for an access to be allowed.


## - CWE 1291: Public Key Re Use for Signing both Debug and Production Code
### Description
The same public key is used for signing both debug and production code.


## CWE 1292: Incorrect Conversion of Security Identifiers
### Description
The product implements a conversion mechanism to map certain bus-transaction signals to security identifiers. However, if the conversion is incorrectly implemented, untrusted agents can gain unauthorized access to the asset.
### Radix Security Rule Template
Information from User accessible signals must not flow to Security sensitive signals unless the security level of the source is validated independent of the bridge.


### Detection Example
The interconnect in the untrusted subsystem of the SoC is implementing the AXI protocol with TrustZone. One of the peripherals is a UART with an OCP interface. It is connected to the AXI interconnect via an OCP - AXI bridge. Since OCP doesn't support TrustZone, one bit in each transaction is used to communicate the security level of the OCP agent. The OCP - AXI reads the bit and sets the TrustZone bits accordingly. 

* Threat Model
The OCP to AXI bridge interprets the security bit in the OCP transaction incorrectly and sets the TrustZone bit incorrectly. This may allow a malicious actor access to security sensitive data connected to the AXI interconnect.

* Security Requirement
Security identifiers must be correctly maintained when they are converted between protocols.


## CWE 1294: Insecure Security Identifier Mechanism
### Description
The System-on-Chip (SoC) implements a Security Identifier mechanism to differentiate what actions are allowed or disallowed when a transaction originates from an entity. However, the Security Identifiers are not correctly implemented.


## CWE 1295: Debug Messages Revealing Unnecessary Information
### Description
The product fails to adequately prevent the revealing of unnecessary and potentially sensitive system information within debugging messages.
### Radix Security Rule Template
Internal Signals carrying confidential information should not flow to device External interfaces readable by untrusted agents. The information flow may be qualified by debug mode condition, but leakage may also occur through for example a UART.


### Detection Example
The SoC has two debug interfaces. The debug port in HRoT is used to access the HRoT only during debug and a UART Peripheral connected to the interconnect in the untrusted part of the SoC which is used to debug the rest of the SoC. The debug port in HRoT has access control limiting access to authorized users. The UART doesn't have access control and allows access to all agents and modules connected to the interconnect unless they have their own access control. The memory MEM is configured to only allow access to a memory range [ PROTECTEDADDREND : PROTECTEDADDRSTART ] to privileged code running on the Core0 processor.

* Threat Model
A malicious actor can read sensitive data stored in memory or in registers when debugging using the UART interface and bypassing normal access protections.

* Security Requirement
Data in the protected area of memory should not be readable through the UART interface at any time.



## CWE 1296: Incorrect Chaining or Granularity of Debug Components
### Description
The product's debug components contain incorrect chaining or granularity of debug components.
### Radix Security Rule Template
Internal Signals carrying confidential information should not flow to device External interfaces readable by untrusted agents unless the proper authentication is done. The authentication may require passing access control at multiple different points in the flow which require different levels of privilege.


### Detection Example
The HW Root of Trust (HRoT) has a debug, Test Access Port which is connected in a chain of debug modules that are eventually connected to the SoC JTAG port. Accessing debug data at different locations in the SoC requires different privileges. Accessing debug data from the HRoT requires the highest (0) level of privilege. A debugger connected to the JTAG port must first authenticate access to the JTAG port and then authenticate access to each debug module in the chain assuming it has the correct credentials. This allows agents with low privilege (3) to access debug data in nonsecure areas of the SoC and agenst with the highest privilege (0) to access debug data in the HRoT. However, due to an implementation error, if the previous TAP module in the chain is authenticated, the authentication check on the next TAP is bypassed.

* Threat Model
A malicious actor can read sensitive data in the HRoT through the debug TAP inteface even if he only has access privilege to a lower privilege module earlier in the chain.

* Security Requirement
Data in the HRoT connected to the debug interface must not be readable by the SoC JTAG interface unless both interfaces has been authenticated.


## CWE 1297: Unprotected Confidential Information on Device is Accessible by OSAT Vendors
### Description
The product does not adequately protect confidential information on the device from being accessed by Outsourced Semiconductor Assembly and Test (OSAT) vendors.



## CWE 1298: Hardware Logic Contains Race Conditions
### Description
A race condition in the hardware logic results in undermining security guarantees of the system.


## CWE 1299: Missing Protection Mechanism for Alternate Hardware Interface
### Description
The lack of protections on alternate paths to access control-protected assets (such as unprotected shadow registers and other external facing unguarded interfaces) allows an attacker to bypass existing protections to the asset that are only performed against the primary path.
### Radix Security Rule Template
Information in the Asset must be prevented from being written with data from user- accessible signals unless the Source ID matches source with allowed source ID. Information in the Asset must not flow to User-accessible signals unless the Source ID matches source with allowed source ID.

### Detection Example
The DMA may only be programmed by the trusted Core0 processor and the tmcu. This is enforced by access control in the interconnect which only allows the transaction if the secure ID of the source is CORE0 or TMCU. One of the peripherals on the interconnect is a GPIO interface. It should not have access to the DMA registers but due to a design oversight, access control is not enforced when the source of the transaction is the GPIO interface.

* Threat Model
The lack of access control on the alternative path from GPIO to protected registers allows a malicious actor to control the DMA.

* Security Requirement
There should be no read of write access to protected DMA registers through alternative paths.


## CWE 1300: Improper Protection Against Physical Side Channels
### Description
The product is missing protections or implements insufficient protections against information leakage through physical channels such as power consumption, electromagnetic emissions (EME), acoustic emissions, or other physical attributes. 


## CWE 1301: Insufficient or Incomplete Data Removal within Hardware Component
### Description
The product's data removal process does not completely delete all data and potentially sensitive information within hardware components.


## CWE 1302: Missing Security Identifier
### Description
The product implements a security identifier mechanism to differentiate what actions are allowed or disallowed when a transaction originates from an entity. A transaction is sent without a security identifier.
### Radix Security Rule Template
Data from a trusted source e.g. an embedded processor is only allowed to flow to Trusted Memory when Security identifier for source is set. Trusted Memory may be defined as an address range in memory.


### Detection Example
Shared memory (MEM) in the untrusted subsystem is divided into separate address ranges for each processor core and each core is only allowed to access memory in its own address range. Each master on the core.interconnect has a unique security identifier. There is a register in interconect.csr which has one bit per master. If the bit for a specific master is set, then read and write access to the destination is allowed. If the bit is not set, the transaction is dropped. There is no master with number 0 so a missing identifier, interpreted as zero will not allow access.

* Threat Model
An attacker may cause one of the cores to omit the security identifier in a memory read or write transaction. This will cause the memory to drop the transaction. This may cause a denial-of-service attack scenario since the code running on the core is not executing as expected.

* Security Requirement
All masters must include a security identifier with every transaction.


## - CWE 1303: Non Transparent Sharing of Microarchitectural Resources
### Description
Hardware structures shared across execution contexts (e.g., caches and branch predictors) can violate the expected architecture isolation between contexts.
### Radix Security Rule Template
Information in Instruction Operands when they are Influenced by unprivileged process and Instructions will be squashed should not affect the Cache State.

### Detection Example
Detecting vulnerabilities like Spectre is challenging because the illegal loading of the data and transmission through the timing side-channel occurs during transient or speculative execution, which is invisible to the programmer's view of the processor. The signals required for the Radix rule is dependent on the processor implementation.

* Threat Model
An attacker can extract data from another user's context through data being loaded into cache for speculative executed instructions before they are being squashed.


## CWE 1304: Improperly Preserved Integrity of Hardware Configuration State During a Power Save/Restore Operation
### Description
The product performs a power save/restore operation, but it does not ensure that the integrity of the configuration state is maintained and/or verified between the beginning and ending of the operation.
### Radix Security Rule Template
Information should not flow from insecure memory, Data stored in insecure location to trusted CPU, Trusted location unless it is validated for example by comparing a saved and calculated secure hash of the data.


### Detection Example
Before the HW Root of Trust (HRoT) is powered down, the configuration state of the tmcu is saved in off-chip flash memory connected to an I2C controller in the Peripherals IP subsystem. Before the state is saved, a secure hash is calculated on the data and it is saved at a pre-determined address in trused non-volatile memory (tnvm) in the HRoT. When powering up the HRoT the configuration data is read from external flash. The I2C controller calculates a secure hash that is appended to the data and the tmcu compares the stored hash with the calculated one and only restores state if they match. 

* Threat Model
A malicious actor may modify the stored configuration to escalate privilege or disable parts of the hardware. If the modified configuration is restored due to missing or omitted validation the attack will be successful.

* Security Requirement
There are 3 requirements for this CWE: 1. Confidentiality: The Stored Hash cannot be read by an untrusted source 2. Integrity: The Stored Hash cannot be written by an untrusted source 3. The saved state in external memory must not be restored if the Stored Hash does not compare to the calculated hash.


## CWE 1310: Missing Ability to Patch ROM Code
### Description
Missing an ability to patch ROM code may leave a System or System-on-Chip (SoC) in a vulnerable state.
### Radix Security Rule Template
If the design doesn't have the ability to patch ROM code, this may be intentional or an implementation oversight. Radix will not find the case where something is missing but it will find cases where there are security violations caused by an incorrect implementation or design.
Information in User accessible signals must not flow to Sensitive status Register.


### Detection Example
The boot code for the tmcu is stored in One Time Programable (OTP) memory. There is a bit in the tmcu that allow the OTP memory to be updated. This bit must only be writable by trusted software running on the tmcu. When the update is complete, a status bit is set to indicate success and the tmcu clear the bit that enable the memory to be written.

* Threat Model
An attacker disables the ability to write to OTP when the firmware update is started. If the update complete bit is still set if the update is not completed, the system looks like it was updated but it still has the old firmware which has security vulnerabilities the attacker can use.

* Security Requirement
There should be no influence on the update complete bit from the control bit that enables the update and there should be no information flow from outside the HRoT to the status bit.


## CWE 1311: Improper Translation of Security Attributes by Fabric Bridge
### Description
The bridge incorrectly translates security attributes from either trusted to untrusted or from untrusted to trusted when converting from one fabric protocol to another.
### Radix Security Rule Template
Information from User accessible signals must not flow to Security sensitive signals when the source has an untrusted privilege level and information from User accessible signals must not flow to Non security sensitive signals when the source has a trusted privilege level. The second case may or may not be a system requirement, but it highlights a mismatch in privilege levels that could be introduced through a bug in a interconnect bridge.


### Detection Example
The SoC has an OCP controller in the Peripherals IP subsystem. Masters connected to the OCP interface has one of four privilege levels: 2'b00 - trusted high, 2'b10 - trusted low, 2'b01 - untrusted high and 2'b11 - untrusted low. Masters with a trusted privilege level are only allowed to read and write secure areas of the SoC e.g. trusted nonvolatile memory (tnvm) and masters with untrusted privilege level are only allowed to read and write non-secure areas of the SoC e.g. shared memory (MEM). A master with trusted privilege level is not allowed to access non-secure areas of the SoC and vice versa. Hence it is important that trust levels are correctly translated throughout the chip. 

* Threat Model
Bugs in the implementation of the interconnect fabric may result in some privilege levels being translated to an incorrect security level. This may allow an attacker to access secure locations in the SoC from an un-trusted master.

* Security Requirement
Security identifiers must be correctly transported and translated by the interconnect fabric of the SoC.


## - CWE 1312: Missing Protection for Mirrored Regions in On Chip Fabric Firewall
### Description
The firewall in an on-chip fabric protects the main addressed region, but it does not protect any mirrored memory or memory-mapped-IO (MMIO) regions.
### Radix Security Rule Template
Information from processor running unprivileged code, non-privileged store data must not flow to a Mirrored memory location if the access to the original memory location notallowed by access control.


### Detection Example
The SoC has a 64k section of shared memory (MEM) that is mirrored by the memory controller for fault tolerance. Access control to the memory is done by the interconnect firewall. The privilege level can be set for each 4k memory block. The same access control should be applied to the original memory region and the mirrored region. Due to a design oversight the firewall doesn't enforce access control on the mirrored region. 

* Threat Model
An attacker could read and write privileged data by reading and writing the mirrored region since access control is missing.

* Security Requirement
The same access control applied to the original memory should be applied to the mirrored region.


## CWE 1313: Hardware Allows Activation of Test or Debug Logic at Runtime
### Description
During runtime, the hardware allows for test or debug logic (feature) to be activated, which allows for changing the state of the hardware. This feature can alter the intended behavior of the system and allow for alteration and leakage of sensitive data by an adversary.
### Radix Security Rule Template
Information on Signals controlable by untrusted agents should not flow to Signals that enable debug unless the access is properly authenticated.


### Detection Example
Debug mode in the SoC is enabled by setting the tmcu.CSR.debugen bit to "1". This is normally done through the debug interface after the access has been properly authenticated. No other user controllable signals can affect the state of the debugen bit so debug mode cannot be entered during normal operations of the device.

* Threat Model
A malicious actor is able to enable debug mode during normal operation of the device through an unintended back door into the HRoT or by bypassing the authentication method, thus exposing sensitive data through the debug interface.

* Security Requirement
It must not be possible to enable debug or testmode during normal runtime for an unauthorized agent.


## CWE 1314: Missing Write Protection for Parametric Data Values
### Description
The device does not write-protect the parametric data values for sensors that scale the sensor value, allowing untrusted software to manipulate the apparent result and potentially damage hardware or cause operational failure.
### Radix Security Rule Template
Information from Signals writable by untrusted agents must not flow to Security sensitive control signals.


### Detection Example
The SoC has a temperature sensor, located in the untrusted subsystem, so that overheating can be detected. The sensed temperature is computed using two parameters: offset and scale as: "sensedtemp = offset + scale * sensorval". The sensedtemp value is available in a Read Only register. The raw sensor value is not available to be read. The offset and scale registers are only writable by the tmcu. None of the cores in the untrusted subsystem can write the offset and scale registers. 

* Threat Model
Due to a design oversight, the offset and scale registers are writable by the untrusted cores. By modifying the values of the parameters, the chip may overheat. This can cause it to malfunction and possibly bypassing security protections.

* Security Requirement
The temperature sensor parameters must not be writable by untrusted software.



## CWE 1315: Improper Setting of Bus Controlling Capability in - Fabric End point
### Description
The bus controller enables bits in the fabric end-point to allow responder devices to control transactions on the fabric.
### Radix Security Rule Template
Information from User controlled signals e.g non-privileged code or a peripheral interface, must not flow to security sensitive control bits. Additional requirements may require control signals to be 0 (disabled) by default


### Detection Example
The un-trusted sub-system of the SoC have three units that can master transactions on the interconnect fabric. They are the Core0 processor, DMA and UART in Peripherals IP sub-system. Each instance connected to the fabric has a control bit, masteren to determine if it is a master or a slave. In a specific implementation of the SoC, only the Core0 processor is allowed to act as a master. The masteren bit in all other instances must be 0 at all times.

* Threat Model
An attacker is able to write to the masteren bit in one of the slaves allowing it to master transactions on the interconnect and bypassing access control.

* Security Requirement
The master / slave control bits should not be writable by anyone. They should always be 0 except for the one Core that is enabled.


## - CWE 1316: Fabric Address Map Allows Programming of Unwarranted Overlaps of Protected and Unprotected Ranges
### Description
The address map of the on-chip fabric has protected and unprotected regions overlapping, allowing an attacker to bypass access control to the overlapping portion of the protected region.
### Radix Security Rule Template
Data in a privileged address range in a shared memory (Privileged data signals) must not influence signals readable by untrusted agents This should always hold true even if the non-privileged address range overlap the privileged address range. Additionally, the privileged address range in shared memory must not be able to be influenced by signals writable by untrusted agents.


### Detection Example
The SoC has two embedded processors, Core0 and Core1, each running user code for two different users. Each user has a private area in shared memory (MEM) which the other user should not have access to. Each user requests a private address range from a privileged process running on one of the cores and of course the two ranges should not overlap. The private range is configured in two sets of registers in the interconnect fabric. Due to hardware implementation bugs or firmware bugs, it is possible that the two private ranges overlap allowing each user access to the other user’s private data. 

* Threat Model
A malicious user is able to program his private address range to overlap with that of another user and will be able to read and write data that is private to the other user.

* Security Requirement
A user should only be able to access data in his own private area in memory even if the memory range overlap with the private area of another user.


## CWE 1317: Missing Security Checks in Fabric Bridge
### Description
A bridge that is connected to a fabric without security features forwards transactions to the slave without checking the privilege level of the master. Similarly, it does not check the hardware identity of the transaction received from the slave interface of the bridge.
### Radix Security Rule Template
Information from User controllable signals should not flow to Security sensitive signals unless the source of the data is privileged.


### Detection Example
The interconnect (tbus) in the Hardware Root of Trust (HRoT) doesn't implement access control since the hrotiface bridge only allow trusted transactions on the bus. The trusted masters (Core0 and DMA) on the interconnect fabric in the untrusted subsystem have an output, priv, which is set when running in privileged mode. Only transactions from masters running in privileged mode are forwarded by the hrotiface bridge to the tbus. The hrotiface bridge is re-used from another project that did not have different privilege levels so all transactions in the HRoT address range are forwarded to the tbus regardless of security status, but this behavior was not mentioned in the documentation.

* Threat Model
A malicios actor may program the DMA to read data from the secure areas of the HRoT despite not running in privileged mode.

* Security Requirement
The access policy of the HRoT should be enforced even if the security checks in connected bridges are broken or missing.


## - CWE 1318: Missing Support for Security Features in On chip Fabrics or Buses
### Description
On-chip fabrics or buses either do not support or are not configured to support privilege separation or other security features, such as access control.
### Radix Security Rule Template
Information from User controllable signals should not flow to Security sensitive signals when the source is in non-secure mode.


### Detection Example
The interconnect fabric in the un-trusted sub-system of the SoC is using Open Core Protocol (OCP). The signals for transporting security attributes are optional and are not implemented even though most masters and slaves supports it. The Power Management Unit (PMU) in the Peripherals sub-system has a control register to set thermal limits. Writing the register is restricted to secure masters e.g., CPUs running privileged code. The MReqInfo output of Core0 is driven to 0 to indicate that a transaction is privileged but it is not transported through the fabric. The MReqInfo input to the PMU is tied to zero since it is not driven by the fabric.

* Threat Model
An attacker running user level code on Core0 can program the thermal limits to out-ofrange vales that will damage the device thus creating a denial-of-service attack.

* Security Requirement
The on-chip interconnect must include security attributes if security sensitive slaves are connected.


## CWE 1319: Improper Protection against Electromagnetic Fault - Injection (EM FI)
### Description
The device is susceptible to electromagnetic fault injection attacks, causing device internal information to be compromised or security mechanisms to be bypassed.


## CWE 1320: Improper Protection for Out of Bounds Signal Level Alerts
### Description
Untrusted agents can disable alerts about signal conditions exceeding limits or the response mechanism that handles such alerts.
### Radix Security Rule Template
Information from User controllable signals should not flow to Security sensitive signals unless the Source is trusted.

### Detection Example
The SoC has an external Digital Temperature Sensor (DTS) so that software can shut down the device to prevent permanent damage due to overheating. The DTS is connected to one of the GPIO pins of the GPIO controller in the Peripherals IP subsystem which sends an interrupt to the Core0 processor. The GPIO controller is configured by the CPU in the HW Root of Trust during secure boot and it should not be modifiable by other agents.

* Threat Model
If a malicious actor can change the GPIO pin from an input to an output, he can perform a denial-of-service attack. The warning signal from the temperature sensor will not reach the CPU and the system may stop working and be permanently damaged.

* Security Requirement
GPIO configuration bits must not be writable by untrusted agents.



## CWE 1323: Improper Management of Sensitive Trace Data
### Description
Trace data collected from several sources on the System-on-Chip (SoC) is stored in unprotected locations or transported to untrusted agents.
### Radix Security Rule Template
Information from Security sensitive signals must not flow to User accessible signals unless the destination is properly authenticated.


### Detection Example
The SoC has a Trace IP module connected to the interconnect in the un-trusted subsystem. It captures transaction type, address and data for every transaction on the interconnect fabric and stores it in local trace memory. Some of the transactions originate in or targets the Hardware Root of Trust and this part of the trace data is security sensitive. The trace data can be read via JTAG from the Trace IP memory. A debugger connected to JTAG must be authenticated before being allowed to read security sensitive trace data. If authentication fails, only non-secure trace data can be read.

* Threat Model
A malicious actor is able to read security sensitive trace data even though the debugger is not authenticated because the Trace IP block did not properly track the source of the trace data and hence allowed access to transactions originating in the HRoT.

* Security Requirement
Trace data from security sensitive source must only be read if the destination is properly authenticated.


## CWE 1324: Sensitive Information Accessible by Physical Probing of JTAG Interface
### Description
Sensitive information in clear text on the JTAG interface may be examined by an eavesdropper, e.g. by placing a probe device on the interface such as a logic analyzer, or a corresponding software technique.
### Radix Security Rule Template
Information from the design is only allowed to flow to User visible signals e.g. the JTAG port if it flows through the AES encryption block


### Detection Example
The JTAG port of the SoC is connected to the debug module in the Hardware Root of Trust, allowing an authenticated user to read data from all modules on the tbus interconnect. In order to protect against anyone reading the data in flight when it has left the SoC, data is encrypted in the AES core before going to the debug block.

* Threat Model
If data on the JTAG pins are not protected, an attacker may snoop on the bus while an authenticated user is performing reads of secure locations in the chip.

* Security Requirement
Only data coming from the AES block is allowed to reach the debug module and thus the JTAG port. There must be no information flow that bypass the AES block.



## CWE 1326: Missing Immutable Root of Trust in Hardware
### Description
A missing immutable root of trust in the hardware results in the ability to bypass secure boot or execute untrusted or adversarial boot code.
### Radix Security Rule Template
Information from User accessible signals must not flow to Immutable signals


### Detection Example
Secure boot in the example SoC is performed by the Hardware Root of Trust (HRoT) sub-system. The boot code, key material and other boot data must be immutable otherwise the implementation is vulnerable to attacks. The HRoT stores this data in ROM, OTP, SRAM and tnvm memory that are assumed to be immutable

* Threat Model
Some locations that store secure boot code and data are mutable which allows an adversary to modify them and execute their choice of code and bypass access control in the system.

* Security Requirement
All secure boot code and data must be immutable i.e. not writable by any agent in the untrusted subsystem of the SoC.



## CWE 1328: Security Version Number Mutable to Older Versions
### Description
Security-version number in hardware is mutable, resulting in the ability to downgrade (roll-back) the boot firmware to vulnerable code versions.
### Radix Security Rule Template
Information on Interfaces controllable by untrusted agents should not flow to Signals carrying confidential information


### Detection Example
A security version number is stored in trusted non-volatile memory in the HW Root of Trust (HRoT). It is used to ensure that firmware signed with a lower version number cannot be loaded and run. The security version number is preserved during power cycles and resets. It must not be modifiable by any agent outside the HRoT.

* Threat Model
If a malicious actor can modify the security version number stored in the HRoT, this allows a roll-back to previous version of firmware which may have vulnerabilities that can be used for an attack.

* Security Requirement
Security version numbers must not be modifiable from outside the Hardware Root of Trust.


## CWE 1330: Remanent Data Readable after Memory Erase
### Description
Confidential information stored in memory circuits is readable or recoverable after being cleared or erased.



## CWE 1331: Improper Isolation of Shared Resources in Network On Chip
### Description
The product does not isolate or incorrectly isolates its on-chip-fabric and internal resources such that they are shared between trusted and untrusted agents, creating timing channels.
### Radix Security Rule Template
Secret data may leak via a timing channel i.e. differences in latency for example through a NOC reveal information about the data. This leakage may be detected using Radix.
Information in secret data should not flow to Module whose behavior is influenced by secure data and it can be observed.



### Detection Example
The interconnect in the untrusted sub-system of the SoC only support one connection to the shared memory at the time. If Core0 is reading from memory, Core1 has to wait. Software running in privileged mode on Core0 is running the RSA encryption algorithm. It reads an encryption key from OTP in the Hardware Root of Trust (HRoT) and store it in a register in Core0. When a bit in the key is 1, RSA performs a multiplication which cause a read from the shared memory.

* Threat Model
An attacker running in user mode on Core1 is doing a series of reads from shared memory while the RSA algorithm is run on Core0. By measuring the latency of each memory read he can determine if the RSA key is 1 or 0.

* Security Requirement
No timing information should flow from the RSA Key to the load store unit in the core executing the algorithm.



## CWE 1332: Insufficient Protection Against Instruction Skipping Via Fault Injection
### Description
The device is missing or incorrectly implements circuitry or sensors to detect and mitigate CPU instruction skips that can be caused by fault injection.


## CWE 1334: Unauthorized Error Injection Can Degrade Hardware Redundancy
### Description
An unauthorized agent can inject errors into a redundant block to deprive the system of redundancy or put the system in a degraded operating mode.


## CWE 1338: Improper Protections Against Hardware Overheating
### Description
A hardware device is missing or has inadequate protection features to prevent overheating.


## CWE 1351: Improper Handling of Hardware Behavior in Exceptionally Cold Environments
### Description
A hardware device, or the firmware running on it, is missing or has incorrect protection features to maintain goals of security primitives when the device is cooled below standard operating temperatures.
### Radix Security Rule Template
Information from Entropy source e.g. SRAM based PUF, should not flow to Location using entropy data e.g. cryptographic function unless the entropy source is verified to be working.


### Detection Example
The RNG used by the AES encryption module is using the output from a PUF as its entropy source. The SRAM based PUF needs to operate at a certain temperature to ensure sufficient entropy. An on-chip temperature sensor measures the temperature of the PUF and if it is too low, it won't allow the PUF to be used and the SoC won't boot.

* Threat Model
An attacker may try to write the temperature sensor control register with a much lower threshold temperature making the PUF output depend on previous data instead of manufacturing inconsistencies. An attacker may also try to boot the SoC even if the PUF entropy test is failing.

* Security Requirement
The temperature sensor control register should not be writable by any agent outside the Hardware Root of Trust (HRoT) module. The PUF output should not be used by the AES unless the temperature is above a threshold and the entropy test of the PUF is passing. 

