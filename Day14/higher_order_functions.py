from functools import reduce

import sys
sys.path.append('\python_30_day')
import data.countries as countri3
import data.countries_data as country_data

countrys = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def decorator_with_parameters(function):
#     def wrapper_accepting_parameters(para1, para2, para3):
#         function(para1, para2, para3)
#         print("I live in {}".format(para3))
#     return wrapper_accepting_parameters

# @decorator_with_parameters
# def print_full_name(first_name, last_name, country):
#     print("I am {} {}. I love to teach.".format(
#         first_name, last_name, country))

# print_full_name("Asabeneh", "Yetayeh",'Finland')
# #level 1


def square(num):
    return num**2

def joinstr(a:str,b:str):
    return a+b

def sumab(a,b):
    return a + b

# print(list(map(square,numbers)))
# print(list(filter(lambda s: s[0] == 'A', names)))
# print(reduce(joinstr,countrys))

# for country in countrys:
#     print(country)

# for name in names:
#     print(name)

# for number in numbers:
#     print(number)

#level 2
def upper(s):
    return s.upper()

print(list(map(lambda x: x.upper(),countrys)))
print(list(map(square,numbers)))
print(list(map(upper,names)))
print(list(filter(lambda x: 'land' in x, countrys)))
print(list(filter(lambda x: len(x)==6, countrys)))
print(list(filter(lambda x: len(x)>=6, countrys)))
print(list(filter(lambda x: x[0] == 'E', countrys)))
print(reduce(sumab,filter(lambda x: x>50,map(square,numbers))))

def get_string_lists(l):
    return list(filter(lambda x: type(x) == str, l))
print(get_string_lists([1,2,3,'sss',[12],'chicken']))

print(reduce(sumab,numbers))

def concat(a,b):
    return a+','+b
print(reduce(concat,countrys))

def categorize_countries(pattern):
    country_list = countri3.country_list
    return list(filter(lambda x: pattern in x, country_list))
print(categorize_countries('land'))

def country_counts():
    count = {}
    for country in countri3.country_list:
        count[country[0]] = count.get(country[0],0) + 1
    return count
print(country_counts())

def get_first_ten():
    return countri3.country_list[0:10]

def get_last_ten():
    return countri3.country_list[-11:-1]
print(get_first_ten())
print(get_last_ten())

#level 3
data = country_data.data
sort_by_name = sorted(data, key= lambda x: x['name'])
#print(sort_by_name)
sort_by_cap = sorted(data, key= lambda x: x['capital'])
#print(sort_by_cap)
sort_by_pop = sorted(data, key= lambda x: x['population'])
#print(sort_by_pop)
