from flask import Flask, render_template, redirect, url_for, request, flash, Blueprint
import uuid
import datetime
from flask_login import login_required, current_user
from .models import User, Task, Note
from . import db
from sqlalchemy import desc


views = Blueprint('views', __name__)


# @app.route("/users")
# def users():
#     users_data = User.query.all()  # Pobieranie danych z bazy danych
#     return render_template("users.html", users=users_data)  # Przekazanie danych do szablonu HTML
#

# to bedzie uzywane przy bazie danych, zeby sprawdzac czy dodalo poprawnie uzytkownika itd

@views.route("/")
@login_required
def home():
    user_notes = Note.query.filter_by(user_id=current_user.id).order_by(desc(Note.date)).all()# sortujemy po dacie dodania
    user_todos = Task.query.filter_by(user_id=current_user.id).order_by(desc(Task.date)).all()
    return render_template("index.html", user=current_user, notes=user_notes, todos=user_todos)


@views.route("/notes", methods=['GET', 'POST'])
@login_required
def notes():
    return render_template("notes.html", user=current_user, notes=Note.query.filter_by(user_id=current_user.id).all())


@views.route("/add_note", methods=['POST'])
def add_note():
    if request.method == 'POST':
        note_text = request.form.get('note_name')
        note_color = request.form.get('note_color')
        if note_text == '':
            flash('Note cannot be empty!', 'error')
            return redirect(url_for('views.notes'))
        else:
            new_note = Note(text=note_text, color=note_color, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
    return redirect(url_for('views.notes', user=current_user))


@views.route("/update_note/<string:note_id>", methods=['POST'])
def update_note(note_id):
    if request.method == 'POST':
        note_edit = request.form.get('new_note_name')
        if note_edit == '':
            flash('Note cannot be empty!', 'error')
            return redirect(url_for('views.notes'))
        else:
            note = Note.query.filter_by(id=note_id).first()
            note.text = note_edit
            db.session.commit()
    return redirect(url_for('views.notes', user=current_user, notes=Note.query.filter_by(user_id=current_user.id).all()))


@views.route("/delete_note/<string:note_id>", methods=['GET', 'POST'])
def delete_note(note_id):
    if request.method == 'POST':
        note = Note.query.filter_by(id=note_id).first()
        db.session.delete(note)
        db.session.commit()    
    return redirect(url_for('views.notes', user=current_user ))


@views.route("/todo", methods=['GET','POST'])  # dodajemy metody POST i GET do routingu który pozwoli nam na dodawanie nowych zadań do listy
@login_required
def todo():
    if request.method == 'POST':
        todo_name = request.form.get('todo_name')
        todo_priority = request.form.get('todo_priority')
        todo_checked = False
        if todo_name == '':
            flash('Task cannot be empty!', 'error')
        else:
            new_todo = Task(text=todo_name, priority=todo_priority, user_id=current_user.id, checked=todo_checked)
            db.session.add(new_todo)
            db.session.commit()
        
    user_todos = Task.query.filter_by(user_id=current_user.id).order_by(desc(Task.date)).all() # Fetch todos from the database
    return render_template("todo.html", user=current_user, todos=user_todos)


@views.route("/delete/<string:todo_id>", methods=['POST'])
def delete_todo(todo_id):
    todo = Task.query.filter_by(id=todo_id).first()  # Znajdź zadanie w bazie danych
    if todo:
        db.session.delete(todo)  # Usuń zadanie z bazy danych
        db.session.commit()
    return redirect(url_for('views.todo'))

@views.route("/update/<string:todo_id>", methods=['POST'])
def update_todo(todo_id):
    if request.method == 'POST':
        new_name = request.form["new_todo_name"]
        todo = Task.query.filter_by(id=todo_id).first()  # Znajdź zadanie w bazie danych
        if todo:
            todo.text = new_name  # Zaktualizuj nazwę zadania 
            db.session.commit()
    user_todos = Task.query.filter_by(user_id=current_user.id).order_by(desc(Task.date)).all()
    return redirect(url_for('views.todo', user=current_user, todos=user_todos))

@views.route("/checked/<string:todo_id>", methods=['POST'])
def checked_todo(todo_id):
    todo = Task.query.filter_by(id=todo_id).first()  # Znajdź zadanie w bazie danych
    if todo:
        todo.checked = not todo.checked  # Zmień status zadania
        db.session.commit()
    return redirect(url_for('views.todo', user=current_user))
