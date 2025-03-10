from  datetime import date, datetime
from decimal import Decimal
import json
from json import JSONDecoder

from serialization.model import Stock, Trade

json_obj='''
{
  "quotes": [
    {
      "symbol": "TSLA",
      "date": "2018-11-22",
      "open": "338.19",
      "high": "338.64",
      "low": "337.60",
      "close": "338.19",
      "volume": 365607,
      "objecttype": "Stock"
    },
    {
      "symbol": "AAPL",
      "date": "2018-11-22",
      "open": "176.66",
      "high": "177.25",
      "low": "176.64",
      "close": "176.78",
      "volume": 3699184,
      "objecttype": "Stock"
    },
    {
      "symbol": "MSFT",
      "date": "2018-11-22",
      "open": "103.25",
      "high": "103.48",
      "low": "103.07",
      "close": "103.11",
      "volume": 4493689,
      "objecttype": "Stock"
    }
  ],
  "trades": [
    {
      "symbol": "TSLA",
      "timestamp": "2018-11-22T10:05:12",
      "order": "buy",
      "price": "338.25",
      "commission": "9.99",
      "volume": 100,
      "objecttype": "Trade"
    },
    {
      "symbol": "AAPL",
      "timestamp": "2018-11-22T10:30:05",
      "order": "sell",
      "price": "177.01",
      "commission": "9.99",
      "volume": 20,
      "objecttype": "Trade"
    }
  ]
}

'''


def json_decoder(arg):
    obj_type = arg.get('objecttype', None)
    if obj_type == Stock.__class__.__name__:
       return decode_stock(arg)
    elif obj_type == Trade.__class__.__name__:
        return decode_trade(arg)
    else:
        return arg

def decode_stock(obj):
    return Stock(
        symbol = obj['symbol'],
        date =datetime.strptime(obj['date'], '%Y-%m-%d').date(),
        open_ = Decimal(obj['open']),
        high = Decimal(obj['high']),
        low = Decimal(obj['low']),
        close = Decimal(obj['close']),
        volume = int(obj['volume'])
    )

def decode_trade(obj):
    return Trade (
        symbol = obj['symbol'],
        timestamp = datetime.strptime(obj['timestamp'], '%Y-%m-%dT%H:%M:%S'),
        order = obj['order'],
        price = Decimal(obj['price']),
        commission = Decimal(obj['commission']),
        volume = int(obj['volume'])
    )

print('Result', json.loads(json_obj, object_hook=json_decoder))


class CustomJSONDecoder(JSONDecoder):
    def decode(self, arg):
        data = json.loads(arg)
        return self.parse_activity(arg)

    def parse_activity(self, obj):
        if isinstance(obj, dict):
            result = json_decoder(obj)
            if isinstance(result, dict):
                for k,v in obj.items():
                    obj[k] = self.parse_activity(obj)
        elif isinstance(obj, list):
            for e in obj:
                self.parse_activity(e)

        return obj

print('Result2', json.loads(json_obj, cls=CustomJSONDecoder))
