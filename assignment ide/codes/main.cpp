#include<Arduino.h>
int F,X=1,Y=0,Z=1;
void setup(){
	pinMode(13,OUTPUT);
}
void loop(){
	F=(X&&!Y&&Z)||(!X&&Y&&Z);
	digitalWrite(13,F);
}


