from flask import Flask, render_template, redirect, url_for, request
import uuid
import datetime

app = Flask(__name__) 
todos = []# lista zadań
notes = []#lista notatek


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/notes")
def notes():
    return render_template("notes.html")


@app.route("/todo", methods=['GET', 'POST'])# dodajemy metody POST i GET do routingu który pozwoli nam na dodawanie nowych zadań do listy
def todo():
    if request.method == 'POST':
        todo_name= request.form["todo_name"]# przyjmujemy dane z formularza do zmiennej todo_name
        current_id = str(uuid.uuid4())  # Generujemy unikalny identyfikator UUID dla nowego zadania
        todos.append({# dodajemy nowy element do listy todos
            'id': current_id,
            'name': todo_name,
            'checked': False,
            'date': datetime.date.today()
        })
    return render_template("todo.html", items=todos)# przekazujemy liste todos do szablonu todo.html

@app.route("/delete/<string:todo_id>", methods=['POST'])# dodajemy metody POST do routingu który pozwoli nam na usuwanie zadań z listy
def delete_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            todos.remove(todo)
    return redirect(url_for('todo'))
#Do zmiany
'''
@app.route("/update/<string:todo_id>", methods=['POST'])# dodajemy metody POST do routingu który pozwoli nam na usuwanie zadań z listy
def update_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            todo['name'] = request.form["new_todo_name"]
    return redirect(url_for('todo'))
'''

# dodajemy metody POST do routingu który pozwoli nam na usuwanie zadań z listy
@app.route("/checked/<string:todo_id>", methods=['POST'])
def checked_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            todo['checked'] = not todo['checked'] # zmieniamy status zadania na przeciwny
            break
    return redirect(url_for('todo'))

###################################################################


#test
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
