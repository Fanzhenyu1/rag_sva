`timescale 1ns/10ps

module tb(); 

    parameter NO_WORDS = 3;
    parameter BIT_WIDTH = 2;

    // all inputs, output, and internal registers of DUT
    reg clk, rst; 
    reg debug_mode_i;
    reg [BIT_WIDTH*NO_WORDS-1:0] key_big2 ; 


    localparam NO_DUT_SIGNALS = BIT_WIDTH*NO_WORDS+1; 
    localparam NO_CLOCKS = 2; 
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
    
    assign test_data_curr = test_data[0] ? test_data[(1*NO_DUT_SIGNALS)+(NO_CLOCKS)-1 +: NO_DUT_SIGNALS]  : test_data[NO_CLOCKS-1 +: NO_DUT_SIGNALS];
   
    assign debug_mode_i   = test_data_curr[BIT_WIDTH*NO_WORDS];
    assign key_big2       = test_data_curr[BIT_WIDTH*NO_WORDS-1:0] ;


endmodule
