class Connection:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Connection, cls).__new__(cls, *args, ** kwargs)

        return cls._instance



conn1 = Connection()
conn2 = Connection()

print(conn1 == conn2)
print(conn1 is conn2)


#===========Use Decorator========================



def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class DBConnection:
    def __init__(self):
        print('Db connection init')


dbcon1= DBConnection()
dbcon2 = DBConnection()

print(dbcon1 == dbcon2)
print(dbcon1 is dbcon2)


#===========Use Meta Class========================


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__( *args, ** kwargs)
        return cls._instances[cls]

class DBConnection(metaclass=Singleton):
    def __init__(self):
        print('Connection init')


dbcon1= DBConnection()
dbcon2 = DBConnection()

print(dbcon1 == dbcon2)
print(dbcon1 is dbcon2)