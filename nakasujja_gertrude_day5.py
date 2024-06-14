#Definng functions

#Function syntax and parameters
# Return values 
# Lambda functions

#Functions in python are defined using the def key word, followed by the function name 
#Parenthesis (), inside the parenthesis you put the parameter name and the colon.

#Example1:
def multiply(a,b):
    return a*b
result = multiply(5, 10)
print(result)

#Example 2: multiple return values
def get_cordinates():
    return 10,20
x,y = get_cordinates()
print(x,y)

#EXERCISE 1: Define the function greet with the parameter name, set to Guest, and print a message i am a sofware programmer
def greet(name="Guest"):
    print("I am a software programmer")

greet()      




#Exercise3> Multiple values

def greet(name="Guest", course="Software Programmer"):
    print("I am a " + course + ", " + name)
    return name, course

result = greet()       
print(result)           

result = greet("Gertrude", "Veterinary doctor")
print(result)           

#Exercise4:Return multiple return values of your name and age

def name_and_age():
    name = "Gertrude"  
    age = 40           
    return name, age

# Example usage:
name, age = name_and_age()
print("Name:", name)
print("Age:", age)

#Notes
"""SUMMARY
def : key word to define a function
function name: name of the function
parameters: optional , arguments passed to the function
Docstrings: optional, describes the function purpose
Return : returns the value from the function"""

#Syntax for defining a function
#define function name(parameters)
   # Docstring optional
    #Function body
    #return value

#Lambda functions: Are small anonymous functions defined using the labda keyword. 
# They are restricted to a single expression

#syntax for lambda function
#lambda parameter: expression
#Example 5: Create a lambda function to add two numbers

def add(a, b) : return a+b
print (add(40, 20))

#Example 6: usecases for lambda function for sorting
coordinates=[(1,2), (2,3), (3,1), (5,0)]
coordinates.sort(key=lambda coordinate:coordinate[1])
print(coordinates)

#Map, filter and reduce
#Example 7:Get the squares of 1 to 5 using map, filter and reduce

number_squares=[1,2,3,4,5]
squares=list(map(lambda x: x**2, number_squares))
print(squares)

#Exercise4: Define a function to get user info that accepts arbitrary keyword argument and 
# print each key value pair
def userInfo(**kwargs):
    for key, value in kwargs.items():
        print(key + ": " + str(value))

        #Another way

userInfo(name="Gertrude", age=30, email="gertrudesnakasujja@gmail.com", course="BSSE")

def user_info(name=None, age=None, email=None):
    if name is not None:
        print("name: " + name)
    if age is not None:
        print("age: " + str(age))
    if email is not None:
        print("email: " + email)

user_info(name="Gertrude", age=30, email="gertrudes.com")

