import sys
sys.path.append('data')
import countries_data

def add_two_num(a,b):
    return a+b
print(add_two_num(1,2))

def area_of_circle(r):
    return 3.14*r*r
print(area_of_circle(15))

def add_all_nums(*nums):
    all_int = True
    for num in nums:
        if not isinstance(num,int):
            all_int = False
            break
    if all_int:
        return sum(nums)
    else:
        return 'not all numbers'
print(add_all_nums(1,2,24,2,343,2,12,4))

def convert_celsius_to_fahrenheit(c):
    return ((c*9/5)+32)
print(convert_celsius_to_fahrenheit(33))

def check_season(month):
    if month in ('January','February','December'):
        return 'Winter'
    elif month in ('March','April','May'):
        return 'Spring'
    elif month in ('June','July','August'):
        return 'Summer'
    else:
        return 'Autumn'
print(check_season('January'))

def calculate_slope(x1,x2,y1,y2):
    return (y1-y2)/(x1-x2)
print(calculate_slope(3,2,5,4))

def solve_quadratic_eqn(a,b,c):
    sol1 = (-b+(((b**2)-(4*a*c))*1/2))/2*a
    sol2 = (-b-(((b**2)-(4*a*c))*1/2))/2*a
    return sol1, sol2
print(solve_quadratic_eqn(6,3,18))

def print_list(l = []):
    for item in l:
        print(item)
print_list(['apple','pear'])

def rev_list(l = []):
    for item in reversed(l):
        print(item)
    #can reverse a list using list[::-1]
rev_list(['apple','pear'])

def capitalize_list_items(l):
    capitalist =  list(map(lambda x: x.capitalize(),l))
    return capitalist

print(capitalize_list_items(['small','bob','chicken']))

def add_item(l, item):
    new_list = l + [item]
    return new_list

print(add_item([1,2,3,4,5],77))

def remove_item(l, item):
    if item in l:
        l.remove(item)
    return l
print(remove_item([1,2,3,4],4))

def sum_of_nums(n):
    s = 0
    for i in range(n):
        s += i+1
    return s
print(sum_of_nums(5))

def sum_of_odds(n):
    s = 0
    for i in range(n):
        if (i+1)%2 == 1:
            s += i+1
    return s
print(sum_of_odds(4))

def sum_of_evens(n):
    s = 0
    for i in range(n):
        if (i+1)%2 != 1:
            s += i+1
    return s
print(sum_of_evens(4))

def even_and_odds(n):
    evens, odds = 0,0
    for i in range(n+1):
        if i%2==1:
            odds+=1
        else:
            evens+=1
    print('evens',evens,' odds', odds)
even_and_odds(100)

def factorial(n):
    res = 1
    for i in range(1,n+1):
        res*=i
    print(res)
factorial(5)

def is_empty(l=[]):
    if len(l) == 0:
        return True
    else:
        return False
print(is_empty(()))

def is_prime(n):
    res = True
    for i in range(2,n):
        if n%i==0:
            res = False
        else:
            res = True
    return res
print(is_prime(44))

def list_unique(l):
    return len(set(l)) == len(l)

def same_type(l):
    return all(list(map(lambda x: isinstance(x,type(l[0])),l)))
print(same_type([1,2,3,4,4,'word']))

def is_var(s):
    return s.isidentifier()
print(is_var('s'))


countries = countries_data.data
def most_spoken_language(countries):
    language_count = {}
    for country in countries:
        for language in country['languages']:
            language_count[language] = language_count.get(language,0) +1
    return list(dict(sorted(language_count.items(), key = lambda x: x[1], reverse = True)))[:10]

print(most_spoken_language(countries))