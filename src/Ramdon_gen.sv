module Ramdon_gen(
Reset           ,
Clk             ,
Init            ,
RetryCnt        ,
Random_time_meet
);
input           Reset           ;
input           Clk             ;
input           Init            ;
input   [3:0]   RetryCnt        ;
output          Random_time_meet;
reg [9:0]       Random_sequence ;
reg [9:0]       Ramdom          ;
reg [9:0]       Ramdom_counter  ;
reg [7:0]       Slot_time_counter;
reg             Random_time_meet;
always @ (posedge Clk or posedge Reset)
    if (Reset) begin
        Random_sequence     <=0;
    end
    else begin
        Random_sequence     <={Random_sequence[8:0],~(Random_sequence[2]^Random_sequence[9])};
    end
always @ (RetryCnt or Random_sequence)
    case (RetryCnt)
        4'h0: begin
            Ramdom={9'b0,Random_sequence[0]};
        end
        4'h1: begin
            Ramdom={8'b0,Random_sequence[1:0]};
        end
        4'h2: begin
            Ramdom={7'b0,Random_sequence[2:0]};
        end
        4'h3: begin
            Ramdom={6'b0,Random_sequence[3:0]};
        end
        4'h4: begin
            Ramdom={5'b0,Random_sequence[4:0]};
        end
        4'h5: begin
            Ramdom={4'b0,Random_sequence[5:0]};
        end
        4'h6: begin
            Ramdom={3'b0,Random_sequence[6:0]};
        end
        4'h7: begin
            Ramdom={2'b0,Random_sequence[7:0]};
        end
        4'h8: begin
            Ramdom={1'b0,Random_sequence[8:0]};
        end
        4'h9: begin
            Ramdom={     Random_sequence[9:0]};
        end
        default: begin
            Ramdom={     Random_sequence[9:0]};
        end
    endcase
always @ (posedge Clk or posedge Reset)
    if (Reset) begin
        Slot_time_counter       <=0;
    end
    else if(Init) begin
        Slot_time_counter       <=0;
    end
    else if(!Random_time_meet) begin
        Slot_time_counter       <=Slot_time_counter+1;
    end
always @ (posedge Clk or posedge Reset)
    if (Reset) begin
        Ramdom_counter      <=0;
    end
    else if (Init) begin
        Ramdom_counter      <=Ramdom;
    end
    else if (Ramdom_counter!=0&&Slot_time_counter==255) begin
        Ramdom_counter      <=Ramdom_counter -1 ;
    end
always @ (posedge Clk or posedge Reset)
    if (Reset) begin
        Random_time_meet    <=1;
    end
    else if (Init) begin
        Random_time_meet    <=0;
    end
    else if (Ramdom_counter==0) begin
        Random_time_meet    <=1;
    end

endmodule
