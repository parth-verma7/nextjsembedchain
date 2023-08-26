from flask import Flask, redirect, render_template, url_for, request, session
import os
from embedchain import App
os.environ["OPENAI_API_KEY"] = "API_KEY"
elon_bot=App()

app = Flask(__name__)
# app.secret_key="dsjdijbfjbvj"

@app.route('/', methods=['GET','POST'])
def input():
    if(request.method=='POST'):
        doc_link=request.form.get('doc')
        print("The link is ", doc_link)
        elon_bot.add(doc_link)
        # session['elon_bot']=elon_bot
        return redirect('/ques')
    return render_template('index.html')

@app.route('/ques', methods=['GET','POST'])
def ques():
    if(request.method=="GET"):
        # elon_bot=session.get('elon_bot')
        print("11111111111111")
        return render_template('ques.html')
    elif(request.method=='POST'):
        que=request.form.get('question')
        ans=elon_bot.query(que)
        return ans
    

if __name__ == '__main__':
    app.run(debug=True)