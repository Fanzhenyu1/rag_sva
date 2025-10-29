import ariane_pkg::*;

module dmi_jtag (
    input  logic         clk_i,      // DMI Clock
    input  logic         rst_ni,     // Asynchronous reset active low
    input  logic         testmode_i,
    input  logic [31:0]  jtag_key, // key for jtag

    output logic         dmi_rst_no, // hard reset
    output dm::dmi_req_t dmi_req_o,
    output logic         dmi_req_valid_o,
    input  logic         dmi_req_ready_i,

    input dm::dmi_resp_t dmi_resp_i,
    output logic         dmi_resp_ready_o,
    input  logic         dmi_resp_valid_i,

    input  logic         tck_i,    // JTAG test clock pad
    input  logic         tms_i,    // JTAG test mode select pad
    input  logic         trst_ni,  // JTAG test reset pad
    input  logic         td_i,     // JTAG test data input pad
    output logic         td_o,     // JTAG test data output pad
    output logic         tdo_oe_o, // Data out output enable
    output logic         umode_o   // Sets the processor to machine mode 
);

    typedef enum logic [1:0] {
                                DMINoError = 2'h0, DMIReservedError = 2'h1,
                                DMIOPFailed = 2'h2, DMIBusy = 2'h3
                             } dmi_error_t;

    enum logic [2:0] { Idle, Read, WaitReadValid, Write, WaitWriteValid } state_d, state_q;


    always_comb begin
        error_dmi_busy = 1'b0;
        // default assignments
        state_d   = state_q;
        address_d = address_q;
        data_d    = data_q;
        error_d   = error_q;

        dmi_req_valid = 1'b0;

        case (state_q)
            Idle: begin
                // make sure that no error is sticky
                if (dmi_access && update_dr && (error_q == DMINoError)) begin
                    // save address and value
                    address_d = dmi.address;
                    data_d = dmi.data;
                    if ((dm::dtm_op_t'(dmi.op) == dm::DTM_READ) && (pass_chk == 1'b1)) begin
                        state_d = Read;
                    end else if ((dm::dtm_op_t'(dmi.op) == dm::DTM_WRITE)) begin
                        state_d = Write;
                    end else if (dm::dtm_op_t'(dmi.op) == dm::DTM_PASS) begin
                        state_d = Read; 
                        if (data_d == pass) begin //checks password
                            pass_chk = 1'b1;    
                        end
                    end
                    // else this is a nop and we can stay here
                end
            end

            Read: begin
                dmi_req_valid = 1'b1;
                if (dmi_req_ready) begin
                    state_d = WaitReadValid;
                end
            end

            WaitReadValid: begin
                // load data into register and shift out
                if (dmi_resp_valid) begin
                    data_d = dmi_resp.data;
                    state_d = Idle;
                end
            end

            Write: begin
                dmi_req_valid = 1'b1;
                // got a valid answer go back to idle
                if (dmi_req_ready) begin
                    state_d = Idle;
                end
            end

            WaitWriteValid: begin
                // just wait for idle here
                if (dmi_resp_valid) begin
                    state_d = Idle;
                end
            end
        endcase

    end

endmodule

