#! /usr/bin/env python

import argparse
import time
from datetime import datetime, timedelta
from random import randint

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

# define argparse description/epilog
description = 'Text scroll with random colors for Adafruit Matrix LED'
epilog = 'The author assumes no liability for any damage caused by use.'

# create argparse Object
parser = argparse.ArgumentParser(prog='./TwoTextScroller.py', description=description, epilog=epilog)

# set optional arguments
parser.add_argument('--text_a', help='String for text a', default='hello world', type=str)
parser.add_argument('--text_b', help='String for text b', default='from rgb matrix', type=str)

# read arguments by user
args = parser.parse_args()

text_a = args.text_a
text_b = args.text_b

# set max duration and text
duration = datetime.now() + timedelta(seconds=30)

# create font
font = graphics.Font()
font.LoadFont("../fonts/7x13.bdf")

# create canvas
canvas = matrix.CreateFrameCanvas()
canvas_tmp = canvas

# get text length - I know it's an ugly implementation
text_a_len = graphics.DrawText(canvas, font, 0, -10, graphics.Color(0, 0, 0), text_a)
text_b_len = graphics.DrawText(canvas, font, 0, -10, graphics.Color(0, 0, 0), text_b)

# start positions
start_text_a = 0 - text_a_len
start_text_b = canvas.width
pos_x_a = start_text_a
pos_x_b = start_text_b

while True:
    if datetime.now() >= duration:
        break
    # draw text
    matrix.Clear()
    graphics.DrawText(canvas, font, pos_x_a, 12,
                      graphics.Color(randint(50, 250), randint(50, 250), randint(50, 250)), text_a)
    graphics.DrawText(canvas, font, pos_x_b, 25,
                      graphics.Color(randint(50, 250), randint(50, 250), randint(50, 250)), text_b)
    # change x positions
    if pos_x_a > canvas.width:
        pos_x_a = start_text_a
    if pos_x_b < (0 - text_b_len):
        pos_x_b = start_text_b
    pos_x_a += 1
    pos_x_b -= 1
    # show on matrix
    canvas = matrix.SwapOnVSync(canvas)
    time.sleep(0.05)

matrix.Clear()
