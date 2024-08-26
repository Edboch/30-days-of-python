#Day 2: 30 days of python programming
import math

first_name = 'Ed'
last_name = 'Chu'
full_name = first_name + ' ' + last_name
country = 'United Kingdom'
city = 'London'
age = 23
year = 2024
is_married, is_true, is_light_on = False, True, True

print(type(first_name))
print(len(first_name))
print(len(first_name)>len((last_name)))

num_one, num_two = 5,4
total = num_one+num_two
diff = num_two- num_one
product = num_one* num_two
division = num_one/num_two
remainder = num_two%num_one
exp = num_one**num_two
floor_division = num_one//num_two

radius = 30
def area(r):
    answer = math.pi*(int(r)**2)
    return answer

def circumference(r):
    d = 2*r
    answer = math.pi*d
    return answer

area_of_circle = area(radius)
circum_of_circle = circumference(radius)

rinput = input('Radius: ')
print('The area is '+ str(area(rinput)) )

fname = input('first name ')
lname = input('last name ')
age = input('age ')
country = input('country ')