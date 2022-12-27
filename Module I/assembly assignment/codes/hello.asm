.include "/sdcard/download/assembly/m328Pdef.inc"
 
main:
 ldi r16, 0b00100000 ;identifying output pins 13
 out DDRB,r16  ;declaring pins as output
 

 

 

 ldi r16,0b00000001 ;initializing X
 ldi r17,0b00000000 ;initializing Y
 ldi r18,0b00000001 ;initializing Z
 ;logical XOR
 eor r16,r17   ;
 eor r18,r16;
 com r18;
 and r18,r16;
 
 
 
  ;following code is for displaying output
;shifting LSB in r16 to 5nd position
ldi r20, 0b00000101 ;counter = 5

rcall loopw  ;calling the loopw routine

out PORTB,r16  ;writing output to pins 13


Start:
rjmp Start

;loop for bit shifting
loopw: lsl r16   ;left shift
 dec r20   ;
 brne loopw ;if counter != 0
 ret
 rjmp main
