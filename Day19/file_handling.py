# Day19/file_handling.py
# file_handling.py

import re,json,sys
sys.path.append('data')
import stop_words
from collections import Counter
import csv

def count_lines(filename):
    with open(f'{filename}') as f:
        txt = f.read().splitlines()
        count = 0
        for line in txt:
            if line != '':
                count+=1
    return count

def words_only_text(filename):
    with open(f'{filename}') as f:
        txt = f.read().lower()
        cleaned = re.sub(r'[^\sa-zA-Z0-9]','',txt)
        cleaned = re.sub(r'(\n)|(  )',' ',cleaned)
    return cleaned

def most_spoken_lang(jsfilename,length):
    file = open(jsfilename, encoding= 'UTF8')
    countries = json.load(file)
    count = {}
    for country in countries:
        for language in country['languages']:
            count[language] = count.get(language,0) + 1
    return dict(sorted(count.items(),key= lambda x: x[1],reverse = True)[:length])

def most_populated_countries(jsfilename,length):
    file = open(jsfilename, encoding= 'UTF8')
    countries = json.load(file)
    count = {}
    for country in countries:
            pop = country['population']
            count[country['name']] = pop
    return dict(sorted(count.items(),key= lambda x: x[1],reverse = True)[:length])


#print(most_spoken_lang('C:/30-days-of-python/data/countries_data.json',10))
#print(most_populated_countries('C:/30-days-of-python/data/countries_data.json',10))
#print(count_lines('C:/30-days-of-python/data/michelle_obama_speech.txt'))
#print(len(word_list('C:/30-days-of-python/data/michelle_obama_speech.txt')))

def extract_emails(file):
    emails = []
    with open(file) as f:
        txt = f.read().split()
        for word in txt:
            pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            if re.fullmatch(pattern,word) != None:
                emails.append(word)
    return list(set(emails))

#print(extract_emails('C:/30-days-of-python/data/email_exchanges_big.txt'))

def find_most_common_words(file,length):
    text = words_only_text(file)
    para_list = text.split()

    counter = Counter(para_list)

    # count = set()
    # for word in para_list:
    #     pattern = rf'{word}\s|^{word}|{word}$'
    #     appearance = len(re.findall(pattern,text,re.I))
    #     count.add((appearance,word))
    # sorted_list  = sorted(list(count),key= lambda x: x[0])
    # return (sorted_list)[-length-1:-1]

    return counter.most_common(length)


# print(find_most_common_words('C:/30-days-of-python/data/obama_speech.txt',10))
# print(find_most_common_words('C:/30-days-of-python/data/michelle_obama_speech.txt',10))
# print(find_most_common_words('C:/30-days-of-python/data/donald_speech.txt',10))
# print(find_most_common_words('C:/30-days-of-python/data/melina_trump_speech.txt',10))

#print(words_only_text('C:/30-days-of-python/data/michelle_obama_speech.txt'))

def remove_stop_words(text):
    return [word for word in text.split() if word not in stop_words.stop_words]

def term_frequency(text,vocabulary):
    count = {w : 0 for w in vocabulary}
    print(count)
    for word in text:
        count[word] += 1
    return count

def cosine_similarity(count1: dict,count2: dict):
    count1_tuples = list(count1.items())
    count2_tuples = list(count2.items())
    dot_prod = 0
    magnitude1 = 0
    magnitude2 = 0
    for i in range(len(count1_tuples)):
        dot_prod += count1_tuples[i][1] * count2_tuples[i][1]
        magnitude1 += count1_tuples[i][1]**2
        magnitude2 += count2_tuples[i][1]**2
    magnitude1 = magnitude1**(1/2)
    magnitude2 = magnitude2**(1/2)
    print(dot_prod)
    print(magnitude1,magnitude2)
    return (dot_prod)/(magnitude1*magnitude2)
        

def check_text_similarity(file1,file2):
    text1 = words_only_text(file1)
    text2 = words_only_text(file2)

    word_list1 = remove_stop_words(text1)
    word_list2 = remove_stop_words(text2)
    
    vocab = set(word_list1+word_list2)

    text1_tf = term_frequency(word_list1,vocab)
    text2_tf = term_frequency(word_list2,vocab)
    score = cosine_similarity(text1_tf,text2_tf)
    print(score)

    
#check_text_similarity('C:/30-days-of-python/data/michelle_obama_speech.txt','C:/30-days-of-python/data/melina_trump_speech.txt')
#print(find_most_common_words('C:/30-days-of-python/data/romeo_and_juliet.txt',10))

with open('C:/30-days-of-python/data/hacker_news.csv') as f:
    csv_reader = csv.reader(f)
    python_lines = 0
    javascript_lines = 0
    java_lines = 0
    for row in csv_reader:
        line = " ".join(row)
        if 'Python' in line or 'python' in line:
            python_lines+=1
        if 'Javascript' in line or 'javascript' in line or 'JavaScript' in line:
            javascript_lines+=1
        if 'Java' in line and 'JavaScript' not in line:
            java_lines+=1
    #print(python_lines,javascript_lines,java_lines)
