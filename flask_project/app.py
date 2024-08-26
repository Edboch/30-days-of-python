from flask import Flask, render_template, request, redirect, url_for
import os
from text_analysis import text_analysis as ta
import pymongo

MONGODB_URI = 'mongodb+srv://<user>:<password>@30daysofpython.0vgwc.mongodb.net/?retryWrites=true&w=majority&appName=30DaysOfPython'
client = pymongo.MongoClient(MONGODB_URI)
db = client.thirty_days_of_python

students = db.students.find().sort('name',-1)
for student in students:
    print(student)



app = Flask(__name__)

@app.route('/')
def home():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 Days Of Python Programming'
    return render_template('home.html', techs=techs, name=name, title='Home')

@app.route('/about')
def about():
    name = '30 Days Of Python Programming'
    return render_template('about.html', name=name, title= ' About Us')

@app.route('/result')
def result():
    content = request.args['content']
    cleaned = ta.clean_text(content)
    words = cleaned.split()
    char_count = len(content)
    number_of_words = len(words)
    most_repeated = ta.most_appearing_word(words)
    variety = ta.lex_density(cleaned)
    word_count = ta.all_word_count(words)
    return render_template('result.html', content=content, word_count=word_count, number_of_words=number_of_words,char_count=char_count, most_repeated=most_repeated, variety=variety)

@app.route('/post', methods= ['GET','POST'])
def post():
    name = 'Text Analyzer'
    if request.method == 'GET':
         return render_template('post.html', name = name, title = name)
    if request.method =='POST':
        content = request.form['content']
        return redirect(url_for('result',content = content))

if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(debug=True,host = '0.0.0.0', port= port)