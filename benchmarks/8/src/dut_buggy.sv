`timescale 1ns/10ps

module adc_ctrl_fsm (
  input clk_aon_i, 
  input rst_aon_ni, 
  input cfg_fsm_rst_i
); 

  parameter BIT_WIDTH = 4; 

  logic [BIT_WIDTH-1:0] wakeup_timer_cnt_q; 

  always_ff @(posedge clk_aon_i or negedge rst_aon_ni) begin
    if (!rst_aon_ni) begin
      wakeup_timer_cnt_q    <= '0;
    end
    else if (wakeup_timer_cnt_clr || cfg_fsm_rst_i || trigger_h2l) begin
      wakeup_timer_cnt_q <= '1;
    end else begin
      wakeup_timer_cnt_q <= wakeup_timer_cnt_d;
    end
  end


endmodule
