# Inheritance and Polymorphism

# Inheritance and method overriding
'''summary line
--description
Inheritance and method overriding allows the class(child class) to inherit attributes and methods from another class(parent class)

key concepts
Base class: class whose properties are inherited by another class
Derived classes: class that inherits the attributes and properties from another base class
'''

# Example1: Create a class where a dog inherits from animal and overrides with the speak method
class Animal:
    def speak(self):
        return 'meow meow meow'
    
class Dog(Animal):
    def speak(self):
        return 'barks'
    
# Implementation of inherited classes
animal = Animal()
dog = Dog()
print(animal.speak())  # Output: meow meow meow
print(dog.speak())     # Output: barks

# Polymorphism and method resolution
# Polymorphism allows objects of different classes to be treated as objects of a common superclass
# Method resolution order (MRO) is the order in which Python looks for a method in a hierarchy of classes

# Example 2: How polymorphism works in Python
class Animal:
    def speak(self):
        return 'HMMMMMMMMMMM'
    
class Dog(Animal):
    def speak(self):
        return 'BARKS'
    
class Cat(Animal):
    def speak(self):
        return 'MEOW MEOW MEOW'

def make_animal_speak(animal):
    print(animal.speak())

make_animal_speak(Dog())  # Output: BARKS
make_animal_speak(Cat())  # Output: MEOW MEOW MEOW

# Exercise 1: Create a simple application to manage different types of vehicles. 
# Implement derived class to demonstrate inheritance and polymorphism

"""
Requirements:
Base class: Vehicle
Attributes: make, model, and year
Methods: display_info

Derived classes: Car and Motorcycle
Car inherits from Vehicle
Attributes: number of doors
Overrides: display_info

Motorcycle inherits from Vehicle
Attributes: type of bike (cruiser, sport, touring)
Overrides: display_info
"""

# Inheritance
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, year, number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors

    def display_info(self):
        return f"{self.year} {self.make} {self.model}, {self.number_of_doors} doors"


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, bike_type):
        super().__init__(make, model, year)
        self.bike_type = bike_type

    def display_info(self):
        return f"{self.year} {self.make} {self.model}, Type: {self.bike_type}"


def manage_vehicle(vehicle):
    print(vehicle.display_info())


# Create instances of Car and Motorcycle
car = Car("Toyota", "Camry", 2020, 4)
motorcycle = Motorcycle("Yamaha", "MT-09", 2019, "Sport")

manage_vehicle(car)          # Output: 2020 Toyota Camry, 4 doors
manage_vehicle(motorcycle)   # Output: 2019 Yamaha MT-09, Type: Sport

def display_vehicle_info(vehicles):
    for vehicle in vehicles:
        print(vehicle.display_info())

# Polymorphism
# Create a list of vehicle objects
vehicles = [
    Car("Honda", "Accord", 2021, 4),
    Motorcycle("Harley-Davidson", "Street 750", 2018, "Cruiser"),
    Car("Tesla", "Model 3", 2022, 4),
    Motorcycle("Ducati", "Panigale V4", 2020, "Sport")
]

display_vehicle_info(vehicles)
# Output:
# 2021 Honda Accord, 4 doors
# 2018 Harley-Davidson Street 750, Type: Cruiser
# 2022 Tesla Model 3, 4 doors
# 2020 Ducati Panigale V4, Type: Sport

# Reading and Writing Files in Python
'''
Working with text files
Handling CSV files
JSON and XML file processing
'''

# Working with text files: open, read, write, and close
# Note: Python provides inbuilt functions to handle text files

# Example 3: Write to and read from a text file
# Writing to a text file
# Example of saving to user directory
with open('C:\\Users\\YourUsername\\gert.txt', 'w') as file:
    file.write('I am Gertrude and I love Python.\n')
    file.write('I use Python for automation.')


# Reading from a text file
with open('C:\\Users\\YourUsername\\gert.txt', 'r') as file:
    content = file.read()
    print(content)

# Handling CSV files
'''CSV (Comma Separated Values) files are widely used for data exchange

Key concepts:
Read CSV file: Using csv.reader()
Write CSV file: Using csv.writer()
DictReader and DictWriter: Classes to read and write CSV files as dictionaries
'''

# Example 4: Writing and Reading CSV files
import csv # type: ignore

# Writing to a CSV file
with open('naka.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['name', 'position', 'course'])
    writer.writerow(['Jeff Geof', 'Lecturer', 'BSE'])
    writer.writerow(['Nankya Elisa', 'Student', 'BSE'])
    writer.writerow(['Nakasujja Gertrude', 'Student', 'BSE'])

# Reading from a CSV file
with open('naka.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)

# JSON and XML file processing
'''JSON (JavaScript Object Notation) and XML (eXtensible Markup Language) are formats used to structure data.

Key concepts:
Loading JSON data: using json.load() for reading JSON files
Parsing JSON data: using json.loads() for handling JSON strings
'''

import json

# Define the student_data dictionary
student_data = {
    'name': 'Gertrude',
    'course': 'BSE',
    'year': 'year 3'
}

# Write the dictionary to a JSON file
with open('student_data.json', 'w') as json_file:
    json.dump(student_data, json_file)

# Read the dictionary from the JSON file
with open('student_data.json', 'r') as json_file:
    student_data_from_file = json.load(json_file)

# Print the data to verify
print(student_data_from_file)
# Output: {'name': 'Gertrude', 'course': 'BSE', 'year': 'year 3'}

# Exercise 2: Read and write from the XML file

import xml.etree.ElementTree as ET # type: ignore

# Define the data
data = ET.Element('data')
items = ET.SubElement(data, 'items')
item1 = ET.SubElement(items, 'item')
item1.set('name', 'item1')
item1.text = 'item1abc'

item2 = ET.SubElement(items, 'item')
item2.set('name', 'item2')
item2.text = 'item2abc'

# Write the XML file
tree = ET.ElementTree(data)
with open('data.xml', 'wb') as xml_file:
    tree.write(xml_file)

# Read the XML file
tree = ET.parse('data.xml')
root = tree.getroot()

# Print the data
for elem in root.iter('item'):
    print(f"Item Name: {elem.get('name')}, Item Text: {elem.text}")

# Exercise 3: Using abstraction to calculate the area and perimeter of a rectangle
from abc import ABC, abstractmethod # type: ignore

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Create a rectangle object
rectangle = Rectangle(10, 5)

# Calculate area and perimeter
print(f"Area of rectangle: {rectangle.area()}")          # Output: Area of rectangle: 50
print(f"Perimeter of rectangle: {rectangle.perimeter()}") # Output: Perimeter of rectangle: 30
