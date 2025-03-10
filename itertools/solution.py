import csv
import itertools
from collections import namedtuple
from datetime import datetime

vehicles = {
    'ssn': lambda v : str(v),
    'vehicle_make': lambda v : str(v),
    'vehicle_model': lambda v : str(v),
    'model_year': lambda v : int(v)
}
Vehicle = namedtuple('Vehicle', " ".join(vehicles.keys()))

update_status = {
    'ssn': lambda v : str(v),
    'last_updated': lambda v : date_parser(v),
    'created': lambda v : date_parser(v),
}
Status = namedtuple('Status', " ".join(update_status.keys()))

personal_info = {
    'ssn': lambda v : str(v),
    'first_name': lambda v : str(v),
    'last_name': lambda v : str(v),
    'gender': lambda v : str(v),
    'language': lambda v : str(v),
}
PersonalInfo = namedtuple('PersonalInfo', " ".join(personal_info.keys()))

employment = {
    'employer': lambda v : str(v),
    'department': lambda v : str(v),
    'employee_id': lambda v : str(v),
    'ssn': lambda v : str(v)
}
Employment = namedtuple('Employment', " ".join(employment.keys()))


def create_object(object_name, keys):
    return namedtuple(object_name, " ".join(keys))

##### Goal 1
# Your first task is to create iterators for each of the four files that contained cleaned up data,
# of the correct type (e.g. string, int, date, etc), and represented by a named tuple.
# For now these four iterators are just separate, independent iterators.

def file_reader(filename):
    with open(filename) as file:
        next(file)
        reader = csv.reader(file, delimiter=",", quotechar='"')
        yield from reader


def date_parser(value, format="%Y-%m-%dT%H:%M:%SZ"):
    if value:
        value = datetime.strptime(value, format)
    return value



##### Goal 2
# Create a single iterable that combines all the columns from all the iterators.
# The iterable should yield named tuples containing all the columns.
# Make sure that the SSN's across the files match!
# All the files are guaranteed to be in SSN sort order, and every SSN is unique, and every SSN appears in every file.
# Make sure the SSN is not repeated 4 times - one time per row is enough!

vehicles_data = file_reader("data/vehicles.csv")
update_status_data = file_reader("data/update_status.csv")
personal_info_data = file_reader("data/personal_info.csv")
employment_data = file_reader("data/employment.csv")

parse_params = lambda d, v : tuple(d[key](value) for key, value in zip(d.keys(), v))

v_cols = tuple(vehicles.keys())
s_cols = tuple(update_status.keys() - ('ssn',))
i_cols = tuple(personal_info.keys() - ('ssn',))
e_cols = tuple(employment.keys() - ('ssn',))

combined_headers = tuple(c for c in itertools.chain.from_iterable([v_cols,s_cols,i_cols,e_cols]))

print("Combined_cols",combined_headers)

filter = [
 *[i in v_cols for i in vehicles.keys()],
 *[i in s_cols for i in update_status.keys()],
 *[i in i_cols for i in personal_info.keys()],
 *[i in e_cols for i in employment.keys()],
 ]

print("filter", list(zip([*vehicles.keys(),*update_status.keys(), *personal_info.keys(),*employment.keys()],filter)))

dataset = []

for vehicle, status, info, empl in zip(vehicles_data, update_status_data, personal_info_data, employment_data):

    v = Vehicle(*parse_params(vehicles, vehicle))
    s = Status(*parse_params(update_status, status))
    i = PersonalInfo(*parse_params(personal_info, info))
    e = Employment(*parse_params(employment, empl))

    merged = [val for val in itertools.chain.from_iterable([v,s,i,e])]
    new_val = [v for v, f in zip(merged, filter) if f == True]

    #print(len(combined_headers), len(filter), len(new_val))

    ResultData = create_object("ResultData", combined_headers)
    dataset.append(ResultData(*new_val))


##### Goal 3
#
# Next, you want to identify any stale records, where stale simply means the record has not been updated since 3/1/2017
# (e.g. last update date < 3/1/2017). Create an iterator that only contains current records (i.e. not stale)
# based on the `last_updated` field from the `status_update` file.

print(dataset[:5])

def get_actual(dataset):
    print("dataset", len(dataset))
    return [r for r in dataset if r.last_updated > datetime.strptime('3/1/2017', "%d/%m/%Y")]

actual = get_actual(dataset)

print('Actual', actual)


##### Goal 4
# Find the largest group of car makes for each gender.
# Possibly more than one such group per gender exists (equal sizes).