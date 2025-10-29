`timescale 1ns/10ps

module tb(); 

    parameter ADDR_WIDTH = 4;
    parameter DATA_WIDTH = 2; 

    // all inputs, output, and internal registers of DUT
    reg clk, rst; 
    logic ct_valid;
    logic [ADDR_WIDTH-1:0] address; 
    logic en; 
    logic [DATA_WIDTH-1:0] rdata ; 


    localparam NO_DUT_SIGNALS = ADDR_WIDTH+DATA_WIDTH+2; 
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
    
    //assign test_data_curr = test_data[0] ? test_data[(1*NO_DUT_SIGNALS)+(NO_CLOCKS)-1 +: NO_DUT_SIGNALS]  : test_data[NO_CLOCKS-1 +: NO_DUT_SIGNALS];
    assign test_data_curr = test_data[NO_CLOCKS-1 +: NO_DUT_SIGNALS];
  
    assign en             = test_data_curr[DATA_WIDTH+ADDR_WIDTH+1]; 
    assign ct_valid       = test_data_curr[DATA_WIDTH+ADDR_WIDTH]; 
    assign address        = test_data_curr[DATA_WIDTH +: ADDR_WIDTH]; 
    assign rdata          = test_data_curr[DATA_WIDTH-1:0] ;

endmodule
