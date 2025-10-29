`timescale 1ns/10ps

module tb(); 

    // all inputs, output, and internal registers of DUT
    reg clk, rst; 
    reg lock;

    reg data; 

    localparam NO_DUT_SIGNALS = 2; 
    localparam NO_CLOCKS = 2; 
    localparam CTR_WIDTH = (NO_DUT_SIGNALS*NO_CLOCKS) + (NO_CLOCKS-1); 
                // + NO_CLOCKS-1 to keep track of when to update counter

    initial begin 
        clk = 'b0; 
        rst = 'b1; 
        #18 rst = 'b0; 
    end
    always #5 clk <= ~clk; 
    
    // generate tests
    reg [(2*6):0] test_data; // size is twice no of signals + 1 (bcz increment only after two cycles)
    wire [(6)-1:0] test_data_curr; 
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
    
    assign test_data_curr = test_data[0] ? test_data[(1*NO_DUT_SIGNALS)+(NO_CLOCKS)-1 +: NO_DUT_SIGNALS]  : test_data[NO_CLOCKS-1 +: NO_DUT_SIGNALS];
    
    assign data       = test_data_curr[1]; 
    assign lock       = test_data_curr[0]; 

endmodule
