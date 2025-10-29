`timescale 1ns/10ps

module csr_regfile (
    priv_lvl_o, // Access control values
    priv_lvl,
    privilege_violation
); 


    input logic [1:0] priv_lvl_o;
    input logic [1:0] priv_lvl; 
    output logic privilege_violation ; 

    // ---------------------------
    // CSR OP Select Logic
    // ---------------------------
    always_comb begin : csr_op_logic
        csr_wdata = csr_wdata_i;
        csr_we    = 1'b1;
        csr_read  = 1'b1;
        mret      = 1'b0;
        sret      = 1'b0;
        dret      = 1'b0;

        unique case (csr_op_i)
            CSR_WRITE: csr_wdata = csr_wdata_i;
            CSR_SET:   csr_wdata = csr_wdata_i | csr_rdata;
            CSR_CLEAR: csr_wdata = (~csr_wdata_i) & csr_rdata;
            CSR_READ:  csr_we    = 1'b0;
            SRET: begin
                // the return should not have any write or read side-effects
                csr_we   = 1'b0;
                csr_read = 1'b0;
                sret     = 1'b1; // signal a return from supervisor mode
            end
            MRET: begin
                // the return should not have any write or read side-effects
                csr_we   = 1'b0;
                csr_read = 1'b0;
                mret     = 1'b1; // signal a return from machine mode
            end
            DRET: begin
                // the return should not have any write or read side-effects
                csr_we   = 1'b0;
                csr_read = 1'b0;
                dret     = 1'b1; // signal a return from debug mode
            end
            default: begin
                csr_we   = 1'b0;
                csr_read = 1'b0;
            end
        endcase
        // if we are retiring an exception do not return from exception
        if (ex_i.valid) begin
            mret = 1'b0;
            sret = 1'b0;
            dret = 1'b0;
        end
    end

    always_comb begin : privilege_check
        // -----------------
        // Privilege Check
        // -----------------
        // if we are reading or writing, check for the correct privilege level
        // this has
        // precedence over interrupts
        privilege_violation = 1'b0;
        if (csr_we || csr_read) begin
            if ((priv_lvl_o & priv_lvl) != priv_lvl) && !(csr_addr.address==riscv::CSR_MEPC)) begin   
                privilege_violation = 1'b1;
                csr_exception_o.cause = riscv::ILLEGAL_INSTR;
            end
            // check access to debug mode only CSRs
            if (csr_addr_i[11:4] == 8'h7b && !debug_mode_q) begin
                privilege_violation = 1'b1;
                csr_exception_o.cause = riscv::ILLEGAL_INSTR;
            end
        end
    end


endmodule

