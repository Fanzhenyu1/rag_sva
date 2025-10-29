`timescale 1ns/10ps

module register_lock (
    clk_i, 
    rst_i, 
    reglk_mem
); 


    parameter NO_WORDS = 3;
    parameter BIT_WIDTH = 2;  

    input logic                   clk_i;
    input logic                   rst_i;
    output reg [NO_WORDS-1:0][BIT_WIDTH-1:0] reglk_mem ; 


    integer j;
    always @(posedge clk_i)
    begin
        if(rst_i)
            begin
              for (j=0; j < NO_WORDS; j=j+1) begin
                reglk_mem[j] <= {BIT_WIDTH{ 1'b1 }};
              end
            end
    end

endmodule
