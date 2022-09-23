
#include <avr/io.h>
#include <util/delay.h>
#include <stdbool.h>

 
int main (void)
{
   bool X=1, Y=0,Z=1;
   bool F ;

 DDRB  = 0b00100000;
 PORTB = 0b00100000;

 //equation
while(1)
{
	F=(X&&!Y&&Z)||(!X&&Y&&Z);
	PORTB &=(F<<5);
} 
  return 0;
}
