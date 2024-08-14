import math
#this is a line comment
'''This is a   
multiline comment
'''

print(5+10)
print(32-10)
print(53*40)
print(5/10)
print(533333%321)
print(5**2)
print(232//10)

print('Ed')
print('Chu')
print('United Kingdom')
print('I am enjoying 30 days of python')

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type('Ed'))
print(type(10>5))
print(type({'shop','apple','clean'}))
print(type(('shop','apple','clean')))
print(type({'Key':'value'}))

def euc(x1, y1, x2, y2):
    xdif = x1 - x2
    ydif = y1 - y2
    #answer = math.sqrt(xsum**2+ysum**2)
    answer = (xdif**2+ydif**2)**(1/2)
    return answer

print(euc(2,3,10,8))