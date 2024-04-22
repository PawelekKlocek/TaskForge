#app.py rozwiazanie zadania 2

from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'thisissecretkey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome', methods=['POST'])
def welcome():
    name = request.form['name']
    # wprowadź kod
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port= 9000)
