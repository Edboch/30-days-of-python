import pandas as pd
import numpy  as np

nums = pd.Series([1,2,3,4])
# print(nums)

data = [['Apples','Orange','Mango'],['Broccoli','Potato','Carrot'],['Fish','Beef','Chicken']]
df = pd.DataFrame(data,columns = ['Fruits','Vegetable','Meat'])
# print(df)
weight_height = pd.read_csv('Day25/weight-height.csv')
print(weight_height)

### exercise
df = pd.read_csv('data/hacker_news.csv')
print(df)
print(df.head())
print(df.tail())
print(df['title'])
print(df.shape)

print(df[df['title'].str.contains('python')])
print(df[df['title'].str.contains('JavaScript')])
