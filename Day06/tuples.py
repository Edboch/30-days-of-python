empty = tuple()
sisters = ('Mabel','Ivankov')
brothers = ('Ken','Bob')
siblings = sisters + brothers
print(siblings)
print(len(siblings))
family = siblings + ('Dad','Mum')
print(family)

#level 2
siblings = family[0:4]
parents = family[4:6]
print(siblings)
print(parents)
fruits = ('Apple','Orange')
veg = ('Eggplant','Bak Choy')
products = ('beans','corn','noodles')
food_stuff_tp = fruits+ veg+ products
print(food_stuff_tp)
food_stuff_list = list(food_stuff_tp)
print(food_stuff_list)
print(food_stuff_list[3:5])
print(food_stuff_list[:3])
print(food_stuff_list[-3:])
del food_stuff_tp
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)