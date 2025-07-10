from flask import Blueprint, render_template

main = Blueprint('main', __name__, template_folder='../templates')

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/directory')
def directory():
    return render_template('directory/list.html')

@main.route('/jobs')
def jobs():
    return render_template('jobs/list.html')

@main.route('/events')
def events():
    return render_template('events/list.html') 

@main.route('/news')
def news():
    return render_template('news/list.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')