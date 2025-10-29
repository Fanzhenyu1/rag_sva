`timescale 1ns/10ps

module tb(); 

    // all inputs, output, and internal registers of DUT
    reg clk, rst; 
    reg pass_mode; 
    reg dmi_req_ready;
    reg dmi_req_valid;
    reg pass_check, we_flag;
    reg dmi_access; 

    localparam NO_DUT_SIGNALS = 6; 
    localparam NO_CLOCKS = 1; 
    localparam CTR_WIDTH = (NO_DUT_SIGNALS*NO_CLOCKS) + (NO_CLOCKS-1); 
                // + NO_CLOCKS-1 to keep track of when to update counter

    // generate clock and reset
    initial begin 
        clk = 'b0; 
        rst = 'b1; 
        #18 rst = 'b0; 
    end
    always #5 clk <= ~clk; 
    
    // generate tests
    reg [CTR_WIDTH-1:0] test_data; 
    wire [NO_DUT_SIGNALS-1:0] test_data_curr; 
    always @(posedge clk) begin
        if (rst) begin
            test_data <= 'b0; 
        end else begin
            if (test_data == {CTR_WIDTH{ 1'b1}}) begin // stop since all inputs are tested
                #5 $display("Testing done, no inputs=%d", test_data+1); 
                $finish; 
            end else begin 
                #5 test_data <= test_data + 1; 
            end 
        end
    end
    
    assign test_data_curr =  test_data[NO_CLOCKS-1 +: NO_DUT_SIGNALS];
    
    assign pass_mode   = test_data_curr[5]; 
    assign dmi_req_ready       = test_data_curr[4]; 
    assign dmi_req_valid       = test_data_curr[3]; 
    assign pass_check       = test_data_curr[2]; 
    assign we_flag       = test_data_curr[1]; 
    assign dmi_access    = test_data_curr[0]; 

endmodule
