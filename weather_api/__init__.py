from flask import Flask
from config import Config
from .site.routes import site
from .authentication.routes import auth
from .models import db, User, login_manager
from flask_migrate import Migrate
from .api.routes import api
from flask_cors import CORS
from .helpers import JSONEncoder


app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'auth.signin' 


migrate = Migrate(app, db)
app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)
CORS(app)
app.json_encoder = JSONEncoder

# ma.init_app(app)



