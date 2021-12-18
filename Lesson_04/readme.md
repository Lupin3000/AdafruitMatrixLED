# Lesson 04

You can now implement your projects with the help of other libraries/packages. You can improve or change these examples at any time.

## Video Player

> Please install OpenCV packages for Python first! Dependent to your Hardware, you will come quickly to the limits.

File: [VideoPlayer.py](./VideoPlayer.py)

```shell
# show help
$ sudo python ./VideoPlayer.py -h

# execute with default
$ sudo python ./VideoPlayer.py

# execute with parameter
$ sudo python ./VideoPlayer.py --video '../video/video.mov'
```

## Crypto LED

> Please install requests packages for Python first! You need the API key from [nomics](https://nomics.com/).

File: [CryptoLED.py](./CryptoLED.py)

```shell
# show help
$ sudo python ./CryptoLED.py -h

# execute with default
$ sudo python ./CryptoLED.py [API KEY]

# execute with parameter
$ sudo python ./CryptoLED.py [API KEY] --currency=CHF
$ sudo python ./CryptoLED.py [API KEY] --currency=CHF --crypto='LTC,ETH,DOT'
```

## Weather LED

> Please install requests packages for Python first! You need the API key from [openweathermap](https://openweathermap.org/).

File: [WeatherLED.py](./WeatherLED.py)

```shell
# show help
$ sudo python ./WeatherLED.py -h

# execute with default
$ sudo python ./WeatherLED.py [ZIP CODE] [COUNTRY CODE] [API KEY]

# execute with parameter
$ sudo python ./WeatherLED.py [ZIP CODE] [COUNTRY CODE] [API KEY] --units 'imperial'
```

[Go Back](../readme.md)