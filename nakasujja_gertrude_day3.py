#python best practices
"""summary
follow PEP 8
Indentation 
Maximum line length; Limit to 79 characters
Blank lines 
Use meaningful names"""

#Example of a meaningfull name is by using underscore not kamocase

def calculate_area(radius):
    pass

total_price = 100000

"""python operators
name of operator           symbol with example
addition                       x+y
subtraction                    x-y
division                       x/y
multiplication                 x*y
modulus                        x%y
exponentiation                 x**y
floor division                 x||y

"""

#Example with comparision operators
"""summary
==: Equal to
!=: Not equal to
>: Greater than
<: Less than
>=: Greater than or equal to
<=: Less than or equal to"""

#Example with logical  operators

"""summary

Logical operators
name of operator           symbol with example
and 
or 
not"""

#Example with membership oprators 
"""
summary

in              x in y
not in          x not in y"""

#Example with bitwise oprators

"""
summary
&: Bitwise AND
|: Bitwise OR
^: Bitwise XOR (exclusive OR)
~: Bitwise NOT
<<: Left shift
>>: Right shift

python cases
   snakecase
   camelCase
   pascalCase
   UPPERCASE
   kebab_case""" 

#Comprehensions (LISTS, DICTIONARY COMPREHENSIONS)
"""Summary
Comprehensions provide a concise way to create lists and dictionaries
what is the symbol for 
lists               [] square brackets \\ used to store multiple items in a single variable
dictionaries        {} curley brackes \\ used to store data values in key:: value pairs"""

#Example 1:Basic list comprehensions
#Create a list of squares in range of 10

list_of_squares= [x**2 for x in range(10)]
print(list_of_squares)

#Example1
#create a list of even squares in the range of 20
even_squares = [x**2 for x in range(20) if x % 2 == 0]
print(even_squares)

#Dictionary comprehensions
#Example2: Create a dictionary comprehension for my favourite cars and count the length of the characters

# List of favorite cars
favorite_cars = ["Tesla Model S", "Ford Mustang", "Chevrolet Camaro", "BMW M3", "Audi R8"]

# Dictionary comprehension to create a dictionary with car names and their length
car_name_lengths = {car: len(car) for car in favorite_cars}
print(car_name_lengths)

#Exercise 2:
#Create a list of tuple where each tuple contains a number and its cube for numbers betweeen 1 and 10 using a dictionary comprehension 
num_cubes = {num: num**3 for num in range(1, 10)}
number_cubes_list = list(num_cubes.items())
print(number_cubes_list)


