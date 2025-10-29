module aes_wrapper #(
    parameter int ADDR_WIDTH         = 32,   // width of external address bus
    parameter int DATA_WIDTH         = 2   // width of external data bus
)(
           clk_i,
           rst_ni,
           key_in,
           debug_mode_i, 
           external_bus_io
       );

    input  logic                   clk_i;
    input  logic                   rst_ni;
    input  logic    [191:0]        key_in;
    input  logic                   debug_mode_i;
    REG_BUS.in                     external_bus_io;

// internal signals

parameter NO_WORDS = 3; 
parameter BIT_WIDTH = 2; 

logic start;
logic [31:0] p_c [0:3];
logic [31:0] state [0:3];
//logic [31:0] key [0:5];

logic   [127:0] p_c_big   ;   // = {p_c[0], p_c[1], p_c[2], p_c[3]};
logic   [127:0] state_big ;  // = {state[0], state[1], state[2], state[3]};
logic   [BIT_WIDTH*NO_WORDS-1:0] key_big ;  // = {key[0], key[1], key[2], key[3], key[4], key[5]};
logic   [127:0] inter_state; 
logic   [127:0] ct;
logic           ct_valid;
const logic   [127:0] state_iv = 127'h3243f6a8_885a308d_00000000_00000001; 


assign external_bus_io.ready = 1'b1;
assign external_bus_io.error = 1'b0;

assign p_c_big    = {p_c[0], p_c[1], p_c[2], p_c[3]};
assign state_big  = {state[0], state[1], state[2], state[3]};
//assign key_big    = {key[0], key[1], key[2], key[3], key[4], key[5]};
assign key_big    = debug_mode_i ? key_in;


endmodule

