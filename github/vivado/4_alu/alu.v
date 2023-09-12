`timescale 1ns / 1ps
//*************************************************************************
//   > �ļ���: alu.v
//   > ����  ��ALUģ�飬����12�ֲ���
//   > ����  : LOONGSON
//   > ����  : 2016-04-14
//*************************************************************************
module alu(
    input  [3:0] alu_control,  // ALU�����ź�
    input  [31:0] alu_src1,     // ALU������1,Ϊ����
    input  [31:0] alu_src2,     // ALU������2��Ϊ����
    output [31:0] alu_result    // ALU���
    );

    // ALU�����źţ�������
    wire alu_add;   //1.�ӷ�����
    wire alu_sub;   //2.��������
    wire alu_slt;   //3.�з��űȽϣ�С����λ�����üӷ���������
    wire alu_sbt;   //4.�з��űȽϣ�������λ�����üӷ���������      1
    wire alu_sltu;  //5.�޷��űȽϣ�С����λ�����üӷ���������
    wire alu_and;   //6.��λ��
    wire alu_nor;   //7.��λ���
    wire alu_or;    //8.��λ��
    wire alu_xor;   //9.��λ���
    wire alu_sll;   //10.�߼�����
    wire alu_srl;   //11.�߼�����
    wire alu_sla;   //12.��������       1
    wire alu_sra;   //13.��������
    wire alu_lui;   //14.��λ����
    wire alu_ldi;   //15.��λ����      1

   //�źŸ�ֵ
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

   //�������Ӧ���
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
   
   //-----{�ӷ���}begin
      //add,sub,slt,sltu ��ʹ�ø�ģ��
      wire [31:0] adder_operand1;
      wire [31:0] adder_operand2;
      wire adder_cin ;
      wire [31:0] adder_result ;
      wire adder_cout ;
      assign adder_operand1 = alu_src1;
      assign adder_operand2 = alu_add ? alu_src2 : ~alu_src2;
      assign adder_cin = ~alu_add; //������Ҫcin,Ĭ��������
      adder adder_module(
       .operand1(adder_operand1),
       .operand2(adder_operand2),
       .cin (adder_cin ),
       .result (adder_result ),
       .cout (adder_cout )
        );
        assign add_sub_result = adder_result;//1.2.�Ӽ�����ϲ�
        assign slt_result[31:1] = 31'd0;
        assign sbt_result[31:1]=31'd0;
        assign slt_result[0]=(alu_src1[31] & ~alu_src2[31]) |(~(alu_src1[31]^alu_src2[31]) & adder_result[31]);//3.�з��űȽ�
        assign sbt_result[0]=~slt_result[0];//4.�з��űȽϣ�������λ
        assign sltu_result = {31'd0, ~adder_cout};//5.�޷��űȽ�
        //-----{�ӷ���}end
   assign and_result = alu_src1 & alu_src2; //6.��λ��
   assign nor_result = ~or_result; //7.��λ���
   assign or_result = alu_src1 | alu_src2; //8.��λ��
   assign xor_result = alu_src1 ^ alu_src2;//9.��λ���
   assign lui_result = {alu_src2[15:0], 16'd0};//14.��λ����
   assign ldi_result = {alu_src2[31:16], 16'd0};//15.��λ����
   
     //-----{��λ��}begin
     wire [4:0] shf;
     assign shf = alu_src1[4:0];
     wire [1:0] shf_1_0;
     wire [1:0] shf_3_2;
     assign shf_1_0 = shf[1:0];
     assign shf_3_2 = shf[3:2];
     // �߼�����
     wire [31:0] sll_step1;
     wire [31:0] sll_step2;
     // ����shf[1:0],����0��1��2��3 λ
     assign sll_step1 = {32{shf_1_0 == 2'b00}} & alu_src2
     | {32{shf_1_0 == 2'b01}} & {alu_src2[30:0], 1'd0}
     | {32{shf_1_0 == 2'b10}} & {alu_src2[29:0], 2'd0}
     | {32{shf_1_0 == 2'b11}} & {alu_src2[28:0], 3'd0};
     // ����shf[3:2],����һ����λ�������0��4��8��12 λ
     assign sll_step2 = {32{shf_3_2 == 2'b00}} & sll_step1
     | {32{shf_3_2 == 2'b01}} & {sll_step1[27:0], 4'd0}
     | {32{shf_3_2 == 2'b10}} & {sll_step1[23:0], 8'd0}
     | {32{shf_3_2 == 2'b11}} & {sll_step1[19:0], 12'd0};
     // ����shf[4],���ڶ�����λ�������0��16 λ
     assign sll_result = shf[4] ? {sll_step2[15:0], 16'd0} : sll_step2;//10.�߼�����
     
     // �߼�����
     wire [31:0] srl_step1;
     wire [31:0] srl_step2;
     // ����shf[1:0],����0��1��2��3 λ����λ��0
     assign srl_step1 = {32{shf_1_0 == 2'b00}} & alu_src2
      | {32{shf_1_0 == 2'b01}} & {1'd0, alu_src2[31:1]}
      | {32{shf_1_0 == 2'b10}} & {2'd0, alu_src2[31:2]}
      | {32{shf_1_0 == 2'b11}} & {3'd0, alu_src2[31:3]};
      // ����shf[3:2],����һ����λ�������0��4��8��12 λ����λ��0
      assign srl_step2 = {32{shf_3_2 == 2'b00}} & srl_step1
      | {32{shf_3_2 == 2'b01}} & {4'd0, srl_step1[31:4]}
      | {32{shf_3_2 == 2'b10}} & {8'd0, srl_step1[31:8]}
      | {32{shf_3_2 == 2'b11}} & {12'd0, srl_step1[31:12]};
      // ����shf[4],���ڶ�����λ�������0��16 λ����λ��0
      assign srl_result = shf[4] ? {16'd0, srl_step2[14:0]} : srl_step2;//11.�߼�����
      
      //��������
      wire [31:0] sla_step1;
      wire [31:0] sla_step2;
      // ����shf[1:0],����0��1��2��3 λ����λ������λ
      assign sla_step1 = {32{shf_1_0 == 2'b00}} & alu_src2
      | {32{shf_1_0 == 2'b01}} & {alu_src2[31],alu_src2[29:0],alu_src2[31]}
      | {32{shf_1_0 == 2'b10}} & {alu_src2[31],alu_src2[28:0],{2{alu_src2[31]}}}
      | {32{shf_1_0 == 2'b11}} & {alu_src2[31],alu_src2[27:0],{3{alu_src2[31]}}};
      // ����shf[3:2],����һ����λ�������0��4��8��12 λ����λ������λ
      assign sla_step2 = {32{shf_3_2 == 2'b00}} & sla_step1
      | {32{shf_3_2 == 2'b01}} & {alu_src2[31],sla_step1[26:0],{4{sla_step1[31]}}}
      | {32{shf_3_2 == 2'b10}} & {alu_src2[31],sla_step1[22:0],{8{sla_step1[31]}}}
      | {32{shf_3_2 == 2'b11}} & {alu_src2[31],sla_step1[18:0],{12{sla_step1[31]}}};
      // ����shf[4],���ڶ�����λ�������0��16 λ����λ������λ
      assign sla_result = shf[4] ? {alu_src2[31],sla_step2[31:16],{16{sla_step2[31]}}} :
      sla_step2;
      // ��������
      wire [31:0] sra_step1;
      wire [31:0] sra_step2;
      // ����shf[1:0],����0��1��2��3 λ����λ������λ
      assign sra_step1 = {32{shf_1_0 == 2'b00}} & alu_src2
       | {32{shf_1_0 == 2'b01}} & {alu_src2[31], alu_src2[31:1]}
       | {32{shf_1_0 == 2'b10}} & {{2{alu_src2[31]}}, alu_src2[31:2]}
       | {32{shf_1_0 == 2'b11}} & {{3{alu_src2[31]}}, alu_src2[31:3]};
       // ����shf[3:2],����һ����λ�������0��4��8��12 λ����λ������λ
       assign sra_step2 = {32{shf_3_2 == 2'b00}} & sra_step1
       | {32{shf_3_2 == 2'b01}} & {{4{sra_step1[31]}}, sra_step1[31:4]}
       | {32{shf_3_2 == 2'b10}} & {{8{sra_step1[31]}}, sra_step1[31:8]}
       | {32{shf_3_2 == 2'b11}} & {{12{sra_step1[31]}}, sra_step1[31:12]};
       // ����shf[4],���ڶ�����λ�������0��16 λ����λ������λ
       assign sra_result = shf[4] ? {{16{sra_step2[31]}}, sra_step2[31:16]} :
       sra_step2;
       //-----{��λ��}end
       
       // ѡ����Ӧ������
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
