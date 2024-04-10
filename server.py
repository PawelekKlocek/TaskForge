from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__) 


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/notes")
def notes():
    return render_template("notes.html")

@app.route("/todo")
def todo():
    return render_template("todo.html")

#logging to page function
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username != 'pawelek' or password != 'krol':
            return redirect(url_for('login'))
        else:
            return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        if username != None and email != None and password != None:
            return redirect(url_for('home'))
    return render_template('register.html')



if __name__ == '__main__':
    app.run(debug=True)
