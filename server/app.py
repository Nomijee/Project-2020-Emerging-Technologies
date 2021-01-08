# Import libraries.
from os import path

from flask import Flask, request, jsonify, render_template
from flask_cors import cross_origin, CORS

from tensorflow.keras.models import load_model

# Create flask app and enable cors.
app = Flask(__name__)
cors = CORS(app)

# Load deep learning model.
model = load_model(path.join(path.abspath('.'), 'model/model.h5'))


# Create a REST endpoint to accept POST requests containing speed as body.
# This REST endpoint is responsible for making predictions for given speeds.
@app.route('/predict', methods=['POST'])
# Enable cross origin to enable this endpoint to accept requests from multiple devices/applications.
@cross_origin()
# This function this method gets executed whenever a request is received at http://localhost:5000/predict endpoint.
def predict():
    # Get speed from request body and cast it to float.
    speed = float(request.json['speed'])
    # Predict the power using deep learning model for the received speed.
    prediction = round(model.predict([speed])[0][0], 3)
    # Return the speed and predicted power as JSON response.
    return jsonify({
        'speed': speed,
        'power': prediction
    })


# Create a REST endpoint to render HTML templates.
# This REST endpoint is responsible rendering the HTML template that you see at http://localhost:5000.
@app.route('/')
# Enable cross origin to enable this endpoint to accept requests from multiple devices/applications.
@cross_origin()
# This function this method gets executed whenever a request is received at http://localhost:5000/ endpoint.
def index():
    # Render the index.html template.
    return render_template('index.html')


# Main function to start app.
if __name__ == '__main__':
    # Run app.
    app.run()
