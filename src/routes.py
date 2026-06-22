from flask import Blueprint, render_template
from forms import EntryForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/add-entry', methods = ['GET', 'POST'])
def add_entry():
    form = EntryForm()
    return render_template('add_entry.html', form = form)