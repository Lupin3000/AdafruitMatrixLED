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

# create fonts and colors
time_font = graphics.Font()
time_font.LoadFont("../fonts/9x15.bdf")
time_color = graphics.Color(250, 250, 250)

meridiem_day_year_font = graphics.Font()
meridiem_day_year_font.LoadFont("../fonts/5x8.bdf")
meridiem_color = graphics.Color(100, 250, 100)
day_year_color = graphics.Color(200, 200, 250)

month_font = graphics.Font()
month_font.LoadFont("../fonts/7x13.bdf")
month_color = graphics.Color(100, 100, 250)

# create canvas
canvas = matrix.CreateFrameCanvas()

while True:
    if datetime.now() >= duration:
        break
    # get current time and date
    now = datetime.now()
    current_time = now.strftime("%I:%M")
    current_meridiem = now.strftime("%p")
    current_month = now.strftime("%B")
    current_day_year = now.strftime("%d, %Y")
    # show on matrix
    matrix.Clear()
    graphics.DrawText(canvas, time_font, 2, 12, time_color, current_time)
    graphics.DrawText(canvas, meridiem_day_year_font, 50, 12, meridiem_color, current_meridiem)
    graphics.DrawText(canvas, month_font, 3, 22, month_color, current_month)
    graphics.DrawText(canvas, meridiem_day_year_font, 3, 30, day_year_color, current_day_year)
    matrix.SwapOnVSync(canvas)

matrix.Clear()
