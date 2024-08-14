#level 1
age = int(input('How old are you? '))
if age >= 18:
    print('You are old enough to drive!')
else:
    print('You need {} more years before you can drive'.format(18-age))

my_age = 23
if my_age>age:
    print('I am {} year(s) older than you!'.format(my_age-age))
elif my_age == age:
    print('We are the same age!')
else:
    print('You are {} year(s) older than me!'.format(age-my_age))

a = int(input('enter number one : '))
b = int(input('enter number two : '))
if a > b:
    print(f'{a} is bigger than {b}!')
elif b>a:
    print('%d is bigger than %d!' %(b,a))
else:
    print('they are both equal!')

### Exercises: Level 2
grade = int(input('grade: '))
if grade >= 80 and grade <= 100:
    print('A grade')
elif grade >=70 and grade<=89:
    print('B grade')
elif grade >=60 and grade<=69:
    print('C grade')
elif grade >=50 and grade<=59:
    print('D grade')
else:
    print('F grade')

month = input('what month is it? ')
if month == 'September' or month == 'October' or month == 'November':
    print('The season is Autumn')
elif month == 'December' or month == 'January ' or month == 'February':
    print('The season is Winter')
elif month == 'March' or month == 'April  ' or month == 'May':
    print('The season is Spring ')
else:
    print('The season is Summer ')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('fruit: ')
if fruit in fruits:
    print('that fruit already exists in the list')
else:
    fruits.append(fruit)
    print(fruits)

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if person['skills']:
    index = (len(person['skills'])-1)//2
    print(person['skills'][index])
    print('This person knows python') if 'Python' in person['skills'] else print('this person does not know python')
    if ['JavaScript', 'React'] == person['skills']:
        print('This person is a front end dev')
    elif ['Node', 'MongoDB', 'Python'] == person['skills']:
        print('This person is a back end dev')
    elif ['Node', 'MongoDB', 'React'] == person['skills']:
        print('This person is a fullstack dev')
    else:
        print('unknown title')

if person['is_marred']:
    print('{} {} lives in {}. they are {}'.format(person['first_name'],person['last_name'],person['country'], 'married'))
else:
    print('{} {} lives in {}. they are {}'.format(person['first_name'],person['last_name'],person['country'], 'not married'))


