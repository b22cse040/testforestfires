from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

## import ridge Regressor
ridge_model = pickle.load(open('models/ridge.pkl', 'rb'))
standardScaler = pickle.load(open(r'models\scaler.pkl', 'rb'))

application = Flask(__name__)
app = application

@app.route("/")
def welcome():
  return render_template("index.html")

@app.route('/predictdata', methods = ['GET', 'POST'])
def predict_datapoint():
  if request.method == 'POST':
    temperature = float(request.form['Temperature'])
    rh = float(request.form['RH'])
    ws = float(request.form['Ws'])
    rain = float(request.form['Rain'])
    ffmc = float(request.form['FFMC'])
    dmc = float(request.form['DMC'])
    isi = float(request.form['ISI'])
    classes = int(request.form['Classes'])
    region = int(request.form['Region'])

    input_data = [temperature, rh, ws, rain, ffmc, dmc, isi, classes, region]
    scaled_data = standardScaler.transform([input_data])

    result = ridge_model.predict(scaled_data)
    return render_template('home.html', results = result[0])

  else:
    return render_template('home.html')

if __name__ == "__main__":
  app.run(host = "0.0.0.0")