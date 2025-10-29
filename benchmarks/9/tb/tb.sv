`timescale 1ns/10ps

module tb(); 

    parameter MIN_CYCLES = 1;
    parameter MAX_CYCLES = 2;

    // all inputs, output, and internal registers of DUT
    reg clk, rst; 
    logic rst_i; 
    logic por_n_i;
    logic rst_por_aon_n; 


    localparam NO_DUT_SIGNALS = 3; 
    localparam NO_CLOCKS = 4; 
    localparam CTR_WIDTH = (NO_DUT_SIGNALS*NO_CLOCKS) + 2; 
                // + 3 to keep track of when to update counter

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
    
    assign test_data_curr = test_data[2:0] == 3'h3 ? test_data[(3*NO_DUT_SIGNALS)+2 +: NO_DUT_SIGNALS]  :
                            test_data[2:0] == 3'h2 ? test_data[(2*NO_DUT_SIGNALS)+2 +: NO_DUT_SIGNALS]  :
                            test_data[2:0] == 3'h1 ? test_data[(1*NO_DUT_SIGNALS)+2 +: NO_DUT_SIGNALS]  :
                                                     test_data[(0*NO_DUT_SIGNALS)+2 +: NO_DUT_SIGNALS];

    assign rst_i          = test_data_curr[2]   ;
    assign por_n_i        = test_data_curr[1]   ;
    assign rst_por_aon_n  = test_data_curr[0] ;

endmodule
