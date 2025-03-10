from datetime import date, datetime
from decimal import Decimal
from marshmallow import Schema, fields, post_load
from serialization.model import Trade, Stock


class StockSchema(Schema):
    symbol= fields.Str()
    date= fields.Date()
    open= fields.Decimal(as_string=True)
    high= fields.Decimal(as_string=True)
    low= fields.Decimal(as_string=True)
    close= fields.Decimal(as_string=True)
    volume= fields.Integer()

    @post_load
    def get_stock(self, data, **kwargs):
        data["open_"] = data.pop("open")
        return Stock(**data)

class TradeSchema(Schema):
    symbol= fields.Str()
    timestamp= fields.DateTime()
    order= fields.Str()
    price= fields.Decimal(as_string=True)
    commission= fields.Decimal(as_string=True)
    volume= fields.Integer()

    @post_load
    def get_trade(self, data, **kwargs):
        return Trade(**data)


class ActivitySchema(Schema):
    quotes = fields.Nested(StockSchema, many=True)
    trades = fields.Nested(TradeSchema, many=True)

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

result_json = ActivitySchema().dumps(activity, indent = 2)

print("json_result", result_json)


deserialize = ActivitySchema().loads(result_json)

print("deserialize", deserialize)
