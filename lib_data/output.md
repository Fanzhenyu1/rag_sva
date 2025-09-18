

# **Radix Coverage for Hardware** **Common Weakness** **Enumeration (CWE) Guide**

## **August 2021 CWE 4.5**

#### **Ensuring hardware security, one chip at a time.** **VISIT: TORTUGALOGIC.COM**


 1




## **Radix Coverage for Hardware Common Weakness** **Enumeration (CWE) Guide**

### **Table of Contents**


Revision History ............................................................................................................... 6


Introduction ...................................................................................................................... 6


Using this Guide ............................................................................................................... 7


Radix Security Rules ........................................................................................................ 8


CWE-203: Observable Discrepancy ................................................................................ 9


CWE-226: Sensitive Information in Resource Not Removed Before Reuse .................. 10


CWE-276: Incorrect Default Permissions ....................................................................... 12


CWE-325: Missing Cryptographic Step .......................................................................... 14


CWE-440: Expected Behavior Violation ......................................................................... 16


CWE-441: Unintended Proxy or Intermediary ('Confused Deputy') ............................... 17


CWE-1053: Missing Documentation for Design ............................................................. 19


CWE-1189: Improper Isolation of Shared Resources on System-on-a-Chip (SoC) ....... 19


CWE-1190: DMA Device Enabled Too Early in Boot Phase .......................................... 21


CWE-1191: Exposed Chip Debug and Test Interface With Insufficient or Missing
Authorization .................................................................................................................. 23


CWE-1192: System-on-Chip (SoC) Using Components without Unique, Immutable
Identifiers ........................................................................................................................ 24


CWE-1193: Power-On of Untrusted Execution Core Before Enabling Fabric Access
Control ............................................................................................................................ 24


CWE-1209: Failure to Disable Reserved Bits ................................................................ 26


CWE-1220: Insufficient Granularity of Access Control ................................................... 28


CWE-1221: Incorrect Register Defaults or Module Parameters .................................... 30


CWE-1223: Race Condition for Write-Once Attributes .................................................. 31


CWE-1224: Improper Restriction of Write-Once Bit Fields ............................................ 34


CWE-1231: Improper Implementation of Lock Protection Registers .............................. 36


CWE-1232: Improper Lock Behavior After Power State Transition ............................... 37


CWE-1233: Improper Hardware Lock Protection for Security Sensitive Controls .......... 39


CWE-1234: Hardware Internal or Debug Modes Allow Override of Locks ..................... 40


CWE-1240: Use of a Risky Cryptographic Primitive ...................................................... 42


CWE-1241: Use of Predictable Algorithm in Random Number Generator ..................... 43


 2





CWE-1242: Inclusion of Undocumented Features or Chicken Bits ................................ 43


CWE-1243: Sensitive Non-Volatile Information Not Protected During Debug ............... 44


CWE-1244: Improper Access to Sensitive Information Using Debug and Test Interfaces
....................................................................................................................................... 46


CWE-1245: Improper Finite State Machines (FSMs) in Hardware Logic ....................... 48


CWE-1246: Improper Write Handling in Limited-write Non-Volatile Memories .............. 50


CWE-1247: Missing or Improperly Implemented Protection Against Voltage and Clock
Glitches .......................................................................................................................... 51


CWE-1248: Semiconductor Defects in Hardware Logic with Security-Sensitive
Implications .................................................................................................................... 51


CWE-1251: Mirrored Regions with Different Values ...................................................... 52


CWE-1252: CPU Hardware Not Configured to Support Exclusivity of Write and Execute
Operations ...................................................................................................................... 54


CWE-1253: Incorrect Selection of Fuse Values ............................................................. 56


CWE-1254: Incorrect Comparison Logic Granularity ..................................................... 57


CWE-1255: Comparison Logic is Vulnerable to Power Side-Channel Attacks .............. 59


CWE-1256: Hardware Features Enable Physical Attacks from Software ...................... 59


CWE-1257: Improper Access Control Applied to Mirrored or Aliased Memory Regions 61


CWE-1258: Exposure of Sensitive System Information Due to Uncleared Debug
Information ..................................................................................................................... 62


CWE-1259: Improper Restriction of Security Token Assignment .................................. 64


CWE-1260: Improper Handling of Overlap Between Protected Memory Ranges .......... 65


CWE-1261: Improper Handling of Single Event Upsets ................................................. 67


CWE-1262: Register Interface Allows Software Access to Sensitive Data or Security
Settings .......................................................................................................................... 69


CWE-1263: Improper Physical Access Control .............................................................. 71


CWE-1264: Hardware Logic with Insecure De-Synchronization between Control and
Data Channels ............................................................................................................... 73


CWE-1266: Improper Scrubbing of Sensitive Data from Decommissioned Device ....... 74


CWE-1267: Policy Uses Obsolete Encoding ................................................................. 76


CWE-1268: Policy Privileges are not Assigned Consistently Between Control and Data
Agents ............................................................................................................................ 78


CWE-1269: Product Released in Non-Release Configuration ....................................... 80


CWE-1270: Generation of Incorrect Security Tokens .................................................... 82


CWE-1271: Uninitialized Value on Reset for Registers Holding Security Settings ........ 83


CWE-1272: Sensitive Information Uncleared Before Debug/Power State Transition .... 84


 3





CWE-1273: Device Unlock Credential Sharing .............................................................. 86


CWE-1274: Insufficient Protections on the Volatile Memory Containing Boot Code ..... 86


CWE-1276: Hardware Child Block Incorrectly Connected to Parent System ................ 88


CWE-1277: Firmware Not Updateable ........................................................................... 90


CWE-1278: Missing Protection Against Hardware Reverse Engineering Using
Integrated Circuit (IC) Imaging Techniques ................................................................... 92


CWE-1279: Cryptographic Operations are run Before Supporting Units are Ready ..... 92


CWE-1280: Access Control Check Implemented After Asset is Accessed .................... 94


CWE-1281: Sequence of Processor Instructions Leads to Unexpected Behavior ......... 95


CWE-1282: Assumed-Immutable Data is Stored in Writable Memory ........................... 95


CWE-1283: Mutable Attestation or Measurement Reporting Data ................................ 97


CWE-1290: Incorrect Decoding of Security Identifiers ................................................... 98


CWE-1291: Public Key Re-Use for Signing both Debug and Production Code ........... 100


CWE-1292: Incorrect Conversion of Security Identifiers .............................................. 100


CWE-1294: Insecure Security Identifier Mechanism .................................................... 102


CWE-1295: Debug Messages Revealing Unnecessary Information ............................ 102


CWE-1296: Incorrect Chaining or Granularity of Debug Components ......................... 104


CWE-1297: Unprotected Confidential Information on Device is Accessible by OSAT
Vendors ........................................................................................................................ 105


CWE-1298: Hardware Logic Contains Race Conditions .............................................. 106


CWE-1299: Missing Protection Mechanism for Alternate Hardware Interface ............. 106


CWE-1300: Improper Protection Against Physical Side Channels .............................. 108


CWE-1301: Insufficient or Incomplete Data Removal within Hardware Component ... 108


CWE-1302: Missing Security Identifier ......................................................................... 108


CWE-1303: Non-Transparent Sharing of Microarchitectural Resources ..................... 110


CWE-1304: Improperly Preserved Integrity of Hardware Configuration State During a
Power Save/Restore Operation ................................................................................... 111


CWE-1310: Missing Ability to Patch ROM Code .......................................................... 113


CWE-1311: Improper Translation of Security Attributes by Fabric Bridge ................... 115


CWE-1312: Missing Protection for Mirrored Regions in On-Chip Fabric Firewall ........ 117


CWE-1313: Hardware Allows Activation of Test or Debug Logic at Runtime .............. 118


CWE-1314: Missing Write Protection for Parametric Data Values ............................... 120


CWE-1315: Improper Setting of Bus Controlling Capability in Fabric End-point .......... 122


CWE-1316: Fabric-Address Map Allows Programming of Unwarranted Overlaps of
Protected and Unprotected Ranges ............................................................................. 123


 4





CWE-1317: Missing Security Checks in Fabric Bridge ................................................ 125


CWE-1318: Missing Support for Security Features in On-chip Fabrics or Buses ........ 127


CWE-1319: Improper Protection against Electromagnetic Fault Injection (EM-FI) ...... 129


CWE-1320: Improper Protection for Out of Bounds Signal Level Alerts ...................... 129


CWE-1323: Improper Management of Sensitive Trace Data ....................................... 130


CWE-1324: Sensitive Information Accessible by Physical Probing of JTAG Interface 132


CWE-1326: Missing Immutable Root of Trust in Hardware ......................................... 134


CWE-1328: Security Version Number Mutable to Older Versions ............................... 135


CWE-1330: Remanent Data Readable after Memory Erase ....................................... 137


CWE-1331: Improper Isolation of Shared Resources in Network On Chip .................. 138


CWE-1332: Insufficient Protection Against Instruction Skipping Via Fault Injection .... 139


CWE-1334: Unauthorized Error Injection Can Degrade Hardware Redundancy ......... 139


CWE-1338: Improper Protections Against Hardware Overheating .............................. 140


CWE-1351: Improper Handling of Hardware Behavior in Exceptionally Cold
Environments ............................................................................................................... 140


Appendix: Security Rule Types .................................................................................... 143


Legal Notices ............................................................................................................... 144


 5





.

### Revision History

|Release Date|CWE|Notes|
|---|---|---|
|**August 2020**|4.0|Initial release|
|**October 2020**|4.0|Added examples for 31 CWEs. Cover partial<br>CWE 4.1 examples. New diagram for example<br>design|
|**January 2021**|4.1|Added examples for 23 CWEs. Complete up to<br>CWE 4.1 and partial coverage of CWE 4.2|
|**July 2021**|4.2|Complete up to CWE 4.2 and partial coverage<br>of CWE 4.3. Verification examples for CWE-<br>1243 and CWE-1328|
|**August 2021**|4.5|Complete up to CWE 4.5. Added remaining 12<br>CWE 4.3 and 4.5 examples. Verification<br>example for CWE-1223|


### Introduction


MITRE's hardware Common Weakness Enumeration (CWE) database aggregates
hardware weaknesses that are the root causes of vulnerabilities in deployed parts. A
complete list can be found on the MITRE Hardware Design Webpage. Hardware CWEs
are ideal to be used alongside internally developed security requirements databases
and have been developed and submitted by both government and commercial design
teams such as the Intel® Corporation and Tortuga Logic.


This guide can be used in conjunction with the CWE list as a resource to aid conversion
from CWEs to Security Rules for use with Tortuga Logic’s Radix™ security verification
tools. It also serves as a guide for design and verification teams to help them answer
the question: “what security vulnerabilities should I verify?”


 6




### Using this Guide


In this guide each CWE is listed along with a template Security Rule that can be filled in
with design-specific signals and used as a baseline test for the respective CWE.


Each Security Rule template is populated by placeholders with plain-language
descriptions surrounded by curly braces, e.g. {{Placeholder in plain-language}}.


To transform these placeholders into valid Security Rules, replace the placeholder with
design signals that match the description in the placeholder.


Because designs are diverse and CWEs apply generally, a bulleted list of mnemonic
macros follow each template description that may be adapted to specific scenarios.
Macros follow the pattern {{PREFIX}}_{{SUFFIX}}, where prefix maps to security
objective (confidentiality, integrity, and availability) and the suffix maps to the asset to
be secured (registers, access controls, general design elements, etc.)


Details about these macros are in tables in the Appendix at the end of this guide.


Each CWE section also contain an example illustrated using a hypothetical SoC which
shows more specifically, using design signals how one can write one or several rules to
verify the weakness is not present in the design.


To learn more about a specific CWE, follow the link in the CWE name at the beginning
of the section referring to that CWE.


Tortuga Logic recommends that projects follow a Security Development Lifecycle (SDL)
in addition to using security tools. Using this guide along with the MITRE Hardware
CWE list, hardware security and development teams can take advantage of a 5-step
process to streamline threat modeling and validation within their SDL, prior to
committing a hardware design to silicon.


The 5-step CWE validation process to convert CWEs to Security Rules within the SDL:


1. Identify CWE(s) relevant to the threat model.


2. State plain-language security requirement identified in the CWE(s).


3. List the assets (in the form of data or design signals), objectives (confidentiality, integrity,
availability), and security boundaries of the design as they correspond to step 2.


4. Use the Radix security rule template for the corresponding CWE in this document. Add
design signals from step 3 to create security rules that can be validated with a hardware
security verification environment, such as Radix™ from Tortuga Logic, alongside standard
verification environments from Cadence®, Mentor® A Siemens Business, and Synopsys®.


5. Leverage the security verification environment to signoff that each CWE has been
successfully checked.


This 5-step validation process provides a valuable bridge between the security
engineers and architects who own the product security requirements, and the design


 7





and verification teams who are building and verifying proper functionality of the device.
Often, Steps 1-3 are maintained by the security engineers and steps 4-5 are handled by
the hardware design and verification teams.

### Radix Security Rules


Security rules are expressed as information flow properties. They decouple the action
from the observation. For example, the "action" is the activity that leads to the
observable behavior. Using Radix Security Rules it is not necessary to specify the
action, only that information should not flow from one location to another.


The core of the rule specification is the not flow operator (=/=>) which allows for
specification of a source (signal or set of signals) to a destination (signal or set of
signals). For example, a confidentiality rule related to a secret encryption key can be
written as:


**assert iflow(secret_key =/=> insecure_mem);**


This rule states that the secret key should “not flow" or leak to an insecure memory
where secret_key and insecure_mem are signals in the Verilog, SystemVerilog, or
VHDL design. The not flow operator makes this specification easy and compact.


Optionally, specific conditions can be used to indicate when confidential information is
being carried by design signals. These can be specified using the _when_ keyword on the
left-hand side of the no-flow operator (=/=>) along with a Boolean conditional expression
based on design signals, such as when a _Privileged-mode bit is set._


 8





.

### - CWE 203: Observable Discrepancy

##### Description


The product behaves differently or sends different responses under different
circumstances in a way that is observable to an unauthorized actor, which exposes
security-relevant information about the state of the product, such as whether a particular
operation was successful or not.

##### Radix Security Rule Template


Rule Template Detail


Information should not flow from _Signals carrying confidential information_ to _Signals that_
_can be observed by an unauthorized actor_ when a _Privileged-mode bit is set._


Security Rule Types

 - CONFIDENTIALITY_DATA

 - CONFIDENTIALITY_SECURITY_STATE

##### Detection Example


The _aes_ encryption engine uses two different length encryption keys and the time it
takes to encrypt plaintext is different in the two cases. The untrusted cores _core{0-N}_
may write data to _sram_ and request it to be encrypted. When encryption is done, an
interrupt is sent to the requesting core and the encrypted data can be read from _sram._
Verifying that the encryption done signal is asserted after the correct number of clock


 9





cycles after encryption is started is a required step in functional verification, but it
doesn't verify that information doesn't flow to a location where it is visible by an
unauthorized actor.


Threat Model


By measuring the time encryption takes, an attacker can obtain information about which
key was used.


Security Requirement


Different configurations of security sensitive operations should all take the same amount
of time to avoid leaking information that can be used in a timing side channel attack.


Completing the Template Based on Design Signals and Security Requirement


From the requirement, the output of the encryption should not be available until after the
longest encryption time. When _aes.done_ is asserted, information from the _aes.csr.key_
will flow to the _sram_ because the encrypted data contains key information. This is OK as
long as it doesn't happen before _aes.done_ is asserted. Radix security rules doesn't
support timing so a counter in the test environment, which is bound to the design, is
used to count the number of cycles between aes start and done. Filling in the template
gives the rule below.




### - CWE 226: Sensitive Information in Resource Not Removed Before Reuse

##### Description

When a device releases a resource such as memory or a file for reuse by other entities,
information contained in the resource is not fully cleared prior to reuse of the resource.

##### Radix Security Rule Template


 10





Rule Template Detail


Information from a resource _(Resource to be cleared)_ must not flow to a new process
_(Signals to be used by process)_ when the resource does not equal the appropriate
cleared value _(Value when cleared)_ or clearing is not needed, indicated by the Boolean
_Okay flag._


_Value when cleared_ will be based on design specifics. For example, if the _value when_
_cleared_ is the same as the secret value (e.g. the memory is zeroized but the secret data
is "0") and the _okay flag_ is incorrectly asserted, a violation will not be flagged so the rule
needs to be adapted to the actual implementation.


Security Rule Types

 - CONFIDENTIALITY_DATA

 - CONFIDENTIALITY_REGISTER

 - INTEGRITY_FSM_STATES

##### Detection Example


In the SoC design above, Hardware Root of Trust (HRoT) local SRAM has a privileged
region bounded by _PRIV_END_ADDR_ and _PRIV_START_ADDR._ In this example, we
expect this region to be set to all zeros (zeroized) when the CSR _zeroize_status_ within
the tmcu.CSR module is non-zero. In this example zeroize_status is non-zero only
during zeroization, other values of zeroize_status indicate different stages of the
zeroization process, and when _zeroize_status == 0_ then zeroization has not been
requested. Request of zeroization can be made via system software or anti-tamper
circuitry. An exception is allowed when the _tmcu_ is in privileged mode, indicated by the
_tmcu.CSR.priv_mode_ register.


