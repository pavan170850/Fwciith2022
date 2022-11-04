module helloworldfpga(

    input  wire A,
    input  wire B,
    input  wire C,
    input  wire D,
    output wire Y,
    );
   // assign A=0;
    //assign B=0;
    //assign C=0;
     //assign D=0;
    always @(*)
    begin
   F=(A|B)&(C|D); 
    end
    endmodule
