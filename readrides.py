from dataclasses import dataclass
import csv


# Memory Use: Current 114,729,038, Peak 114,759,608
def read_rides_as_tuples(filename):
    """
    Read the bus ride data as a list of tuples
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # skip headers
        for row in rows:
            match row:
                case [route, date, daytype, rides]:
                    records.append((route, date, daytype, int(rides)))
    return records


# Memory Use: Current 179,414,528, Peak 179,445,166
def read_rides_as_dict(filename):
    """
    Read the bus ride data as a list of dicts
    """
    records = []
    with open(filename) as f:
        rows = csv.DictReader(f)
        headings = next(rows)  # skip headers
        for row in rows:
            row["rides"] = int(row["rides"])
            records.append(row)
    return records


# A user-defined class
# Memory Use: Current 128,593,798, Peak 128,624,368
def read_rides_as_class(filename):
    """
    Read the bus ride data as a list of user-defined class
    """

    @dataclass
    class Row:
        route: str
        date: str
        daytype: str
        rides: int

    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # skip headers
        for row in rows:
            match row:
                case [route, date, daytype, rides]:
                    records.append(Row(route, date, daytype, int(rides)))
    return records


# A named tuple
# Memory Use: Current 119,354,865, Peak 119,385,435
def read_rides_as_nt(filename):
    """
    Read the bus ride data as a list of namedtuples
    """
    from collections import namedtuple

    Row = namedtuple("Row", ["route", "date", "daytype", "rides"])
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # skip headers
        for row in rows:
            match row:
                case [route, date, daytype, rides]:
                    records.append(Row(route, date, daytype, int(rides)))
    return records


# A class with __slots__
# Memory Use: Current 110,111,046, Peak 110,141,616
def read_rides_as_slot(filename):
    """
    Read the bus ride data as a list of classes with slots
    """

    class Row:
        __slots__ = ["route", "date", "daytype", "rides"]

        def __init__(self, route, date, daytype, rides):
            self.route = route
            self.date = date
            self.daytype = daytype
            self.rides = rides

    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # skip headers
        for row in rows:
            match row:
                case [route, date, daytype, rides]:
                    records.append(Row(route, date, daytype, int(rides)))
    return records


if __name__ == "__main__":
    import tracemalloc

    tracemalloc.start()
    # rows = read_rides_as_tuples("Data/ctabus.csv")
    # rows = read_rides_as_dict("Data/ctabus.csv")
    # rows = read_rides_as_class("Data/ctabus.csv")
    rows = read_rides_as_nt("Data/ctabus.csv")
    # rows = read_rides_as_slot("Data/ctabus.csv")
    print("Memory Use: Current %d, Peak %d" % tracemalloc.get_traced_memory())
