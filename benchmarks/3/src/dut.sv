`timescale 1ns/10ps

module ariane_testharness (
    acc_ctrl, // Access control values
    acc_ctrl_c
); 

    parameter NB_PERIPHERALS = 4;
    parameter BIT_WIDTH = 2;  

    input logic [BIT_WIDTH*NB_PERIPHERALS-1 :0]   acc_ctrl; // Access control values
    output logic [BIT_WIDTH-1:0][NB_PERIPHERALS-1:0] acc_ctrl_c;

   genvar i, j;
   generate
       for (i=0; i < BIT_WIDTH; i++) begin
        for (j=0; j < NB_PERIPHERALS; j++) begin
           assign acc_ctrl_c[i][j] = acc_ctrl[j*BIT_WIDTH+i];
        end
       end 
   endgenerate 


endmodule
