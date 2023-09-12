`timescale 1ns / 1ps
//*************************************************************************
//   > 文件名: alu.v
//   > 描述  ：ALU模块，可做12种操作
//   > 作者  : LOONGSON
//   > 日期  : 2016-04-14
//*************************************************************************
module alu(
    input  [3:0] alu_control,  // ALU控制信号
    input  [31:0] alu_src1,     // ALU操作数1,为补码
    input  [31:0] alu_src2,     // ALU操作数2，为补码
    output [31:0] alu_result    // ALU结果
    );

    // ALU控制信号，独热码
    wire alu_add;   //1.加法操作
    wire alu_sub;   //2.减法操作
    wire alu_slt;   //3.有符号比较，小于置位，复用加法器做减法
    wire alu_sbt;   //4.有符号比较，大于置位，复用加法器做减法      1
    wire alu_sltu;  //5.无符号比较，小于置位，复用加法器做减法
    wire alu_and;   //6.按位与
    wire alu_nor;   //7.按位或非
    wire alu_or;    //8.按位或
    wire alu_xor;   //9.按位异或
    wire alu_sll;   //10.逻辑左移
    wire alu_srl;   //11.逻辑右移
    wire alu_sla;   //12.算数左移       1
    wire alu_sra;   //13.算术右移
    wire alu_lui;   //14.高位加载
    wire alu_ldi;   //15.低位加载      1

   //信号赋值
   assign alu_add = ~alu_control[3]&~alu_control[2]&~alu_control[1]&alu_control[0];//0001
   assign alu_sub = ~alu_control[3]&~alu_control[2]&alu_control[1]&~alu_control[0];//0010
   assign alu_slt = ~alu_control[3]&~alu_control[2]&alu_control[1]&alu_control[0];//0011
   assign alu_sbt=~alu_control[3]&alu_control[2]&~alu_control[1]&~alu_control[0];//0100;
   assign alu_sltu = ~alu_control[3]&alu_control[2]&~alu_control[1]&alu_control[0];//0101
   assign alu_and = ~alu_control[3]&alu_control[2]&alu_control[1]&~alu_control[0];//0110
   assign alu_nor = ~alu_control[3]&alu_control[2]&alu_control[1]&alu_control[0];//0111
   assign alu_or = alu_control[3]&~alu_control[2]&~alu_control[1]&~alu_control[0];//1000
   assign alu_xor = alu_control[3]&~alu_control[2]&~alu_control[1]&alu_control[0];//1001
   assign alu_sll = alu_control[3]&~alu_control[2]&alu_control[1]&~alu_control[0];//1010
   assign alu_srl = alu_control[3]&~alu_control[2]&alu_control[1]&alu_control[0];//1011
   assign alu_sla = alu_control[3]&alu_control[2]&~alu_control[1]&~alu_control[0];//1100
   assign alu_sra = alu_control[3]&alu_control[2]&~alu_control[1]&alu_control[0];//1101
   assign alu_lui = alu_control[3]&alu_control[2]&alu_control[1]&~alu_control[0];//1110
   assign alu_ldi = alu_control[3]&alu_control[2]&alu_control[1]&alu_control[0];//1111

   //各运算对应结果
   wire [31:0] add_sub_result;
   wire [31:0] slt_result;
   wire [31:0] sbt_result;
   wire [31:0] sltu_result;
   wire [31:0] and_result;
   wire [31:0] nor_result;
   wire [31:0] or_result;
   wire [31:0] xor_result;
   wire [31:0] sll_result;
   wire [31:0] srl_result;
   wire [31:0] sla_result;
   wire [31:0] sra_result;
   wire [31:0] lui_result;
   wire [31:0] ldi_result;
   
   //-----{加法器}begin
      //add,sub,slt,sltu 均使用该模块
      wire [31:0] adder_operand1;
      wire [31:0] adder_operand2;
      wire adder_cin ;
      wire [31:0] adder_result ;
      wire adder_cout ;
      assign adder_operand1 = alu_src1;
      assign adder_operand2 = alu_add ? alu_src2 : ~alu_src2;
      assign adder_cin = ~alu_add; //减法需要cin,默认做减法
      adder adder_module(
       .operand1(adder_operand1),
       .operand2(adder_operand2),
       .cin (adder_cin ),
       .result (adder_result ),
       .cout (adder_cout )
        );
        assign add_sub_result = adder_result;//1.2.加减运算合并
        assign slt_result[31:1] = 31'd0;
        assign sbt_result[31:1]=31'd0;
        assign slt_result[0]=(alu_src1[31] & ~alu_src2[31]) |(~(alu_src1[31]^alu_src2[31]) & adder_result[31]);//3.有符号比较
        assign sbt_result[0]=~slt_result[0];//4.有符号比较，大于置位
        assign sltu_result = {31'd0, ~adder_cout};//5.无符号比较
        //-----{加法器}end
   assign and_result = alu_src1 & alu_src2; //6.按位与
   assign nor_result = ~or_result; //7.按位或非
   assign or_result = alu_src1 | alu_src2; //8.按位或
   assign xor_result = alu_src1 ^ alu_src2;//9.按位异或
   assign lui_result = {alu_src2[15:0], 16'd0};//14.高位加载
   assign ldi_result = {alu_src2[31:16], 16'd0};//15.低位加载
   
     //-----{移位器}begin
     wire [4:0] shf;
     assign shf = alu_src1[4:0];
     wire [1:0] shf_1_0;
     wire [1:0] shf_3_2;
     assign shf_1_0 = shf[1:0];
     assign shf_3_2 = shf[3:2];
     // 逻辑左移
     wire [31:0] sll_step1;
     wire [31:0] sll_step2;
     // 依据shf[1:0],左移0、1、2、3 位
     assign sll_step1 = {32{shf_1_0 == 2'b00}} & alu_src2
     | {32{shf_1_0 == 2'b01}} & {alu_src2[30:0], 1'd0}
     | {32{shf_1_0 == 2'b10}} & {alu_src2[29:0], 2'd0}
     | {32{shf_1_0 == 2'b11}} & {alu_src2[28:0], 3'd0};
     // 依据shf[3:2],将第一次移位结果左移0、4、8、12 位
     assign sll_step2 = {32{shf_3_2 == 2'b00}} & sll_step1
     | {32{shf_3_2 == 2'b01}} & {sll_step1[27:0], 4'd0}
     | {32{shf_3_2 == 2'b10}} & {sll_step1[23:0], 8'd0}
     | {32{shf_3_2 == 2'b11}} & {sll_step1[19:0], 12'd0};
     // 依据shf[4],将第二次移位结果左移0、16 位
     assign sll_result = shf[4] ? {sll_step2[15:0], 16'd0} : sll_step2;//10.逻辑左移
     
     // 逻辑右移
     wire [31:0] srl_step1;
     wire [31:0] srl_step2;
     // 依据shf[1:0],右移0、1、2、3 位，高位补0
     assign srl_step1 = {32{shf_1_0 == 2'b00}} & alu_src2
      | {32{shf_1_0 == 2'b01}} & {1'd0, alu_src2[31:1]}
      | {32{shf_1_0 == 2'b10}} & {2'd0, alu_src2[31:2]}
      | {32{shf_1_0 == 2'b11}} & {3'd0, alu_src2[31:3]};
      // 依据shf[3:2],将第一次移位结果右移0、4、8、12 位，高位补0
      assign srl_step2 = {32{shf_3_2 == 2'b00}} & srl_step1
      | {32{shf_3_2 == 2'b01}} & {4'd0, srl_step1[31:4]}
      | {32{shf_3_2 == 2'b10}} & {8'd0, srl_step1[31:8]}
      | {32{shf_3_2 == 2'b11}} & {12'd0, srl_step1[31:12]};
      // 依据shf[4],将第二次移位结果右移0、16 位，高位补0
      assign srl_result = shf[4] ? {16'd0, srl_step2[14:0]} : srl_step2;//11.逻辑右移
      
      //算数左移
      wire [31:0] sla_step1;
      wire [31:0] sla_step2;
      // 依据shf[1:0],右移0、1、2、3 位，高位补符号位
      assign sla_step1 = {32{shf_1_0 == 2'b00}} & alu_src2
      | {32{shf_1_0 == 2'b01}} & {alu_src2[31],alu_src2[29:0],alu_src2[31]}
      | {32{shf_1_0 == 2'b10}} & {alu_src2[31],alu_src2[28:0],{2{alu_src2[31]}}}
      | {32{shf_1_0 == 2'b11}} & {alu_src2[31],alu_src2[27:0],{3{alu_src2[31]}}};
      // 依据shf[3:2],将第一次移位结果右移0、4、8、12 位，高位补符号位
      assign sla_step2 = {32{shf_3_2 == 2'b00}} & sla_step1
      | {32{shf_3_2 == 2'b01}} & {alu_src2[31],sla_step1[26:0],{4{sla_step1[31]}}}
      | {32{shf_3_2 == 2'b10}} & {alu_src2[31],sla_step1[22:0],{8{sla_step1[31]}}}
      | {32{shf_3_2 == 2'b11}} & {alu_src2[31],sla_step1[18:0],{12{sla_step1[31]}}};
      // 依据shf[4],将第二次移位结果右移0、16 位，高位补符号位
      assign sla_result = shf[4] ? {alu_src2[31],sla_step2[31:16],{16{sla_step2[31]}}} :
      sla_step2;
      // 算术右移
      wire [31:0] sra_step1;
      wire [31:0] sra_step2;
      // 依据shf[1:0],右移0、1、2、3 位，高位补符号位
      assign sra_step1 = {32{shf_1_0 == 2'b00}} & alu_src2
       | {32{shf_1_0 == 2'b01}} & {alu_src2[31], alu_src2[31:1]}
       | {32{shf_1_0 == 2'b10}} & {{2{alu_src2[31]}}, alu_src2[31:2]}
       | {32{shf_1_0 == 2'b11}} & {{3{alu_src2[31]}}, alu_src2[31:3]};
       // 依据shf[3:2],将第一次移位结果右移0、4、8、12 位，高位补符号位
       assign sra_step2 = {32{shf_3_2 == 2'b00}} & sra_step1
       | {32{shf_3_2 == 2'b01}} & {{4{sra_step1[31]}}, sra_step1[31:4]}
       | {32{shf_3_2 == 2'b10}} & {{8{sra_step1[31]}}, sra_step1[31:8]}
       | {32{shf_3_2 == 2'b11}} & {{12{sra_step1[31]}}, sra_step1[31:12]};
       // 依据shf[4],将第二次移位结果右移0、16 位，高位补符号位
       assign sra_result = shf[4] ? {{16{sra_step2[31]}}, sra_step2[31:16]} :
       sra_step2;
       //-----{移位器}end
       
       // 选择相应结果输出
       assign alu_result = (alu_add|alu_sub) ? add_sub_result[31:0] :
       alu_slt ? slt_result :
       alu_sbt ? sbt_result:
       alu_sltu ? sltu_result :
       alu_and ? and_result :
       alu_nor ? nor_result :
       alu_or ? or_result :
       alu_xor ? xor_result :
       alu_sll ? sll_result :
       alu_srl ? srl_result :
       alu_sla ? sla_result :
       alu_sra ? sra_result :
       alu_lui ? lui_result :
       alu_ldi ? ldi_result :
       32'd0;
endmodule