Threat Model


In this example we assume that threats are bugs or malice in parts of the system
external to the HRoT-local SRAM that may obtain privileged information from uncleared
privileged regions after a mode-switch.


 11





Security Requirement


Information from the range _[PRIV_END_ADDR : PRIV_START_ADDR]_ must not leave
the SRAM once zeroization has been triggered unless the range is zeroized, the tmcu is
in privileged mode, or zeroization has not been requested.


Completing the Template Based on Design Signals and Security Requirement


Based on the security goal we fill in the template from the example signals, obtaining
the rule below. The values for _PRIV_END_ADDR_ and _PRIV_START_ADDR_ are
parameters provided by the user.

### - CWE 276: Incorrect Default Permissions

##### Description


During installation, installed file permissions are set to allow anyone to modify those
files.

##### Radix Security Rule Template


 12





Rule Template Detail


Information from the _Asset_ must be prevented from being read and/or written with data
from _user-accessible signals_ unless the _permission bits_ are correctly set to the _value_
_indicating asset should be readable/writable._


Depending on security requirements, either one or both templates may be used. _Note:_
Values for the permission bits needs to be obtained from the design specification.


Security Rule Types

 - CONFIDENTIALITY_ASSET

 - INTEGRITY_ACCESS_CONTROL_CONFIG

 - INTEGRITY_ASSET

 - VERIFY_ACCESS_CONTROL_CONFIG

##### Detection Example


Assume that security-critical settings and identifiers are available in a range of registers
bounded by _PRIV_END_ADDR:PRIV_START_ADDR_ in the CSR module of the tmcu.
These values are locked or unlocked (e.g. in an authenticated debug mode) based on
the _tmcu.csr.lock_bit_ register in the same module.


Threat Model


We assume that untrusted software (the threat) has access to the input and output ports
of the _hrot_iface_ and may incorrectly read / write security critical information.


Security Requirement


Information from the address range _PRIV_END_ADDR:PRIV_START_ADDR_ must not
be readable or writable via _hrot_iface_ unless tmcu.csr.lock_bit is zero (or a value that
indicates it is not locked)


Completing the Template Based on Design Signals and Security Requirement


Based on the security goal we fill in the template which gives the rule below. The values
for _PRIV_END_ADDR_ and _PRIV_START_ADDR_ are constants provided by the user.


 13




### - CWE 325: Missing Cryptographic Step

##### Description


The product does not implement a required step in a cryptographic algorithm, resulting
in weaker encryption than advertised by the algorithm.

##### Radix Security Rule Template


_Note:_ Radix will detect missing steps in established algorithms so long as the transitions
between steps are framed as information flow properties. For example, it can detect

could make this happen, and AES works okay with different numbers of rounds, and

functional verification plan.


Rule Template Detail


Information from _Signals in the previous step_ must not flow to _Signals in the next step_
unless the _Previous step is complete._


Security Rule Types

 - CONFIDENTIALITY_ASSET


 14





 - INTEGRITY_ASSET

 - ISOLATE_ASSET


Detection Example


The SoC has a configurable AES cipher which supports 128-, 192- and 256-bit keys. It
goes through different number of rounds depending on the size of the key. For example,
for a 128-bit key, it goes through 10 rounds. The cipher text or plain text must not be
output until all rounds are completed.


Threat Model


A mistake in the implementation of the AES algorithm allows a malicious actor to access
the cipher text before all rounds have completed.


Security Requirement


No information about the data in the cipher should flow to the output until all rounds are
completed.


Completing the Template Based on Design Signals and Security Requirement


Based on the security goal we fill in the template from the example signals, obtaining
the rule below. _Note:_ The _NUM_ROUNDS_ parameter needs to be set depending on the
key length configuration.


 15




### - CWE 440: Expected Behavior Violation

##### Description


A feature, API, or function does not perform according to its specification.

##### Radix Security Rule Template


_Note:_ Due to the breadth of CWE-440 there are many rule variations that could detect
unexpected use.


Rule Template Detail


A commonly implemented solution to detect and prevent accidental misuse of a feature
or API is raise an interrupt and set an error flag. The template is designed to detect
finite state machine (FSM) issues that may result in a security rule violation if the FSM is
forced into an incorrect state. In this template, _Signal with next state,_ _Signal with current_
_state_ and _State transition criteria_ are all in reference to the target FSM. The conditional
_when_ _Next state is security-sensitive_ denotes the state which the FSM should not enter
unless the correct _State transition criteria_ are met.


Security Rule Types

 - INTEGRITY_FSM_STATES

##### Detection Example


In this example, _core0_ implements an error handler using the programmable interrupt
controller module _core0.pic_ . The module contains an FSM that that may transition into
a state that is intended to triple fault, the core0 CPU and reset the device. The FSM
must only go to the error state if the CPU is running privileged code. If an attacker can


 16





force this FSM into the state that triggers the triple fault then they may be able to lock
the device into a reset loop and cause a denial-of-service attack.


Threat Model


We assume that the attacker can send arbitrary commands to the core0.pic hardware
via software or hardware running at the user privilege level.


Security Requirement


core0.pic.fsm must not enter the triple fault-triggering state unless authorization flags
associate with the privilege level are set i.e. the CPU is running privileged code.


Completing the Template Based on Design Signals and Security Requirement


Based on the security goal, assuming user privilege is "1" and above, we fill in the
template which gives the rule below.

### ' ' - CWE 441: Unintended Proxy or Intermediary ( Confused Deputy )

##### Description


The product receives a request, message, or directive from an upstream component,
but the product does not sufficiently preserve the original source of the request before
forwarding the request to an external actor that is outside of the product's control
sphere. This causes the product to appear to be the source of the request, leading it to
act as a proxy or other intermediary between the upstream component and the external
actor.

##### Radix Security Rule Template







 17





Rule Template Detail


An untrusted agent should not be able to read or write security sensitive data regardless
if the access is done through another party such as a DMA. _Signals writable by_
_untrusted agents_ should not flow to _Signals with sensitive data_ via any path and _Signals_
_with sensitive data_ should not flow to _Signals readable by untrusted agents_ via any path.


Security Rule Types

 - INTEGRITY_ASSET

 - CONFIDENTIALITY_ASSET

 - INTEGRITY_ACCESS_CONTROL_MECHANISM

##### Detection Example


The _Core0_ processor is running software at the lowest privilege level and the security
access policy prevents it from accessing any data in the HRoT.SRAM memory. The
access policy allow the DMA to read and write data in the HRoT.SRAM memory.


Threat Model


An untrusted agent running code on the _Core0_ processor can access data in the HRoT
SRAM by programming the DMA so that it appears that the DMA is the source of the
transaction.


Security Requirement


The untrusted processor must not be able to access data in the HRoT SRAM.


Completing the Template Based on Design Signals and Security Requirement


Based on the security requirement, we fill in the template which gives the rules below.


 18




### - CWE 1053: Missing Documentation for Design

##### Description


The product does not have documentation that represents how it is designed.

##### Radix Security Rule Template


Radix currently does not cover this CWE, refer to the MITRE website for suggested
mitigations.

### - - CWE 1189: Improper Isolation of Shared Resources on System - - on a Chip (SoC)

##### Description


The product does not properly isolate shared resources between trusted and untrusted
agents.

##### Radix Security Rule Template


 19





Rule Template Detail


A shared resource _(Shared signals)_ must not influence _signals readable by untrusted_
_agents_ when the resource is in a _privileged mode condition._ Additionally, the shared
resource must not be able to be influenced by _signals writable by untrusted agents_
unless the resource is not in the privileged mode condition.


Security Rule Types

 - ISOLATE_ASSET

 - VERIFY_ACCESS_CONTROL_CONFIG

##### Detection Example


The Hardware Root of Trust (HRoT) local sram is memory mapped in the _core{0-N}_
address space. The HRoT allows or disallows access to private memory ranges, thus
allowing the _sram_ to function as a mailbox for communication between untrusted and
trusted HRoT partitions.


Threat Model


In this example, we assume that the threat is from malicious software in the untrusted
domain. We assume this software has access to the _core{0-N}_ memory map and can be
running at any privilege level on the untrusted cores. The capability of this threat in this
example is communication to and from the mailbox region of SRAM modulated by the
_hrot_iface._


Security Requirement


Information must not enter or exit the shared region of SRAM through hrot_iface when
in secure or privileged mode.


Completing the Template Based on Design Signals and Security Requirement


From the requirement, if the _priv_mode_ control and status register (CSR) within the
tmcu is set to _1'b1_ this corresponds to a secure mode when the privileged memory
should not be accessible. The privileged range in the SRAM model is bounded by
_SHARED_START_ADDR_ and _SHARED_END_ADDR._ The values for


 20





_SHARED_END_ADDR_ and _SHARED_START_ADDR_ are constants provided by the
user. Filling in the template gives the rule below.





_Note:_ The privilege mode bit used in the rule refers to privilege level of the resource
being accessed. If the privilege mode is changed, information may propagate, and the
rule be violated.

### - CWE 1190: DMA Device Enabled Too Early in Boot Phase

##### Description


The product enables a Direct Memory Access (DMA) capable device before the security
configuration settings are established, which allows an attacker to extract data from or
gain privileges on the product.

##### Radix Security Rule Template


Rule Template Detail


The _DMA data input_ must not flow to the _Data-carrying signals in the DMA controller_
unless the _security settings are set._ This is not identical to the CWE description because
enabling the DMA could be done in several ways. However, in each scenario where the
CWE applies the security goal is for the DMA not to act on any data prior to setting up
the security configuration to modulate DMA access.


 21





This rule template covers many scenarios by triggering a rule violation when the DMA
may move data prior to the system being in a secure state.


Security Rule Types


 - INTEGRITY_ACCESS_CONTROL_MECHANISM

 - VERIFY_ACCESS_CONTROL_CONFIG

##### Detection Example


The untrusted _DMA_ in the SoC example may be enabled by one of the untrusted cores
_core{0-N}_ and may access the entire memory range of the SoC before the security
configuration is set up by the Hardware Root of Trust (HRoT).


Threat Model


An attacker running un-privileged code may set up the _dma_ to read and write protected
resources such as _sram_ in the HRoT before the security policy is configured and thus
access sensitive data.


Security Requirement


The un-trusted DMA must not be active until the full secure boot sequence is complete.
This means data in the dma must not flow out of the _dma_ and data must not flow into
the _dma_ until secure boot is complete.


Completing the Template Based on Design Signals and Security Requirement


From the requirement, data must not flow into or out of the dma until boot is complete.
Filling in the template gives the rules below.


 22




### - CWE 1191: Exposed Chip Debug and Test Interface With Insufficient or Missing Authorization

##### Description


The chip does not implement or does not correctly check whether users are authorized
to access internal registers.

##### Radix Security Rule Template


Rule Template Detail


Internal data should not flow to _signals readable by untrusted agents_ unless _Debug is_
_enabled._


Security Rule Types

 - ISOLATE_REGISTER

 - ISOLATE_SECURITY_STATE

 - VERIFY_ACCESS_CONTROL_CONFIG

##### Detection Example


 23





Assuming the debug interface in the HRoT is disabled by default and is only enabled
when sufficiently authorized e.g., through password protection. Unless debug is
enabled, no information should flow from assets to the output of the debug module.


Threat Model


A malicious actor can read internal signals in the design through the debug interface if
the disabling logic is bypassed.


Security Requirement


Information on the internal signals connected to the _tbus_ may flow to the debug
interface outputs unless the debug interface is enabled.


Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rules below.

### - - - CWE 1192: System on Chip (SoC) Using Components without Unique, Immutable Identifiers

##### Description


The System-on-Chip (SoC) does not have unique, immutable identifiers for each of its
components.

##### Radix Security Rule Template


Radix currently does not cover this CWE, refer to the MITRE website for suggested
mitigations.

### - - CWE 1193: Power On of Untrusted Execution Core Before Enabling Fabric Access Control

##### Description


The product enables components that contain untrusted firmware before memory and
fabric access controls have been enabled.


 24




##### Radix Security Rule Template





Rule Template Detail


Information should not flow from _Signals storing untrusted firmware_ to _Instruction read_
_signals in untrusted components_ unless _Access controls are enabled._


Security Rule Types

 - INTEGRITY_ACCESS_CONTROL_MECHANISM

 - INTEGRITY_FSM_STATES

 - VERIFY_ACCESS_CONTROL_CONFIG

##### Detection Example


The un-trusted cores _core{0-N}_ fetch instructions from instruction memory in the
_peripheral IP & memory_ sub-system and master transactions on the interconnect
system. These processors should not be enabled until the interconnect access policy is
programmed by the _tmcu_ during the secure boot process.


Threat Model


Untrusted software executes before interconnect access policy is configured allowing
access to the entire SoC memory space including secure areas.


Security Requirement


Untrusted software must not execute i.e. un-trusted cores may not read instruction
memory before secure boot process is complete.


 25





Completing the Template Based on Design Signals and Security Requirement




### - CWE 1209: Failure to Disable Reserved Bits

##### Description

The reserved bits in a hardware design are not disabled prior to production. Typically,
reserved bits are used for future capabilities and should not support any functional logic
in the design. However, designers might covertly use these bits to debug or further
develop new capabilities in production hardware. Adversaries with access to these bits
will write to them in hopes of compromising hardware state.

##### Radix Security Rule Template


Rule Template Detail


Information should not flow from _Inputs to memory block with reserved range_ to
_Reserved range in memory array._


Security Rule Types

 - CONFIDENTIALITY_ASSET

 - INTEGRITY_ASSET

 - VERIFY_ACCESS_CONTROL_CONFIG


 26




##### Detection Example


There are registers in _tmcu_ that are reserved for future features. They may enable
certain features during the development cycle but will be disabled in the production
version of the design.


Threat Model


Features controlled by reserved bits are not properly disabled in the production version
of the design allowing an adversary to enable unsupported features which may have
negative security consequences.


Security Requirement


All reserved register bits should have no effect on design behavior and reserved register
bits should not be writable.


Completing the Template Based on Design Signals and Security Requirement


From the requirement that information in bits in the reserved address range should not
have any effect on design behavior, i.e. information should not flow to the output of the
memory or register module which holds the information, we can write the rule below.
The values for _RESERVED_ADDR_START_ and _RESERVED_ADDR_END_ are
constants provided by the user.


_Note:_ Additional Radix security rules may be required to verify additional register or
memory module outputs and to ensure reserved register bits are not writable.


 27




### - CWE 1220: Insufficient Granularity of Access Control

##### Description


The product implements access controls via a policy or other feature with the intention
to disable or restrict accesses (reads and/or writes) to assets in a system from untrusted
agents. However, implemented access controls lack required granularity, which renders
the control policy too broad because it allows accesses from unauthorized agents to the
security-sensitive assets.

##### Radix Security Rule Template





Rule Template Detail


Information should not flow from/to _Asset_ to/from _Untrusted readers/writers_ when

access control is enabled.


Security Rule Types

 - CONFIDENTIALITY_ASSET

 - INTEGRITY_ACCESS_CONTROL_MECHANISM

 - VERIFY_ACCESS_CONTROL_CONFIG


 28




##### Detection Example


The _sram_ in HRoT has an address range that is readable and writable by un-privileged
software, and it has an area that is only readable by un-privileged software. The _tbus_
interconnect enforces access control for slaves on the bus but uses only one bit to
control both read and write access. Address _0xA0000000 - 0xA000FFFF_ is readable
and writable by the un-trusted cores _core{0-N}_ and address _0xA0010000 - 0xA001FFFF_
is only readable by the un-trusted cores _core{0-N}_


Threat Model


The security policy access control is not granular enough as it uses one bit to enable
both read and write access. This gives write access to an area that should only be
readable by un-privileged agents.


Security Requirement


Access control logic should differentiate between read and write access and to have
sufficient address granularity.


Completing the Template Based on Design Signals and Security Requirement


From the requirement that address _0xA0010000 - 0xA001FFFF_ should not be writable
follows the rule below when filling in the template:


 29




### - CWE 1221: Incorrect Register Defaults or Module Parameters

##### Description


Hardware description language code incorrectly defines register defaults or hardware IP
parameters to insecure values.

##### Radix Security Rule Template





Rule Template Detail


Information should not flow from/to _Asset_ to/from _User-observable signals._


_Note:_ these templates are generic because the consequences of insecure defaults in
hardware description language source code are unpredictable in general. A thorough
set of security rules is required to catch all cases and these rules must use values
specified in the design specification, not what is coded in the RTL. Verifying correct
register default values is part of functional verification and can also be checked using
SVA assertions.


Security Rule Types

 - INTEGRITY_CONFIG

 - VERIFY_ACCESS_CONTROL_CONFIG


 30




##### Detection Example


The _otp_ fuses in the Hardware Root of Trust (HRoT) are readable by untrusted software
running on _core{0-N}_ in debug mode only. In non-debug mode they are not accessible
to untrusted software.


Threat Model


