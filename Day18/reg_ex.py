import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
# It returns an object with span, and match
match = re.search('first', txt, re.I) #match is only used for start of string
#print(match.span())
start, end = match.span()
substring = txt[start:end]
#print(substring)

matches = re.findall('python', txt, re.I)
matches2 = re.findall('python|Python',txt)
matches3 = re.findall('[Pp]ython',txt)
#print(matches,matches2,matches3)

matched_replaced = re.sub('[Pp]ython','Javascript',txt)
#print(matched_replaced)


txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

txt = re.sub('%', '', txt)
#print(txt)

#print(re.split('\n',txt))
regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
#print(matches)  # ['apple']

# To make case insensitive adding flag '
matches = re.findall(regex_pattern, txt, re.I)
#print(matches)  # ['Apple', 'apple']
# or we can use a set of characters method
regex_pattern = r'[Aa]pple'  # this mean the first letter could be Apple or apple
matches = re.findall(regex_pattern, txt)
#print(matches)  # ['Apple', 'apple']

#level 1
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
def most_frequent_words(txt):
    cleared_para = re.sub(r'[.]','',txt)
    #print(cleared_para)
    para_list = cleared_para.split()
    #print(para_list)
    count = set()
    for word in para_list:
        pattern = rf'{word}\s|^{word}|{word}$'
        appearance = len(re.findall(pattern,cleared_para,re.I))
        count.add((appearance,word))
    sorted_list  = sorted(list(count),key= lambda x: x[0])
    return (sorted_list)

para = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'
cleared_para = re.sub(r'[a-zA-Z,.]|[-]+\D','',para)
#print(cleared_para)
points = sorted(list(map(lambda x: int(x), cleared_para.split())))
distance = points[-1] - points[0]
#print(distance)

#level 2
def is_valid_variable(id: str):
    pattern = r'^[a-z_]+[a-zA-Z\d_]*'
    match = re.match(pattern,id)
    if match==None:
        print(False)
    else:
        start,end = match.span()
        checkstring = id[start:end]
        print(id==checkstring)


#is_valid_variable('first_name') # True
#is_valid_variable('first-name') # False
#is_valid_variable('1first_name') # False
#is_valid_variable('firstname') # True

#level 3
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(txt:str):
    pattern = r'[!@#$%^&*();]*'
    cleaned = re.sub(pattern,'',txt)
    return (cleaned)
cleaned_text = clean_text(sentence)
#print(cleaned_text)
#print(most_frequent_words(cleaned_text))