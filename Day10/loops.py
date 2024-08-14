import sys
sys.path.append('data')
import countries
import countries_data

for i in range(11):
    print(i)

i = 0
while i!=11:
    print(i)
    i+=1

for i in range(10,-1,-1):
    print(i)

i = 10
while i!=-1:
    print(i)
    i-=1

for i in range(7):
    string = '#'
    print(string*(i+1))

for i in range(8):
    for j in range(8):
        print('#', end= ' ')
    print()

for i in range(11):
    print('{} x {} = {}'.format(i,i,i*i))

coding = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in coding:
    print(item)

for i in range(101):
    if i%2 != 1:
        print(i)

for i in range(101):
    if i%2 == 1:
        print(i)

sum = 0
sum_odd = 0
sum_even = 0
for i in range(101):
    sum+=i
    if i%2 == 1:
        sum_odd+=i
    else:
        sum_even+=i
print(sum,sum_even,sum_odd)

country_list = countries.country_list
hasland = []
for country in country_list:
    if 'land' in country:
        hasland.append(country)

fruits = ['banana', 'orange', 'mango', 'lemon']
for fruit in fruits:
    fruits.remove(fruit)
    fruits.insert(0,fruit)
print(fruits)

country_data = countries_data.data

language_data = []
for country in country_data:
    language_data+= country['languages']
count = {}
for lang in language_data:
    count[lang] = count.get(lang,0) + 1
print(len(count))

def sort_dictionary(d, reverse=False):
    return dict(sorted(d.items(),key = lambda x: x[1], reverse=reverse))

sorted_count = sort_dictionary(count,True)
print(list(sorted_count.keys())[0:10])

pop = {}
for country in country_data:
    pop[country['name']] = country['population']
sorted_pop = sort_dictionary(pop,True)

print(list(sorted_pop.keys())[0:10])