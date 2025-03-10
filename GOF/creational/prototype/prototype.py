import copy


class Person():
    def __init__(self, name, address):
        self.name = name
        self. address = address

    def __str__(self):
        return f'Person {self.name} adress: {self.address}'


class Address():
    def __init__(self, city, street):
        self.city = city
        self.street = street

    def __str__(self):
        return f'Address({self.city}, {self.street})'

address = Address('London', 'Dive str')

john = Person('John', address)
jane = Person('Jane', address)
print('before')
print(john)
print(jane)
# will override both address
jane.address.street = 'Trafalgar str'
print('after')
print(john)
print(jane)
print('=========== Fixed ================')
#===================================
address = Address('London', 'Dive str')
john_address = copy.deepcopy(address)
jane_address = copy.deepcopy(address)

john = Person('John', john_address)
jane = Person('Jane', jane_address)
print('before')
print(john)
print(jane)
# will override both address
jane.address.street = 'Trafalgar str'
print('after')
print(john)
print(jane)

