from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Load the saved model
with open('models/rf_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Route for rendering the frontend
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the POST request
        data = request.json
        features = np.array(data['features']).reshape(1, -1)  # Ensure correct shape
        
        # Predict using the loaded model
        prediction = model.predict(features)
        return jsonify({'quality': prediction[0]})  # Return prediction
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
