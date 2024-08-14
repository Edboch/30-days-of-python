numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negatives = [i for i in numbers if i < 1]
print(negatives)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten = [number for row in list_of_lists for number in row[0]]
print(flatten)

list_of_tup = [(i,i**0,i**1,i**2,i**3,i**4,i**5) for i in range(11)]
print(list_of_tup)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flat_countries = [[country[0][0].upper(),country[0][0][:3].upper(),country[0][1].upper()] for country in countries]
print(flat_countries)

list_of_dic = [{'country':country[0][0].upper(),'city':country[0][1].upper()} for country in countries ]
print(list_of_dic)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
floor_names = [name[0][0]+' '+name[0][1] for name in names]
print(floor_names)

slope = lambda y1,y2,x1,x2: (y1-y2)/(x1-x2)
print(slope(6,4,9,2))