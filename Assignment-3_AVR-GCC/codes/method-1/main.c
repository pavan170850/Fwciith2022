
#include <avr/io.h>
#include <stdbool.h>
int main (void)
{

	 bool A=1,B=0,C=1,D=1,Y;
	  DDRB =  0b00100000;  
	   Y = (A|B)&(C|D);
	    PORTB |= (Y<< 5);
	     return 0;
}
