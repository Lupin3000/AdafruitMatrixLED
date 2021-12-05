#! /usr/bin/env python

import argparse
import cv2
import time

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

# define argparse description/epilog
description = 'Video player for Adafruit Matrix LED'
epilog = 'The author assumes no liability for any damage caused by use.'

# create argparse Object
parser = argparse.ArgumentParser(prog='./VideoPlayer.py', description=description, epilog=epilog)

# set optional arguments
parser.add_argument('--video', help='Path and video file', default='../video/video.mov', type=str)

# read arguments by user
args = parser.parse_args()

# read video file
print('read video file: {}'.format(args.video))

# noinspection PyArgumentList
movie = cv2.VideoCapture(args.video)

# set start frame
currentframe = 0

# set max size
MAX_SIZE = (64, 32)

# create canvas
canvas = matrix.CreateFrameCanvas()

while True:
    ret, frame = movie.read()
    if not ret:
        print('no more frames')
        break
    print('read frame: {}'.format(currentframe))
    # convert frames to images
    pil_img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    pil_img.thumbnail(MAX_SIZE, Image.ANTIALIAS)
    # resize and RGB mode
    canvas.SetImage(pil_img.convert('RGB'), 0, 0)
    # show on matrix
    matrix.Clear()
    canvas = matrix.SwapOnVSync(canvas)
    currentframe += 1
    # stop to prevent flicker effect
    time.sleep(0.005)

# movie finished
movie.release()
print('movie is finished')

matrix.Clear()
