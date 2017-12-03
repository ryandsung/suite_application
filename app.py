from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from data import Articles


app = Flask(__name__)
Bootstrap(app)

Articles = Articles()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/announcements')
def announcements():
    return render_template('announcements.html')

@app.route('/pictures')
def pictures():

    return render_template('pictures.html', pictures = Articles)

if __name__ == "__main__":
    app.run(debug=True)