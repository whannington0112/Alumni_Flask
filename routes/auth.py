from flask import Blueprint, render_template, redirect, url_for, flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from models.user import User

auth = Blueprint('auth', __name__, template_folder='../templates/auth')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Placeholder: Add real authentication logic here
        flash('Login functionality coming soon!', 'info')
    return render_template('auth/login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Placeholder: Add real registration logic here
        flash('Registration functionality coming soon!', 'info')
    return render_template('auth/register.html')

@auth.route('/logout')
def logout():
    flash('Logout functionality coming soon!', 'info')
    return redirect(url_for('main.home')) 