from flask import Flask, render_template

# Create flask app.
app = Flask(__name__)

# Home.
@app.route('/')
def home():
	return render_template('home.html')

# http://127.0.0.1:5000/user/diyorbek
@app.route('/user/<name>')
def user(name):
	return f'Hello {name.title()}'