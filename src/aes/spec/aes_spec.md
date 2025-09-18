## AES 128/192/256 (ECB) A VALON [®] -MM S LAVE

##### Thomas Ruschival and opencores.org

www.opencores.org ruschi@opencores.org


avs_aes_doc (v. 0.8) - 2011/05/15


**AES** **128/192/256** **(ECB)** **A** **VALON** **[®]** **-MM** **S** **LAVE** **2/** **15**

##### **Contents**


**1** **Introduction** **3**


**2** **Interface** **3**


2.1 Configuration Generics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3


2.2 Signals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4


**3** **Memory Map** **4**


3.1 Control Register . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5


**4** **Protocol Sequence** **6**


4.1 Interrupt Behavior . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7


**5** **The Inner Core** **7**


**6** **Throughput Calculation** **10**


**7** **FPGA implementations** **11**


**8** **Simulation** **12**


8.1 Testbench . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12


8.2 Simulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12


**9** **Software Driver** **12**


9.1 Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12


**10 License and Liability** **13**


**Acronyms** **14**


avs_aes_doc (v. 0.8) - 2011/05/15 All rights reserved - ©2011 Thomas Ruschival
and opencores.org


**AES** **128/192/256** **(ECB)** **A** **VALON** **[®]** **-MM** **S** **LAVE** **3/** **15**

##### **1 Introduction**


The Advanced Encryption Standard (AES) is a symmetric block cipher operating on fixed block
sizes of 128 Bit and is specified for key sizes of 128, 192 and 256 Bit designed by Joan Daemen
and Vincent Rijmen. The algorithm was standardized by National Institute of Standards and
Technology (NIST). For more information on the algorithm see [1].
This component implements an AES encryption decryption data path in Electronic Code Book
(ECB) mode with either 128,192 or 256 Bit keys. The key length is determined by generics at
compile time. Also the decryption data path can be disabled by generics if it is not needed for
the application.
The component provides an Avalon [®] Memory Mapped (Avalon-MM) slave interface to connect
to an Altera [®] Avalon [®] switch fabric. The Avalon [®] interface is implemented in a way that it can
also be used to connect to a Whishbone master if the signals are correctly mapped, see [2]. For
further information about the Whishbone bus refer to [3].

##### **2 Interface**


The AES core is accessed by the interface described in this section. An Avalon [®] interface was
chosen for its simplicity and compatibility with wishbone. Furthermore Avalon [®] defines interrupt
request signals for slaves which would be separate signals in a Wishbone implementation.The
component can be used both in polling mode or can provide an interrupt for signalling.
Unfortunately Avalon [®] is an Altera [®] proprietary technology. The actual AES core however is a
self contained entity and can be embedded into other System on Chip (SoC) bus interfaces as
well or used independently.


**2.1** **Configuration Generics**


The AES core can be configured by generics shown in table 1, consequently they are provided
by the Avalon [®] interface.

|Generic name|type|Description|
|---|---|---|
|KEYLENGTH|NATURAL|Size of initial user key. Must be 128, 192 or 256 ~~1 ~~.|
|DECRYPTION|BOOLEAN|Enables the instantiation of the decrypt data path if<br>true.|



Table 1: Component generics


Note: KEYLENGTH of 192 fail synthesis with Xilinx ISE [®] because of division by 6 in key schedule
that cannot be mapped to shift operations ( keyexpansion.vhd ).


1 All other values raise a compilation failure


All rights reserved - ©2011 Thomas Ruschival avs_aes_doc (v. 0.8) - 2011/05/15
and opencores.org


**AES** **128/192/256** **(ECB)** **A** **VALON** **[®]** **-MM** **S** **LAVE** **4/** **15**


**2.2** **Signals**


The Avalon [®] MM Slave interface is described in [4], the component implements the signals shown
in table 2.2. All signals are synchronous, sampled at the rising edge of the clock. The type for
all signals is IEEE1164 std_logic or std_logic_vector . For signals wider that 1 Bit the range
is Most Significant Bit (MSB) downto Least Significant Bit (LSB).
This components has only output signals driven by registers no input signals are directly combinatorially connected to the output signals, thus combinational loops are avoided. All signals are
active high. This component does not support burst transfers.

|Signal name|Width|In/Out|Description|
|---|---|---|---|
|clk|1|in|Avalon® bus clock, also used to drive the core.<br>|
|reset|1|in|_Synchronous_ reset signal for Avalon® bus interface.<br>The core itself is designed without need for reset sig-<br>nals.|
|writedata|32|in|Input data to write to location designated by address.<br>Bit 31 is most signiﬁcant Bit.|
|address|5|in|Word offset to the components base address.<br>The<br>memory map of the component for the respective off-<br>set is described in 3.<br>Only full 32-Bit words can be<br>addressed no byte addressing is implemented.|
|write~~1~~|1|in|If asserted enable write of data at writedata to location<br>designated by address.|
|read~~1~~|1|in|If asserted output data at location designated by<br>address to readdata.|
|readdata|32|out|Data output port for reading data at the location deﬁned<br>by address. Bit 31 is most signiﬁcant Bit.|
|waitrequest|1|out|Asserted if writedata was not accepted, this is the case<br>if the keyexpansion is not yet complete and a new is<br>written to the KEY address range without previous de-<br>assertion of the KEY_VALID Bit|
|irq|1|out|If Interrupt behavior is enabled IRQ will be asserted<br>when the operation has terminated. For use of inter-<br>rupt see 4.1|



Table 2: Avalon [®] Bus interface signals

##### **3 Memory Map**


The AES core Avalon [®] slave has an address space of 31 words accessible through the offset
described by the signal address, see 2.2. This address space is divided into three main sections
for the 4-word input data, the 4-word result of the operation and the user key. The actual length
of the user key can vary between 4, 6 and 8 words depending on the keysize. For control signals
and status information of the component and a control word is provided. The memory mapping


1 read and write are mutually exclusive and must not be asserted simultaneously.


avs_aes_doc (v. 0.8) - 2011/05/15 All rights reserved - ©2011 Thomas Ruschival
and opencores.org


**AES** **128/192/256** **(ECB)** **A** **VALON** **[®]** **-MM** **S** **LAVE** **5/** **15**


is described in table 3.

|Offset|Name|Description|
|---|---|---|
|0x00-0x07|KEY|Initial user key that will be used for encryption and decryption. The<br>most signiﬁcant word is written to offset 0x00. This memory section<br>is_ write-only_ to the Avalon® interface.|
|0x08-0x0B|DATA|Input data, can be either interpreted as cyphertext for decryption or<br>plain text for encryption. The most signiﬁcant word shall be written to<br>offset 0x08. This memory section is_ write-only_ to the Avalon® inter-<br>face.|
|0x10-0x13|RESULT|Result of the operation. The most signiﬁcant word of the result at off-<br>set 0x10. This memory section is_ read-only_ to the Avalon® Interface.|
|0x14-0x1E|—|reserved|
|0x1F|CTRL|Control and status word of the component can be read and written.<br>Detailed description see 3.1|



Table 3: Memory map of the AES core Avalon [®] slave


**3.1** **Control Register**


The AES Core offers the register CTRL to control the function of the core and poll its status. The
control register can be accessed in read and write mode. When writing to the register reserved
Bits shall be assigned a value of 0 . Individual Bits have following functionality described in table
3.1.
In case of a Avalon [®] Bus reset this register is set to 0x00000000 thus invalidating all previously
written keys and resetting the AES core.


All rights reserved - ©2011 Thomas Ruschival avs_aes_doc (v. 0.8) - 2011/05/15
and opencores.org


**AES** **128/192/256** **(ECB)** **A** **VALON** **[®]** **-MM** **S** **LAVE** **6/** **15**

|Offset|Name|Description|
|---|---|---|
|31-8|—|reserved|
|7|KEY_VALID|If asserted key data in the KEY memory range is regarded valid and will<br>be expanded to round keys. When deasserted all keys are invalidated<br>and the current operation of the core is aborted. It must be asserted<br>as long as the key shall be used for either encryption or decryption.<br>This bit must be cleared for one clock cycle to load a new key.|
|6|IRQ_ENA|Enable use of the interrupt request signal. If asserted the component<br>will set IRQ after completing an operation. If not set the component<br>operates in polling mode only.|
|5-2|—|reserved|
|1|DEC ~~1~~|If asserted memory content of the DATA range is regarded to be valid<br>and will be_ decrypted_. This Bit shall only be deasserted externally if a<br>running AES operation is aborted by deasserting KEY_VALID. 1 It will<br>be set 0 by the core to signal completion of the operation.|
|0|ENC ~~1~~|If asserted memory content of the DATA range is regarded to be valid<br>and will be_ encrypted_. This Bit shall only be deasserted externally if a<br>running AES operation is aborted by deasserting KEY_VALID. It will be<br>set 0 by the core to signal completion of the operation.|



Table 4: Bits in the control register

##### **4 Protocol Sequence**


The AES component appears as memory mapped peripheral. All writes are fundamental slave
write transfers, see [4] and take one clock cycle of the Avalon [®] bus clock clk . It is not necessary
to write all words of a input parameter successively or in one transfer. Bursts are not supported.


Before any AES operation can be started the initial user key has to be written to KEY segment of
the memory map.After the user key is transferred to the component the KEY_VALID Bit must be
set to start the key expansion. This Bit can be set simultaneously with DEC or ENC Bit of the control
register. To invalidate the previous key and use another key the KEY_VALID must be deasserted
for at least one Avalon [®] bus clock cycle During this cycle the new key can already be transferred.


Once a key is passed and marked valid data blocks can be transferred to the DATA segment
of the memory map. The AES operation is started by asserting the ENC Bit for encryption or DEC
Bit for decryption. While asserting ENC or DEC the KEY_VALID Bit must be kept asserted.
The ENC or DEC Bit respectively is deasserted by the component after completing the requested
operation. The result of the operation can be read from the RESULT area of the memory and is
not cleared. It will be overwritten by succeeding operations.


The underlying AES core uses the Finite State Machine (FSM) shown in 1 for processing of the
data. The signals data_stable and key_stable are accessible over the control status word CTRL
3.1. key_ready is a signal driven by the key generator when all keys are expanded. The signal


1 ENC and DEC are mutually exclusive and must not be asserted simultaneously.


avs_aes_doc (v. 0.8) - 2011/05/15 All rights reserved - ©2011 Thomas Ruschival
and opencores.org


**AES** **128/192/256** **(ECB)** **A** **VALON** **[®]** **-MM** **S** **LAVE** **7/** **15**


round_index is the counter for the rounds and the address to select a round key.
NO_ROUNDS is the total number of rounds the processing takes, a constant defined by the generic
KEYLENGTH 2.1. The AES standard in[1] defines 10 rounds for 128 Bit key, 12 rounds for a 192
Bit key and 14 rounds for a 265 Bit key.
Thus depending on the key length the processing of a data block needs at maximum 15 clock
cycles from data_stable=1 to completion, if the key is already expanded.


Figure 1: Finite State Machine of encryption and decryption process


**4.1** **Interrupt Behavior**


By setting IRQ_ENA in the control register 3.1 the component is configured to issue interrupt
requests. If IRQ_ENA is asserted the interrupt request IRQ 2.2 will be set when the computation
has completed in addition to clearing the ENC or DEC Bit. The IRQ 2.2 signal will remain set until
clearing IRQ_ENA or a read operation on the RESULT area of the components address range.

##### **5 The Inner Core**


The algorithmic core is divided into two separate data paths one for encryption and a second for
decryption operation. The two data paths are independent, however they share the keyexpansion component which provides decrypt and encrypt keys (which are the same only in opposite


All rights reserved - ©2011 Thomas Ruschival avs_aes_doc (v. 0.8) - 2011/05/15
and opencores.org


**AES** **128/192/256** **(ECB)** **A** **VALON** **[®]** **-MM** **S** **LAVE** **8/** **15**


order). Each data path is controlled by its own FSM. If configured by the generic DECRYPTION 2.1
the decryption data path is included and some multiplexers are generated for the shared signals,
e.g. result or roundkey_index .
For reference the encryption data path of aes_core.vhd is given in figure 2. The decryption data
path is left for the reader or any other author of this document.


avs_aes_doc (v. 0.8) - 2011/05/15 All rights reserved - ©2011 Thomas Ruschival
and opencores.org


**AES** **128/192/256** **(ECB)** **A** **VALON** **[®]** **-MM** **S** **LAVE** **9/** **15**

|[23:16]|[15:8]|Col3|[7:0]|
|---|---|---|---|
|sbox(0)<br>(Highword)|sbox(0)<br>(Highword)|sbox(0)<br>(LowWord)|sbox(0)<br>(LowWord)|
|[23:16]|[15:8]|[15:8]|[7:0]|


|Col1|[15:8]|Col3|[7:0]|
|---|---|---|---|
|sbox(3)<br>(Highword)|sbox(3)<br>(Highword)|sbox(3)<br>(LowWord)|sbox(3)<br>(LowWord)|
|sbox(3)<br>(Highword)|[15:8]|[15:8]|[7:0]|



Figure 2: Encrypt data path of the AES core as implemented in aes_core.vhd


All rights reserved - ©2011 Thomas Ruschival avs_aes_doc (v. 0.8) - 2011/05/15
and opencores.org


**AES** **128/192/256** **(ECB)** **A** **VALON** **[®]** **-MM** **S** **LAVE** **10/** **15**

##### **6 Throughput Calculation**


The Avalon [®] interface communicates a 32-Bit DWORD per clock cycle. Therefore a key is transmitted in 4 to 8 cycles plus one cycle to activate keyexpansion with the control word 3.1. A
payload data block or the result consist always of 4 DWORDs, thus it takes 4 cycles to send data
to the core, one cycle to activate the computation with the control register 3.1 and 4 cycles to
retrieve the data.


The keyexpansion component computes one column of a roundkey in two clock cycles. In the
first cycle the column is substituted throught the s-box, in the second cycle the shift-operation
is executed. AES specifies [1], depending on the key length _N_ _roundkeys_ = _{_ 10, 12, 14 _}_ roundkeys
with 4 columns each. The FSM of the keyexpansion module adds o clockcycle for the “DONE”

state.
_T_ _keyexpansion_ ( _N_ _roundkeys_ ) = 2 · 4 · _N_ _roundkeys_ + 1 (1)


The keyexpansion therefore takes 81, 97 or 115 clockcycles until the encryption or decryption
can start. The roundkeys are stored until invalidated, see 4 thus this step is is only needed once
after power-up until the key changes.


The AES core computes one iteration (round) of the Rijndael-Algorithm each clock cycle, thus a
128 Bit data block is encrypted or decrypted in 10, 12 or 14 cycles plus an initial round.


The maximum throughput _T_ _max_ [ _Bits_ ] depends on the maximum operation frequency _f_ _max_ and the
key length which influences the number of rounds _N_ _rnd_ _ϵ{_ 10, 12, 14 _}_ .


_T_ _max_ = [(][1 +] _[ N]_ _[rnd]_ [)][ · 128] _[Bit]_ (2)

_f_ _max_


Note: Equation 2 assumes that the roundkeys are already generated and does not include the
constant of 4+1+4 Avalon [®] bus cycles for transmission of data, activation and result retrieval.


avs_aes_doc (v. 0.8) - 2011/05/15 All rights reserved - ©2011 Thomas Ruschival
and opencores.org


**AES** **128/192/256** **(ECB)** **A** **VALON** **[®]** **-MM** **S** **LAVE** **11/** **15**

##### **7 FPGA implementations**


The component has only be implemented and tested on an Altera [®] Cyclone-II EP2C35 FPGA.
For this setup a Makefile is provided in ./sys/Altera_Quartus9.1 . All other values in the table
are only results of synthesis [0] and are not verified on actual hardware.


The design is kept vendor independent in generic VHDL. AES SubByte component is specially
designed using M4K block RAM as dual-port ROM. For non-Altera [®] FPGAs a second VHDL
architecture exists also trying to make use of ROM functions of the target chips however the
success varies on RTL compiler capabilities. Later versions of Altera [®] Quartus-II [®] show the
same results whether M4K blocks are used or the generic version in selected.






























|Configuration|Target FPGA1|LE / Slices|HW RAM|f [Mhz]<br>max|
|---|---|---|---|---|
|256 Bit Key,<br>encrypt + decrypt|Xilinx® Spartan3A<br>XC3S1400A-5FG484<br>|- / 1609|18 RAMB16BWE|91|
|256 Bit Key,<br>encrypt + decrypt|Xilinx~~® ~~Virtex5<br>XC5VLX30-3FF324<br>|- / 297|18 18k-Blocks<br>4 36k-Blocks|224|
|256 Bit Key,<br>encrypt + decrypt|Altera~~® ~~Cyclone-II<br>EP2C35F484C8<br>|1937 / -|39912 Bits<br>in<br>22 M4K-Blocks|65|
|256 Bit Key,<br>encrypt + decrypt|Altera~~® ~~StratixII<br>EP2S30F484C5<br>|585 / -|39912 Bits<br>in<br>22 M4K-Blocks|103|
|128 Bit Key,<br>encrypt + decrypt|Xilinx® Spartan3A<br>XC3S1400A-5FG484<br>|- / 1523|18 RAMB16BWE|91|
|128 Bit Key,<br>encrypt + decrypt|Altera~~® ~~Cyclone-II<br>EP2C35F484C8<br>|1776 / -|39912 Bits<br>in<br>22 M4K-Blocks|65|
|256 Bit Key,<br>encrypt|Xilinx® Spartan3A<br>XC3S1400A-5FG484<br>|- / 680|14 RAMB16BWE|159|
|256 Bit Key,<br>encrypt|Xilinx~~® ~~Virtex5<br>XC5VLX30-3FF324<br>|- / 297|10 18k-Blocks<br>4 36k-Blocks|268|
|256 Bit Key,<br>encrypt|Altera~~® ~~Cyclone-II<br>EP2C35F484C8<br>|969 / -|22528 Bits<br>in<br>14 M4K|97|
|256 Bit Key,<br>encrypt|Altera~~® ~~StratixII<br>EP2S30F484C5<br>|524 / -|22528 Bits<br>in<br>14 M4K|145|
|128 Bit Key,<br>encrypt|Xilinx® Spartan3A<br>XC3S1400A-5FG484<br>|- / 594|14 RAMB16BWE|159|
|128 Bit Key,<br>encrypt|Altera~~® ~~Cyclone-II<br>EP2C35F484C8|797 / -|22528 Bits<br>in<br>14 M4K|95|



Table 5: ressource usage on different targets and configuration


All configurations in table 7 use hardware key expansion. Downloading of software generated
roundkeys is not yet supported. The decryption and encryption data paths share a common
keyexpansion block, multiplexing the address signals is one of the main reasons for regression
of the maximum frequency _f_ _max_ of the configuration compared to encryption only versions.


0 Synthesized with Altera ® Quartus-II ® Web edition Version 9.1 or Xilinx ® ISE 9.1 Webpack
1 This table is not meant to be a benchmark between FPGAs of different vendors, it is only a rough estimation for
the user of the core. The FPGA families cannot be compared easily, see also [5] and [6]for further details.


All rights reserved - ©2011 Thomas Ruschival avs_aes_doc (v. 0.8) - 2011/05/15
and opencores.org


**AES** **128/192/256** **(ECB)** **A** **VALON** **[®]** **-MM** **S** **LAVE** **12/** **15**

##### **8 Simulation**


**8.1** **Testbench**


In ./bench/VHDL/ a “self-checking testbench” is provided which runs tests for a default TESTKEYSIZE
is 256 Bit . For different key lengths the constant TESTKEYSIZE has to be changed appropriately.
Expected results for all test cases and key lengths are included. The expected results were
generated by AES Calculator applet, written by Lawrie Brown from ADFA, Canberra Australia

[7]. The testbench consists of a sequence of 5 test cases:


1. load key1, load data1, encrypt : (basic encryption test)


2. key1, data1, decrypt: (basic decryption test)


3. key1, data1, encrypt: (test if internal state was changed)


4. key1, data2, encrypt: (encryption test with new data)


5. key2, data2, encrypt: (encryption test with new key)


**8.2** **Simulation**


The component library is “ avs_aes_lib ”. All files are expected to be compiled into this library as
all files depend at least on the package avs_aes_lib.avs_aes_pkg .
A Makefile for Mentor Graphics [®] Modelsim [®] is given in ./sim/ . The default make target simaes
will create the library “ avs_aes_lib ” and a “ work ” library, compile all files and run a testbench.

##### **9 Software Driver**


This AES Core Avalon [®] slave was also tested on a NiosII [®] processor. To use it in software a
simple driver is provided in ./sw/ among with an example program of the basic usage. The
driver consist of the two files avs_aes.c and avs_aes.h . Find more detailed description in the
doxygen documentation in ./doc/sw/html .


**9.1** **Configuration**


To be adapted to different address mappings and key sizes two macros are use in avs_aes.h :

|define|default|Description|
|---|---|---|
|KEYWORDS|8|Key size in 32 Bit words|
|AES_BASEADDR|0x40000|Base address at which the AES Core is mapped to the<br>Avalon® switch-fabric|



Table 6: user changeable macros in header


avs_aes_doc (v. 0.8) - 2011/05/15 All rights reserved - ©2011 Thomas Ruschival
and opencores.org


**AES** **128/192/256** **(ECB)** **A** **VALON** **[®]** **-MM** **S** **LAVE** **13/** **15**

##### **10 License and Liability**


The “AES 128/192/256 (ECB) Avalon [®] -MM Slave” component, all its subcomponents and documentation (like this document you are reading) are published under following license:


Copyright (c) 2009, Thomas Ruschival - All rights reserved.


Redistribution and use in source and binary forms, with or without modification, are permitted
provided that the following conditions are met:


     - Redistributions of source code must retain the above copyright notice, this list of conditions
and the following disclaimer.


     - Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided
with the distribution.


    - Neither the name of the organization nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written permission.


THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS

"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.

IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY

DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE


Note: The term “SOFTWARE” in the above licence applies in this case not only to software as
executable code but also to documentation, hardware description or compiled netlists for actual
target hardware. As Chips generally don’t just reproduce “the above copyright notice, this list
of conditions and the following disclaimer in the documentation and/or other materials provided
with the distribution” the data sheet of the product must also contain it.


Altera, Cyclone-II, Stratix-II, Quartus, NIOS and Avalon are registered trademarks of the Altera
Corporation 101 Innovation Drive, San Jose CA USA
Xilinx, Spartan3A and Virtex5 are registered trademarks of Xilinx Inc. 2100 Logic Drive, San
Jose CA USA
Mentor Graphics and ModelSim are registered trademarks of Mentor Graphics Corporation 8005
SW Boeckman Road, Wilsonville OR USA


All rights reserved - ©2011 Thomas Ruschival avs_aes_doc (v. 0.8) - 2011/05/15
and opencores.org


**AES** **128/192/256** **(ECB)** **A** **VALON** **[®]** **-MM** **S** **LAVE** **14/** **15**

##### **Acronyms**


**AES**

Advanced Encryption Standard. 3


**ECB**


Electronic Code Book. 3


**FSM**


Finite State Machine. 6, 8, 10


**LSB**

Least Significant Bit. 4


**MSB**

Most Significant Bit. 4


**NIST**

National Institute of Standards and Technology. 3


**SoC**

System on Chip. 3

##### **References**


[1] “Fips-197 announcing the advanced encryption standard (aes),” National Institute of
Standards and Technology (NIST), 100 Bureau Drive, Stop 1070, Gaithersburg, MD, US,
[Nov. 2001. [Online]. Available: http://csrc.nist.gov/publications/fips/fips197/fips-197.pdf](http://csrc.nist.gov/publications/fips/fips197/fips-197.pdf)


[[2] “Wishbone - computer bus,” wikipedia.org. [Online]. Available: http://en.wikipedia.org/wiki/](http://en.wikipedia.org/wiki/Wishbone_computer_bus)#Comparisons)
[Wishbone_computer_bus)#Comparisons](http://en.wikipedia.org/wiki/Wishbone_computer_bus)#Comparisons)


[3] R. Herveille, “Wishbone soc architecture specification, revision b.3,” Opencores
Organization, Sept. 2002. [Online]. Available: [http://www.opencores.org/downloads/](http://www.opencores.org/downloads/wbspec_b3.pdf)
[wbspec_b3.pdf](http://www.opencores.org/downloads/wbspec_b3.pdf)


[4] “Avalon interface specification,” Altera Corporation, 101 Innovation Drive, San Jose, CA, US,
[2005. [Online]. Available: http://www.altera.com/literature/manual/mnl_avalon_spec.pdf](http://www.altera.com/literature/manual/mnl_avalon_spec.pdf)


[5] A. Percey, “Advantages of the virtex-5 fpga 6-input lut architecture,” Xilinx Inc.,
2100 Logic Drive, San Jose CA USA, Dec. 2007. [Online]. Available: [http:](http://www.xilinx.com/support/documentation/white_papers/wp284.pdf)
[//www.xilinx.com/support/documentation/white_papers/wp284.pdf](http://www.xilinx.com/support/documentation/white_papers/wp284.pdf)


[6] “Stratix iii fpgas vs. xilinx virtex-5 devices: Architecture and performance comparison,”
Altera Corporation, 101 Innovation Drive, San Jose CA USA, Oct. 2007. [Online]. Available:
[http://www.altera.com/literature/wp/wp-01007.pdf](http://www.altera.com/literature/wp/wp-01007.pdf)


[7] L. Brown, “Aes calculator,” ADFA, Canberra, Australia, 2005. [Online]. Available:
[http://www.unsw.adfa.edu.au/~lpb/src/AEScalc/index.html](http://www.unsw.adfa.edu.au/~lpb/src/AEScalc/index.html)


avs_aes_doc (v. 0.8) - 2011/05/15 All rights reserved - ©2011 Thomas Ruschival
and opencores.org


**AES** **128/192/256** **(ECB)** **A** **VALON** **[®]** **-MM** **S** **LAVE** **15/** **15**

##### **Change History**

|Rev.|Chapter|Description|Date|Reviewer|
|---|---|---|---|---|
|0.1<br>0.2<br>0.3<br>0.4<br>0.5<br>0.6<br>0.7<br>0.8|all<br>all<br>all<br>all<br>all<br>3,6<br>3,6<br>6|initial document<br>added interrupt<br>added generics<br>cleanup for opencores.org<br>ﬁnal release<br>ﬁxed memory map,<br>added test-<br>bench description<br>ﬁxed typos<br>corrected key schedule|2009/02/01<br>2009/03/25<br>2009/04/20<br>2009/05/20<br>2010/03/07<br>2010/04/02<br>2010/04/03<br>2011/05/15|T. Ruschival<br>T. Ruschival<br>T. Ruschival<br>T. Ruschival<br>T. Ruschival<br>T. Ruschival<br>T. Ruschival<br>T. Ruschival|



All rights reserved - ©2011 Thomas Ruschival avs_aes_doc (v. 0.8) - 2011/05/15
and opencores.org


