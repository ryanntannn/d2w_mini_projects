from app import db
from app import login
from datetime import datetime 
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


# example of how to create association table
#association_table = db.Table('association', 
#    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
#    db.Column('challenge_id', db.Integer, db.ForeignKey('challenge.id'))
#)

@login.user_loader
def load_user(id):
	return User.query.get(int(id))

class User(UserMixin, db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def __repr__(self):
		return f'<User {self.username:}>'

# create your model for the database here
class PredictorInput(db.Model):
    __tablename__ = 'prediction'
    id = db.Column(db.Integer, primary_key=True)
    scenario_name = db.Column(db.String(64))
    total_population = db.Column(db.Integer)
    gdp_per_capita = db.Column(db.Integer)
    percentage_male = db.Column(db.Integer)
    percentage_urban = db.Column(db.Integer)
    human_development_index = db.Column(db.Float)
    temperature_increase = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.now())
	