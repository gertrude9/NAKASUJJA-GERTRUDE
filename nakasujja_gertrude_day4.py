#Dictionaries
#Creating and using dictionaries
#Dictionary methods and operations

"""summary
Dictionaries in python are a collection of keys and values
-Unordered
-mutable and 
-indexed by keys
"""

#Example 1: Create a dictionary
#Create a dictionary for a student pursuing software engineering, 
# the key must be your name, age , technology interest, course and year of study.
#  Put your own details

student_dict= {
    'name':'Gertrude',
    'age':'33',
    'technology':'Networking',
    'course':'BSSE',
    'year':'year 3'
    

}
student_dict['age'] = '34'
student_dict['technology']='AI and ML'

print(student_dict['year'])
print(student_dict['name'])
print(student_dict['age'])
print(student_dict['technology'])
print(student_dict['course'])

#Exercise1: modify age and technology
#Adding keys and values
student_dict['email']='gertrudesnakasujja@gmail.com'


#Exercise2: Remove a key and a value from the dictionary
del student_dict['year']
print(student_dict)

#common dictionary methods

"""summary
get()  //it returns the value for the specified key if the key is in the dictionary. If not it returns the default value.
update()  //  updates the dictionary with the elements from another dictionary.
pop()  // removes the specified key with the corresponding value

"""
#Example 2: use the get( )to get the value
print(student_dict.get('name'))
print(student_dict.get('technology'))

#Exercise3: USse the update METHOD TO CHANGE VALUE IN YOUR AGE 
student_dict.update({'age': '34'})  

print(student_dict['name'])
print(student_dict['age'])
print(student_dict['technology'])
print(student_dict['course'])

#Exercise4: use the if to check if the age is present in the dictionary

student_dict = {
    'name': 'Gertrude',
    'age': '33',
    'technology': 'Networking',
    'course': 'BSSE',
    'year': 'year 3'
}

# Check if 'age' is present in the dictionary and return the value
if 'age' in student_dict:
    age_value = student_dict['age']
    print(f"Age: {age_value}")
else:
    print("The age is not present in the dictionary.")

#keys(), values() and items() methods
print(student_dict.keys())
print(student_dict.values())
print(student_dict.items())

"""summary

keys() returns the view of objects that display a list of all keys
values() returns the view of objects that display a list of all values
items() returns the view of objects that display a list of all keys and value tuple pairs"""

#Exercise4: use the update method to change the course and add a new key like 'whatsapp number to the dictionary'
student_dict = {
    'name': 'Gertrude',
    'age': '33',
    'technology': 'Networking',
    'course': 'BSSE',
    'year': 'year 3'
}

student_dict.update({'course': 'CSC', 'whatsapp number': '07737444171'})

# Print the updated dictionary
print(student_dict)


