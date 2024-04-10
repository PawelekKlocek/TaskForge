from flask import Flask, render_template, redirect, url_for, request, session
import sqlalchemy
app = Flask(__name__) 

notes = []
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/notes")
def notes():
    return render_template('notes.html')

@app.route("/todo")
def todo():
    return render_template("todo.html")
#test
#logging to page function
users = {
    'user1': 'password1',
    'user2': 'password2',
    'pawel': 'krol'
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in users or users[username] != password:
            error = "Invalid Credentials. Please try again."
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        if username != "" and email != "" and password != "":
            return redirect(url_for('home'))
        else:
            error = "Invalid Credentials. Please try again."
    return render_template('register.html', error=error)



if __name__ == '__main__':
    app.run(debug=True)
