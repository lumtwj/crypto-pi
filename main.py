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

crypto_iterator = CryptoIterator()
chart = Chart()

w, h = 250, 122
font = ImageFont.truetype(os.path.join('./assets/OpenSans-Bold.ttf'), 14)
small_font = ImageFont.truetype(os.path.join('./assets/OpenSans-Bold.ttf'), 12)

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
        tw, th = small_font.getsize(last_updated)
        draw.text((w - tw, 0), last_updated, font=small_font, fill=0)

        # draw text
        text = symbol.upper() + '  $' + price + '  ' + percentage_change
        tw, th = font.getsize(text)
        draw.text((10, h - th - 5), text, font=font, fill=0)

        rotated_image = image.rotate(180)

        epd.display(epd.getbuffer(rotated_image))

        crypto_iterator.next()
except KeyboardInterrupt:
    epd.Clear(0xFF)
