#! /usr/bin/env python

import datetime
import random
import time

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

# set max duration
duration = datetime.datetime.now() + datetime.timedelta(seconds=10)

# create canvas
canvas = matrix.CreateFrameCanvas()

while True:
    if datetime.datetime.now() >= duration:
        break
    # show on matrix
    canvas.Fill(random.randint(0, 250), random.randint(0, 250), random.randint(0, 250))
    matrix.SwapOnVSync(canvas)
    time.sleep(1)

matrix.Clear()
