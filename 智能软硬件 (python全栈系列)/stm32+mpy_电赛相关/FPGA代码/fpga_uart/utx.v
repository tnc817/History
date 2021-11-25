`timescale 1ns / 1ps

// WARNING: Do NOT edit the input and output ports in this file in a text
// editor if you plan to continue editing the block that represents it in
// the Block Editor! File corruption is VERY likely to occur.

// Copyright (C) 2018  Intel Corporation. All rights reserved.
// Your use of Intel Corporation's design tools, logic functions
// and other software and tools, and its AMPP partner logic
// functions, and any output files from any of the foregoing
// (including device programming or simulation files), and any
// associated documentation or information are expressly subject
// to the terms and conditions of the Intel Program License
// Subscription Agreement, the Intel Quartus Prime License Agreement,
// the Intel FPGA IP License Agreement, or other applicable license
// agreement, including, without limitation, that your use is for
// the sole purpose of programming logic devices manufactured by
// Intel and sold by Intel or its authorized distributors.  Please
// refer to the applicable agreement for further details.


// Generated by Quartus Prime Version 18.0 (Build Build 614 04/24/2018)
// Created on Wed Jul 03 10:54:00 2019

//  Module Declaration
module utx
(
// {{ALTERA_ARGS_BEGIN}} DO NOT REMOVE THIS LINE!
clk, rst_n, data, tx_int, tx,busy
// {{ALTERA_ARGS_END}} DO NOT REMOVE THIS LINE!
);
// Port Declaration

// {{ALTERA_IO_BEGIN}} DO NOT REMOVE THIS LINE!
input clk;
input rst_n;
input [7:0] data;
input tx_int;
output tx;
output busy;
// {{ALTERA_IO_END}} DO NOT REMOVE THIS LINE!

wire bps_start2,clk_bps2;

assign busy = bps_start2;

///////////////////////////////////////////						
speed_select		speed_tx(	
							.clk(clk),	//波特率�?�择模块
							.rst_n(rst_n),
							.bps_start(bps_start2),
							.clk_bps(clk_bps2)
						);

my_uart_tx			my_uart_tx(		
							.clk(clk),	//发�?�数据模�?
							.rst_n(rst_n),
							.rx_data(data),
							.rx_int(tx_int),
							.rs232_tx(tx),
							.clk_bps(clk_bps2),
							.bps_start(bps_start2)
						);
endmodule
