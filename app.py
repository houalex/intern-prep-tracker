from flask import Flask, session, g
import config
from config import Config
from exts import db
from models import UserModel
from blueprints.auth import bp as auth_bp
from blueprints.progress import bp as progress_bp
from flask_migrate import Migrate

app=Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(auth_bp)
app.register_blueprint(progress_bp)

@app.before_request
def my_before_request():
    user_id = session.get("user_id")
    if user_id:
        user = db.session.get(UserModel, user_id)
        setattr(g, "user", user)
    else:
        setattr(g, "user", None)

@app.context_processor
def my_context_processor():
    return {"user": g.user}