The default value of the register bit enabling debug mode is incorrectly set to 1 in the
RTL. Hence, allowing untrusted software to read security sensitive data in normal
operating mode.


Security Requirement


Default register values and instantiation parameters which has a security impact needs
to be verified against the values specified in the design specification.


Completing the Template Based on Design Signals and Security Requirement


From the requirement that the _otp_ fuses should not be readable follows the rule below
based on the template. The rule doesn't include the value of the debug mode bit which
means the rule will fail if debug mode is incorrectly set to"1".

### - - CWE 1223: Race Condition for Write Once Attributes

##### Description


A write-once register in hardware design is programmable by an untrusted software
component earlier than the trusted software component, resulting in a race condition
issue.


 31




##### Radix Security Rule Template





Rule Template Detail


Information should not flow from software through the _Store signals in the Load Store_
_Units (LSUs) of untrusted CPUs_ to _Write-once registers_ unless the _Write-once values_
_are set_ i.e. they are have been previously written.


Security Rule Types

 - INTEGRITY_ACCESS_CONTROL_MECHANISM

 - ISOLATE_ASSET

##### Detection Example


The _interconnect_ in the untrusted section of the SoC contains write-once registers that
define the security access policy for all masters and slaves connected to the
interconnect. The access policy registers are programmed by the _tmcu_ during secure
boot.


_Note:_ Multiple implementations of rules for this CWE are possible due to other system
requirements. Here, it doesn't say that the write-once register should not be accessible
to untrusted components, or that they shouldn't be allowed to make an attempted write.
It also doesn't say that the trusted and untrusted cores are fixed over the life of the
device.


Threat Model


If there is a race condition and the access control policy registers are programmed by
untrusted software before the trusted _tmcu_ can program them during secure boot, a less
restrictive access policy may be implemented giving a malicious actor access to security
sensitive data.


 32





Security Requirement


The write-once configuration registers should not be writable by untrusted agents unless
the write-once register is set.


Completing the Template Based on Design Signals and Security Requirement


From the security requirement we can fill out the rule template which gives the rule
below. The rule doesn't say that the access register should be writable if the
_write_once_status_ is set, only that it shouldn't fail in that case.


Verification


Using the security rules above, the Tortuga Radix tool will build a security monitor which
when simulated together with the design will flag any violation of the rules. In this
example, the rule is violated at time 1100. Viewing the violation for the first source,
Core_0, in the Radix GUI path view we see how information flows through the hierarchy
of the design from the core0 Load Store Unit to the top level to the csr instance in the
interconnect.


To understand which signals are involved in the unexpected information flow and what
values they have, we can analyze the waveform.


 33




### - - CWE 1224: Improper Restriction of Write Once Bit Fields

##### Description


The hardware design control register "sticky bits" or write-once bit fields are improperly
implemented, such that they can be reprogrammed by software.

##### Radix Security Rule Template





Rule Template Detail


Information should not flow from software through the _Store signals in the LSUs of_
_untrusted CPUs_ to the _State-carrying signals of write-once registers_ when the
_write_once_status_ is set


Security Rule Types

 - INTEGRITY_REGISTER

 - VERIFY_ACCESS_CONTROL_CONFIG


 34




##### Detection Example


The _interconnect_ in the untrusted section of the SoC above contains write-once
registers that define the security access policy for all the masters and slaves. The
access policy registers are programmed by the _tmcu_ during secure boot. Hence they
must not be re-written by any of the untrusted CPUs.


Threat Model


If the write-once registers are implemented incorrectly so that the "written once" state
depends on the data written, an attacker running un-privileged code may write one of
the write-once registers after secure boot and thus altering the security access policy
and potentially elevating its own privilege level.


Security Requirement


Write-once registers should be truly write-once and the status should not depend on the
value written only if the status bit is set.


Completing the Template Based on Design Signals and Security Requirement


From the security requirement we can fill out the rule template which gives the rule
below:


 35




### - CWE 1231: Improper Implementation of Lock Protection Registers

##### Description


The product incorrectly implements register lock bit protection features such that
protected controls can be programmed even after the lock has been set.

##### Radix Security Rule Template


Rule Template Detail


Information should not flow from software through the _Protected register data signals_ to
the _State-carrying signals of protected registers_ unless the _Protected registers are_
_unlocked._


Security Rule Types

 - INTEGRITY_ACCESS_CONTROL_MECHANISM

 - INTEGRITY_REGISTER

##### Detection Example


The SoC above contains a thermal sensor with a programmable max temperature.
Another register _tmcu.csr.temp_shutdown_ determines the action to take when the max
temperature is reached. If the register is programmed to "1", the SoC is shut down to
avoid malfunction or damage. The max temperature register and the temp_shutdown
register are protected by a lock bit. When trusted firmware sets the lock bit in
_tmcu.csr.reg_lock_ it is not possible to modify the registers. Due to a design bug, the
temp_shutdown register is not protected by the lock bit.


 36





Threat Model


Malicious software running on one of the un-trusted cores can potentially do a fault
injection attack by disabling the _tmcu.csr.temp_shutdown_ register thus allowing the
device to overheat to a point where behavior is unpredictable and security features are
no longer active.


Security Requirement


Critical registers which should not be modifiable after configuration, should be protected
by a lock mechanism.


Completing the Template Based on Design Signals and Security Requirement


From the security requirement we can fill out the rule template which gives the rule
below. Here we assume that _reg_lock == 0_ indicate that registers are unlocked and
hence writable.

### - CWE 1232: Improper Lock Behavior After Power State Transition

##### Description


Register lock bit protection disables changes to system configuration once the bit is set.
Some of the protected registers or lock bits become programmable after power state
transitions (e.g., Entry and wake from low power sleep modes) causing the system
configuration to be changeable.

##### Radix Security Rule Template


Rule Template Detail


Information should not flow from software through the _Protected register data signals_ to
the _State-carrying signals of protected registers_ unless the _Protected registers are_
_unlocked._


 37





Security Rule Types

 - INTEGRITY_ACCESS_CONTROL_MECHANISM

 - INTEGRITY_REGISTER

##### Detection Example


When the SoC above enters a hibernate power state, the memory in the _peripheral IP &_
_memory_ sub-system is powered down and loses configuration settings. In normal mode,
the configuration registers cannot be modified by the un-trusted cores _core{0-N}_ when
the _tmcu.csr.reg_lock_ bit is set. When resuming operations from hibernate mode, the
trusted processor _tmcu_ will disable the lock bit and re-configure the memory before
leaving the resume state.


Threat Model


Improper clearing of the lock bit after power state transitions enables malicious software
to modify configuration registers.


Security Requirement


Security critical device configuration registers protected by a lock bit must remain
protected when returning to operation after power state transitions.


Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rules below for the
_core0_ processor register.


 38




### - CWE 1233: Improper Hardware Lock Protection for Security Sensitive Controls

##### Description


The product implements a register lock bit protection feature that permits security
sensitive controls to modify the protected configuration.

##### Radix Security Rule Template


_Note:_ Several security rules may be written for this CWE. In addition, the user needs to
review which address ranges and memories should be protected by a lock bit
mechanism.


Rule Template Detail


Signals controllable by untrusted software or agents must not flow to _Security-critical_
_Device Configuration_ memory ranges or registers unless the lock protection mechanism
is disabled i.e. the device configuration space must not be modified by un-trusted
agents.


Security Rule Types

 - ISOLATE_SECURITY_STATE

 - VERIFY_ACCESS_CONTROL_CONFIG

##### Detection Example


The SoC contains a thermal sensor with a programmable max temperature. Another
register _tmcu.csr.temp_shutdown_ determines the action to take when the max
temperature is reached. If the register is programmed to "1", the SoC is shut down to
avoid malfunction or damage. The max temperature register and the temp_shutdown


 39





register are protected by a lock bit. When trusted firmware sets the lock bit in
_tmcu.csr.reg_lock_ it is not possible to modify the registers. Due to a design bug, the
temp_shutdown register is not protected by the lock bit. It is also assumed that the lock
bit _tmcu.csr.reg_lock_ remains set during normal operation.


Threat Model


Malicious software running on one of the un-trusted cores can potentially do a fault
injection attack by disabling the _tmcu.csr.temp_shutdown_ register thus allowing the
device to overheat to a point where behavior is unpredictable and security features are
no longer active.


Security Requirement


Critical registers which should not be modifiable after configuration, should be protected
by a lock mechanism. The lock bit should be set during normal operation, i.e. after
secure boot is done.


Completing the Template Based on Design Signals and Security Requirement


From the security requirement we can fill out the rule template which gives the rules
below. Note that the second rule will fail during boot since boot_done will be 0 and
additional qualifying signals may be required.




### - CWE 1234: Hardware Internal or Debug Modes Allow Override of Locks

##### Description

System configuration protection may be bypassed during debug mode.

##### Radix Security Rule Template


 40





Rule Template Detail


Information should not flow from un-trusted software through the _User-controllable_
_signals_ to the _Security-sensitive configuration locations_ when the lock bit is set. This rule
applies if un-trusted software is never allowed to modify the configuration registers or
memory locations when the lock bit is set regardless of other hardware internal, or
debug modes being set. If some accesses are allowed, add the _(debug mode || scan_
_mode)_ condition to check specific modes.


_Note:_ Depending on design implementation, only one of the template rules applies since
the condition when access is allowed is different.


Security Rule Types

 - INTEGRITY_ACCESS_CONTROL_MECHANISM

##### Detection Example


Trusted firmware running on the _tmcu_ configures memory in the _peripheral IP & memory_
subsystem during secure boot. The _memory.csr.configuration_ register is protected by
the _tmcu.csr.lock_bit_ which is set after configuration is done by the _tmcu_ . When the
SoC is in debug or scan mode, the lock bit for the configuration register is overridden.


Threat Model


If un-trusted software is able to control either the scan or debug mode bits it will override
the lock bit for the configuration register so that it can modify the memory configuration.


 41





Security Requirement


Depending on design intent, there are two different requirements. If overriding the lock
bit for the configuration is a design bug or oversight, then configuration should only be
writable when the lock bit is not set. If overriding the lock bit for the configuration is
intended, then no other way of writing the register should be possible.


Completing the Template Based on Design Signals and Security Requirement


From the requirements, we can fill in the template which gives the rules below for the
two cases:

### - CWE 1240: Use of a Risky Cryptographic Primitive

##### Description


This device implements a cryptographic algorithm using a non-standard or unproven
cryptographic primitive.

##### Radix Security Rule Template


Radix currently does not cover this CWE, refer to the MITRE website for suggested
mitigations.


 42




### - CWE 1241: Use of Predictable Algorithm in Random Number Generator

##### Description


The device uses an algorithm that is predictable and generates a pseudo-random
number.

##### Radix Security Rule Template


Radix currently does not cover this CWE, refer to the MITRE website for suggested
mitigations.

### - CWE 1242: Inclusion of Undocumented Features or Chicken Bits

##### Description


The device includes chicken bits or undocumented features that can create entry points
for unauthorized actors.

##### Radix Security Rule Template


_Note:_ Chicken bits should be permanently disabled in production devices or adequate
protection should ensure they are not controllable by users. Designers need to
document the address range for accessing chicken bits in internal documentation.
Depending on system requirements, the chicken bits may or may not be readable
registers. If they are readable, additional rules may be required if read access to the bits
is restricted.


Rule Template Detail


The Radix Security Rules checks that information doesn't flow from _User-accessible_
_signals_ to _Chicken bits in registers or memory._ That is, un-authorized software or agents
can't control the chicken bits.


Security Rule Types

 - CONFIDENTIALITY_ASSET

 - INTEGRITY_ASSET


 43




##### Detection Example


The SoC design contains chicken bits in a range of memory in the _tmcu.csr._ These bits
must not be controllable in a production device by un-authorized users. Only trusted
software running on the _tmcu_ may write to chicken bits.


Threat Model


Un-trusted agents being able to control chicken bits may enable features that violate
security access policy thus giving the un-trusted agent access to privileged data.


Security Requirement


Chicken bits should not be controllable in a production device unless done by a trusted
agent.


Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rule below. The values
for _CHICKEN_END_ and _CHICKEN_START_ are constants provided by the user.


_Note:_ Chicken bits must be documented in internal specifications to enable verification
and hidden in external documentation.

### - - CWE 1243: Sensitive Non Volatile Information Not Protected During Debug

##### Description


Access to security-sensitive information stored in fuses is not limited during debug.


 44




##### Radix Security Rule Template





Rule Template Detail


Information in blown fuses or ROM, _Security-sensitive Fuse Values,_ should not flow to
_User-accessible signals_ such as an untrusted debugger when the device is in debug
mode.


Security Rule Types

 - ISOLATE_REGISTER

##### Detection Example


Security sensitive information is stored in blown fuses in the _otp_ block and in a section
of the _rom.mem._ During normal operation mode, access control methods prevent untrusted system components from reading this data.


Threat Model


Data in _rom.mem_ and _otp_ fuses may be visible through the debug interface when the
device is in debug mode and normal access control may not be set up. This would give
access to sensitive data through an untrusted debugger.


Security Requirement


Data in _rom_ and _otp_ must not be readable through the debug interface


Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rule below. The values
for _FUSED_END_ and _FUSED_START_ are constants provided by the user.


 45





Verification


If the security rule from OTP is violated when simulating the design, the violation is
debugged in the Radix GUI. In this example, the rule is violated at time 2900ns. Viewing
the violation in the Radix GUI path view we see how information flows through the
hierarchy of the design from the otp instance through the tbus interconnect to the
dbg_data_o output in the debug instance.


To understand which signals are involved in the unexpected information flow and what
values they have, we can analyze the waveform.

### - CWE 1244: Improper Access to Sensitive Information Using Debug and Test Interfaces

##### Description


The product's physical debug and test interface protection does not block untrusted
agents, resulting in unauthorized access to and potentially control of sensitive assets.


 46




##### Radix Security Rule Template





Rule Template Detail


Information should not flow from/to the _Security-critical signals_ to/from the _User-_
_accessible debug interface_ unless the debug interface access has been property
authenticated.


Security Rule Types

 - INTEGRITY_ACCESS_CONTROL_MECHANISM

 - VERIFY_ACCESS_CONTROL_CONFIG

##### Detection Example


A debugger connected to the debug interface needs to provide a correct response to a
challenge in order to access internal registers of the Hypothetical SoC, for example
registers in the _tmcu_ . If the authorization is successful, the _debug.authentication_
register is set to "1".


 47





Threat Model


The challenge response authorization is not applying to all debug accesses thus giving
an attacker access to some security sensitive registers.


Security Requirement


There should be no read or write access to security sensitive registers unless the debug
agent has been properly authenticated.


Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rules below:

### - CWE 1245: Improper Finite State Machines (FSMs) in Hardware Logic

##### Description


Faulty finite state machines (FSMs) in the hardware logic allow an attacker to put the
system in an undefined state, to cause a denial of service (DoS) or gain privileges on
the victim's system.

##### Radix Security Rule Template


 48





Rule Template Detail


Critical Finite State Machines in the design should not be able to enter undefined states
where the behavior is undefined. The Radix Security Rule ensures the _FSM next state_
variable does not flow to the _FSM current state_ variable unless the Next State is a valid

state.


Security Rule Types

 - INTEGRITY_FSM_STATES

##### Detection Example


The _aes.csr_ FSM determines read, write or read/write access permissions for registers
in the _aes_ module based on source security ID of the initiator of the accesss. The FSM
have 4 valid states: IDLE, RD, WR and RDWR. The state is one-hot encoded with 4
state bits for performance reasons which means there are many possible undefined
states.


Threat Model


An attacker may cause the FSM into an undefined state where access permissions are
not enforced, allowing access to security sensitive registers.


Security Requirement


Security sensitive FSMs should not be able to enter undefined states.


Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rule below:


 49




### - - - CWE 1246: Improper Write Handling in Limited write Non Volatile Memories

##### Description


The product does not implement or incorrectly implements wear leveling operations in
limited-write non-volatile memories.

##### Radix Security Rule Template


_Note:_ Functional verification should ensure that write leveling is implemented correctly
as this is part of the device's defined functionality. However, Radix Security Rules can
also be used since violations have security implications.


Rule Template Detail


_Store data_ from an un-secure processor must not flow to a _limited-write Non-volatile_
_memory location_ if the maximum number of write for that location has been reached. A
trusted processor may be allowed to write anyway depending on system design.


Security Rule Types

 - INTEGRITY_FSM_STATES

##### Detection Example


The _nvm_ flash memory implements write leveling to prevent premature failures of the
memory. The _nvm_ has a register that defines the maximum number of writes per
location. This register is only readable and writable by the secure _tmcu_ processor.


 50





Threat Model


A malicious actor may be able to bypass the write leveling logic and perform a large
number of writes to the same location thus making part of the flash unreliable. This may
lead to undefined states in the system where security policies are not enforced or may
enable a denial-of-service attack.


Security Requirement


Non-volatile memory locations should not be writable by un-trusted agents when the
maximum number of writes for the location has been reached.


Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rule below:

### - CWE 1247: Missing or Improperly Implemented Protection Against Voltage and Clock Glitches

##### Description


