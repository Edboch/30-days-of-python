dog = dict()
dog = {
    'name' : 'Poochie',
    'color' : 'Brown',
    'breed' : 'golden retriever',
    'legs': 'yes',
    'age'  : 4
}
print(dog.items())

student = {'firstname' : '',
           'lastname': '',
           'gender':'',
            'age': '',
            'marital status': '', 
            'skills':['Dance','Acting'],
            'country':'', 
            'city':'', 
            'address':''}
print(len(student))
print(type(student['skills']))
print(student.keys())
print(student.values())
studtup = list(student.items())
print(studtup)
del student['skills'][0]
print(student.items())
student.pop('age')
print(student.keys())
