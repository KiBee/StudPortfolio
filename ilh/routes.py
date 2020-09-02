from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from ilh import db, app
# from ilh.models import Message, User


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')