import json
import requests

class CurrencyTrading(object):
    """Class for trading currency"""
    def __init__(self):
        data = requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")
        self.json = data.json()
        self.course = [[d[i] for i in d] for d in self.json]
        print(self.course)
    @property
    def currencys(self):
        return ["USD", "EUR", "RUB", "UAH"]
    def trade(self, curr_from, curr_to, ammoun_of_money):
        if curr_from in self.currencys and curr_to in self.currencys:
            try:
                money = int(ammoun_of_money)
                if money <= 0:
                    raise Exception
                for d in self.json:
                    pass
            except Exception:
                return "Wrong ammount of money"
        else:
            return "Wrong currency"
        



