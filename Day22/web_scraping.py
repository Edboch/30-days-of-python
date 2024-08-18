import requests
from bs4 import BeautifulSoup
import json
import datetime
import regex

### 1
url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

facts = soup.find_all('section',{'class': 'stat-section'})
collection = []

for fact in facts:
    group = {}
    group['Category'] = fact.find('h4').text
    for info in fact.find('ul').find_all('li'):
        data = info.find_all('span')
        group[data[0].text] = data[1].text
    collection.append(group)

with open('Day22\scrapped_data.json','w') as f:
    json.dump(collection,f)

### 3
url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
response = requests.get(url)
soup = BeautifulSoup(response.content,'html.parser')
table = soup.find('table',{'class':'wikitable'})

#keys
#Number order of presidents
#name
#birth death
#serving time
#party
#election

presidents = []
for items in soup.find('table',{'class':'wikitable'}).find_all('tr')[1::1]:
    pres = {}
    data = items.find_all(['th','td'])
    pres['No'] = data[0].a.text
    pres['Name'] = data[2].a.text
    serving = []
    for date in data[3].find_all('span'):
        value = date.text
        date_format = '%B %d, %Y'
        res = True
        try:
            res = bool(datetime.datetime.strptime(value,date_format))
        except ValueError:
            res = False
        if res:
            serving.append(date.text)
    pres['Term'] = " - ".join(serving)
    pres['Party'] = [tag.text for tag in data[5].find_all('a')]
    pres['Election'] = [tag.text for tag in data[6] if tag.text.isdigit()]
    presidents.append(pres)

#print(presidents)
with open('Day22\presidents.json','w') as f:
    json.dump(presidents,f)