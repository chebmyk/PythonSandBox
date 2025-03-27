class Person:
    def __init__(self, age):
        self.age = age

    def drink(self):
        return 'drinking'

    def drive(self):
        return 'driving'

    def drink_and_drive(self):
        return 'driving while drunk'



class ResponsiblePerson:

    def __init__(self, person):
        self.person = person


    def drink(self):
        if self.person.age < 18:
            return 'too young'
        else:
            return self.person.drink()

    def drive(self):
        if self.person.age < 16:
            return f'too young'
        else:
            return self.person.drive()

    def drink_and_drive(self):
        return 'dead'

p = Person(10)
p1 = ResponsiblePerson(p)

print(p1.drink())
print(p1.drive())
print(p1.drink_and_drive())

p1.age = 20

print(p1.drink())
print(p1.drive())
print(p1.drink_and_drive())