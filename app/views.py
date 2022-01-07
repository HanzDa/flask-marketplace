from app import app
from flask import render_template

from app.forms import SignUpForm


@app.route('/')
@app.route('/home/')
def index():
    return render_template('base.html', show_navbar=True, show_footer=True)

@app.route('/register/', methods=['GET', 'POST'])
def regiter():
    form = SignUpForm()
    if form.validate_on_submit():
        name = form.names.data
        
    return render_template('user/register.html', form = form)