class Car:
    def __init__(self, driver):
        self.driver = driver

    def drive(self):
        print(f"car is driven by {self.driver.name}")


class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class CarProxy:
    def __init__(self, driver):
        self.driver = driver
        self.car = Car(self.driver)

    def drive(self):
        if self.driver.age < 16:
            print(f'Driver age is less then 16')
        else:
            self.car.drive()

#========================================================
driver_john = Driver('John', 5)
car = Car(driver_john)
car.drive()
#=========================================================
car2 = CarProxy(Driver('Sam', 14))
car2.drive()