The device does not contain or contains improperly implemented circuitry or sensors to
detect and mitigate voltage and clock glitches and protect sensitive information or
software contained on the device.

##### Radix Security Rule Template


Radix currently does not cover this CWE, refer to the MITRE website for suggested
mitigations.

### - CWE 1248: Semiconductor Defects in Hardware Logic with - Security Sensitive Implications

##### Description


The security-sensitive hardware module contains semiconductor defects.


 51




##### Radix Security Rule Template


Radix currently does not cover this CWE, refer to the MITRE website for suggested
mitigations.

### - CWE 1251: Mirrored Regions with Different Values

##### Description


The product's architecture mirrors regions without ensuring that their contents always
stay in sync.

##### Radix Security Rule Template


_Note:_ This CWE overlaps with the functional requirement to keep two resources in sync
and this should be addressed in the functional verification plan. Radix Security Rules
can be used to ensure no illegal data access when resources are not in sync as this has
security implications.


Assuring that, for example, data in a cache location is equal to data in memory can be
done using functional assertions such as:


assert (@ posedge clk) (update not in progress) => (core0.dcache[flush_dst]
== nvm.mem[flush_dst]);


Rule Template Detail


Data in a duplicated resource must not flow to a location that is user accessible while an
update of the resource controlling the data is in progress.


Security Rule Types

 - INTEGRITY_FSM_STATES

 - INTEGRITY_MEMORY_REGION

 - VERIFY_MEMORY_REGION


 52




##### Detection Example


There are 3 processors in the SoC design example, core0, core1 & core2, running user
code. For performance reasons, there is one main Memory Management Unit (MMU)
and one shadow MMUs. The main MMU handles memory accesses by core0 and the
shadow MMU handles memory accesses from _core1_ & _core2._ Updates to the main
MMU is done by the _tmcu_ and then the main MMU updates the shadow MMU through
messages on the interconnect. If the accessible address range for the untrusted cores
is updated in the main MMU, there is a time when the three processors may have
access to different memory ranges.


Threat Model


A malicious agent running on _core2_ may be able to access memory locations outside its
allowed range because the shadow MMU does not yet have the same configuration as
the main MMU. If _core2_ can flood the interconnect with traffic and delay the update
request, the update to the shadow MMU may be delayed, extending the time available
for access.


Security Requirement


No access to memory through the shadow MMU should be allowed while an update is
in progress.


Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rules below:


 53




### - CWE 1252: CPU Hardware Not Configured to Support Exclusivity of Write and Execute Operations

##### Description


The CPU is not configured to provide hardware support for exclusivity of write and
execute operations on memory. This allows an attacker to execute data from all of

memory.

##### Radix Security Rule Template


Rule Template Detail


A processor must not be able to write data in instruction memory and it should only be
able to read instructions from instruction memory. _Store data_ in the Load Store Unit
(LSU) should not flow to memory location in the instruction address range and data in
Memory should not flow to _instruction fetch unit_ in the CPU if the address is outside the
address range for instruction memory.


Security Rule Types

 - INTEGRITY_FSM_STATES

 - ISOLATE_MEMORY_REGION


 54




##### Detection Example


In this example, the _tmcu_ doesn't have support for write exclusivity and the SoC doesn't
have an Memory Protection Unit (MPU) or Memory Management Unit (MMU) to isolate
memory regions as execute only. Hence, the _tmcu_ load store unit can write to the entire
_sram.mem_ memory and the instruction fetch unit can execute code in the entire
_sram.mem_ as well.


Threat Model


An attacker can write malicious code to memory and later execute the code.


Security Requirement


If the processor lacks support for write exclusivity, other logic must implement this
functionality to prevent writes to instruction memory and instruction fetch from outside
instruction memory.


Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rules below. The
address range in _sram_ used for instruction memory is defined in the
_tmcu.mpu.imem_start_addr_ and _tmcu.mpu.imem_end_addr_ .


 55




### - CWE 1253: Incorrect Selection of Fuse Values

##### Description


The logic level used to set a system to a secure state relies on a fuse being unblown.
An attacker can set the system to an insecure state merely by blowing the fuse.

##### Radix Security Rule Template


Rule Template Detail


A fuse having its blown value and the corresponding security feature being enabled
should always hold true. The requirement in this CWE should also be verified during
functional verification. The Radix security rule could also be written as a System Verilog
Assertion since the condition should always hold true.


Security Rule Types

 - VERIFY_ACCESS_CONTROL_CONFIG

 - VERIFY_ASSET

##### Detection Example


The control word defined by the fuses in _otp_ determine what security related features
are enabled in the chip following manufacturing. For example, scan mode is
permanently disabled after manufacturing test by blowing the corresponding fuse (the
value 1 represents a blown fuse) e.g. bit [0] in otp.fuses.


 56





Threat Model


If disabling scan mode incorrectly corresponded to fuse value == 0, an attacker could
blow the fuse and thus enable scan mode and get access to every register in the design
through the JTAG port.


Security Requirement


A blown one time programmable fuse should always correspond to the most secure,
restrictive operating mode of the device


Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rule below.

### - CWE 1254: Incorrect Comparison Logic Granularity

##### Description


The product's comparison logic is performed over a series of steps rather than across
the entire string in one operation. If there is a comparison logic failure on one of these
steps, the operation may be vulnerable to a timing attack that can result in the
interception of the process for nefarious purposes.

##### Radix Security Rule Template


Rule Template Detail


The result of a comparison operation must not be visible to an untrusted agent at
different latency if the comparison may take a different amount of time to complete
depending on the result of the compare.


_Note:_ Radix security rules don't support timing in the rule itself, however, a signal can be
created in the testbench and bound to the design and then used in the security rule.


Security Rule Types

 - INTEGRITY_ASSET


 57





 - INTEGRITY_FSM_STATES

 - ISOLATE_MEMORY_REGION

##### Detection Example


The debug unit checks a user-provided password to grant access to a user. The
password is 64 bits but the comparison logic is implemented using an 8 bit comparator,
checking each byte of the password on consecutive clock cycles. If the password
compare fails in the first byte, the fail status signal is asserted and access is denied. If
all 8 compares pass, access is granted.


Threat Model


By measuring the time between request and the fail indication, the timing side channel
leaks information about which byte of the password does not match. If you know which
byte fails, it is easy to guess the correct password.


Security Requirement


The compare function should indicate pass / fail after the same amount of time
regardless if the fail happened before the last byte.


Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rule below. The signal
_debug.check_wait_ is created in the testbench and is asserted for 8 cycles while the
compare is in progress. It is bound to the debug instance. The amount of time required
to complete the comparison is design dependent and 8 cycles is just used as an
example.


 58




### - - CWE 1255: Comparison Logic is Vulnerable to Power Side Channel Attacks

##### Description


A device's real time power consumption may be monitored during security token
evaluation and the information gleaned may be used to determine the value of the
reference token.

##### Radix Security Rule Template


Radix currently does not cover this CWE, refer to the MITRE website for suggested
mitigations.

### - CWE 1256: Hardware Features Enable Physical Attacks from Software

##### Description


Software-controllable device functionality such as power and clock management
permits unauthorized modification of memory or register bits.

##### Radix Security Rule Template


Rule Template Detail


Information in the _Asset_ which control physical parameters on chip must be prevented
from being written with data from _user-accessible signals_ unless the _permission bits_ are
correctly set to the _value indicating asset should be writable._


Security Rule Types

 - INTEGRITY_ACCESS_CONTROL_CONFIG

 - INTEGRITY_ASSET

 - VERIFY_ACCESS_CONTROL_CONFIG


 59




##### Detection Example


Security-critical settings for scaling clock frequency and voltage are available in a range
of registers bounded by _[PRIV_END_ADDR : PRIV_START_ADDR]_ in the _tmcu.csr_
module in the HW Root of Trust. These values are writable based on the _lock_bit_
register in the same module. The _lock_bit_ is only writable by privileged software running
on the _tmcu._


Threat Model


We assume that untrusted software running on any of the _Core{0-N}_ processors, (the
threat) has access to the input and output ports of the _hrot_iface._ If untrusted software
can clear the _lock_bit_ or write the clock frequency and voltage registers due to
inadequate protection, a fault injection attack could be performed.


Security Requirement


Information in the address range [ _PRIV_END_ADDR:PRIV_START_ADDR_ ] must not
be writable via _hrot_iface_ unless _tmcu.csr.lock_bit_ is zero. The _tmcu.csr.lock_ bit must
never be writable from the _hrot_iface_ interface.


Completing the Template Based on Design Signals and Security Requirement


Based on the security goal we fill in the template which gives the two rules below. The
values for _PRIV_END_ADDR_ and _PRIV_START_ADDR_ are constants provided by the

user.


 60




### - CWE 1257: Improper Access Control Applied to Mirrored or Aliased Memory Regions

##### Description


Aliased or mirrored memory regions in hardware designs may have inconsistent
read/write permissions enforced by the hardware. A possible result is that an untrusted
agent is blocked from accessing a memory region but is not blocked from accessing the
corresponding aliased memory region.

##### Radix Security Rule Template





Rule Template Detail


Security sensitive memory mapped registers or memory areas must not flow to signals
readable by untrusted agents even if an aliased address is used.


Security Rule Types

 - INTEGRITY_ACCESS_CONTROL_MECHANISM

 - VERIFY_ACCESS_CONTROL_CONFIG

##### Detection Example


ROM in the SoC is 64k and it is mapped to address _0x08000000 - 0x0800FFFF_ . The
ROM is security sensitive and is only readable by the _tmcu_ . In order to simplify the
address decoding logic, the ROM only decodes the lower 16 address bits and relies on
the Memory Protection Unit (MPU) to enforce access control.


 61





Threat Model


One of the untrusted cores, _core{0-N}_ has read permission from address 0x0400beef.
Due to improper access control, the ROM decodes the address as 0xbeef and responds
to the read request even though the un-trusted core should not have access to address
_0x0800_0000_ and above.


Security Requirement


No location in ROM should flow to untrusted agents in the system even if the address at
the ROM is in the correct range due to memory aliasing.


Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rule:


_Note:_ The "when" condition in the rule is not needed if the untrusted core is not allowed
to read any data in _rom._

### - CWE 1258: Exposure of Sensitive System Information Due to Uncleared Debug Information

##### Description


The hardware does not fully clear security-sensitive values, such as keys and
intermediate values in cryptographic operations, when debug mode is entered.

##### Radix Security Rule Template









 62





Rule Template Detail


Security sensitive registers must be cleared when a clear request signal is asserted,
and their contents must not flow to other locations until the contents has been cleared.


Security Rule Types

 - INTEGRITY_FSM_STATES

 - VERIFY_SECURITY_STATE

##### Detection Example


Keys for AES are stored in internal registers _aes.csr.key_ . These registers are blocked
for access by software and other untrusted agents of the SoC. When the design is in
debug mode, all registers are accessible through the debug interface. To avoid keys
being accessible to unauthorized users, they will be cleared when entering debug
mode. The register clear request signal in the template is generated from the debug
mode signal in the tmcu. A register in _AES_ indicate that the value is zero.


Threat Model


If the aes key register is not cleared when entering debug mode, an untrusted debugger
can gain access to the keys.


Security Requirement


The aes key register and other sensitive registers should be cleared when entering
debug mode.


Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rule for the aes key
register. The _tmcu.clear_request_ signal is asserted when the _tmcu_ enables debug mode
and de-asserted on completion of clearing the register.


 63




### - CWE 1259: Improper Restriction of Security Token Assignment

##### Description


The System-On-A-Chip (SoC) implements a Security Token mechanism to differentiate
what actions are allowed or disallowed when a transaction originates from an entity.
However, the Security Tokens are improperly protected.

##### Radix Security Rule Template


Rule Template Detail


Security sensitive registers must not be changed unless a write is done by a secure
processor or they are set to reset values during chip reset.


Security Rule Types

 - CONFIDENTIALITY_SECURITY_STATE

 - INTEGRITY_SECURITY_STATE

##### Detection Example


Access to secret registers such as AES key registers is configured in access-policy
registers and is determined based on security identifiers. Each agent in the SoC have a


 64





Security identifier register which is programmed to a unique value by the tmcu during
secure boot.


Threat Model


If one of the untrusted cores, _core{0-N}_ can change its own or another agent's security
identifier, the access policy will allow access to registers that would otherwise be
protected from this agent.


Security Requirement


The Security Identifier for an agent should not change unless it is programmed by the
_tmcu_ or it is cleared during reset.


Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rules below for the
_core0_ processor register.


_Note:_ Additional security rules for each unsecure master is required.

### - CWE 1260: Improper Handling of Overlap Between Protected Memory Ranges

##### Description


The product allows address regions to overlap, which can result in the bypassing of
intended memory protection.

##### Radix Security Rule Template


 65





Rule Template Detail


Data in a privileged address range in a shared memory _(Privileged data signals)_ must
not influence _signals readable by untrusted agents_ This should always hold true even if
the non-privileged address range overlap the privileged address range. Additionally, the
privileged address range in shared memory must not be able to be influenced by _signals_
_writable by untrusted agents._


Security Rule Types

 - ISOLATE_DATA

 - ISOLATE_MEMORY_REGION

##### Detection Example


The Hardware Root of Trust (HRoT) local _sram_ is memory mapped in the _core{0-N}_
address space and is also accessible to the _tmcu_ . The address range for privileged
memory space is defined in _tmcu.csr_ registers. It is only readable and writable by
privileged software. The un-trusted cores, _core{0-N}_ can define an unprivileged area in
memory where they have read and write access.


Threat Model


In this example, we assume that the threat is from malicious software in the untrusted
domain. We assume this software has access to the _core{0-N}_ un-privileged memory
map and can also change the location of its un-privileged area. If the software running
in the untrusted domain can program the un-privileged memory area to overlap with the
privileged memory area, this would allow the malicious software to read and write
privileged memory.


 66





Security Requirement


Data in the privileged area of memory must not flow to the _hrot_iface_ and data on the
_hrot_iface_ must not flow to the privileged area of memory regardless of how the nonprivileged address space is programmed


Completing the Template Based on Design Signals and Security Requirement


From the requirement, the privileged memory should not be read or write accessible.
The privileged range in the SRAM model is bounded by _PRIV_START_ADDR_ and
_PRIV_END_ADDR._ The values for _PRIV_END_ADDR_ and _PRIV_START_ADDR_ are
constants provided by the user. Filling in the template gives the rule below.




### - CWE 1261: Improper Handling of Single Event Upsets

##### Description

The hardware logic does not effectively handle when single-event upsets (SEUs) occur.

##### Radix Security Rule Template


 67





Rule Template Detail


Security sensitive information should not flow to _signals readable by untrusted agents_
when the circuit is in an error state caused by a Single Event Upset. Additionally,
security sensitive data must not be able to be influenced by _signals writable by_
_untrusted agents_ when the circuit is in an error state caused by a Single Event Upset.


Security Rule Types

 - CONFIDENTIALITY_ASSET

 - INTEGRITY_ASSET

 - ISOLATE_ASSET

##### Detection Example


The SoC above has logic to detect errors, e.g. parity on memory data or duplicated logic
running in lock-step, to detect Single Event Upset (SEU) faults. When an SEU fault is
detected, an error bit is set in CSR and software on _tmcu_ tries to recover back to normal
operation. During this error state, secure data for example in the SRAM must not be
overwritten or be visible to un-trusted cores or on the debug interface.


Threat Model


In this example, we assume that the threat is from a malicious user either relying on a
random event or intentional fault insertion to bring the design into an error state where
normal security policies may no longer apply. If malicious software running in the
untrusted domain is able to bypass the security policy, this would allow the malicious
user to read and write privileged memory. If the malicious user has physical access to
the chip, he can try to access secure data through the debug interface which may no
longer be protected in an error scenario.


Security Requirement


Data in the sram memory must not flow to the debug module and data from the debug
module must not flow to the memory when an SEU is detected


 68





Completing the Template Based on Design Signals and Security Requirement


From the requirement, the _sram_ memory should not be read or write accessible from the
debug module when the SEU error bit is set. The SEU may affect the SRAM address so
it is safer to check the entire memory. Filling in the template gives the rule below.

### - CWE 1262: Register Interface Allows Software Access to Sensitive Data or Security Settings

##### Description


Memory-mapped registers provide access to hardware functionality from software and if
not properly secured can result in loss of confidentiality and integrity.

##### Radix Security Rule Template


_Note:_ Due to breadth of access control policies for different memory mapped registers,
there are many rule variations to detect disallowed accesses by software.


 69





Rule Template Detail


Sensitive data should not flow to _signals readable by untrusted agents_ unless a
"permitted condition" is true. Additionally, sensitive data must not be able to be
influenced by _signals writable by untrusted agents_ .


Security Rule Types

 - ISOLATE_DATA

 - ISOLATE_REGISTER

##### Detection Example


Assume that the registers in the HRoT aes core are memory mapped in the _core{0-N}_
address space. All the aes core memory mapped registers have an access control
policy specifying read or write access and access by _tmcu_ or _core{0-N}_ . For example,
the aes.reg.key register is only readable and writable by _tmcu_, the _aes.reg.data_in_
register is writable but not readable by _core{0-N}_ and the _aes.reg.data_out_ register is
only readable when the _aes.done_ bit is set.


