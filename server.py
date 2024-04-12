from flask import Flask, render_template, redirect, url_for, request
import uuid
import datetime

app = Flask(__name__)
todos = []# lista zadań
notes_list = []#lista notatek


@app.route("/")
def home():
    return render_template("index.html")



@app.route("/notes", methods=['GET', 'POST'])
def notes():
    return render_template("notes.html", notes=notes_list)

@app.route("/add_note", methods=['POST'])
def add_note():
    note_text = request.form['note_name']
    note_color = request.form['note_color']
    current_id = str(uuid.uuid4())
    notes_list.append({'text': note_text, 'color': note_color, 'id' : current_id})
    return redirect(url_for('notes'))

@app.route("/update_note/<string:note_id>", methods=['POST'])
def update_note(note_id):
    if request.method == 'POST':
        new_note = request.form["new_note_name"]
        for note in notes_list:
            if note['id'] == note_id:
                note['text'] = new_note
                break
    return redirect(url_for('notes'))
@app.route("/delete_note/<string:note_id>", methods=['GET','POST'])
def delete_note(note_id):
    if request.method == 'POST':
        for note in notes_list:
            if str(note['id']) == note_id:
                notes_list.remove(note)
                break
    return redirect(url_for('notes'))

@app.route("/todo", methods=['GET', 'POST'])# dodajemy metody POST i GET do routingu który pozwoli nam na dodawanie nowych zadań do listy
def todo():
    if request.method == 'POST':
        todo_name= request.form["todo_name"]# przyjmujemy dane z formularza do zmiennej todo_name
        todo_priority = request.form["todo_priority"]
        current_id = str(uuid.uuid4())  # Generujemy unikalny identyfikator UUID dla nowego zadania
        todos.append({# dodajemy nowy element do listy todos
            'id': current_id,
            'name': todo_name,
            'checked': False,
            'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'priority':todo_priority
        })
    return render_template("todo.html", items=todos)# przekazujemy liste todos do szablonu todo.html

@app.route("/delete/<string:todo_id>", methods=['POST'])# dodajemy metody POST do routingu który pozwoli nam na usuwanie zadań z listy
def delete_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            todos.remove(todo)
    return redirect(url_for('todo'))
    
#Do zmiany
@app.route("/update/<string:todo_id>", methods=['POST'])
def update_todo(todo_id):
    if request.method == 'POST':
        new_name = request.form["new_todo_name"]
        for todo in todos:
            if todo['id'] == todo_id:
                todo['name'] = new_name
                break
    return redirect(url_for('todo'))


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
