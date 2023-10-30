from flask import Flask, render_template, request, redirect, url_for
import model
from forms import QuizForm

import os
SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

# <!-- List of correct answers --> 
correct_ans = ["c", "c", "b", "a", "a"]

@app.route('/')
@app.route('/index')
def index():
  return render_template("index.html")

@app.route('/success')
def success():
  return render_template("success.html")

@app.route('/no_success')
def no_success():
  return render_template("no_success.html")

# route to the quiz
@app.route('/trivia', methods=['GET', 'POST'])
@app.route('/trivia', methods=['GET', 'POST'])
def trivia():
  if request.method == 'POST':
    results = model.processform(request.form)
    return render_template('results.html', results=results)
  else:
    return render_template('trivia.html', results='')
    
@app.route('/practice')
def practice():
  return render_template('/practice.html')
# got it to work lol
app.run(host='0.0.0.0', port=81)
