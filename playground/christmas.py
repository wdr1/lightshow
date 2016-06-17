#!/usr/bin/env python

# Light each LED in sequence, and repeat.

import opc, time

numLEDs = 50
client = opc.Client('localhost:7890')

red_pixel = (255, 0, 0)
green_pixel = (0, 255, 0)
base_color = green_pixel

while True:
        if base_color == green_pixel:
                base_color = red_pixel
                alt_color = green_pixel
        else:
                alt_color = red_pixel
                base_color = green_pixel

	pixels = [ base_color ] * numLEDs
        
	for i in range(0, numLEDs, 2):
		pixels[i] = alt_color
                
	client.put_pixels(pixels)
	time.sleep(0.1)
