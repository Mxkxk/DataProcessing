import json
import requests

class CurrencyTrading(object):
    """Class for trading currency"""
    def __init__(self):
        data = requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")
        self.json = data.json()
        self.course = [[d[i] for i in d] for d in self.json]
    @property
    def currencys(self):
        return ["USD", "EUR", "RUB", "UAH"]
    #return list with result and value
    def trade(self, curr_from, curr_to, ammoun_of_money):        
        if curr_from in self.currencys and curr_to in self.currencys and curr_from != curr_to:
            try:
                money = float(ammoun_of_money)
                if money <= 0:
                    raise Exception
                #
                if curr_from != "UAH":
                    money *= float(self.course[self.currencys.index(curr_from)][2])
                    if curr_to != "UAH":
                        money /= float(self.course[self.currencys.index(curr_to)][2])
                else:
                    money /= float(self.course[self.currencys.index(curr_to)][3])
                #форматуємо сумму гроше до копійок
                return ["Success trade", float("".join(str(money)[0:(str(money).find(".")+3)]))]
            except Exception:
                return ["Wrong ammount of money", -1]
        else:
            return ["Wrong currency" if (curr_from != curr_to) else "Currencies must be different" , -1]