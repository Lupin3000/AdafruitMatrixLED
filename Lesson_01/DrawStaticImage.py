#! /usr/bin/env python

import time

from PIL import Image, ImageDraw
from rgbmatrix import RGBMatrix, RGBMatrixOptions

# set matrix options
options = RGBMatrixOptions()
options.chain_length = 2
options.cols = 32
options.rows = 32
options.parallel = 1
options.brightness = 50
options.disable_hardware_pulsing = True
options.drop_privileges = 1
options.gpio_slowdown = 1
options.hardware_mapping = 'adafruit-hat'
options.inverse_colors = False
options.led_rgb_sequence = "RGB"
options.multiplexing = 0
options.pixel_mapper_config = ''
options.pwm_bits = 11
options.pwm_dither_bits = 0
options.pwm_lsb_nanoseconds = 130
options.row_address_type = 0
options.scan_mode = 0
options.show_refresh_rate = False

matrix = RGBMatrix(options=options)

# draw image
image = Image.new("RGB", size=(matrix.width, matrix.height))
draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, 63, 31), fill=(10, 100, 10), outline=(0, 0, 255))
draw.rectangle((2, 2, 61, 13), fill=(0, 0, 0), outline=(255, 0, 0))
draw.ellipse((5, 5, 20, 20), fill=(100, 0, 0), outline=(0, 255, 0))

# show on matrix
matrix.SetImage(image)

time.sleep(10)
matrix.Clear()
