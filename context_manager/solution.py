import csv
from collections import namedtuple
from itertools import islice

def get_csv_dialect(filename, lines=1000):
    with open(filename) as file:
        return csv.Sniffer().sniff(file.read(lines))


class FileParser:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self._f = open(self.filename)
        self._reader = csv.reader((self._f), get_csv_dialect(self.filename))
        headers = map(lambda s: s.lower(), next(self._reader))
        self._row = namedtuple('Data', headers)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._f.close()
        return False

    def __iter__(self):
        return self

    def __next__(self):
        if self._f.closed:
            raise StopIteration

        return self._row(*next(self._reader))


with FileParser('cars.csv') as data:
    for row in islice(data, 10):
        print(row)