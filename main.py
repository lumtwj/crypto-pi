try:
    from waveshare_epd import epd2in13_V2
except ImportError:
    pass

from app.chart import Chart
from app.crypto_iterator import CryptoIterator
from PIL import Image, ImageDraw, ImageFont
import os

epd = epd2in13_V2.EPD()
epd.init(epd.FULL_UPDATE)
epd.Clear(0xFF)

c = Chart()
data = c.load()

w, h = 250, 122
font = ImageFont.truetype(os.path.join('./assets/OpenSans-Bold.ttf'), 14)

ci = CryptoIterator(data)
while True:
    d = Chart().load()
    chart = d[ci.get()]

    symbol = chart['symbol'].upper()
    chart_path = chart['chart_path']
    price = chart['price']
    percentage_change = chart['percentage']

    print(symbol, price, percentage_change)

    image = Image.new(mode='1', size=(epd2in13_V2.EPD_HEIGHT, epd2in13_V2.EPD_WIDTH), color=255)
    HRedImage = Image.new(mode='1', size=(epd2in13_V2.EPD_HEIGHT, epd2in13_V2.EPD_WIDTH), color=255)
    draw = ImageDraw.Draw(image)

    # draw chart
    c = Image.open(chart_path)
    image.paste(c, (0, 0))

    # draw text
    text = symbol + '  $' + price + '  ' + percentage_change
    tw, th = font.getsize(text)
    draw.text((10, h - th - 5), text, font=font, fill=0)

    rotated_image = image.rotate(180)

    epd.display(epd.getbuffer(rotated_image))

    ci.next()
