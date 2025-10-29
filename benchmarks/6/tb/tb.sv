`timescale 1ns/10ps

module tb(); 

    // all inputs, output, and internal registers of DUT
    reg clk, rst; 
    logic [2:0] csr_op_i;  
    reg [1:0] priv_lvl_o;
    reg [1:0] priv_lvl; 
    reg privilege_violation ; 

    parameter CSR_WRITE = 2;
    parameter CSR_SET = 3; 
    parameter CSR_CLEAR = 4; 
    parameter CSR_READ = 5;

    localparam NO_DUT_SIGNALS = 8; 
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
    
    assign test_data_curr = test_data[NO_CLOCKS-1 +: NO_DUT_SIGNALS];
   
    assign csr_op_i             = test_data_curr[7:5];
    assign priv_lvl_o           = test_data_curr[4:3];
    assign priv_lvl             = test_data_curr[2:1];
    assign privilege_violation  = test_data_curr[0];

endmodule
