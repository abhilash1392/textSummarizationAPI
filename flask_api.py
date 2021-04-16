from logging import debug
from flask import Flask, request, jsonify, render_template, Response
from model_summarization import summary_text 


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarized',methods=['POST'])
def summarized():
    """
    For rendering results on HTML GUI
    """
    text = request.form['Text']
    text = str(text)

    summary_answer = summary_text(text)

    return render_template('index.html',text = text, summary = summary_answer)


if __name__ == "__main__":
    app.run(debug=True)   