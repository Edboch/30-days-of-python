# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#level 1
print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
it_companies.update({'Intel','AMD','NVidia'})
print(it_companies)
print(it_companies.pop())
print(it_companies)
it_companies.discard('Apple') #.remove()
print(it_companies)

#level 2
print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(B.union(A))
print(A.symmetric_difference(B))
del A, B

#level 3
age_set = set(age)
print(age_set)
print(len(age_set)>len(age))

#string: characters encased in speech marks '' or ""
#list: encased in [] ordered list of any data type and is changeable
#tuple: () list of ordered data of different types and is immutable
#set: {} list of randomly ordered and unindexed data of the same type and is unique

sent = 'I am a teacher and I love to inspire and teach people'
sentl = sent.split()
sents = set(sentl)
print(sents)
print(len(sentl),len(sents))