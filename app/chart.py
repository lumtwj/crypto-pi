import matplotlib.pyplot as plt
import decimal
import json
import time
from datetime import datetime

ctx = decimal.Context()
ctx.prec = 20
token_store = './output/tokens.json'

plt.style.use('./assets/presentation.mplstyle')


def mm_to_inch(mm):
    return mm * 0.0393701


class Chart:
    def __init__(self):
        self.data = []
        self.last_updated = None

    def generate_line_chart(self, coin_id, symbol, y):
        x = [x for x in range(len(y))]

        fig, ax = plt.subplots()
        ax.plot(x, y, color='black')
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.margins(x=0)

        fig.set_size_inches(mm_to_inch(50.55), mm_to_inch(25.71))
        frame1 = plt.gca()
        frame1.axes.get_xaxis().set_ticks([])

        chart_path = './output/{coin_id}.png'.format(coin_id=coin_id)
        plt.savefig(chart_path, transparent=True, bbox_inches='tight', dpi=130)

        price = y[-1]
        percentage = (price - y[0]) / y[0] * 100

        formatted_price = (float_to_str(price) if price < 0.01 else "{0:,.2f}".format(price))
        formatted_percentage = "{:.1f}".format(percentage) + '%'

        self.data.append({
            'chart_path': chart_path,
            'symbol': symbol,
            'price': formatted_price,
            'percentage': formatted_percentage
        })

    def save(self):
        f = open(token_store, "w")
        f.write(json.dumps({
            'data': self.data,
            'last_updated': time.time()
        }))
        f.close()

        return self.data

    def load(self):
        f = open(token_store, "r")
        tokens = json.loads(f.read())
        self.data = tokens['data']
        last_updated = datetime.fromtimestamp(tokens['last_updated'])
        self.last_updated = last_updated.strftime("%d %b %Y, %H:%M")

        return self.data

    def get_last_updated(self):
        return self.last_updated


def float_to_str(f):
    """
    Convert the given float to a string,
    without resorting to scientific notation
    """
    d1 = ctx.create_decimal(repr(f))
    return format(d1, 'f')[:14]
