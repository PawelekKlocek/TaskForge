
from . import db # importujemy db z pliku __init__.py z obecnego pakietu
from flask_login import UserMixin # dziedziczymy po UserMixin, żeby móc używać metod związanych z logowaniem
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)# primary key to unikalny identyfikator użytowany do identyfikacji rekordu w bazie danych
    username = db.Column(db.String(100), unique=True)# unique=True oznacza, że wartość w tej kolumnie musi być unikalna
    password = db.Column(db.String(100))
    tasks = db.relationship('Task', backref='user')
    notes = db.relationship('Note', backref='user')

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)
    date = db.Column(db.DateTime(timezone=True), default=db.func.now())# sql dodaje date automatycznie za nas
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))# przypisujemy zadanie do użytkownika o danym id// w sql repreznetacja klasy User to user
    priority = db.Column(db.String(100))
    checked = db.Column(db.Boolean)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)
    color = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
