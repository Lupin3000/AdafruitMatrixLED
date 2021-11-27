#! /usr/bin/env python

import time
from datetime import datetime, timedelta

from PIL import Image, ImageDraw
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

# create canvas
canvas = matrix.CreateFrameCanvas()

# draw images
image_left = Image.new("RGB", size=(matrix.width / 2, matrix.height))
draw_left = ImageDraw.Draw(image_left)
draw_left.ellipse((5, 5, 25, 25), fill=(0, 250, 0), outline=None)

image_right = Image.new("RGB", size=(matrix.width / 2, matrix.height))
draw_right = ImageDraw.Draw(image_right)
draw_right.rectangle((1, 1, 30, 30), fill=(0, 0, 250), outline=None)

# set start positions
start_pos_y = -32
pos_y = start_pos_y

while True:
    if datetime.now() >= duration:
        break
    # change position
    if pos_y > canvas.height:
        pos_y = start_pos_y
    # draw to matrix
    matrix.Clear()
    canvas.SetImage(image_left, 0, pos_y)
    canvas.SetImage(image_right, 32, pos_y)
    pos_y += 1
    # show on matrix
    canvas = matrix.SwapOnVSync(canvas)
    time.sleep(0.05)

matrix.Clear()
