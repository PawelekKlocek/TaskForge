# from flask import Flask, render_template, redirect, url_for, request, flash
# import uuid
# import datetime
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import UserMixin
# from flask_bcrypt import Bcrypt
# # from flask_security import current_user, login_required
#
# app = Flask(__name__)
# bcrypt = Bcrypt(app) # potrzebne do zaszyfrowania haseł
# # db = SQLAlchemy(app)
#
# # DB_NAME = "database.db"
# #
# # app.secret_key= 'thisissecretkey' #pozniej to zrobimy tajne chyba
# # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' #plik z baza danych
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
#
#
# todos = []  # lista zadań
# notes_list = []  # lista notatek
#
# # class User(db.Model, UserMixin):
# #     id = db.Column(db.Integer, primary_key=True)
# #     username = db.Column(db.String(20), nullable=False, unique=True)
# #     password = db.Column(db.String(20), nullable=False)
#
#
# @app.route("/")
# def home():
#     # if 'user_id' in session:
#     #     user_id = session['user_id']
#     #     print("welcome, ", user_id)
#     # else:
#     #     print("nie ma id")
#     return render_template("index.html")
#
#
# @app.route("/notes", methods=['GET', 'POST'])
# def notes():
#     return render_template("notes.html", notes=notes_list)
#
#
# @app.route("/add_note", methods=['POST'])
# def add_note():
#     note_text = request.form['note_name']
#     note_color = request.form['note_color']
#     current_id = str(uuid.uuid4())
#     # if 'user_id' not in session:
#     #     flash('You have to be logged in!', 'error')
#     #     return redirect(url_for('login'))
#     # else:
#     notes_list.append({'text': note_text, 'color': note_color, 'id': current_id})
#     return redirect(url_for('notes'))
#
#
# @app.route("/update_note/<string:note_id>", methods=['POST'])
# def update_note(note_id):
#     if request.method == 'POST':
#         new_note = request.form["new_note_name"]
#         for note in notes_list:
#             if note['id'] == note_id:
#                 note['text'] = new_note
#                 break
#     return redirect(url_for('notes'))
#
#
# @app.route("/delete_note/<string:note_id>", methods=['GET', 'POST'])
# def delete_note(note_id):
#     if request.method == 'POST':
#         for note in notes_list:
#             if str(note['id']) == note_id:
#                 notes_list.remove(note)
#                 break
#     return redirect(url_for('notes'))
#
#
# @app.route("/todo", methods=['GET','POST'])  # dodajemy metody POST i GET do routingu który pozwoli nam na dodawanie nowych zadań do listy
# def todo():
#     if request.method == 'POST':
#         todo_name = request.form["todo_name"]  # przyjmujemy dane z formularza do zmiennej todo_name
#         todo_priority = request.form["todo_priority"]
#         current_id = str(uuid.uuid4())  # Generujemy unikalny identyfikator UUID dla nowego zadania
#         # if 'user_id' not in session:
#         #     flash('You have to be logged in!', 'error')
#         #     return redirect(url_for('login'))
#         # else:
#         #
#         todos.append({  # dodajemy nowy element do listy todos
#             'id': current_id,
#             'name': todo_name,
#             'checked': False,
#             'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#             'priority': todo_priority
#         })
#     return render_template("todo.html", items=todos)  # przekazujemy liste todos do szablonu todo.html
#
#
# @app.route("/delete/<string:todo_id>",
#            methods=['POST'])  # dodajemy metody POST do routingu który pozwoli nam na usuwanie zadań z listy
# def delete_todo(todo_id):
#     for todo in todos:
#         if todo['id'] == todo_id:
#             todos.remove(todo)
#     return redirect(url_for('todo'))
#
#
# # Do zmiany
# @app.route("/update/<string:todo_id>", methods=['POST'])
# def update_todo(todo_id):
#     if request.method == 'POST':
#         new_name = request.form["new_todo_name"]
#         for todo in todos:
#             if todo['id'] == todo_id:
#                 todo['name'] = new_name
#                 break
#     return redirect(url_for('todo'))
#
#
# # dodajemy metody POST do routingu który pozwoli nam na usuwanie zadań z listy
# @app.route("/checked/<string:todo_id>", methods=['POST'])
# def checked_todo(todo_id):
#     for todo in todos:
#         if todo['id'] == todo_id:
#             todo['checked'] = not todo['checked']  # zmieniamy status zadania na przeciwny
#             break
#     return redirect(url_for('todo'))
#
#
# ###################################################################
#
#
#
#
# # test
# # logging to page function
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     data = request.form
#     print(data)
#     # if request.method == 'POST':
#     #     username = request.form['username']
#     #     password = request.form['password']
#     #     user = User.query.filter_by(username=username).first()
#     #     if user:
#     #         if bcrypt.check_password_hash(user.password, password): #funkcja porownoje zhashowane haslo z haslem wpisanym przez uzytkownika
#     #             session['user_id'] = user.id
#     #             return redirect(url_for('home'))
#     #         else:
#     #             flash('Invalid password. Please try again.', 'error') #flash to metoda do wypisywania wiadomosci z wydarzen w aplikacji, np. errorow
#     #     else:
#     #         flash('User not found.', 'error')
#     #
#     return render_template('login.html')
#
# @app.route('/logout', methods=['GET'])
# def logout():
#     # print(session)
#     # session.clear()
#     # print(session)
#     flash('You have been logged out!', 'success')
#     return redirect(url_for('login'))
#
#
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     data = request.form
#     if request.method == 'POST':
#         username = request.form.get('username')
#         hashed_password =bcrypt.generate_password_hash(request.form.get('password'))
#         if len(username) < 2:
#             flash('The username must be greater than 1 character.', category='error')
#         user = User.query.filter_by(username=username).first()
#         if user:
#             flash('The username is already taken. Please choose a different one.')
#             return redirect(url_for('register'))
#             new_user = User(username=username, password=hashed_password)
#             db.session.add(new_user)
#             db.session.commit()
#             flash('Registration successful! You can now log in.', 'success')
#             return redirect(url_for('login'))
#
#     return render_template('register.html')
#
# @app.route("/users")
# def users():
#     users_data = User.query.all()  # Pobieranie danych z bazy danych
#     return render_template("users.html", users=users_data)  # Przekazanie danych do szablonu HTML
#
#
# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)