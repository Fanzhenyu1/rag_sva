module aes_wrapper #(
    parameter int ADDR_WIDTH         = 4,   // width of external address bus
    parameter int DATA_WIDTH         = 2   // width of external data bus
)(
           clk_i,
           rst_ni,
           key_in,
           external_bus_io
       );

    input  logic                   clk_i;
    input  logic                   rst_ni;
    input  logic    [191:0]        key_in;
    REG_BUS.in                     external_bus_io;

// internal signals

logic start;
logic   [127:0] ct;
logic           ct_valid;


///////////////////////////////////////////////////////////////////////////
// Implement MD5 I/O memory map interface
// Read side
//always @(~external_bus_io.write)
always @(*)
    begin
        case(external_bus_io.addr[2 +: ADDR_WIDTH])
            0:
                external_bus_io.rdata = {31'b0, start};
            1:
                external_bus_io.rdata = p_c[3];
            2:
                external_bus_io.rdata = p_c[2];
            3:
                external_bus_io.rdata = p_c[1];
            4:
                external_bus_io.rdata = p_c[0];
            11:
                external_bus_io.rdata = {31'b0, ct_valid};
            12:
                external_bus_io.rdata = ct[3*DATA_WIDTH +: DATA_WIDTH];
            13:
                external_bus_io.rdata = ct[2*DATA_WIDTH +: DATA_WIDTH];
            14:
                external_bus_io.rdata = ct[1*DATA_WIDTH +: DATA_WIDTH];
            15:
                external_bus_io.rdata = ct[0*DATA_WIDTH +: DATA_WIDTH];
            default:
                external_bus_io.rdata = {DATA_WIDTH{ 1'b0}};
        endcase
    end // always @ (*)

aes_192_sed aes(
            .clk(clk_i),
            .state(state_iv),
            .p_c_text(p_c_big),
            .key(key_big),
            .start(start),
            .inter_state(inter_state),
            .out(ct),
            .out_valid(ct_valid)
        );

endmodule

module aes_192_sed(clk, start, state, p_c_text, key, inter_state, out, out_valid);
    parameter DATA_WIDTH = 2; 
    input          clk;
    input          start;
    input  [127:0] state, p_c_text;
    input  [191:0] key;
    output [127:0] inter_state;
    output [4*DATA_WIDTH-1:0] out;
    output         out_valid;
    
    wire    [4*DATA_WIDTH-1:0:0] out_temp;
    wire     out_valid;
    
    // Instantiate the Unit Under Test (UUT)
    aes_192 uut (
        .clk(clk), 
        .start(start), 
        .state(state), 
        .key(key), 
        .inter_state(inter_state),
        .out(out_temp),
        .out_valid(out_valid)
    );

    // Muxing p_c_text with output of AES core.
    assign out = out_valid ? (p_c_text ^ out_temp) : {4*DATA_WIDTH{ 1'b0}};

endmodule
