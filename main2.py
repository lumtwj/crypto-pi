try:
    from waveshare_epd import epd2in13_V2
except ImportError:
    pass

from app.chart import Chart
from app.crypto_iterator import CryptoIterator
from app.coingecko import Coingecko
from PIL import Image, ImageDraw, ImageFont
import os

epd = epd2in13_V2.EPD()
epd.init(epd.FULL_UPDATE)
epd.Clear(0xFF)

crypto_iterator = CryptoIterator(interval=10)
chart = Chart()

w, h = 250, 122
font = ImageFont.truetype(os.path.join('./assets/OpenSans-Bold.ttf'), 14)

try:
    while True:
        token = crypto_iterator.get()

        coingecko = Coingecko(token)
        symbol = coingecko.get_symbol()
        coingecko.get_chart_data()
        prices = coingecko.get_prices()

        chart_path, price, percentage_change, last_updated = chart.generate_line_chart(token, prices)

        print(symbol, price, percentage_change)

        image = Image.new(mode='1', size=(epd2in13_V2.EPD_HEIGHT, epd2in13_V2.EPD_WIDTH), color=255)
        HRedImage = Image.new(mode='1', size=(epd2in13_V2.EPD_HEIGHT, epd2in13_V2.EPD_WIDTH), color=255)
        draw = ImageDraw.Draw(image)

        # draw chart
        chart_image = Image.open(chart_path)
        image.paste(chart_image, (0, 0))

        # draw text
        tw, th = font.getsize(last_updated)
        draw.text((w - tw, 0), last_updated, font=font, fill=0)

        # draw text
        text = symbol.upper() + '  $' + price + '  ' + percentage_change
        tw, th = font.getsize(text)
        draw.text((10, h - th - 5), text, font=font, fill=0)

        rotated_image = image.rotate(180)

        epd.display(epd.getbuffer(rotated_image))

        crypto_iterator.next()
except KeyboardInterrupt:
    epd.Clear(0xFF)

# chart = Chart()
# data = chart.load()

# w, h = 250, 122
# font = ImageFont.truetype(os.path.join('./assets/OpenSans-Bold.ttf'), 14)
#
# crypto_iterator = CryptoIterator(data)
# try:
#     while True:
#         data = chart.load()
#         chart_data = data[crypto_iterator.get()]
#
#         symbol = chart_data['symbol'].upper()
#         chart_path = chart_data['chart_path']
#         price = chart_data['price']
#         percentage_change = chart_data['percentage']
#
#         print(symbol, price, percentage_change)
#
#         image = Image.new(mode='1', size=(epd2in13_V2.EPD_HEIGHT, epd2in13_V2.EPD_WIDTH), color=255)
#         HRedImage = Image.new(mode='1', size=(epd2in13_V2.EPD_HEIGHT, epd2in13_V2.EPD_WIDTH), color=255)
#         draw = ImageDraw.Draw(image)
#
#         # draw text
#         last_updated_text = chart.last_updated()
#         tw, th = font.getsize(last_updated_text)
#         draw.text((w - tw, 0), last_updated_text, font=font, fill=0)
#
#         # draw chart
#         chart_image = Image.open(chart_path)
#         image.paste(chart_image, (0, 0))
#
#         # draw text
#         text = symbol + '  $' + price + '  ' + percentage_change
#         tw, th = font.getsize(text)
#         draw.text((10, h - th - 5), text, font=font, fill=0)
#
#         rotated_image = image.rotate(180)
#
#         epd.display(epd.getbuffer(rotated_image))
#
#         crypto_iterator.next()
# except KeyboardInterrupt:
#     epd.Clear(0xFF)
