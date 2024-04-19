CC=avr-gcc
OBJCOPY=avr-objcopy
AVRDUDE=sudo avrdude

CFLAGS=-Os -mmcu=atmega328p -I/usr/lib/avr/include

all: blink.hex

blink.o: blink.c
	$(CC) $(CFLAGS) -c $^

blink.elf: blink.o
	$(CC) -mmcu=atmega328p -o $@ $^

blink.hex: blink.elf
	$(OBJCOPY) -j .text -j .data -O ihex $^ $@

flash: blink.hex
	$(AVRDUDE) -c usbasp -p m328p -U flash:w:$^

clean:
	rm -f *.o *.elf *.hex


