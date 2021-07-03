import matplotlib.pyplot as plt
import decimal
from datetime import datetime

ctx = decimal.Context()
ctx.prec = 20
token_store = './output/tokens.json'

plt.style.use('./assets/presentation.mplstyle')


class Chart:
    @staticmethod
    def generate_line_chart(coin_id, y):
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

        last_updated = datetime.now().strftime("%d %b %Y, %H:%M")

        return chart_path, formatted_price, formatted_percentage, last_updated


def mm_to_inch(mm):
    return mm * 0.0393701


def float_to_str(f):
    """
    Convert the given float to a string,
    without resorting to scientific notation
    """
    d1 = ctx.create_decimal(repr(f))
    return format(d1, 'f')[:14]
