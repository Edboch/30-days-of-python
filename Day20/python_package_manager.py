import webbrowser
import sys
import requests
sys.path.append('Day19')
import file_handling as fh
from collections import Counter
import json
import numpy
import pandas
from bs4 import BeautifulSoup
url = "https://google.com"
# webbrowser.open_new_tab(url)
response = requests.get(url)
# print(response)
# print(response.status_code)
# print(response.headers)
# print(response.text)

### 1
romeo_and_juliet = 'https://www.gutenberg.org/cache/epub/1513/pg1513.txt'
response = requests.get(romeo_and_juliet)
# print(response.text)

word_list = response.text.split()
# print(Counter(word_list).most_common(10))

### 2
cats_api =  'https://api.thecatapi.com/v1/breeds'
response = requests.get(cats_api)
cats = response.json()
weights = [(int(cat['weight']['metric'].split(" - ")[0]) + int(cat['weight']['metric'].split(" - ")[1]))/2 for cat in cats]
print('min weight:',min(weights))
print('max weight:',max(weights))
mean = numpy.mean(weights)
print('mean weight:',mean)
sd = numpy.std(weights)
print('weight sd:',sd)

lifespan = [(int(cat['life_span'].split(' - ')[0]) + int(cat['life_span'].split(' - ')[1]))/2 for cat in cats]
print('min lifespan:',min(lifespan))
print('max lifespan:',max(lifespan))
mean = numpy.mean(lifespan)
print('mean lifespan:',mean)
sd = numpy.std(lifespan)
print('lifespan sd:',sd)

data = pandas.read_json(cats_api)
origin_freq = data['origin'].value_counts()
print(origin_freq)

### 3
country_api = 'https://restcountries.com/v3.1/all'
response = requests.get(country_api)
data = response.json()
country_sizes = []
for country in data:
    country_sizes.append((country['name']['common'],country['area']))
print(sorted(country_sizes,key=lambda x: x[1],reverse=True)[0:10])

language_count = {}
for country in data:
    if 'languages' in country.keys():
        for lang in country['languages'].values():
            language_count[lang] = language_count.get(lang,0)+1
sorted_count = dict(sorted(language_count.items() ,key= lambda x: x[1],reverse=True))
print(list(sorted_count.keys())[:10])

total_lang_count = 0
print('Total languages',sum([language_count[x] for x in language_count]))

response = requests.get('https://archive.ics.uci.edu/datasets')
soup = BeautifulSoup(response.text,'html.parser')
print(soup.body.get_text().strip())