from flask import Flask, redirect, render_template, url_for, request, session, jsonify
import os
from embedchain import App
from flask_cors import CORS
os.environ["OPENAI_API_KEY"] = "API_KEY"
elon_bot = App()

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

submitted_url=""

@app.route('/', methods=['GET','POST'])
def submit_url():
    if request.method == 'POST':
        global submitted_url
        data = request.get_json()
        submitted_url = data.get('url')
        print(submitted_url)
        elon_bot.add(doc_link)
        return redirect('/ques')
    return "get response"

@app.route('/process-text', methods=['POST'])
def process_text():
    global submitted_url
    data = request.get_json()
    text = data.get('text')
    result = {"processedText": f"Processed: {text}"}
    ques=result['processedText']
    ans=elon_bot.query(ques)
    print(ans)
    result={'ans':ans}
    return jsonify(result)


# @app.route('/', methods=['GET','POST'])
# def input():
#     if(request.method=='POST'):
#         doc_link=request.form.get('doc')
#         print("The link is ", doc_link)
#         elon_bot.add(doc_link)
#         # session['elon_bot']=elon_bot
#         return redirect('/ques')
#     return render_template('index.html')

# @app.route('/ques', methods=['GET','POST'])
# def ques():
#     if(request.method=="GET"):
#         # elon_bot=session.get('elon_bot')
#         print("checking")
#         return render_template('ques.html')
#     elif(request.method=='POST'):
#         que=request.form.get('question')
#         ans=elon_bot.query(que)
#         return ans
    

if __name__ == '__main__':
    app.run(debug=True)
