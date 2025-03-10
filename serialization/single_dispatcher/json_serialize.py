import json
from datetime import datetime, date
from decimal import Decimal
from functools import singledispatch

from serialization.model import Stock, Trade

activity = {
    "quotes": [
        Stock('TSLA', date(2018, 11, 22),
              Decimal('338.19'), Decimal('338.64'), Decimal('337.60'), Decimal('338.19'), 365_607),
        Stock('AAPL', date(2018, 11, 22),
              Decimal('176.66'), Decimal('177.25'), Decimal('176.64'), Decimal('176.78'), 3_699_184),
        Stock('MSFT', date(2018, 11, 22),
              Decimal('103.25'), Decimal('103.48'), Decimal('103.07'), Decimal('103.11'), 4_493_689)
    ],

    "trades": [
        Trade('TSLA', datetime(2018, 11, 22, 10, 5, 12), 'buy', Decimal('338.25'), 100, Decimal('9.99')),
        Trade('AAPL', datetime(2018, 11, 22, 10, 30, 5), 'sell', Decimal('177.01'), 20, Decimal('9.99'))
    ]
}

@singledispatch
def json_format(obj):
    try:
        d = obj.as_dict()
        d['objecttype'] = obj.__class__.__name__
        return d
    except:
        try:
            return super().default(obj)
        except:
            return str(obj)


@json_format.register(datetime)
def _(obj):
    return obj.isoformat()

@json_format.register(date)
def _(obj):
    return obj.isoformat()

@json_format.register(Decimal)
def _(obj):
    return (f"{str(obj)}")

print(json.dumps(activity, default=json_format ))
