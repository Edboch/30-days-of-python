multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)

#1
string = "Thirty " + "Days " + "of "+ "Python"
print(string)
#2
string = "Coding " + "For "+"all"
print(string)
#3,4,5
company = "Coding for all"
print(company)
print(len(company))
#6
print(company.upper())
#7
print(company.lower())
#8
print(company.capitalize())
print(company.title())
print(company.swapcase())
#9
print(company[0:6])
#10
print(company.index('Coding'))
print(company.find('Coding'))
#11
print(company.replace('Coding','Python'))
#12
string = "Python for everyone"
print(string.replace('everyone','all'))
#13
print(company.split())
#14
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))
#15
print(company[0])
#16
print(company[-1])
#17
print(company[10])
#18
companyarr = company.upper().split()
print(companyarr[0][0]+companyarr[1][0]+companyarr[2][0])
#19
stringarr = string.upper().split()
print(stringarr[0][0]+stringarr[1][0]+stringarr[2][0])
#20
print(company.index('C'))
#21
print(company.index('f'))
#22
print(company.rfind('l'))
#23
print('You cannot end a sentence with because because because is a conjunction'.find('because'))
#24
print('You cannot end a sentence with because because because is a conjunction'.rindex('because'))
#25
string = 'You cannot end a sentence with because because because is a conjunction'
print(string.replace('because because because', ''))
#26
print(string.find('because'))
#27
print(string.replace('because because because', ''))
#28
print(company.startswith('Coding'))
#29
print(company.endswith('coding'))
#30
string = '   Coding For All      ' 
print(string[3:17])
print(string.rstrip().lstrip())
#31
string= '30daysofpython'
print(string.isidentifier()) #false
string = 'thirty_days_of_python'
print(string.isidentifier()) #true
#32
libr = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("# ".join(libr))
#33
string = "I am enjoying this challenge.\nI just wonder what is next."
print(string)
#34
string = "Name\tAge\tCountry\tCity\nEdmond\t23\tEngland\tLondon"
print(string)
#35
radius = 10
area = 3.14 * radius ** 2
areastr = "The area of a circle with radius {} is {} meters squared".format(radius,area)
areastr2 = "The area of a circle with radius %d is %.1f meters squared" %(radius,area)
areastr3 = f"The area of a circle with radius {radius} is {area} meters squared"
print(areastr)
print(areastr2)
print(areastr3)
#36
n1 = 8
n2 = 6
print(f'{n1} + {n2} = {n1+n2}')
print(f'{n1} - {n2} = {n1-n2}')
print(f'{n1} * {n2} = {n1*n2}')
print(f'{n1} / {n2} = {n1/n2}')
print(f'{n1} % {n2} = {n1%n2}')
print(f'{n1} // {n2} = {n1//n2}')
print(f'{n1} ** {n2} = {n1**n2}')
