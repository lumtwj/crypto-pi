try:
    from waveshare_epd import epd2in13_V2
except ImportError:
    pass

from app.chart import Chart
from PIL import Image, ImageDraw, ImageFont
import os

epd = epd2in13_V2.EPD()
epd.init(epd.FULL_UPDATE)
epd.Clear(0xFF)

chart = Chart()
data = chart.load()

w, h = 250, 122
font = ImageFont.truetype(os.path.join('./assets/OpenSans-Bold.ttf'), 14)

for chart in data:
    image = Image.new(mode='1', size=(epd2in13_V2.EPD_HEIGHT, epd2in13_V2.EPD_WDITH), color=255)
    HRedImage = Image.new(mode='1', size=(epd2in13_V2.EPD_HEIGHT, epd2in13_V2.EPD_WIDTH), color=255)
    draw = ImageDraw.Draw(image)

    # draw chart
    c = Image.open(chart['chart_path'])
    image.paste(c, (0, 0))

    # draw text
    text = chart['symbol'].upper() + '  $' + chart['price'] + '  ' + chart['percentage']
    tw, th = font.getsize(text)
    draw.text((10, h - th - 5), text, font=font, fill=0)

    epd.display(epd.getbuffer(image), epd.getbuffer(HRedImage))
    break
