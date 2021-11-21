#! /usr/bin/env python

import time
from datetime import datetime, timedelta

from PIL import Image
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

# set max duration and text
duration = datetime.now() + timedelta(seconds=30)

# create image
image = Image.open('../img/pacman.jpg').convert('RGB')
img_width, img_height = image.size
image.thumbnail((img_width / 2, img_height / 2), Image.ANTIALIAS)

# image start, x and y position
img_start_pos = img_x_pos = 64
img_y_pos = (32 - (img_height / 2)) / 2

while True:
    if datetime.now() >= duration:
        break
    # change position
    img_x_pos -= 1
    if (img_x_pos + img_width / 2) < 0:
        img_x_pos = img_start_pos
    # show on matrix
    matrix.Clear()
    matrix.SetImage(image, img_x_pos, img_y_pos)
    time.sleep(0.05)

matrix.Clear()
