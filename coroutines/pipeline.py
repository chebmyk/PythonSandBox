import csv
import itertools


def csv_read(filename):
    with open(filename) as  file:
        dialect = csv.Sniffer().sniff(file.read(2000))
        file.seek(0)
        next(file)
        yield from csv.reader(file, dialect= dialect)

def filter(rows, contains):
    for row in rows:
        if contains in row[0]:
            yield row



# data = csv_read('cars.csv')
# chevrolet_filter = filter(data, 'Chevrolet')
# chevrolet_carlo = filter(chevrolet_filter, 'Carlo')
#
# for row in itertools.islice(chevrolet_carlo, 5):
#     print(row)
#

def result_filter(filename, *filters):
    data = csv_read(filename)
    for f in filters:
        data = filter(data, f)
    yield from data



result = result_filter('cars.csv', "Chevrolet", 'Carlo')

for i in result:
    print(i)