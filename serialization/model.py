class Stock:
    def __init__(self, symbol, date, open_, high, low, close, volume):
        self.symbol = symbol
        self.date = date
        self.open = open_
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def __repr__(self):
        return f'''
        Stock (
            symbol= {self.symbol}
            date= {self.date}
            open= {self.open}
            high= {self.high}
            low= {self.low}
            close= {self.close}
            volume= {self.volume}
        )
        '''

    def as_dict(self):
        return dict (
            symbol= self.symbol,
            date= self.date,
            open= self.open,
            high= self.high,
            low= self.low,
            close= self.close,
            volume= self.volume
        )


class Trade:

    def __init__(self, symbol, timestamp, order, price, volume, commission):
        self.symbol = symbol
        self.timestamp = timestamp
        self.order = order
        self.price = price
        self.commission = commission
        self.volume = volume

    def as_dict(self):
        return dict(
            symbol = self.symbol,
            timestamp = self.timestamp,
            order = self.order,
            price = self.price,
            commission = self.commission,
            volume = self.volume
        )

    def __repr__(self):
        return f'''
        Trade(
            symbol = {self.symbol},
            timestamp = {self.timestamp},
            order = {self.order},
            price = {self.price},
            commission = {self.commission},
            volume = {self.volume}
        )
        '''

