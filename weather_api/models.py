from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid
import secrets
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin
from flask_marshmallow import Marshmallow
# from flask_migrate import Migrate




db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True, unique = True)
    email = db.Column(db.String(150), unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)
    token = db.Column(db.String, unique = True, nullable = False)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    weather = db.relationship('Weather', backref = 'owner', lazy = True)

    def __init__(self, email, password, token = '', id = ''):
        self.id = self.set_id()
        self.email = email
        self.password = self.set_password(password)
        self.token = self.set_token(24)

    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def set_token(self, lenght):
        return secrets.token_hex(lenght)

    
class Weather(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(150), nullable = False)
    description = db.Column(db.String(300), nullable = False)
    city = db.Column(db.String(100), nullable = False)
    country = db.Column(db.String(100), nullable = False)
    temperature = db.Column(db.String(100), nullable = False)
    wind_speed = db.Column(db.String(100), nullable = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)


    def __init__(self, name, description, city, country, temperature, wind_speed, date_created, user_token, id = ''):
        self.id = self.set_id()
        self.name = name
        self.description = description
        self.city = city
        self.country = country
        self.temperature = temperature
        self.wind_speed = wind_speed
        self.date_created = date_created
        self.user_token = user_token


    def set_id(self):
        return (secrets.token_urlsafe())


class WeatherSchema(ma.Schema):
    class Meta:
        fields = ['id', 'name', 'description', 'city', 'country', 'temperature', 'wind_speed', 'date_created']

weather_schema = WeatherSchema()
weathers_schema = WeatherSchema(many=True)



