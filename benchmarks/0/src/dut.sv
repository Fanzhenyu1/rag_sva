`timescale 1ns/10ps

module lock_reg (
    input data_in, 
    output data_out, 
    input r_en, 
    input w_en, 
    input lock,
    input clk, 
    input rst
); 

reg data; 

always @ (posedge clk) begin
    if (rst) begin
        data <= #1 0; 
    end
    else begin
        if (w_en)
            data <= #1 lock ? data: data_in; 
    end
end

assign data_out = r_en ? data : 'b0; 

endmodule
