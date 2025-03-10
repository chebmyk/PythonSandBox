from collections import namedtuple, defaultdict
from datetime import datetime

#
# Summons Number,Plate ID,Registration State,Plate Type,Issue Date,Violation Code,Vehicle Body Type,Vehicle Make,Violation Description
# 4006478550,VAD7274,VA,PAS,10/5/2016,5,4D,BMW,BUS LANE VIOLATION

##### Goal 1
# Create a lazy iterator that will return a named tuple of the data in each row. The data types should be appropriate -
# i.e. if the column is a date, you should be storing dates in the named tuple, if the field is an integer,
# then it should be stored as an integer, etc.



file = 'nyc_parking_tickets_extract.csv'


class TicketIterator():

    file_header = {
        "number": lambda d: int(d),
        "plate": lambda d: str(d),
        "registration": lambda d: str(d),
        "plate_type": lambda d: str(d),
        "issue_date": lambda d: datetime.strptime(d, '%m/%d/%Y').date(),
        "violation_code": lambda d: int(d),
        "body_type":  lambda d: str(d),
        "make":  lambda d: str(d),
        "violation": lambda d: str(d),
    }

    Ticket = namedtuple("Ticket", " ".join(file_header.keys()))

    def __init__(self, filename):
        self.file = self.read_file(filename)


    def read_file(self, filename):
        with open(filename) as file:
            next(file)
            yield from file

    def __iter__(self):
        return self

    def __next__(self):
        values =  tuple(self.file_header[header](data) for header, data in zip(self.file_header, next(self.file).replace('\n','').split(',')))
        return self.Ticket(*values)




## Goal 2
# Calculate the number of violations by car make.

summary = defaultdict(int)

for ticket in TicketIterator(file):
    summary[ticket.make] +=1

print(    "Summary",
          {
              k: v for k, v in sorted(summary.items(), key=lambda k: k[1], reverse=True)
          }
      )
