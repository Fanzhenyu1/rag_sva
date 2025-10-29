`timescale 1ns/10ps

module traffic_controller (
    input walk, 
    output reg [1:0] signal, 
    input clk, 
    input rst
); 

localparam RED = 0;
localparam GREEN = 1;
localparam YELLOW = 2;
localparam WALK_TIME = 4; 

reg [2:0] walk_ctr; 


// red - yellow - green control FSM
always @ (posedge clk) begin
    if (rst) begin
        signal <= #1 RED; 
    end
    else begin
        case (signal)
            RED: begin
                if (walk) begin
                    signal <= #1 RED; 
                end
                else if (walk_ctr != 'b0) begin
                    signal <= #1 RED; 
                end
                else
                    signal <= #1 GREEN; 
            end
            GREEN: begin
                if (walk) begin
                    signal <= #1 RED; 
                end
                else
                    signal <= #1 YELLOW; 
            end
            YELLOW: begin
                signal <= #1 RED; 
            end
            default: 
                signal <= #1 RED; 
        endcase
    end
end

// walk counter
always @ (posedge clk) begin
    if (rst) begin
        walk_ctr <=  #1 'b0;  
    end
    else begin
        if (walk) begin
            walk_ctr <= #1 WALK_TIME; 
        end
        else if (signal == RED) begin
            walk_ctr <= #1 (walk_ctr == 'b0) ? 'b0 : walk_ctr - 1; 
        end
    end
end


endmodule
