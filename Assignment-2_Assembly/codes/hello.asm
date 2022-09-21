.include "/home/pavank/assembly/codes/m328Pdef.inc" ;your m328Pdef file location
ldi r16,0b11000011
out DDRD,r16
ldi r16,0b00100000
out DDRB,r16            ;declaring 8th pin as output
loop:                   ;loop for reading the input from pins 2,3,4,5 continously
        ldi r17, 0b00111100 ;

        ldi r24,0b00000100
        mov r18,r17
        and r18,r24
        ldi r25,0b00000010
        loop1:  lsr r18  ;A
        dec r25
        brne    loop1

        mov r19,r17
        ldi r24,0b00001000
        and r19,r24
        ldi r25,0b00000011
        loop2:  lsr r19   ;B
        dec r25
        brne    loop2

        ldi r24,0b00010000
        mov r20,r17
        and r20,r24
        ldi r25,0b00000100
        loop3:  lsr r20  ;C
        dec r25
        brne    loop3

        ldi r24,0b00100000
        mov r21,r17
        and r21,r24
        ldi r25,0b00000101
        loop4:  lsr r21  ;D
        dec r25
        brne    loop4
    


or r19,r18
or r20,r21
and r20,r19

        ldi r26,0b00000101
        loop5:  lsl r20 
        dec r26
        brne    loop5
     out PORTB,r20
    rjmp loop
