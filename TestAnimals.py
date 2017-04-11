import unittest
from animals import *


class TestTheAnimals(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.animal = Animal('Buddy', 'Panda')
        self.angus = Dog('Angus')
        self.animal.name = "Goofball"

    def test_animal_name_property_has_correct_value(self):
        self.assertEqual(self.animal.name, 'Buddy')

    def test_animal_name_property_has_correct_value(self):
        self.assertEqual(self.animal.species, 'Panda')

    def test_animal_name_property_has_correct_value(self):
        self.assertEqual(self.angus.species, 'Dog')

    def test_walk_method_sets_speed(self):
        legs = 4
        self.animal.set_legs(legs)
        self.animal.walk()

        self.angus.set_legs(legs)
        self.angus.walk()

        self.assertEqual(self.animal.speed, 0.4)
        self.assertEqual(self.angus.speed, 0.8)

    def test_animal_is_correct_type(self):

    def test_dog_is_correct_type(self):
        self.assertIsInstance(self.angus, Dog)

# class Dog()
# def __init__(self, name):
#         """Initialize name and age attributes."""
#         self.name = name
#         self.walk = walk
#         #attributes
#
#     def sit(self):
#         """Simulate a dog sitting in response to a command."""
#         print(self.name.title() + " is now sitting.")
#     def roll_over(self):
