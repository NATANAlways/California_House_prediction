from flask import Flask, render_template, request, jsonify, url_for, app
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the model
with open('regmodel.pkl', 'rb') as file:
    model = pickle.load(file)

with open('scaling.pkl', 'rb') as file:
    scaler = pickle.load(file)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    # std
    print(np.array(list(data.values())).reshape(1, -1))
    new_data = scaler.transform(np.array(list(data.values())).reshape(1, -1))
    predict = model.predict(new_data)
    print(predict[0])
    return jsonify(predict[0])

@app.route('/predict_data', methods=['POST'])
def predict_data():
    data = [float(i) for i in request.form.values()]
    final_ip = scaler.transform(np.array(data).reshape(1, -1))
    print(final_ip)
    model_out = model.predict(final_ip)[0]
    return render_template('home.html', prediction_text=f'Predicted Price: ${model_out * 100000:,.2f}')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')