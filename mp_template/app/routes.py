from app import application
from app.predictor import predict_all_emission_sources
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, PredictorForm, RegistrationForm 
from flask_login import current_user, login_user, logout_user, login_required
from app.models import PredictorInput, User 
from werkzeug.urls import url_parse
from app import db
from flask import request 
from app.serverlibrary import * 

@application.route('/')
@application.route('/index')
def index():
	return render_template('index.html', title='Home')

@application.route('/predictor', methods=['GET', 'POST'])
@login_required
def predictor():
	form = PredictorForm()
	history = PredictorInput.query.all()
	if form.validate_on_submit():
		predictor_input = PredictorInput(
			scenario_name=form.scenario_name.data,
			total_population=form.total_population.data,
			gdp_per_capita=form.gdp_per_capita.data,
			percentage_urban=form.percentage_urban.data,
			percentage_male=form.percentage_male.data,
			human_development_index=form.human_development_index.data,
			temperature_increase=form.temperature_increase.data
        )
		db.session.add(predictor_input)
		db.session.commit()
		predictions = predict_all_emission_sources(form.total_population.data, form.gdp_per_capita.data, form.percentage_male.data, form.percentage_urban.data, form.human_development_index.data, form.temperature_increase.data)
		return render_template('predictor.html', title='Predictor', form=form, predictions=predictions, history=history)
	return render_template('predictor.html', title='Predictor', form=form, predictions=[], history=history)

@application.route('/history', methods=['GET'])
@login_required
def history():
	history = PredictorInput.query.all()
	return render_template('history.html', title='History', history=history)

@application.route('/history/<int:id>', methods=['GET'])
@login_required
def history_detail(id):
	prediction_input = PredictorInput.query.get(id)
	if prediction_input is None:
		flash('History not found')
	predictions = predict_all_emission_sources(prediction_input.total_population, prediction_input.gdp_per_capita, prediction_input.percentage_male, prediction_input.percentage_urban, prediction_input.human_development_index, prediction_input.temperature_increase)
	return render_template('history_detail.html', title='History Detail',prediction_input=prediction_input, predictions=predictions)

@application.route('/users')
@login_required
def users():
	users = User.query.all()	
	# mergesort(users, lambda item: item.username)
	usernames = [u.username for u in users]
	return render_template('users.html', title='Users',
							users=usernames)

@application.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
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

@application.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@application.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(username=form.username.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Congratulations, you are now a registered user.')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)

