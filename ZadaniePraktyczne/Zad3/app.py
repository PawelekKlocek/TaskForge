# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///basket.db'
db = SQLAlchemy(app)

class Product(db.Model):
    #uzupełnij klasę Product z polami id, name, quantity


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_product', methods=['POST'])
def add_product():
    #dodaj pola name i quantity do bazy danych 
    #pobierz dane z formularza
    
    return redirect(url_for('basket'))

@app.route('/basket')
def basket():
    #wyświetl wszystkie produkty z bazy danych
    
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True )