Threat Model


In this example, we assume that the threat is from malicious software running on one of
the untrusted processors. It will attempt to read and write all memory mapped registers
in the aes address space hoping the access control policy is insufficient. If any access
succeeds, information about the key may be obtained.


Security Requirement


Only the _aes.reg.data_in_ register is writable by _core{0-N}_ and only the _aes.reg.data_out_
register is readable by _core{0-N}_ when encryption is done. The _aes.data_out_ register is
never writable and the _aes.data_in_ register is never readable by _core{0-N)._


Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rules below for the
_data_out_ register. Similarly, rules are required for the _data_in_ register.


 70




### - CWE 1263: Improper Physical Access Control

##### Description


The product is to be designed with access restricted to certain information, but it does
not sufficiently protect against an unauthorized actor's ability to access these areas.

##### Radix Security Rule Template


Rule Template Detail


Information from/to _Physically user-accessible signals_ must not flow to/from _Restricted_
_signals_ if the physical access protection has been violated. Verification of the physical
protection in the manufactured device is beyond the scope of functional verification but
Radix rules can stil be used to ensure correct behavior when the physial protection
detects a violation.


Security Rule Types

 - CONFIDENTIALITY_ASSET


 71





 - INTEGRITY_ASSET

 - ISOLATE_ASSET

##### Detection Example


The SoC has an anti-tamper detection circuit to detect if the device is de-capped. If the
device is de-capped then the memories will be zeroized so no information will be leaked
to an attacker. The processors will also halt to avoid leaking any information.


Threat Model


An attacker may decap the device and probe internal signals to access sensitive data in
memories or registers or observe the program running on the embedded processors.


Security Requirement


When physical tampering is detected e.g. when someone is de-capping the device, the
processors should stop and memories should be cleared i.e. zeroized to avoid sensitive
data leakage.


Completing the Template Based on Design Signals and Security Requirement


Based on the requirements we can write rules that ensure the memories are properly
scrubbed and that the processors don't fetch any data or instructions from memory.
_Note:_ additional rules are needed to check all memories and information flow to all

processors.


 72




### - - CWE 1264: Hardware Logic with Insecure De Synchronization between Control and Data Channels

##### Description


The hardware logic for error handling and security checks can incorrectly forward data
before the security check is complete.

##### Radix Security Rule Template


Rule Template Detail


Privileged data shall not flow to the cache if the requestor doesn't have permission to
access data or permission check is not completed.


Security Rule Types

 - CONFIDENTIALITY_ASSET

 - INTEGRITY_ASSET

 - ISOLATE_ASSET

##### Detection Example


The _tmcu_ and _core{0-N}_ processors are interconnected through AXI. The security policy
(bus firewall) is implemented in an IP block separate from the data routing interconnect.


 73





The Hardware Root of Trust (HRoT) processor, _tmcu_ should not be able to share data
with the untrusted _core{0-N}_ processors and the bus firewall prevents the untrusted
processors from accessing for example rom data in the HRoT.


Threat Model


If the firewall logic becomes de-synchronized with the data routing an untrusted
processor may be able to read privileged data before the security policy is ready and
enforced


Security Requirement


All privileged data is buffered or blocked by the interconnect until it has determined that
the requestor has permission to access the data


Completing the Template Based on Design Signals and Security Requirement


Based on the security goal we fill in the template which gives the rule below.




### - CWE 1266: Improper Scrubbing of Sensitive Data from Decommissioned Device

##### Description

The product does not properly provide a capability for the product administrator to
remove sensitive data at the time the product is decommissioned. A scrubbing
capability could be missing, insufficient, or incorrect.

##### Radix Security Rule Template


Note: Radix Security Rules do not apply to post-RTL verification. Please implement
policies to scrub sensitive data when product in use. Security rules may be written to
verify scrubbing implementations in RTL or software during the design phase.


 74





Rule Template Detail


Sensitive data to be scrubbed should not flow to the same location when scrubbing has
started and is done i.e. sensitive data values are cleared.


Security Rule Types

 - CONFIDENTIALITY_ASSET

 - VERIFY_SECURITY_STATE

##### Detection Example


The _aes.csr.key_ register contains sensitive information that needs to be removed after
use. This is done by HW setting the key to all zero. The operation is started by the tmcu
writing "1" to the _aes.csr.data_clear_ register. The _aes.csr.clear_done_ bit is set to "1"
when the clear operation is done. The tmcu will then clear the _aes.csr.data_clear_ bit to
complete the operation.


Threat Model


If the clear is not successful, bits of the key may remain that could leak to unauthorized
locations.


Security Requirement


No information should flow from the key register prior to clearing back to the key register
when clearing is done.


Completing the Template Based on Design Signals and Security Requirement


Based on the security goal we fill in the template which gives the rule below. This rule
only checks for leakage of the key after the clearing is completed so it will fail if the
clearing of the key was not successful.


 75




### - CWE 1267: Policy Uses Obsolete Encoding

##### Description


The product uses an obsolete encoding mechanism to implement access controls.

##### Radix Security Rule Template


Rule Template Detail


Information from/to _Asset-carrying signals in trusted IP_ must not flow to/from
_Inputs/Outputs of untrusted IP._ Or, Information from/to _Asset-carrying signals in trusted_
_IP_ must not flow to/from _Inputs/Outputs of untrusted IP unless it is allowed by up to
date access policy.


_Note:_ Depending on which case is chosen, this form of rule handles obsolete policy
encodings implicitly by detecting flows of information that may be caused by incorrect
policies. Using the unless condition may reduce the number of false violations but the
condition must be based on up to date system documentation to ensure correctness.


Security Rule Types

 - CONFIDENTIALITY_ASSET

 - INTEGRITY_ASSET

 - ISOLATE_ASSET


 76




##### Detection Example


The access control block in the hrot_iface is being re-used from another design. It is
using security tokens to identify the source of the transaction and determine if the
access is allowed. The old design only had 2 masters in the untrusted area so only 1 bit
was used for the security token. The new SoC has additional masters and the size of
the security token is now 4 bits. However, the reused access control is not updated. For
example, Core0 is allowed to access the ROM in HRoT but the newly added Core1 is
not. The security token for Core0 is 4'b0000 and for Core1 it is 4'b1010 but access
control only considers bit [0] so they incorrectly have the same access privilege. The
DMA previously was not allowed to write SRAM indicated by bit [0] being 1 but it is now
allowed.


Threat Model


The obsolete access policy may allow an untrusted agent access to secure information.


Security Requirement


Access policy enforcement must use up to date policy settings and implementations.


Completing the Template Based on Design Signals and Security Requirement


Based on the security goal we fill in the template from the example signals, obtaining
the rule below. The first rule doesn't need a condition because ROM data is never
allowed by be read by Core1. The second rule will fail because access control only
allows the access when bit [0] is 0 even though it should be allowed.


 77




### - CWE 1268: Policy Privileges are not Assigned Consistently Between Control and Data Agents

##### Description


The product's hardware-enforced access control for a particular resource improperly
accounts for privilege discrepancies between control and write policies.

##### Radix Security Rule Template


Rule Template Detail


_Note:_ Several Security Rules may be required to check for this CWE since it may be
caused by incorrect software or incorrect hardware. Untrusted software through _User-_
_accessible signals_ should not flow to any of the critical configuration registers. Sensitive
signals, e.g. register values should not flow to _User-accessible signals_ . These rules will
flag any confidentiality and integrity violation on the specified signals which may be
stricter than the intended access policy. Please review the system design
documentation and add exceptions to rules as required.


Security Rule Types

 - CONFIDENTIALITY_ASSET

 - INTEGRITY_ASSET

 - ISOLATE_ASSET


 78




##### Detection Example


All the registers in the _aes_ block are protected by different access policies. For example,
the _aes.csr.key_ register is readable and writable by the _tmcu_ only. The _aes.csr.status_
register is readable by a specific master when the _aes.csr.control_ registers is enabled
for that specific master.


Threat Model


A less privileged access policy may override a higher privileged access policy due to
incorrect implementation thus allowing access for an untrusted agent to privileged data.


Security Requirement


Sensitive access controlled signals should adhere to intended access control policy as
defined in design specification.


Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rules below for the
_aes.csr.control_ register. Verify information flow assuming no access for untrusted
agents and update rules based on design specification if incorrect violations are seen.


 79




### - - CWE 1269: Product Released in Non Release Configuration

##### Description


The product released to market is released in pre-production or manufacturing
configuration.

##### Radix Security Rule Template


_Note:_ Radix detects pre-silicon vulnerabilities, however, we consider errors in the
process (such as faulty scripts to be run by the OEM) that would result in release of
devices in an insecure configuration to be covered under this CWE. Radix can be used
to verify that asset protection is implemented correctly with respect to manufacturing
status.









Rule Template Detail


Information from/to _Asset_ must not flow to/from _User-visible signals_ unless
_Manufacturing is not complete._


Security Rule Types

 - CONFIDENTIALITY_ASSET

 - INTEGRITY_ASSET

 - ISOLATE_ASSET


 80




##### Detection Example


The SoC has status registers that aid in debug and development that should not be
readable after the device is manufactured. For example, the _tmcu.csr.info_ register
should not be readable by any agent after manufacturing. After manufacturing, the fuse
_otp.manufacturing_done_ is blown, i.e. set to 1 to indicate that manufacturing is done. A
separate post-manufacturing verification step ensuring the fuse is blown is required.


Threat Model


An untrusted agent is able to read status registers that contain sensitive information in
the manufactured device


Security Requirement


Status registers containing sensitive information should not be readable when the
manufacturing done fuse is blown.


Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rule below.


_Note:_ All registers that should not be readable post manufacturing needs to be listed as
source in one or many Radix rules.


 81




### - CWE 1270: Generation of Incorrect Security Tokens

##### Description


The product implements a Security Token mechanism to differentiate what actions are
allowed or disallowed when a transaction originates from an entity. However, the
Security Tokens generated in the system are incorrect.

##### Radix Security Rule Template


_Note:_ Radix security rules can be written to ensure that the access policy is followed
and that an agent cannot change its own security identifier. See security rule example
for CWE-1259.


Rule Template Detail


Any access policy register should be set to 0 after system boot i.e. no access to any
protected resources. This is likely more restrictive than intended but will report incorrect
settings by software. The user should review the design specification and update the
rule accordingly.


Security Rule Types

 - ISOLATE_ACCESS_CONTROL_MECHANISM

 - VERIFY_ACCESS_CONTROL_CONFIG

##### Detection Example


Access to secret registers such as AES key registers is configured in access-policy
registers and is determined based on security identifiers. Each agent in the SoC has a
Security identifier register which is programmed to a unique value by the _tmcu_ during
secure boot.


 82





Threat Model


If the security identifiers are programmed incorrectly an untrusted agent may get access
to sensitive data.


Security Requirement


All security identifies should be programmed to unique values reflecting the access
privilege level specified in the design specification for each agent.


Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rule below for the
_core0_ processor.The actual value expected in the Core0.CSR.access_policy register
should be obtained from the design specification. The rule will fail if the boot process is
simulated since boot_done will be 0 so additional qualifying signals may be required.


_Note:_ This security rule needs to be created for each unsecure bus master in the SoC.

### - CWE 1271: Uninitialized Value on Reset for Registers Holding Security Settings

##### Description


Security-critical logic is not set to a known value on reset.

##### Radix Security Rule Template


_Note:_ This CWE is more effectively checked by a RTL lint tool as it doesn't require
specifying each register to check, instead all uninitialized registers are reported.
Checking unknown values in specific registers may be done in SVA or Radix Security
Rules.


Rule Template Detail


Security critical control registers should not have unknown values after the device is
reset.


 83





Security Rule Types

 - VERIFY_REGISTER

 - VERIFY_SECURITY_STATE

##### Detection Example


The flip flop implementing the _debug.csr.enable_ register is not connected to reset.


Threat Model


The debug.csr.enable bit is unknown after reset. In the real chip, it will randomly take
the value 0 or 1 meaning the chip may be in debug mode after reset. An attacker can
repeatedly reset the chip until debug mode is enabled.


Security Requirement


All security critical control registers should be set to a known value during reset.


Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rule below assuming
that reset is active high.

### - CWE 1272: Sensitive Information Uncleared Before Debug/Power State Transition

##### Description


Sensitive information may leak as a result of a debug or power state transition when
information access restrictions change as a result of the transition.


 84




##### Radix Security Rule Template





Rule Template Detail


Security critical signals should not flow to _User-accessible signals_ e.g. read by software,
unless the device is operating in a privileged operating mode. If the operating mode is
changed to "user mode" or "low power mode" the security critical signals should not be
accessible.


Security Rule Types

 - CONFIDENTIALITY_ASSET

 - ISOLATE_ASSET

##### Detection Example


When running in privileged mode, the _dma_ will copy security sensitive data from
_otp.data_ to registers in the _aes._ However, it first copies data from _otp_ to _sram_ and then
from _sram_ to _aes_ registers. When the device transitions from privileged mode to "user
mode" or "low power mode" the data that was moved must not flow outside the
Hardware Root of Trust (HRoT).


Threat Model


When the device transition from one mode to another, sensitive data may remain in
registers or memory locations that are readable by un-trusted agents in the new mode
and thus leak sensitive data


Security Requirement


Security sensitive data accessed in one operating mode must not be accessible when
transitioning to another operating mode.


 85





Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rule below.

### - CWE 1273: Device Unlock Credential Sharing

##### Description


The credentials necessary for unlocking a device are shared across multiple parties and
may expose sensitive information.

##### Radix Security Rule Template


Radix currently does not cover this CWE, refer to the MITRE website for suggested
mitigations.

### - CWE 1274: Insufficient Protections on the Volatile Memory Containing Boot Code

##### Description


The protections on the product's non-volatile memory containing boot code are
insufficient to prevent the bypassing of secure boot or the execution of an untrusted,
boot code chosen by an adversary.

##### Radix Security Rule Template


 86





Rule Template Detail


For confidentiality, information must not flow from the boot code storage location
_(Signals storing boot code)_ to _User-accessible signals._ For integrity, information from
_User-accessible signals_ must not flow to _Signals carrying boot code_ from _User-_
_accessible signals_ unless _Boot is complete._


Note: confidentiality and integrity rules are subtly different. For confidentiality, the
storage signals (typically an RTL model of a boot ROM) are the source. This differs from
the integrity targets, which are the many signals carrying boot code that might be
interfered with prior to full boot.


Security Rule Types

 - INTEGRITY_FSM_STATES

 - ISOLATE_ASSET

##### Detection Example


As part of the secure boot process in the SoC above, the _tmcu_ fetches bootloader code
from non-volatile memory, _tnvm_ and writes it to _sram_ .


Threat Model


If the device has insufficient protections, an adversary could read the bootloader code
from _tnvm_ memory, modify it or replace it and write it to sram before boot is complete
and thus have the system boot using malicious code.


Security Requirement


The memory storing boot code should not be readable by un-trusted agents and the
_sram_ storing boot code should not be writable by un-trusted agents until boot is
completed.


 87





Completing the Template Based on Design Signals and Security Requirement


From the security requirement we can fill out the rule template which gives the rules
below. The values for _BOOT_CODE_ADDR_HI_ and _BOOT_CODE_ADDR_LO_ are
constants provided by the user.

### - CWE 1276: Hardware Child Block Incorrectly Connected to Parent System

##### Description


Signals between a hardware IP and the parent system design are incorrectly connected
causing security risks.

##### Radix Security Rule Template


_Note:_ Many functional testing strategies can be used to check for correct connectivity in
general. The template below covers the security use case where known security-critical
signals will be isolated from those that are user-accessible when the hardware block is
correctly connected.


 88





Rule Template Detail


Information should not flow from/to the _Security-critical signals of hardware block_
to/from _User-accessible signals._


Security Rule Types

 - CONFIDENTIALITY_ASSET

 - INTEGRITY_ASSET

 - ISOLATE_ASSET

##### Detection Example


The interconnect in the untrusted sub-system of the SoC uses a security level bit to
determine if a transaction is secure or not. _core0_ is configured as secure and _core1_ is
configured as un-secure by the _tmcu_ at boot time. The _nvm_ memory uses the security
level bit to determine if a read transaction is allowed or not. If security_level == 0, a read
is allowed, if security_level == 1, it is not. During implementation the _nvm.security_level_
input is incorrectly tied to 0 instead of connected to the corresponding interconnect
signal. This means all masters; even un-secure ones will be allowed to read the _nvm._


Threat Model


Malicious software running on an un-trusted core will be able to access secure data
since access control is effectively disabled.


Security Requirement


Trusted data must not flow to un-trusted agents based on the security level of the
master. Use the security level programmed in the destination to detect illegal data flows
caused by incorrect connections of the IP.


Completing the Template Based on Design Signals and Security Requirement


From the security requirement we can fill out the rule template which gives the rule
below:


 89





_Note:_ Additional rules will be required for all masters connected to the interconnect.

### - CWE 1277: Firmware Not Updateable

##### Description


