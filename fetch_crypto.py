from app.coingecko import Coingecko
from app.chart import Chart
import json
import glob
import os

token_list = []

with open('./config.json') as reader:
    json_string = reader.read()
    json_data = json.loads(json_string)
    token_list = json_data["token_list"]

chart = Chart()

for token in token_list:
    coingecko = Coingecko(token)
    symbol = coingecko.get_symbol()
    coingecko.get_chart_data()
    prices = coingecko.get_prices()
    chart.generate_line_chart(token, symbol, prices)

chart.save()

output_path = './output/'
chart_paths = output_path + '*.png'

for chart_path in glob.glob(chart_paths):
    chart_file_name = chart_path[len(output_path):]
    token_name = chart_file_name[:chart_file_name.rfind('.')]
    if token_name not in token_list:
        os.remove(chart_path)
