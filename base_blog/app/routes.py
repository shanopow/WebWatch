from app import app, db
from app.forms import LoginForm, RegistrationForm, TesterForm
from app.models import User
from flask_login import login_user, logout_user, current_user, login_required
from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    try:
        if current_user.is_admin == 1:
            tester_form = TesterForm()
            if tester_form.admin_choice.data == 'delete':
                User.query.filter_by(**{ tester_form.choices.data : tester_form.filter_val.data}).delete()
                users = User.query.all()
                db.session.commit()
                flash('User Deleted.')

            elif tester_form.admin_choice.data == 'search':
                users = User.query.filter_by(**{ tester_form.choices.data : tester_form.filter_val.data})
                if users.count() == 0:
                    flash('User not found')
                else:    
                    flash('User found.')
            else:
                users = User.query.order_by(User.id.desc()).limit(15).all()

            return render_template('admin.html', title='Admin', users=users, tester_form=tester_form, gen_get='First 15 Users')       
        else:
            return redirect(url_for('index'))
    except AttributeError:
        flash('Access Forbidden')
        return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        if current_user.is_authenticated:
            flash("Already logged in.")
            return redirect(url_for('index'))
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user is None or not user.check_password(form.password.data):
                flash('Invalid username or password')
                return redirect(url_for('login'))
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
        return render_template('login.html', title='Sign In', form=form)
    except:
        flash('Something went wrong there.')
        return redirect(url_for('index'))    


@app.route('/logout')
def logout():
    logout_user()
    flash('Logged Out.')
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash("Already logged in.")
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        admin_stat = 2
        if form.is_admin.data == 'bing':
            admin_stat = 1
        
        user = User(username=form.username.data, email=form.email.data, is_admin=admin_stat)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)