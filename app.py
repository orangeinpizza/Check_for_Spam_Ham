from flask import Flask, render_template, request
import pickle
import string
from nltk.corpus import stopwords

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/')
# def change(mess):
#     mess=list(mess)
#     i=[i for i in mess if i not in string.punctuation]
#     x=''.join(i)
#     x=x.split()
#     i=[i for i in x if i.lower() not in stopwords.words('english')]
#     return i

@app.route('/')
def classify(text):
    model=pickle.load(open('Spam_or_Ham.pkl','rb'))
    ans=model.predict([text,text])
    return ans[0]

@app.route('/',methods=['POST','GET'])
def submit():
    if request.method=='POST':
        text=str(request.form['text_123'])
    ans=classify(text)
    return render_template('index.html',a=ans)    


if __name__=='__main__':
    app.run(debug=True)
