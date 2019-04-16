from flask import Flask, render_template,request,redirect
from pymongo import MongoClient
client = MongoClient()
db = client.seminar #데이터베이스 설정

app = Flask(__name__) # import 한 Flask 클래스를 객체화 시켜서 app 변수에 저장

@app.route("/") # flask의 route 데코레이터를 사용하여 엔드포인트를 등록
def hello():
    articles = []
    docs = db.articles.find()
    for article in docs:
        articles.append(article) #mongoDB에서 데이터를 불러와 articles라는 배열에 저장
    return render_template('index.html',articles = articles)#데이터를 html파일로 전달

@app.route("/new",methods = ['GET','POST'])
def new():
    if request == 'POST':
        db.articles.insert({"title":request.form.title,
                            "content":request.form.content})
        redirect(url_for(''))
    return render_template('new.html')

@app.route("/edit/<title>",methods =['GET','POST'])
def edit(title):
    if request.method == 'POST':
        db.articles.update({"title":title,
                            "$set":{"title":title,
                                    "content":request.form.content}})
        redirect(url_for(''))
    article = db.articles.find_one({"title":title})
    return render_template('new.html',article)
if __name__ == '__main__':
    app.run()
