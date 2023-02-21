import json
import requests
from botconfig import exchange

class APIException(Exception):
    pass

class Convertor:
    @staticmethod
    def get_price(base, quote, amount):
        try:
            base_key = exchange[base.lower()]
        except KeyError:
            raise APIException(f"Валюта {base} не найдена!")

        try:
            quote_key = exchange[quote.lower()]
        except KeyError:
            raise APIException(f"Валюта {quote} не найдена!")

        if base_key == quote_key:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}!')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}!')

        payload = {}
        headers = {
        "apikey": "hUKFE6tpeYBbne8SF9I6ZQxhE7SKCfg6"
        }
        r = requests.get(f"https://api.apilayer.com/exchangerates_data/latest?base={base_key}&symbols={quote_key}",
                     headers=headers, data=payload)
        respond = json.loads(r.content)
        new_price = respond['rates'][quote_key] * amount
        new_price = round(new_price, 3)
        message = f"Цена {amount} {base} в {quote} : {new_price}"
        return message