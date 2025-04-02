import unittest
from descriptors.field_validators import IntegerField

class TestIntField(unittest.TestCase):
    class Person:
        age = IntegerField(0, 120)

    def test_age_valid(self):
        p = self.Person()
        p.age = 30
        self.assertEqual(p.age, 30)

    def test_age_invalid(self):
        p = self.Person()
        with self.assertRaises(ValueError) as context:
            p.age = -10
        self.assertEqual(str(context.exception), "age must be greater than or equal to 0")


class TestIntField2(unittest.TestCase):
    @staticmethod
    def create_person_class(min_age, max_age):
        _cls = type('Person', (object,), {'age': IntegerField(min_age, max_age)})  # Create a new class dynamically
        return _cls()


    def test_age_valid_type(self):
        _min = 0
        _max = 10
        person = self.create_person_class(_min, _max)

        for i,value in enumerate(range(_min, _max + 1)):
            with self.subTest(test_number = i):
                person.age = value
                self.assertEqual(person.age, value)

    def test_age_invalid_type(self):
        min_ = -10
        max_ = 10


        person = self.create_person_class(min_, max_)

        for i,value in enumerate(range(min_, -5, min_)):  # Testing invalid values below the minimum
            with self.subTest(test_number = i):
                with self.assertRaises(ValueError) as context:
                        person.age = value

    def test_class_get_name(self):
        """
        Test to ensure the class name is set correctly when creating a new class dynamically.
        """
        min_ = 0
        max_ = 10
        person = self.create_person_class(min_, max_)

        # Check if the class name is 'Person'
        self.assertEqual(person.__class__.__name__, 'Person')
        self.assertIsInstance(type(person).age, IntegerField)


if __name__ == '__main__':

    def run_tests(test_class):
        unittest.TextTestRunner().run(
            unittest.TestLoader().loadTestsFromTestCase(test_class)
        )

    run_tests(TestIntField)
    run_tests(TestIntField2)

