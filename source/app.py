from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

# Load the pickled model
with open('final_model.sav', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input values from the form
    input_values = [float(request.form['input1']),
                    float(request.form['input2']),
                    float(request.form['input3']),
                    float(request.form['input4'])]

    # Convert inputs into a NumPy array
    input_array = np.array(input_values).reshape(1, -1)

    # Make prediction using the model
    prediction = model.predict(input_array)

    return render_template('index.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)