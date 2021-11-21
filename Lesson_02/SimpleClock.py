#! /usr/bin/env python

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

# set max duration
duration = datetime.now() + timedelta(seconds=30)

# create font
font = graphics.Font()
font.LoadFont("../fonts/7x13.bdf")
fontcolor = graphics.Color(200, 200, 200)

# create canvas with text
canvas = matrix.CreateFrameCanvas()

while True:
    if datetime.now() >= duration:
        break
    # get current time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    # show on matrix
    matrix.Clear()
    graphics.DrawText(canvas, font, 5, 15, fontcolor, current_time)
    matrix.SwapOnVSync(canvas)

matrix.Clear()
