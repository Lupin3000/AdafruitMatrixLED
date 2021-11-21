#! /usr/bin/env python

import time

from datetime import datetime, timedelta
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

# set max duration and text
duration = datetime.now() + timedelta(seconds=30)
text = 'Hello world from RGB Matrix LED'

# create font
font = graphics.Font()
font.LoadFont("../fonts/9x15.bdf")
fontcolor = graphics.Color(250, 250, 250)

# create canvas
canvas = matrix.CreateFrameCanvas()

# get canvas position
canvas_pos = canvas.width

while True:
    if datetime.now() >= duration:
        break
    # get length of text
    text_len = graphics.DrawText(canvas, font, canvas_pos, 20, fontcolor, text)
    # change position
    canvas_pos -= 1
    if (canvas_pos + text_len) < 0:
        canvas_pos = canvas.width
    # show on matrix
    time.sleep(0.05)
    matrix.Clear()
    canvas = matrix.SwapOnVSync(canvas)

matrix.Clear()
