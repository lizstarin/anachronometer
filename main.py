from flask import Flask, render_template, request
from wtforms import Form, TextField, TextAreaField, SubmitField, validators
import urllib2
import validator, text_analyzer

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/submit_text', methods=['POST'])
def submit_text():
	try:
		date = validator.validate_year(request.form['date'])
		text = validator.validate_text(request.form['text'])
		words = text_analyzer.parse_text(text)
	except:
		return render_template('index.html')

if __name__ == "__main__":
    app.run()
 