import csv
from collections import namedtuple
from contextlib import contextmanager
from itertools import islice


def data_iter(iter, data_class):
    for row in iter:
        yield data_class(*row)


def get_csv_dialect(filename, lines=1000):
    with open(filename) as file:
        return csv.Sniffer().sniff(file.read(lines))


@contextmanager
def parse_data(filename):
    file = open(filename)
    try:
        reader = csv.reader(file, get_csv_dialect(filename))
        headers = map(lambda s: s.lower(), next(reader))
        row = namedtuple('Data', headers)
        yield data_iter(reader, row)
    finally:
        file.close()


with parse_data('cars.csv') as data:
    for row in islice(data, 10):
        print(row)