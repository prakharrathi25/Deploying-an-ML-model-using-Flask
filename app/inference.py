''' Importing Necesaary libraries '''
import numpy as np
import keras
import json
import requests

SIZE = 128 # defining image dimensions
MODEL_URI = "http://localhost:8502/v1/models/pets:predict"
CLASSES = ['Cat', 'Dog']

# Function to retrive an image
def get_prediction(img_path):
    img = keras.preprocessing.image.load_img(
        img_path,
        target_size=(SIZE,SIZE)
    )
    # Convert image to a numpy array
    img = keras.preprocessing.image.img_to_array(img)
    img = keras.applications.mobilenet_v2.preprocess_input(img)
    img = np.expand_dims(img, axis=0)

    # Convert to a json object to send to the server
    data = json.dumps({
        'instances': img.tolist()
    })
    response = requests.post(MODEL_URI, data=data.encode()) # Response to the POST request
    result = json.loads(response.text)

    # Labeling our predictions
    pred = np.squeeze(result['predictions'][0])
    pred_class = CLASSES[int(pred > 0.5)] # If greater than 0.5 then dog, else cat

    return pred_class