A product's firmware cannot be updated or patched, leaving weaknesses present with
no means of repair and the product vulnerable to attack.

##### Radix Security Rule Template


If the design doesn't have the ability to patch ROM code, this may be intentional or an
implementation oversight. Radix will not find the case where something is missing but it
will find cases where there are security violations caused by an incorrect
implementation or design.


Rule Template Detail


Information in _User accessible signals_ must not flow to _Sensitive Register_ locations
related to booting from updated firmware. Information from _Security sensitive data_ such
as updated firmware must not flow to _User accessible signals_ when booting from
updated firmware in an alternative location.


Note: Please also see CWE-1310 which describe a similar scenario.


Security Rule Types

 - CONFIDENTIALITY_DATA

 - INTEGRITY_DATA


 90




##### Detection Example


The _tmcu_ in the Hardware Root of Trust (HRoT) loads firmware from the ROM in the
HRoT. The ROM is programmed at manufacturing and cannot be changed. To provide
a method to update the firmware, new firmware can be written to the trusted non-volatile
memory (tnvm) and a bit set in the tmcu will instruct the tmcu to read firmware from a
pre-determined address in tnvm instead.


Threat Model


An attacker may be able to read the modified firmware and later write back malicious
code to the tnvm. The attacker may also clear the control bit in the tnvm so that the
device falls back to executing old firmware which may have known security
vulnerabilities and thereby enabling further attacks.


Security Requirement


The tmcu register controlling firmware location must not be writable from outside the
HRoT. The updated firmware must not be readable or writable from outside the HRoT
when it is being used by the tmcu.


Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rules below.


 91




### - CWE 1278: Missing Protection Against Hardware Reverse Engineering Using Integrated Circuit (IC) Imaging Techniques

##### Description


Information stored in hardware may be recovered by an attacker with the capability to
capture and analyze images of the integrated circuit using techniques such as scanning
electron microscopy.

##### Radix Security Rule Template


Radix currently does not cover this CWE, refer to the MITRE website for suggested
mitigations.

### - CWE 1279: Cryptographic Operations are run Before Supporting Units are Ready

##### Description


Performing cryptographic operations without ensuring that the supporting inputs are
ready to supply valid data may compromise the cryptographic result.

##### Radix Security Rule Template





Rule Template Detail


Information should not flow from the _Crypto IP outputs_ to _User-accessible signals_ when
the _Supporting IP self-test not passed._


Security Rule Types

 - ISOLATE_ASSET

 - VERIFY_SECURITY_STATE


 92




##### Detection Example


The _aes_ block is using random numbers from an internal True Random Number
Generator (TRNG). The TRNG runs a self-test after reset to ensure system integrity.
The _aes_ engine must not use the generated random numbers unless the self-test
passes. This means no read or write access of the AES block are allowed from
untrusted agents outside the Hardware Root of Trust (HRoT) until the TRNG self-test
has passed.


Threat Model


A malicious actor is able read and write data to and from _aes_ before the self-test is
completed and has passed and may alter the state of the encryption module or access
privileged data.


Security Requirement


There should be no access to the crypto block by untrusted agents until the integrity of
the TRNG is verified.


Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rules below:


 93




### - CWE 1280: Access Control Check Implemented After Asset is Accessed

##### Description


A product's hardware-based access control check occurs after the asset has been
accessed.

##### Radix Security Rule Template


Rule Template Detail


Information about the _Asset_ must not reach the _Asset's point of use_ unless the _Access_
_control check is successful._ Note: Finding bad coding styles and missing reset values
should be done as part of functional verification.


Security Rule Types

 - INTEGRITY_ACCESS_CONTROL_MECHANISM

 - ISOLATE_ASSET

 - VERIFY_ACCESS_CONTROL_CONFIG

##### Detection Example


Read access to the _sram.csr.configuration_ register is only allowed for the _tmcu_ .
Hardware access control checks that the bus master doing the read is valid before the
register value is driven to the output.


 94





Threat Model


If the register value is driven on the bus before the access control check is complete, an
un-trusted agent may get access to privileged information.


Security Requirement


Information in access controlled registers must not be available before the access
control check is complete and successful.


Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rules below:

### - CWE 1281: Sequence of Processor Instructions Leads to Unexpected Behavior

##### Description


Specific combinations of processor instructions lead to undesirable behavior such as
locking the processor until a hard reset performed.

##### Radix Security Rule Template


Radix currently does not cover this CWE, refer to the MITRE website for suggested
mitigations.

### - - CWE 1282: Assumed Immutable Data is Stored in Writable Memory

##### Description


Immutable data, such as a first-stage bootloader, device identifiers, and "write-once"
configuration settings are stored in writable memory that can be re-programmed or
updated in the field.


 95




##### Radix Security Rule Template





Rule Template Detail


Information from _User-accessible signals_ should not affect the _Memory storing_
_immutable data._


Security Rule Types

 - INTEGRITY_DATA

 - INTEGRITY_MEMORY_REGION

##### Detection Example


In the SoC above, cryptographic hash digests, encryption keys, the first stage
bootloader and other trusted data is stored in ROM and one-time programmable fuses.
This data is not modifiable after manufacturing. Another case is if the immutable data is
stored in sram because the memory type was not defined in the design specification.
The immutable data is accessible in the address range [ _IMM_ADDR_START_ :
_IMM_ADDR_END_ ], defined in the system specification.


Threat Model


An attacker is able to modify a hash digest stored in what was supposed to be read only
memory. Any code the attacker loads after that can be verified as trusted.


Security Requirement


All immutable code or data should be programmed into ROM or write-once memory that
cannot be modified in the field.


 96





Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rules below. The first
rule may incorrectly flag a violation since there is no condition checking if data is
actually written to the memory as opposed to data flowing to the data input of the
memory only. However, any write attempt to immutable data may indicate a security
vulnerability. The second rule doesn't specify which physical memory data must not flow
to, only the address range that should not be writable.








### - CWE 1283: Mutable Attestation or Measurement Reporting Data

##### Description

The register contents used for attestation or measurement reporting data to verify boot
flow are modifiable by an adversary.

##### Radix Security Rule Template


Rule Template Detail


Information from _User-accessible signals_ should not affect the _Memory storing_
_attestation and/or measurement data._


Security Rule Types

 - INTEGRITY_MEMORY

 - INTEGRITY_REGISTER

 - INTEGRITY_SECURITY_STATE


 97




##### Detection Example


The final hash value calculated on the code during secure boot is written to a register by
the _tmcu._ This value is readable by the un-trusted cores _core{0-N}_ and by the _debug_
interface. It is not writable by any un-trusted agent or debug module.


Threat Model


An attacker is able to modify the final hash values due to a design bug so that malicious
code that failed verification will now pass and it appears that secure boot passed even
though the system is running malicious software


Security Requirement


Measurement reporting data such as the final hash value should be stored in read only
registers or have access protection to prevent modification.


Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rule below.

### - CWE 1290: Incorrect Decoding of Security Identifiers

##### Description


The product implements a decoding mechanism to decode certain bus-transaction
signals to security identifiers. If the decoding is implemented incorrectly, then untrusted
agents can now gain unauthorized access to the asset.


 98




##### Radix Security Rule Template





Rule Template Detail


Information from _Untrusted signals_ must not flow to _Security sensitive signals_ unless the
security level of the source is validated independent of the access control logic i.e., the
security identifier allows the access.


Security Rule Types

 - CONFIDENTIALITY_ASSET

 - INTEGRITY_ASSET

 - ISOLATE_ASSET

##### Detection Example


The hrot_iface access control module only allows access to slaves in the Hardware
Root of Trust (HRoT) if the source security identifier matches the access policy defined
in the interface. Each master in the untrusted sub-system has a 3-bit security identifier.
For example: Core0 is 3'b101 and Core1 is 3'b100. According to the access policy
Core0 is allowed to access for example SRAM in the HRoT sub-system but Core1 is
not. The three security identifier bits are out of band inputs to the hrot_iface interface.
There are less than 4 masters in the untrusted subsystem so the access control module
only use the lower 2 bits to determine if the security identifier matches the policy.


Threat Model


The access control module incorrectly decodes the security identifiers and grant access
to untrusted masters.


 99





Security Requirement


Security identifiers must be correctly decoded for an access to be allowed.


Completing the Template Based on Design Signals and Security Requirement


Based on the security goal we fill in the template from the example signals, obtaining
the rule below. No information from the untrusted sub-system should flow into the
Hardware Root of Trust unless the secure id of the source matches the ones in the
access policy. The "unless" condition needs to list all allowed security ids based on
system documentation, not based on implementation.

### - - CWE 1291: Public Key Re Use for Signing both Debug and Production Code

##### Description


The same public key is used for signing both debug and production code.

##### Radix Security Rule Template


Radix currently does not cover this CWE, refer to the MITRE website for suggested
mitigations.

### - CWE 1292: Incorrect Conversion of Security Identifiers

##### Description


The product implements a conversion mechanism to map certain bus-transaction
signals to security identifiers. However, if the conversion is incorrectly implemented,
untrusted agents can gain unauthorized access to the asset.

##### Radix Security Rule Template


 100





Rule Template Detail


Information from _User accessible signals_ must not flow to _Security sensitive signals_
unless the security level of the source is validated independent of the bridge.


Security Rule Types

 - CONFIDENTIALITY_ASSET

 - INTEGRITY_ASSET

 - ISOLATE_ASSET

##### Detection Example


The interconnect in the untrusted subsystem of the SoC is implementing the AXI
protocol with TrustZone. One of the peripherals is a UART with an OCP interface. It is
connected to the AXI interconnect via an OCP - AXI bridge. Since OCP doesn't support
TrustZone, one bit in each transaction is used to communicate the security level of the
OCP agent. The OCP - AXI reads the bit and sets the TrustZone bits accordingly.


Threat Model


The OCP to AXI bridge interprets the security bit in the OCP transaction incorrectly and
sets the TrustZone bit incorrectly. This may allow a malicious actor access to security
sensitive data connected to the AXI interconnect.


Security Requirement


Security identifiers must be correctly maintained when they are converted between
protocols


Completing the Template Based on Design Signals and Security Requirement


Based on the security goal we fill in the template from the example signals, obtaining
the rule below. The signal _UART.secure_trans_ is unlikely to exist in the design since
that is the information that is encoded in the OCP transaction. One solution is to


 101





implement logic in the test environment to decode the security level of the transaction
and use that in the security rule.




### - CWE 1294: Insecure Security Identifier Mechanism

##### Description

The System-on-Chip (SoC) implements a Security Identifier mechanism to differentiate
what actions are allowed or disallowed when a transaction originates from an entity.
However, the Security Identifiers are not correctly implemented.

##### Radix Security Rule Template


This CWE entry is currently under development by MITRE but will be covered by Radix
once the entry is complete. Please see the MITRE website at cwe.mitre.org for the
status of this CWE.

### - CWE 1295: Debug Messages Revealing Unnecessary Information

##### Description


The product fails to adequately prevent the revealing of unnecessary and potentially
sensitive system information within debugging messages.

##### Radix Security Rule Template


Rule Template Detail


Internal _Signals carrying confidential information_ should not flow to device _External_
_interfaces readable by untrusted agents._ The information flow may be qualified by
debug mode condition, but leakage may also occur through for example a UART.


 102





Security Rule Types

 - CONFIDENTIALITY_ASSET

 - CONFIDENTIALITY_DATA

 - CONFIDENTIALITY_SECURITY_STATE

##### Detection Example


The SoC has two debug interfaces. The debug port in HRoT is used to access the
HRoT only during debug and a UART Peripheral connected to the interconnect in the
untrusted part of the SoC which is used to debug the rest of the SoC. The debug port in
HRoT has access control limiting access to authorized users. The UART doesn't have
access control and allows access to all agents and modules connected to the
interconnect unless they have their own access control. The memory MEM is configured
to only allow access to a memory range [ _PROTECTED_ADDR_END_ :
_PROTECTED_ADDR_START_ ] to privileged code running on the Core0 processor.


Threat Model


A malicious actor can read sensitive data stored in memory or in registers when
debugging using the UART interface and bypassing normal access protections.


Security Requirement


Data in the protected area of memory should not be readable through the UART
interface at any time.


Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rules below. The
parameters _PROTECTED_ADDR_END_ and _PROTECTED_ADDR_START_ are
constants that need to be defined by the user.


 103




### - CWE 1296: Incorrect Chaining or Granularity of Debug Components

##### Description


The product's debug components contain incorrect chaining or granularity of debug
components.

##### Radix Security Rule Template


Rule Template Detail


Internal _Signals carrying confidential information_ should not flow to device _External_
_interfaces readable by untrusted agents_ unless the proper authentication is done. The
authentication may require passing access control at multiple different points in the flow
which require different levels of privilege.


Security Rule Types

 - CONFIDENTIALITY_ASSET

 - CONFIDENTIALITY_DATA

 - CONFIDENTIALITY_SECURITY_STATE

##### Detection Example


 104





The HW Root of Trust (HRoT) has a debug, Test Access Port which is connected in a
chain of debug modules that are eventually connected to the SoC JTAG port. Accessing
debug data at different locations in the SoC requires different privileges. Accessing
debug data from the HRoT requires the highest (0) level of privilege. A debugger
connected to the JTAG port must first authenticate access to the JTAG port and then
authenticate access to each debug module in the chain assuming it has the correct
credentials. This allows agents with low privilege (3) to access debug data in nonsecure areas of the SoC and agenst with the highest privilege (0) to access debug data
in the HRoT. However, due to an implementation error, if the previous TAP module in
the chain is authenticated, the authentication check on the next TAP is bypassed.


Threat Model


A malicious actor can read sensitive data in the HRoT through the debug TAP inteface
even if he only has access privilege to a lower privilege module earlier in the chain.


Security Requirement


Data in the HRoT connected to the debug interface must not be readable by the SoC
JTAG interface unless both interfaces has been authenticated.


Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rules below.

### - CWE 1297: Unprotected Confidential Information on Device is Accessible by OSAT Vendors

##### Description


The product does not adequately protect confidential information on the device from
being accessed by Outsourced Semiconductor Assembly and Test (OSAT) vendors.

##### Radix Security Rule Template


This CWE entry is currently under development by MITRE but will be covered by Radix
once the entry is complete. Please see the MITRE website at cwe.mitre.org for the
status of this CWE.


 105




### - CWE 1298: Hardware Logic Contains Race Conditions

##### Description


A race condition in the hardware logic results in undermining security guarantees of the
system.

##### Radix Security Rule Template


Radix currently does not cover this CWE, refer to the MITRE website for suggested
mitigations.

### - CWE 1299: Missing Protection Mechanism for Alternate Hardware Interface

##### Description


The lack of protections on alternate paths to access control-protected assets (such as
unprotected shadow registers and other external facing unguarded interfaces) allows an
attacker to bypass existing protections to the asset that are only performed against the
primary path.

##### Radix Security Rule Template


Rule Template Detail


Information in the _Asset_ must be prevented from being written with data from _user-_
_accessible signals_ unless the _Source ID_ matches _source with allowed source ID._
Information in the _Asset_ must not flow to _User-accessible signals_ unless the _Source ID_
matches _source with allowed source ID._


 106





Security Rule Types

 - INTEGRITY_ACCESS_CONTROL_CONFIG

 - INTEGRITY_ASSET

 - VERIFY_ACCESS_CONTROL_CONFIG

##### Detection Example


The DMA may only be programmed by the trusted _Core0_ processor and the _tmcu._ This
is enforced by access control in the interconnect which only allows the transaction if the
secure ID of the source is CORE0 or TMCU. One of the peripherals on the interconnect
is a GPIO interface. It should not have access to the DMA registers but due to a design
oversight, access control is not enforced when the source of the transaction is the GPIO
interface.


Threat Model


The lack of access control on the alternative path from GPIO to protected registers
allows a malicious actor to control the DMA.


Security Requirement


There should be no read of write access to protected DMA registers through alternative
paths.


Completing the Template Based on Design Signals and Security Requirement


Based on the security goal we fill in the template which gives the two rules below.







 107




### - CWE 1300: Improper Protection Against Physical Side Channels

##### Description


The product is missing protections or implements insufficient protections against
information leakage through physical channels such as power consumption,
electromagnetic emissions (EME), acoustic emissions, or other physical attributes.

##### Radix Security Rule Template


Radix currently does not cover this CWE, refer to the MITRE website for suggested
mitigations.

### - CWE 1301: Insufficient or Incomplete Data Removal within Hardware Component

##### Description


The product's data removal process does not completely delete all data and potentially
sensitive information within hardware components.

##### Radix Security Rule Template


Radix currently does not cover this CWE, refer to the MITRE website for suggested
mitigations.

### - CWE 1302: Missing Security Identifier

##### Description


The product implements a security identifier mechanism to differentiate what actions are
allowed or disallowed when a transaction originates from an entity. A transaction is sent
without a security identifier.

##### Radix Security Rule Template


 108





Rule Template Detail


Data from a trusted source e.g. an embedded processor is only allowed to flow to
_Trusted Memory_ when _Security identifier for source is set._ Trusted Memory may be
defined as an address range in memory.


