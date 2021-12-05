#! /usr/bin/env python

import argparse
import time

import requests
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

# default
source = None

# define argparse description/epilog
description = 'Show your crypto courses on the Adafruit Matrix LED'
epilog = 'The author assumes no liability for any damage caused by use.'

# create argparse Object
parser = argparse.ArgumentParser(prog='./CryptoLED.py', description=description, epilog=epilog)

# set optional arguments
parser.add_argument('--currency', help='Set your currency', metavar='[CHF]', default='EUR', type=str)
parser.add_argument('--crypto', help='Set your cryptos comma separated',
                    metavar='[ETH,BTC]', default='ETH,BTC,DOT', type=str)

# set mandatory arguments
parser.add_argument('apikey', help='', type=str)

# read arguments by user
args = parser.parse_args()

# set api values
api_key = args.apikey
api_currency = args.currency
api_cryptos = args.crypto

# create fonts
crypto_font = graphics.Font()
crypto_font.LoadFont("../fonts/7x13.bdf")

value_font = graphics.Font()
value_font.LoadFont("../fonts/5x8.bdf")

font_crypto_color = graphics.Color(250, 250, 250)
font_value_color = graphics.Color(100, 100, 255)

# matrix canvas
canvas = matrix.CreateFrameCanvas()

# api request
url = 'https://api.nomics.com/v1/currencies/ticker'
params = dict(key=api_key,
              ids=api_cryptos,
              convert=api_currency,
              interval='1d')

res = requests.get(url, params)

# api response
if res.status_code != 200:
    print('Something went wrong')
    exit()
else:
    source = res.json()

for event in source:
    # create display content
    text_a = event['name']
    crypto_pos = (64 - (len(text_a) * 7)) / 2
    text_b = float(event['price'])
    text_b = api_currency + ' ' + str(round(text_b, 2)).encode('utf-8')
    text_c = float(event['1d']['price_change'])
    text_c = '24h ' + str(round(text_c, 4)).encode('utf-8')
    # show on matrix
    matrix.Clear()
    graphics.DrawText(canvas, crypto_font, crypto_pos, 12, font_crypto_color, text_a)
    graphics.DrawText(canvas, value_font, 2, 21, font_value_color, text_b)
    graphics.DrawText(canvas, value_font, 2, 30, font_value_color, text_c)
    matrix.SwapOnVSync(canvas)
    # time to show
    time.sleep(5)

matrix.Clear()
