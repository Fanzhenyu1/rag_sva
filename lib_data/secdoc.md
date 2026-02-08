### A simple register lock module. "threat model": ["The register (named data) cannot be modified when the lock signal is on."]. "security property": "at every positive edge of clock, the value of the data register is same as its value in the previous clock cycle if the value of the lock signal in the previous clock cycle is 1".

### A simple traffic controller. Traffic changes from red -> green -> yellow -> red. "threat model": ["Traffic controller skips yellow before going red when walk button is pressed on green"]. "security property": "at every positive edge of clock, if the value of the signal register is RED, then the value of the signal register in the previous clock cycle is either RED or YELLOW".

### JTAG module in cva6 processor. It is locked with a password by default. "threat model": ["Able to 'write' to locked JTAG"]. "security property":"at every positive edge of clock, the value of the dmi_req_valid signal is 0 if the value of the pass_check signal is 0".

### Access control bus in cva6 processor, "threat model": ["Access to HMAC peripheral grants it access to PKT peripheral"], "security property": " at every positive edge of clock, for each of the PRIV_TYPES number of privilege arrays in the acc_ctrl_c matrix, the value of each of the NB_PERIPHERALS number of peripherals is same as the corresponding bit in the acc_ctrl array where the value for the ith privilege type of the jth peripheral is stored in the (j*PRIV_TYPES + i)th bit".

### AES accelerator, "threat model": ["Internal register of AES are visible externally"], "security property":" at every positive edge of clock, the value of the rdata signal is 0 if the value of ct_valid signal is 0 and the value of the address is greater than or equal to 12 and less than or equal to 15 and the value of the en signal is 1".

### AES accelerator, "threat model": ["Secret keys are not cleared when entering debug mode"], "security property":" at every positive edge of clock, the value of the key_big2 signal is 0 if the value of the debug_mode_i signal is 1 in the current clock cycle and 0 in the past clock cycle".

### CSR controller of CVA6 processor, "threat model": ["Access to privileged CSR"], "security property": "at every positive edge of clock, the value of the privilege_violation signal is 1 if any bit of the priv_lvl_o signal is 0 while the corresponding bit of the priv_lvl signal is 1 and the value of the csr_op_i signal is among the four values CSR_WRITE, CSR_SET, CSR_CLEAR, CSR_READ".

### Register lock feature, "threat model": ["Incorrect default values"], "security property": "at every positive edge of clock, all the BIT_WIDTH number of bits of each of the NO_WORDS number of elements in the reglk_mem array are set to 1 if the rst signal in the previous clock cycle is 1.".

### ADC controller, "threat model": ["Wakeup timer is incorrectly configured at reset"], "security property": "at every positive edge of clock other than when the rst_i signal is 0, the value of the wakeup_timer_cnt_q signal is 0 in the next clock cycle if the value of the cfg_fsm_rst_i signal in this clock cycle is 1".

### Reset manager, "threat model": ["No reset even after maximum clock cycles of input trigger"], "security property": " at every positive edge of clock other than when the rst_i signal is 1, if the por_n_i signal falls, then in a minimum of MIN_CYCLES clock cycles and a maximum of MAX_CYCLES clock cycles, the value of the por_n_i signal should become 1 or the value of the rst_por_aon_n signal should become 0".