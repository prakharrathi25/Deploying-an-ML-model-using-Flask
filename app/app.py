''' Importing necessary libraries''' 
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

# Creating an instance of the flask app
app = Flask(__name__)
Bootstrap(app) # Pass app into the bootstrap Class to use Bootstrap functions

''' 
ROUTES
'''
# Route when we recieve a GET request 
@app.route('/', methods=['GET']) 
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)