
""" summary
    Control structures
    Conditional statements(if, elif, else)
    Loops (for, while)
    Comprehensions (lists, dictionary, comprehensions)"""
age= 30

'''if age > 18:
    print('You are an adult')
elif age > 65:
    print('You are a senior citizen')
else:
    print('You are a youth')'''


#90, above excellent, 80 above is very good,  70 good otherwise not good

"""grade = 88

if grade >= 90:
    print('Excellent')

elif grade >= 80:
    print('Very good')
elif grade >= 70:
    print('Good')
else:
    print('Not good')"""

    
"""Exercise, Write a python file to determine the price of a movie based on age
    condition1 if you children under 13yrs get discount for price to be 1000shs
    Teenagers between 13 and 18 get discount price of 500shs
    Adults 18 and above just pay all the price 200shs
    Senior citizens pay shs 10000"""

"""Age = 60
Price = 2000

if Age < 13:
     print("Pay",Price-1000 ,"shs")

elif (Age > 13 and Age < 18):
     print("Pay",Price-500 ,"shs")
    
elif Age > 18 and Age < 30: 
        print("No price discount")

else:
     print('Pay 10000 for the movie')"""

"""Loops
for loop iterate over a sequence (list, turple, dictionary, set, string)
The while loop repeats as longas codition is true"""

cars=['tesla', 'audi','BMW', 'jeep','rangerover']
for car in cars:
      print(car)


count = 1
while count <=10:
    
      print ('count 1 to 10:', count)
      count +=1

#Exercise
"""summary
create your own list of favourite colors using for loop
create a reverse of the input 12345 to be 54321 using while loop"""

colors = ['blue','black', 'brown', 'green','violet']
for color in colors:
      print(color)

      reversed_color=colors[::-1]
      for color in reversed_color:
        print(color)

        index=len(colors)-1
        while index>=0:
             print(colors[index])
             index-=1

count = 5
while count >=1:
      print('count is ',count )
      count-=1

