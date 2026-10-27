from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_session import Session
from app.auth import auth
from app.tasks import task_bp
from dotenv import load_dotenv
import os


app = Flask(__name__)
load_dotenv()
app.secret_key = os.environ['SECRET_KEY']
app.register_blueprint(auth)
app.register_blueprint(task_bp)


app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
