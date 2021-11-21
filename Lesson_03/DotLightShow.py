#! /usr/bin/env python

import argparse
import random
import time
from datetime import datetime, timedelta

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

# define argparse description/epilog
description = 'Simple Dot Light Show for Adafruit Matrix LED'
epilog = 'The author assumes no liability for any damage caused by use.'

# create argparse Object
parser = argparse.ArgumentParser(prog='./DotLightShow.py', description=description, epilog=epilog)

# set optional arguments
parser.add_argument('-d', '--duration', help='Duration in seconds for whole Light Show', default=10,
                    choices=range(1, 60), metavar='[1-60]', type=int)
parser.add_argument('-n', '--number', help='Number of dots at same time', default=32,
                    choices=range(1, 90), metavar='[1-90]', type=int)

# read arguments by user
args = parser.parse_args()

# set all values
duration = datetime.now() + timedelta(seconds=int(args.duration))
dot_count = int(args.number)

while True:
    if datetime.now() >= duration:
        break
    # draw image
    image = Image.new("RGB", size=(matrix.width, matrix.height))
    draw = ImageDraw.Draw(image)
    # draw dots
    for x in range(dot_count):
        draw.point((random.randint(0, 63), random.randint(0, 31)),
                   fill=(random.randint(10, 250), random.randint(10, 250), random.randint(10, 250)))
    # show on matrix
    matrix.SetImage(image)
    time.sleep(0.05)

matrix.Clear()
