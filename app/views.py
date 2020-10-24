from flask import render_template
from app import app

# Views
#@app.route('/news/<int:news_id>')
#def news(news_id):
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    # message = 'Hello World'
    title = 'Home - A place where you find Accurate News Online'
    return render_template('index.html', title = title)







