try:
    from waveshare_epd import epd2in13_V2
except ImportError:
    pass

epd = epd2in13_V2.EPD()
epd.init(epd.FULL_UPDATE)
epd.Clear(0xFF)