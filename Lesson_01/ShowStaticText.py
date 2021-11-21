#! /usr/bin/env python

import time

from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics

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

# create font
font = graphics.Font()
font.LoadFont("./7x13.bdf")
fontcolor = graphics.Color(175, 175, 175)

# create canvas with text
canvas = matrix.CreateFrameCanvas()
graphics.DrawText(canvas, font, 15, 15, fontcolor, 'hello')
graphics.DrawText(canvas, font, 15, 25, fontcolor, 'Sonja')

# show on matrix
matrix.Clear()
matrix.SwapOnVSync(canvas)

time.sleep(10)
matrix.Clear()
