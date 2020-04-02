''' Importing necessary libraries'''
from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap
import os

# Importing the inference module that was created
import inference
# Creating an instance of the flask app
app = Flask(__name__)
Bootstrap(app) # Pass app into the bootstrap Class to use Bootstrap functions

'''
ROUTES
'''
# Route when we recieve a GET or POST request
@app.route('/', methods=['GET', 'POST'])
def index():
	# when the image has been uploaded
	if request.method == 'POST':
		uploaded_file = request.files['file']
		if uploaded_file.filename != '': # check if the click was valid

			''' ADD A filetype validation here '''

			# Saving a copy of the uploaded image to static to display along with the picture
			image_path = os.path.join('static', uploaded_file.filename)  # A unique filaneme creattion method can be used here
			uploaded_file.save(image_path)

			# Get the predicted class name from the inference module function
			class_name = inference.get_prediction(image_path)
			print('The identified animal is a: {}'.format(class_name)) # Display the result

			# Result to be displayed
			result = {
				'class_name': class_name,
				'image_path': image_path
			}
			return render_template('show.html', result=result)
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
