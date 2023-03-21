from app import app
from flask import render_template

@app.route('/80s')
def hello_world():
    return render_template('80s_songs.html')

@app.route('/sneakers')
def hello_test():
    return render_template('sneakers.html')
