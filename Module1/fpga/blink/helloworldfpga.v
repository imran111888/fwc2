 module boolean(
	 input X,Y,Z,
	 output F
 );
 assign F=((X&&!Y&&Z)||(!X&&Y&&Z));
endmodule
//end of the module
























