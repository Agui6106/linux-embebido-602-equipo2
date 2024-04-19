#define F_CPU 16000000UL
#include <avr/io.h>
#include <util/delay.h>

int main (void)
{
    DDRB |= _BV(PORTB0);      // set pin 0 of port B as an output pin
    DDRB |= _BV(PORTB1);      // set pin 0 of port B as an output pin
    DDRB |= _BV(PORTB2);      // set pin 0 of port B as an output pin

    for (;;) {
        //PRENDE
        PORTB |= _BV(PORTB0);  // set pin 0 of port B high
        _delay_ms(200);  // loop for 62500 iterations * 4 cycles / 1MHz clock ~= 250ms
        PORTB |= _BV(PORTB1);  // set pin 0 of port B high
        _delay_ms(200);  // loop for 62500 iterations * 4 cycles / 1MHz clock ~= 250ms
        PORTB |= _BV(PORTB2);  // set pin 0 of port B high
        _delay_ms(200);  // loop for 62500 iterations * 4 cycles / 1MHz clock ~= 250ms
        //APAGA
        PORTB &= ~_BV(PORTB0); // set pin 0 of port B low
        _delay_ms(200);  // loop for 62500 iterations * 4 cycles / 1MHz clock ~= 250ms
        PORTB &= ~_BV(PORTB1); // set pin 0 of port B low
        _delay_ms(200);  // loop for 62500 iterations * 4 cycles / 1MHz clock ~= 250ms
        PORTB &= ~_BV(PORTB2); // set pin 0 of port B low
        _delay_ms(200);  // loop for 62500 iterations * 4 cycles / 1MHz clock ~= 250ms
    }
}
