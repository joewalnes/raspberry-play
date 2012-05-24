#!/usr/bin/env python

# Demonstrates using a 16 LED shift register to create an animation
# using only 3 GPIO pins.
#
# The frames of the animation are defined in animation.txt.
#
# -Joe Walnes (@joewalnes)

from itertools import cycle
from time import sleep

# Connect the shift register pins to these GPIO pins.
data_pin = 17
clock_pin = 21
latch_pin = 22

def digital_write(pin, value):
	path = '/sys/class/gpio/gpio%d/value' % pin
	with open(path, 'w') as f:
		f.write('1' if value else '0')

def init():
	digital_write(data_pin, 0)
	digital_write(clock_pin, 0)
	digital_write(latch_pin, 0)

def shift_bit(value):
	digital_write(data_pin, value)
	digital_write(clock_pin, 1)
	digital_write(clock_pin, 0)

def latch():
	digital_write(latch_pin, 1)
	digital_write(latch_pin, 0)

def read_lines(filename):
	with open(filename) as f:
		for line in f:
			yield line.strip()

def main():
	init()
	filename = 'animation.txt'
	for frame in cycle(read_lines(filename)):
		#print frame
		for pixel in frame:
			shift_bit(pixel == '#')
		latch()
		sleep(0.05)

if __name__ == '__main__':
	main()

	
