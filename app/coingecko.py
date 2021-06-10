from requests.models import PreparedRequest
import requests

root_url = 'https://api.coingecko.com/api/v3'


class Coingecko:
    def __init__(self, coin_id, fiat_currency='usd', days=1):
        self.coin_id = coin_id
        self.fiat_currency = fiat_currency
        self.days = days
        self.result = None

    def get_chart_data(self):
        api = root_url + '/coins/{coin_id}/market_chart'.format(coin_id=self.coin_id)

        params = {'vs_currency': self.fiat_currency, 'days': self.days}
        req = PreparedRequest()
        req.prepare_url(api, params)

        url = req.url
        r = requests.get(url)

        self.result = r.json()

    def get_symbol(self):
        api = root_url + '/coins/{coin_id}'.format(coin_id=self.coin_id)
        r = requests.get(api)

        result = r.json()
        return result['symbol']

    def get_prices(self):
        prices = self.result['prices']
        return [price[1] for price in prices]

    def get_data(self):
        return self.result
