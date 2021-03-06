# testing_animals
# Unit Test Coverage for an animal module

#SETUP
mkdir -p ~/workspace/python/exercises/testing && cd $_
touch animals.py
Copy the contents of animals.py into the file you just created.

# Overview
* Building out unit test coverage in the animal module
* Covering edge cases

# Instructions

<!-- - Wrote test cases to verify the I/O of the following methods of Animal and Dog. -->

<!-- - In the test class' setUpClass() method, create an instance of Animal and Dog. -->
- Animal object has the correct name property.
- Set a species and verify that the object property of species has the correct value.
- Invoking the walk() method set the correct speed on the both objects.
- The animal object is an instance of Animal.
- The dog object is an instance of Dog.

# Test Discovery

Read the Test Discovery section of the Python docs. It explains how you can run all tests inside a directory. This allows you to split your unit test suite into many, smaller, more maintainable modules, and the use a pattern matcher to find tests in all matching files.

# Command To Run:
python -m unittest discover -s . -p "Test*.py" -v
