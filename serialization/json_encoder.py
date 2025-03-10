from json import JSONEncoder
from datetime import date, datetime
from decimal import Decimal
import json
from serialization.model import Trade, Stock

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


class StockEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return (f"{str(obj)}")
        elif isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, date):
            return obj.isoformat()
        else:
            try:
                d = obj.as_dict()
                d['objecttype'] = obj.__class__.__name__
                return d
            except:
                return super().default(obj)


print(json.dumps(activity, cls=StockEncoder, indent=2))
