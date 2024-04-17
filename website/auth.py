from flask import Flask, render_template, redirect, url_for, request, flash, Blueprint
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':# dlatego żeby wykonywał się tylko jak ejst post request
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password): #funkcja porownoje zhashowane haslo z haslem wpisanym przez uzytkownika
                #session['user_id'] = user.id
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Invalid password. Please try again.', 'error') #flash to metoda do wypisywania wiadomosci z wydarzen w aplikacji, np. errorow
        else:
            flash('User not found.', 'error')
    
    return render_template('login.html', user=current_user)

@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    # print(session)
    # session.clear()
    # print(session)
    logout_user()
    flash('You have been logged out!', category='success')
    return redirect(url_for('auth.login')) 



@auth.route('/register', methods=['GET', 'POST'])
def register():
    data = request.form
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if len(username) < 2:
            flash('The username must be greater than 1 character.', category='error')
        elif len(password) < 8:
            flash('The password must be blalblabla.', category='error')
        elif user:
            flash('The username is already taken. Please choose a different one.', category='error')
        else:
            new_user = User(username=username, password=generate_password_hash(password, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created.', category='success')
            return redirect(url_for('auth.login'))

    return render_template('register.html', user=current_user)
