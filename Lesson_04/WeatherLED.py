#! /usr/bin/env python

import time
import argparse
import requests
from PIL import Image
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
description = 'Weather display for Adafruit Matrix LED'
epilog = 'The author assumes no liability for any damage caused by use.'

# create argparse Object
parser = argparse.ArgumentParser(prog='./WeatherLED.py', description=description, epilog=epilog)

# set mandatory arguments
parser.add_argument('zip', help="Zip code", type=int)
parser.add_argument('country', help='Country code', type=str)
parser.add_argument('apikey', help='unique api key for openweathermap.org', type=str)

# set optional arguments
parser.add_argument('-u', '--units', help='set units of measurement (metric or imperial)',
                    metavar='[metric]', default='metric')

# read arguments by user
args = parser.parse_args()

# variables
zip_code = args.zip
country_code = args.country
units = args.units
api_key = args.apikey
location_code = str(zip_code) + ',' + str(country_code)

# create fonts
city_font = graphics.Font()
city_font.LoadFont("../fonts/6x10.bdf")
city_font_color = graphics.Color(200, 250, 200)

value_font = graphics.Font()
value_font.LoadFont("../fonts/5x8.bdf")
value_font_color = graphics.Color(200, 200, 250)


# functions
def make_api_request(location, unit, key):
    api_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = dict(zip=location, units=unit, appid=key)
    return requests.get(api_url, params)


def set_unit(unit):
    if unit == 'metric':
        val = 'C'
    else:
        val = 'F'
    return val


# main program
res = make_api_request(location_code, units, api_key)

if res.status_code != 200:
    print('Something went wrong: Code {}'.format(res.status_code))
    exit()
else:
    # parse json values
    source = res.json()
    city = source['name']
    humidity = 'H:' + str(source['main']['humidity']) + '%'
    temp = 'T:' + str(source['main']['temp']) + u"\N{DEGREE SIGN}" + str(set_unit(units))
    icon = source['weather'][0]['icon']
    # get weather icon
    icon_url = 'https://openweathermap.org/img/wn/' + icon + '@2x.png'
    img = Image.open(requests.get(icon_url, stream=True).raw)
    img.thumbnail((20, 20), Image.ANTIALIAS)
    # matrix canvas
    canvas = matrix.CreateFrameCanvas()
    # show on matrix
    matrix.Clear()
    graphics.DrawText(canvas, value_font, 1, 10, value_font_color, temp)
    graphics.DrawText(canvas, value_font, 1, 20, value_font_color, humidity)
    canvas.SetImage(img.convert('RGB'), 42, 0)
    graphics.DrawText(canvas, city_font, 1, 30, city_font_color, city)
    matrix.SwapOnVSync(canvas)
    time.sleep(15)

matrix.Clear()
