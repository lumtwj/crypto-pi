import matplotlib.pyplot as plt
import decimal
import json

ctx = decimal.Context()
ctx.prec = 20
token_store = './output/tokens.json'

plt.style.use('./assets/presentation.mplstyle')


def mm_to_inch(mm):
    return mm * 0.0393701


class Chart:
    def __init__(self):
        self.data = []

    def generate_line_chart(self, symbol, y):
        x = [x for x in range(len(y))]

        fig, ax = plt.subplots()
        ax.plot(x, y, color='black')
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.margins(x=0)

        fig.set_size_inches(mm_to_inch(50.55), mm_to_inch(25.71))
        frame1 = plt.gca()
        frame1.axes.get_xaxis().set_ticks([])

        chart_path = './output/{symbol}.png'.format(symbol=symbol)
        plt.savefig(chart_path.format(symbol=symbol), transparent=True, bbox_inches='tight', dpi=130)

        price = y[-1]
        percentage = (price - y[0]) / y[0] * 100

        formatted_price = (float_to_str(price) if price < 0.01 else "{:.2f}".format(price))
        formatted_percentage = "{:.1f}".format(percentage) + '%'

        self.data.append({
            'chart_path': chart_path,
            'symbol': symbol,
            'price': formatted_price,
            'percentage': formatted_percentage
        })

    def save(self):
        f = open(token_store, "w")
        f.write(json.dumps(self.data))
        f.close()

        return self.data

    def load(self):
        f = open(token_store, "r")
        self.data = json.loads(f.read())

        return self.data


def float_to_str(f):
    """
    Convert the given float to a string,
    without resorting to scientific notation
    """
    d1 = ctx.create_decimal(repr(f))
    return format(d1, 'f')[:14]
