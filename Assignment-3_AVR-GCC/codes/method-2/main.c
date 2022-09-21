#include <avr/io.h>
#include <stdbool.h>
int main (void)
{

	 bool A,B,C,D,Y;
	  DDRB =  0b00100000;  
	   DDRD =  0b11000011;
	    PORTD = 0b00111100;   

	    while(1)
	    {   A = (PIND & (1 << PIND2)) == (1 << PIND2);
		    B = (PIND & (1 << PIND3)) == (1 << PIND3);
		    C = (PIND & (1 << PIND4)) == (1 << PIND4);
		    D = (PIND & (1 << PIND5)) == (1 << PIND5);
		    Y = ((A|B)&(C|D));
		    PORTB |= (Y<< 5);
	    }
	    return 0;
}
