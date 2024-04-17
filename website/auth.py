from flask import Flask, render_template, redirect, url_for, request, flash, Blueprint
# import uuid
# import datetime
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import UserMixin
# from flask_bcrypt import Bcrypt
# from flask_security import current_user, login_required

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    if request.method == 'POST':
        username = request.form['username']
    #     password = request.form['password']
    #     user = User.query.filter_by(username=username).first()
    #     if user:
    #         if bcrypt.check_password_hash(user.password, password): #funkcja porownoje zhashowane haslo z haslem wpisanym przez uzytkownika
    #             session['user_id'] = user.id
    #             return redirect(url_for('home'))
    #         else:
    #             flash('Invalid password. Please try again.', 'error') #flash to metoda do wypisywania wiadomosci z wydarzen w aplikacji, np. errorow
    #     else:
    #         flash('User not found.', 'error')
    #
    return render_template('login.html')

@auth.route('/logout', methods=['GET'])
def logout():
    # print(session)
    # session.clear()
    # print(session)
    flash('You have been logged out!', category='success')
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    data = request.form
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if len(username) < 2:
            flash('The username must be greater than 1 character.', category='error')
        elif len(password) < 8:
            flash('The password must be blalblabla.', category='error')

        else:
            print("utworzono konto")
            flash('Account created.', category='success')

        # user = User.query.filter_by(username=username).first()
        # if user:
        #     flash('The username is already taken. Please choose a different one.')
        #     return redirect(url_for('register'))
        #     new_user = User(username=username, password=hashed_password)
        #     db.session.add(new_user)
        #     db.session.commit()
        #     flash('Registration successful! You can now log in.', 'success')
        #     return redirect(url_for('login'))

    return render_template('register.html')
