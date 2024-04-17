from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.secret_key = 'thisissecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # mówimy gdzie ma być baza danych przechoywana
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Task, Note

    create_database(app)

    login_manager = LoginManager() #tworzymy obiekt do zarzadzania logowaniem
    login_manager.login_view = 'auth.login' #jak ktos nie jest zalogowany to przekierowuje na strone logowania
    login_manager.init_app(app) #inicjalizujemy obiekt do zarzadzania logowaniem

    @login_manager.user_loader # mówi jak ma być ładowany użytkownik
    def load_user(id):
        return User.query.get(int(id))

    return app

#sprawdza czy baza danych istnieje, jeśli nie to ją tworzy
def create_database(app):
    with app.app_context():
        if not path.exists('website/' + DB_NAME):#???
            db.create_all()
            print('Created Database!')