Security Rule Types

 - INTEGRITY_DATA

 - ISOLATE_MEMORY_REGION

##### Detection Example


Shared memory (MEM) in the untrusted subsystem is divided into separate address
ranges for each processor core and each core is only allowed to access memory in its
own address range. Each master on the core.interconnect has a unique security
identifier. There is a register in interconect.csr which has one bit per master. If the bit for
a specific master is set, then read and write access to the destination is allowed. If the
bit is not set, the transaction is dropped. There is no master with number 0 so a missing
identifier, interpreted as zero will not allow access.


Threat Model


An attacker may cause one of the cores to omit the security identifier in a memory read
or write transaction. This will cause the memory to drop the transaction. This may cause
a denial-of-service attack scenario since the code running on the core is not executing
as expected.


Security Requirement


All masters must include a security identifier with every transaction.


 109





Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rule below. If a write
from Core0 doesn't have a security identifier, data will reach the memory but the unless
conditon is false so the rule will fail.

### - - CWE 1303: Non Transparent Sharing of Microarchitectural Resources

##### Description


Hardware structures shared across execution contexts (e.g., caches and branch
predictors) can violate the expected architecture isolation between contexts.

##### Radix Security Rule Template





Rule Template Detail


Information in _Instruction Operands_ when they are _Influenced by unprivileged process_
and _Instructions will be squashed_ should not affect the _Cache State._


Security Rule Types

 - CONFIDENTIALITY_ASSET

##### Detection Example


Detecting vulnerabilities like Spectre is challenging because the illegal loading of the
data and transmission through the timing side-channel occurs during transient or
speculative execution, which is invisible to the programmer's view of the processor. The
signals required for the Radix rule is dependent on the processor implementation.


 110





Threat Model


An attacker can extract data from another user's context through data being loaded into
cache for speculative executed instructions before they are being squashed.


Detecting Spectre Using Radix


For more details on how to detect Spectre type vulneabilities, see the article at:
https://tortugalogic.com/detecting-spectre-using-radix/

### - CWE 1304: Improperly Preserved Integrity of Hardware Configuration State During a Power Save/Restore Operation

##### Description


The product performs a power save/restore operation, but it does not ensure that the
integrity of the configuration state is maintained and/or verified between the beginning
and ending of the operation.

##### Radix Security Rule Template


Rule Template Detail


Information should not flow from insecure memory, _Data stored in insecure location_ to
trusted CPU, _Trusted location_ unless it is validated for example by comparing a saved
and calculated secure hash of the data.


Security Rule Types

 - CONFIDENTIALITY_ASSET

 - INTEGRITY_ASSET


 111




##### Detection Example


Before the HW Root of Trust (HRoT) is powered down, the configuration state of the
tmcu is saved in off-chip flash memory connected to an I2C controller in the Peripherals
IP subsystem. Before the state is saved, a secure hash is calculated on the data and it
is saved at a pre-determined address in trused non-volatile memory (tnvm) in the HRoT.
When powering up the HRoT the configuration data is read from external flash. The I2C
controller calculates a secure hash that is appended to the data and the tmcu compares
the stored hash with the calculated one and only restores state if they match.


Threat Model


A malicious actor may modify the stored configuration to escalate privilege or disable
parts of the hardware. If the modified configuration is restored due to missing or omitted
validation the attack will be successful.


Security Requirement


There are 3 requirements for this CWE: 1. Confidentiality: The Stored Hash cannot be
read by an untrusted source 2. Integrity: The Stored Hash cannot be written by an
untrusted source 3. The saved state in external memory must not be restored if the
Stored Hash does not compare to the calculated hash.


Completing the Template Based on Design Signals and Security Requirement


From the third requirement that information in the flash memory connected to the I2C
controller must not flow to the inputs of tmcu unless the calculated and stored secure
hash of the data match.


 112





Additional Radix security rules may be required to verify that the secure hash stored in
tnvm is not writable, for example:





The first confidentiality requirement that the stored hash cannot be read by an untrusted
source will be checked by the rule:

### - CWE 1310: Missing Ability to Patch ROM Code

##### Description


Missing an ability to patch ROM code may leave a System or System-on-Chip (SoC) in
a vulnerable state.

##### Radix Security Rule Template


If the design doesn't have the ability to patch ROM code, this may be intentional or an
implementation oversight. Radix will not find the case where something is missing but it
will find cases where there are security violations caused by an incorrect
implementation or design.


Rule Template Detail


Information in _User accessible signals_ must not flow to _Sensitive status Register._


Note: Please also see CWE-1277 which describe a similar scenario.


Security Rule Types

 - CONFIDENTIALITY_DATA


 113





 - INTEGRITY_DATA

##### Detection Example


The boot code for the tmcu is stored in One Time Programable (OTP) memory. There is
a bit in the tmcu that allow the OTP memory to be updated. This bit must only be
writable by trusted software running on the tmcu. When the update is complete, a status
bit is set to indicate success and the tmcu clear the bit that enable the memory to be
written.


Threat Model


An attacker disables the ability to write to OTP when the firmware update is started. If
the update complete bit is still set if the update is not completed, the system looks like it
was updated but it still has the old firmware which has security vulnerabilities the
attacker can use.


Security Requirement


There should be no influence on the update complete bit from the control bit that
enables the update and there should be no information flow from outside the HRoT to
the status bit.


Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rules below.


 114




### - CWE 1311: Improper Translation of Security Attributes by Fabric Bridge

##### Description


The bridge incorrectly translates security attributes from either trusted to untrusted or
from untrusted to trusted when converting from one fabric protocol to another.

##### Radix Security Rule Template


Rule Template Detail


Information from _User accessible signals_ must not flow to _Security sensitive signals_
when the source has an untrusted privilege level and information from _User accessible_
_signals_ must not flow to _Non security sensitive signals_ when the source has a trusted
privilege level. The second case may or may not be a system requirement, but it
highlights a mismatch in privilege levels that could be introduced through a bug in a
interconnect bridge.


Security Rule Types

 - CONFIDENTIALITY_ASSET

 - INTEGRITY_ASSET

 - ISOLATE_ASSET


 115




##### Detection Example


The SoC has an OCP controller in the Peripherals IP subsystem. Masters connected to
the OCP interface has one of four privilege levels: 2'b00 - trusted high, 2'b10 - trusted
low, 2'b01 - untrusted high and 2'b11 - untrusted low. Masters with a trusted privilege
level are only allowed to read and write secure areas of the SoC e.g. trusted nonvolatile
memory (tnvm) and masters with untrusted privilege level are only allowed to read and
write non-secure areas of the SoC e.g. shared memory (MEM). A master with trusted
privilege level is not allowed to access non-secure areas of the SoC and vice versa.
Hence it is important that trust levels are correctly translated throughout the chip.


Threat Model


Bugs in the implementation of the interconnect fabric may result in some privilege levels
being translated to an incorrect security level. This may allow an attacker to access
secure locations in the SoC from an un-trusted master.


Security Requirement


Security identifiers must be correctly transported and translated by the interconnect
fabric of the SoC.


Completing the Template Based on Design Signals and Security Requirement


Based on the security goal we fill in the template with the design signals to obtain the
rules below. The rules use the actual source privilege level to ensure no information
flows to the destination if the privilege level was incorrectly translated by the
interconnect fabric.


 116




### - - CWE 1312: Missing Protection for Mirrored Regions in On Chip Fabric Firewall

##### Description


The firewall in an on-chip fabric protects the main addressed region, but it does not
protect any mirrored memory or memory-mapped-IO (MMIO) regions.

##### Radix Security Rule Template


Rule Template Detail


Information from processor running unprivileged code, _non-privileged store data_ must
not flow to a _Mirrored memory location_ if the access to the original _memory location_
_not_allowed by access control._


Security Rule Types

 - CONFIDENTIALITY_ASSET

 - INTEGRITY_ASSET

##### Detection Example


 117





The SoC has a 64k section of shared memory (MEM) that is mirrored by the memory
controller for fault tolerance. Access control to the memory is done by the interconnect
firewall. The privilege level can be set for each 4k memory block. The same access
control should be applied to the original memory region and the mirrored region. Due to
a design oversight the firewall doesn't enforce access control on the mirrored region.


Threat Model


An attacker could read and write privileged data by reading and writing the mirrored
region since access control is missing.


Security Requirement


The same access control applied to the original memory should be applied to the
mirrored region.


Completing the Template Based on Design Signals and Security Requirement


Based on the security goal we fill in the template with the design signals to obtain the
rule below. By using the access permissions for the original memory, address bit [16] ==
0 for all accesses the rule will fail if the mirrored memory is accessed, and the original
memory is protected. This rule will also fail if the firewall is correctly enforcing access
control of the mirrored region of memory, but the privilege is programmed differently
than the original memory location.

### - CWE 1313: Hardware Allows Activation of Test or Debug Logic at Runtime

##### Description


During runtime, the hardware allows for test or debug logic (feature) to be activated,
which allows for changing the state of the hardware. This feature can alter the intended
behavior of the system and allow for alteration and leakage of sensitive data by an
adversary.

##### Radix Security Rule Template


 118





Rule Template Detail


Information on _Signals controlable by untrusted agents_ should not flow to _Signals that_
_enable debug_ unless the access is properly authenticated.


Security Rule Types

 - ISOLATE_REGISTER

 - ISOLATE_SECURITY_STATE

 - VERIFY_ACCESS_CONTROL_CONFIG

##### Detection Example


Debug mode in the SoC is enabled by setting the _tmcu.CSR.debug_en_ bit to "1". This is
normally done through the debug interface after the access has been properly
authenticated. No other user controllable signals can affect the state of the debug_en bit
so debug mode cannot be entered during normal operations of the device.


Threat Model


A malicious actor is able to enable debug mode during normal operation of the device
through an unintended back door into the HRoT or by bypassing the authentication
method, thus exposing sensitive data through the debug interface.


Security Requirement


It must not be possible to enable debug or testmode during normal runtime for an
unauthorized agent.


Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rules below.


 119




### - CWE 1314: Missing Write Protection for Parametric Data Values

##### Description


The device does not write-protect the parametric data values for sensors that scale the
sensor value, allowing untrusted software to manipulate the apparent result and
potentially damage hardware or cause operational failure.

##### Radix Security Rule Template


Rule Template Detail


Information from _Signals writable by untrusted agents_ must not flow to _Security sensitive_
_control signals._


Security Rule Types

 - INTEGRITY_ASSET

 - ISOLATE_ASSET


 120




##### Detection Example


The SoC has a temperature sensor, located in the untrusted subsystem, so that
overheating can be detected. The sensed temperature is computed using two
parameters: offset and scale as: "sensed_temp = offset + scale * sensor_val". The
sensed_temp value is available in a Read Only register. The raw sensor value is not
available to be read. The offset and scale registers are only writable by the tmcu. None
of the cores in the untrusted subsystem can write the offset and scale registers.


Threat Model


Due to a design oversight, the offset and scale registers are writable by the untrusted
cores. By modifying the values of the parameters, the chip may overheat. This can
cause it to malfunction and possibly bypassing security protections.


Security Requirement


The temperature sensor parameters must not be writable by untrusted software


Completing the Template Based on Design Signals and Security Requirement


Based on the security goal we fill in the template from the example signals, obtaining
the rule below. _Note:_ Additional rules for each of the cores in the untrusted subsystem
will be required.


 121




### - CWE 1315: Improper Setting of Bus Controlling Capability in - Fabric End point

##### Description


The bus controller enables bits in the fabric end-point to allow responder devices to
control transactions on the fabric.

##### Radix Security Rule Template


Rule Template Detail


Information from _User controlled signals_ e.g non-privileged code or a peripheral
interface, must not flow to _security sensitive control bits._ Additional requirements may
require control signals to be 0 (disabled) by default


Security Rule Types

 - CONFIDENTIALITY_ASSET

 - INTEGRITY_ASSET

##### Detection Example


The un-trusted sub-system of the SoC have three units that can master transactions on
the interconnect fabric. They are the Core0 processor, DMA and UART in Peripherals
IP sub-system. Each instance connected to the fabric has a control bit, _master_en_ to
determine if it is a master or a slave. In a specific implementation of the SoC, only the
Core0 processor is allowed to act as a master. The _master_en_ bit in all other instances
must be 0 at all times.


 122





Threat Model


An attacker is able to write to the _master_en_ bit in one of the slaves allowing it to master
transactions on the interconnect and bypassing access control.


Security Requirement


The master / slave control bits should not be writable by anyone. They should always be
0 except for the one Core that is enabled.


Completing the Template Based on Design Signals and Security Requirement


Based on the security goal we fill in the template with the design signals to obtain the
rules below. If the configuration is static, one rule per instance checking that the
master_en bit is always 0 is sufficient. If for example the trusted processor (tmcu) may
change the value, a variant of the first rule can be used.

### - - CWE 1316: Fabric Address Map Allows Programming of Unwarranted Overlaps of Protected and Unprotected Ranges

##### Description


The address map of the on-chip fabric has protected and unprotected regions
overlapping, allowing an attacker to bypass access control to the overlapping portion of
the protected region.

##### Radix Security Rule Template









 123





Rule Template Detail


Data in a privileged address range in a shared memory (Privileged data signals) must
not influence signals readable by untrusted agents This should always hold true even if
the non-privileged address range overlap the privileged address range. Additionally, the
privileged address range in shared memory must not be able to be influenced by signals
writable by untrusted agents.


Security Rule Types

 - CONFIDENTIALITY_ASSET

 - INTEGRITY_ASSET

 - ISOLATE_DATA

 - ISOLATE_MEMORY_REGION

##### Detection Example


The SoC has two embedded processors, Core0 and Core1, each running user code for
two different users. Each user has a private area in shared memory (MEM) which the
other user should not have access to. Each user requests a private address range from
a privileged process running on one of the cores and of course the two ranges should
not overlap. The private range is configured in two sets of registers in the interconnect
fabric. Due to hardware implementation bugs or firmware bugs, it is possible that the
two private ranges overlap allowing each user access to the other user’s private data.


Threat Model


A malicious user is able to program his private address range to overlap with that of
another user and will be able to read and write data that is private to the other user.


 124





Security Requirement


A user should only be able to access data in his own private area in memory even if the
memory range overlap with the private area of another user.


Completing the Template Based on Design Signals and Security Requirement


Based on the security goal we fill in the template with the design signals to obtain the
rules below. PRIV_START_ADDR_A and PRIV_END_ADDR_A specify the addresses
for the private area for user A and PRIV_START_ADDR_B and PRIV_END_ADDR_B
specify the addresses for the private area for user B. They are programmed in four
registers in the interconnect fabric. Note: One set of rules for read (confidentiality) and
one set of rules for write (integrity) are required.

### - CWE 1317: Missing Security Checks in Fabric Bridge

##### Description


A bridge that is connected to a fabric without security features forwards transactions to
the slave without checking the privilege level of the master. Similarly, it does not check
the hardware identity of the transaction received from the slave interface of the bridge.


 125




##### Radix Security Rule Template





Rule Template Detail


Information from _User controllable signals_ should not flow to _Security sensitive signals_
unless the source of the data is privileged.


Security Rule Types

 - CONFIDENTIALITY_ASSET

 - INTEGRITY_ASSET

##### Detection Example


The interconnect (tbus) in the Hardware Root of Trust (HRoT) doesn't implement access
control since the hrot_iface bridge only allow trusted transactions on the bus. The
trusted masters (Core0 and DMA) on the interconnect fabric in the untrusted subsystem have an output, priv, which is set when running in privileged mode. Only
transactions from masters running in privileged mode are forwarded by the hrot_iface
bridge to the tbus. The hrot_iface bridge is re-used from another project that did not
have different privilege levels so all transactions in the HRoT address range are
forwarded to the tbus regardless of security status, but this behavior was not mentioned
in the documentation.


Threat Model


A malicios actor may program the DMA to read data from the secure areas of the HRoT
despite not running in privileged mode.


 126





Security Requirement


The access policy of the HRoT should be enforced even if the security checks in
connected bridges are broken or missing.


Completing the Template Based on Design Signals and Security Requirement


Based on the security requirement we fill in the template with the design signals to
obtain the rules below. Note: additional rules are needed for other masters that should
be allowed to access the tbus in privileged mode. The third rule ensures that other
masters are not able to access tbus regardless of privilege mode. Using the source
privilege signal for verification removes the dependency of the bridge which is the
component we want to verify.

### - - CWE 1318: Missing Support for Security Features in On chip Fabrics or Buses

##### Description


On-chip fabrics or buses either do not support or are not configured to support privilege
separation or other security features, such as access control.

##### Radix Security Rule Template


 127





Rule Template Detail


Information from _User controllable signals_ should not flow to _Security sensitive signals_
when the source is in non-secure mode.


Security Rule Types

 - INTEGRITY_DATA

##### Detection Example


The interconnect fabric in the un-trusted sub-system of the SoC is using Open Core
Protocol (OCP). The signals for transporting security attributes are optional and are not
implemented even though most masters and slaves supports it. The Power
Management Unit (PMU) in the Peripherals sub-system has a control register to set
thermal limits. Writing the register is restricted to secure masters e.g., CPUs running
privileged code. The MReqInfo output of Core0 is driven to 0 to indicate that a
transaction is privileged but it is not transported through the fabric. The MReqInfo input
to the PMU is tied to zero since it is not driven by the fabric.


