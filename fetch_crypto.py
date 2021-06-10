from app.coingecko import Coingecko
from app.chart import Chart

token_list = ['kishu-inu', 'chainlink', 'bitcoin']

chart = Chart()

for token in token_list:
    coingecko = Coingecko(token)
    symbol = coingecko.get_symbol()
    coingecko.get_chart_data()
    prices = coingecko.get_prices()
    chart.generate_line_chart(symbol, prices)

chart.save()
