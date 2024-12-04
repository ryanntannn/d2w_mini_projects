from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectMultipleField, IntegerField, HiddenField, FloatField
from wtforms.validators import DataRequired, ValidationError, EqualTo, NumberRange
from app.models import User

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	password2 = PasswordField('Repeat Password', 
							   validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Register')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('Please use a different username.')


class PredictorForm(FlaskForm):
	scenario_name = StringField('Scenario Name', validators=[DataRequired()], default='China 2024')
	total_population = IntegerField('Total Population', validators=[DataRequired()], default=1419321278)
	percentage_urban = IntegerField('Percentage Urban', validators=[DataRequired(), NumberRange(min=0, max=100)], default=65)
	percentage_male = IntegerField('Percentage Male', validators=[DataRequired(), NumberRange(min=0, max=100)], default=51)
	gdp_per_capita = IntegerField('GDP per Capita', validators=[DataRequired()], default=12614)
	human_development_index = FloatField('Human Development Index', default=0.788)   
	temperature_increase = FloatField('Temperature Increase', default=1.5)
	submit = SubmitField('Predict')



	