Threat Model


An attacker running user level code on Core0 can program the thermal limits to out-ofrange vales that will damage the device thus creating a denial-of-service attack.


Security Requirement


The on-chip interconnect must include security attributes if security sensitive slaves are
connected.


Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rule below. The
therm_limit register should not be writable by the Core0 processor when it is running
user level code.


 128




### - CWE 1319: Improper Protection against Electromagnetic Fault - Injection (EM FI)

##### Description


The device is susceptible to electromagnetic fault injection attacks, causing device
internal information to be compromised or security mechanisms to be bypassed.

##### Radix Security Rule Template


Radix currently does not cover this CWE, refer to the MITRE website for suggested
mitigations.

### - CWE 1320: Improper Protection for Out of Bounds Signal Level Alerts

##### Description


Untrusted agents can disable alerts about signal conditions exceeding limits or the
response mechanism that handles such alerts.

##### Radix Security Rule Template


Rule Template Detail


Information from _User controllable signals_ should not flow to _Security sensitive signals_
unless the _Source is trusted._


Security Rule Types

 - INTEGRITY_DATA


 129




##### Detection Example


The SoC has an external Digital Temperature Sensor (DTS) so that software can shut
down the device to prevent permanent damage due to overheating. The DTS is
connected to one of the GPIO pins of the GPIO controller in the Peripherals IP subsystem which sends an interrupt to the Core0 processor. The GPIO controller is
configured by the CPU in the HW Root of Trust during secure boot and it should not be
modifiable by other agents.


Threat Model


If a malicious actor can change the GPIO pin from an input to an output, he can perform
a denial-of-service attack. The warning signal from the temperature sensor will not
reach the CPU and the system may stop working and be permanently damaged.


Security Requirement


GPIO configuration bits must not be writable by untrusted agents.


Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rule below.

### - CWE 1323: Improper Management of Sensitive Trace Data

##### Description


Trace data collected from several sources on the System-on-Chip (SoC) is stored in
unprotected locations or transported to untrusted agents.


 130




##### Radix Security Rule Template





Rule Template Detail


Information from _Security sensitive signals_ must not flow to _User accessible signals_
unless the destination is properly authenticated.


Security Rule Types

 - CONFIDENTIALITY_ASSET

##### Detection Example


The SoC has a Trace IP module connected to the interconnect in the un-trusted subsystem. It captures transaction type, address and data for every transaction on the
interconnect fabric and stores it in local trace memory. Some of the transactions
originate in or targets the Hardware Root of Trust and this part of the trace data is
security sensitive. The trace data can be read via JTAG from the Trace IP memory. A
debugger connected to JTAG must be authenticated before being allowed to read
security sensitive trace data. If authentication fails, only non-secure trace data can be
read.


Threat Model


A malicious actor is able to read security sensitive trace data even though the debugger
is not authenticated because the Trace IP block did not properly track the source of the
trace data and hence allowed access to transactions originating in the HRoT.


Security Requirement


Trace data from security sensitive source must only be read if the destination is properly
authenticated.


 131





Completing the Template Based on Design Signals and Security Requirement


Based on the security requirement we fill in the template with the design signals to
obtain the rule below. In this case we assume transactions from the tmcu, OTP and
AES block in the Hardware Root of Trust are security sensitive. Note: Radix will track
the information from the identified secure sources anywhere in the design to determine
if they reach the TDO output. The verification engineer doesn't have to know the path
through the system or if it was temporarily stored in a memory.

### - CWE 1324: Sensitive Information Accessible by Physical Probing of JTAG Interface

##### Description


Sensitive information in clear text on the JTAG interface may be examined by an
eavesdropper, e.g. by placing a probe device on the interface such as a logic analyzer,
or a corresponding software technique.

##### Radix Security Rule Template


The weakness in this CWE involves physical probing of a device and cannot be
addressed by verification tools prior to manufacture. However, the mitigations for the
weakness can be verified using Radix. One mitigation is to encrypt the data before it
leaves the chip via the debug block and the authorized user will decrypt it at his network
endpoint.


Rule Template Detail


Information from the design is only allowed to flow to _User visible signals_ e.g. the JTAG
port if it flows through the AES encryption block


 132





Security Rule Types

 - CONFIDENTIALITY_DATA

##### Detection Example


The JTAG port of the SoC is connected to the debug module in the Hardware Root of
Trust, allowing an authenticated user to read data from all modules on the tbus
interconnect. In order to protect against anyone reading the data in flight when it has left
the SoC, data is encrypted in the AES core before going to the debug block.


Threat Model


If data on the JTAG pins are not protected, an attacker may snoop on the bus while an
authenticated user is performing reads of secure locations in the chip.


Security Requirement


Only data coming from the AES block is allowed to reach the debug module and thus
the JTAG port. There must be no information flow that bypass the AES block.


Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rule below.





 133




### - CWE 1326: Missing Immutable Root of Trust in Hardware

##### Description


A missing immutable root of trust in the hardware results in the ability to bypass secure
boot or execute untrusted or adversarial boot code.

##### Radix Security Rule Template


Rule Template Detail


Information from _User accessible signals_ must not flow to _Immutable signals_


Security Rule Types

 - INTEGRITY_ASSET

 - ISOLATE_ASSET

##### Detection Example


Secure boot in the example SoC is performed by the Hardware Root of Trust (HRoT)
sub-system. The boot code, key material and other boot data must be immutable
otherwise the implementation is vulnerable to attacks. The HRoT stores this data in
ROM, OTP, SRAM and tnvm memory that are assumed to be immutable


Threat Model


Some locations that store secure boot code and data are mutable which allows an
adversary to modify them and execute their choice of code and bypass access control
in the system.


 134





Security Requirement


All secure boot code and data must be immutable i.e. not writable by any agent in the
untrusted subsystem of the SoC.


Completing the Template Based on Design Signals and Security Requirement


Based on the security goal we fill in the template from the example signals, obtaining
the rule below. It is assumed that the entire ROM, OTP and tnvm are immutable and a
sub-set of the SRAM bounded by IMMUTE_ADDR_END and IMMUTE_ADDR_START
is immutable. The two constants IMMUTE_ADDR_END and IMMUTE_ADDR_START
are provided by the user.

### - CWE 1328: Security Version Number Mutable to Older Versions

##### Description


Security-version number in hardware is mutable, resulting in the ability to downgrade
(roll-back) the boot firmware to vulnerable code versions.

##### Radix Security Rule Template









Rule Template Detail


Information on _Interfaces controllable by untrusted agents_ should not flow to _Signals_
_carrying confidential information_


Security Rule Types

 - INTEGRITY_ASSET

 - INTEGRITY_DATA


 135




##### Detection Example


A security version number is stored in trusted non-volatile memory in the HW Root of
Trust (HRoT). It is used to ensure that firmware signed with a lower version number
cannot be loaded and run. The security version number is preserved during power
cycles and resets. It must not be modifiable by any agent outside the HRoT.


Threat Model


If a malicious actor can modify the security version number stored in the HRoT, this
allows a roll-back to previous version of firmware which may have vulnerabilities that
can be used for an attack.


Security Requirement


Security version numbers must not be modifiable from outside the Hardware Root of
Trust.


Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rules below. In this
case we assume the security version number is stored at address id_addr in the nonvolatile memory array.


Verification


If the security rule is violated when simulating the design, the violation is debugged in
the Radix GUI. In this example, the rule is violated at time 1000. Viewing the violation in
the Radix GUI path view we see how information flows through the hierarchy of the
design from the hrot_iface instance through the tbus interconnect to the nvm_array in
the tnvm instance.


 136





To understand which signals are involved in the unexpected information flow and what
values they have, we can analyze the waveform.

### - CWE 1330: Remanent Data Readable after Memory Erase

##### Description


Confidential information stored in memory circuits is readable or recoverable after being
cleared or erased.

##### Radix Security Rule Template


Radix currently does not cover this CWE, refer to the MITRE website for suggested
mitigations.


 137




### - CWE 1331: Improper Isolation of Shared Resources in Network On Chip

##### Description


The product does not isolate or incorrectly isolates its on-chip-fabric and internal
resources such that they are shared between trusted and untrusted agents, creating
timing channels.

##### Radix Security Rule Template


Secret data may leak via a timing channel i.e. differences in latency for example through
a NOC reveal information about the data. This leakage may be detected using Radix.


Rule Template Detail


Information in secret data should not flow to _Module whose behavior is influenced by_
_secure data_ and it can be observed.


Security Rule Types

 - CONFIDENTIALITY_DATA

##### Detection Example


The interconnect in the untrusted sub-system of the SoC only support one connection to
the shared memory at the time. If Core0 is reading from memory, Core1 has to wait.
Software running in privileged mode on Core0 is running the RSA encryption algorithm.
It reads an encryption key from OTP in the Hardware Root of Trust (HRoT) and store it
in a register in Core0. When a bit in the key is 1, RSA performs a multiplication which
cause a read from the shared memory.


 138





Threat Model


An attacker running in user mode on Core1 is doing a series of reads from shared
memory while the RSA algorithm is run on Core0. By measuring the latency of each
memory read he can determine if the RSA key is 1 or 0.


Security Requirement


No timing information should flow from the RSA Key to the load store unit in the core
executing the algorithm.


Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rule below. In this
example, the RSA key is stored in register R0.

### - CWE 1332: Insufficient Protection Against Instruction Skipping Via Fault Injection

##### Description


The device is missing or incorrectly implements circuitry or sensors to detect and
mitigate CPU instruction skips that can be caused by fault injection.

##### Radix Security Rule Template


Radix currently does not cover this CWE, refer to the MITRE website for suggested
mitigations.

### - CWE 1334: Unauthorized Error Injection Can Degrade Hardware Redundancy

##### Description


An unauthorized agent can inject errors into a redundant block to deprive the system of
redundancy or put the system in a degraded operating mode.


 139




##### Radix Security Rule Template


Radix currently does not cover this CWE, refer to the MITRE website for suggested
mitigations.

### - CWE 1338: Improper Protections Against Hardware Overheating

##### Description


A hardware device is missing or has inadequate protection features to prevent
overheating.

##### Radix Security Rule Template


Radix currently does not cover this CWE, refer to the MITRE website for suggested
mitigations.

### - CWE 1351: Improper Handling of Hardware Behavior in Exceptionally Cold Environments

##### Description


A hardware device, or the firmware running on it, is missing or has incorrect protection
features to maintain goals of security primitives when the device is cooled below
standard operating temperatures.

##### Radix Security Rule Template


Detecting security violations for this CWE assumes that the entropy of the Random
Number Generator (RNG) is tested at power up and boot will be disabled if the test fails.


Rule Template Detail


Information from _Entropy source_ e.g. SRAM based PUF, should not flow to _Location_
_using entropy data_ e.g. cryptographic function unless the entropy source is verified to be
working.


 140





Security Rule Types

 - CONFIDENTIALITY_DATA

##### Detection Example


The RNG used by the AES encryption module is using the output from a PUF as its
entropy source. The SRAM based PUF needs to operate at a certain temperature to
ensure sufficient entropy. An on-chip temperature sensor measures the temperature of
the PUF and if it is too low, it won't allow the PUF to be used and the SoC won't boot.


Threat Model


An attacker may try to write the temperature sensor control register with a much lower
threshold temperature making the PUF output depend on previous data instead of
manufacturing inconsistencies. An attacker may also try to boot the SoC even if the
PUF entropy test is failing.


Security Requirement


The temperature sensor control register should not be writable by any agent outside the
Hardware Root of Trust (HRoT) module. The PUF output should not be used by the
AES unless the temperature is above a threshold and the entropy test of the PUF is
passing.


Completing the Template Based on Design Signals and Security Requirement


From the requirement, we can fill in the template which gives the rule below.


 141





 142





.

### Appendix: Security Rule Types


Prefixes are correlated with security objective









|Prefix|Common Rule Pattern|Summary|
|---|---|---|
|CONFIDENTIALITY|asset =/=> {attacker_observables}|no-flow to outputs|
|INTEGRITY|{attacker_controllables} =/=> asset|no-flow from inputs|
|ISOLATE|asset =/=><br>{invalid_outputs} {invalid_inputs} =/=><br>asset|Two rules, logical union of<br>confidentiality and integrity|
|VERIFY|asset == secure_value|asset value does not enable<br>violation of security objectives|


Suffixes are correlated with asset type

















|Suffix|Strategy|
|---|---|
|ACCESS_CONTROL_CONFIG|Mixture of ACL values and derived configuration info. May be<br>implicit. Ask about external information sources such as files<br>input to testbenches. Likely use-case for VERIFY prefix|
|ACCESS_CONTROL_MECHANISM|Stateful logic, may require widgets to interact with or inject taint<br>or observe FSM states. ACLs to firewalls may require multiple<br>rules for each whitelisted endpoint pair (src/dest, master/slave,<br>host/device)|
|ASSET|Refers to general assets requiring either a little or a lot of<br>design-specific customization over the rule pattern|
|DATA|Usually regions in ROM or NVM containing data or local SRAM<br>or TCM. For each data-at-rest location taint**all** nearest data-<br>carrying signals|
|FSM_STATES|Track the next state and add exceptions for transitions e.g.<br>**next_state =/=> current_state unless ( list_of_conditions )**|
|MEMORY_REGION|A shared region of a memory resource, does not refer to the<br>data in that region, often with ISOLATE-style rules for non-<br>interference. Beware physical address aliasing: ensure that**all** <br>memory ranges that refer to the physical region are tracked.|
|REGISTER|Likely not register itself, security bugs residing in "sticky"<br>registers, locks, lock ranges, and the control logic are found<br>following the pattern**inputs =/=> my_reg unless ( condition )**|
|SECURITY_STATE|ISOLATE-style rules when combined with CONFIDENTIALITY.<br>Similar to REGISTER plus CONFIDENTIALITY to ensure state<br>registers are secret (when applicable) and incorruptible.|


 143





.

### Legal Notices


Terms of Use for Materials from the MITRE CWE Database


CWE™ is free to use by any organization or individual for any research, development, and/or commercial purposes, per these CWE


Terms of Use. The MITRE Corporation (“MITRE”) has copyrighted the CWE List, Top 25, CWSS, and CWRAF for the benefit of the


community in order to ensure each remains a free and open standard, as well as to legally protect the ongoing use of it and any


resulting content by government, vendors, and/or users. CWE is a trademark of MITRE. Please contact cwe@mitre.org if you


require further clarification on this issue.


_LICENSE_


CWE Submissions: By submitting materials to The MITRE Corporation’s (“MITRE”) Common Weakness Enumeration Program


(CWE™), you hereby grant to MITRE a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license to


use, reproduce, prepare derivative works of, publicly display, publicly perform, sublicense, and distribute your submitted materials


and derivative works. Unless otherwise required by applicable law or agreed to in writing, it is understood that you are providing


such materials on an “AS IS” BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied,


including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR


A PARTICULAR PURPOSE.


CWE Usage: MITRE hereby grants you a non-exclusive, royalty-free license to use CWE for research, development, and


commercial purposes. Any copy you make for such purposes is authorized on the condition that you reproduce MITRE’s copyright


designation and this license in any such copy.


_DISCLAIMERS_


ALL DOCUMENTS AND THE INFORMATION CONTAINED IN THE CWE ARE PROVIDED ON AN “AS IS” BASIS AND THE


CONTRIBUTOR, THE ORGANIZATION HE/SHE REPRESENTS OR IS SPONSORED BY (IF ANY), THE MITRE CORPORATION,


ITS BOARD OF TRUSTEES, OFFICERS, AGENTS, AND EMPLOYEES, DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED,


INCLUDING BUT NOT LIMITED TO ANY WARRANTY THAT THE USE OF THE INFORMATION THEREIN WILL NOT INFRINGE


ANY RIGHTS OR ANY IMPLIED WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE AND


NONINFRINGEMENT.


IN NO EVENT SHALL THE CONTRIBUTOR, THE ORGANIZATION HE/SHE REPRESENTS OR IS SPONSORED BY (IF ANY),


THE MITRE CORPORATION, ITS BOARD OF TRUSTEES, OFFICERS, AGENTS, AND EMPLOYEES BE LIABLE FOR ANY


CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING


FROM, OUT OF OR IN CONNECTION WITH THE INFORMATION OR THE USE OR OTHER DEALINGS IN THE CWE.


Tortuga Logic Terms of Use and Copyright


This Radix Coverage for Hardware Common Weakness Enumeration (CWE) Guide (“Guide”), including all material and information


included in in this Guide, is provided on an “as is” basis. Tortuga Logic disclaims all warranties of any kind, either express or implied.


Tortuga Logic shall not be liable for any direct, indirect, punitive, incidental, special, or consequential damages that result from the


use of, or inability to use, this Guide.


TORTUGA LOGIC is a trademark of Tortuga Logic, Inc. Other product or company names are the property of their respective


owners. They are used in the Guide for identification purposes only and do not imply endorsement or affiliation.


 144


