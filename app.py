# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 10:23:34 2021

@author: VG6196
"""

from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json
import pandas as pd
import os

app = Flask(__name__)


@app.route("/api/home")
def home_view():
        return "<h1>Welcome to Geeks for Geeks</h1>"

@app.route('/api/predict', methods=['POST'])
def makecalc():
    data = request.get_json()
    # print(data)
    # prediction = np.array2string(model.predict(data))
    data_json=json.loads(data)
    df=pd.DataFrame(data_json)
    
    multiplier = float(request.headers.get('multiplier'))
    
    df["Vente Simulée"] = df['Vente'].apply(lambda x: x*multiplier)
    prediction = df.to_dict(orient="records")
    # prediction = [0, 1] ; # data.copy()
    # return jsonify(prediction)
    return json.dumps(prediction)

if __name__ == '__main__':
    # modelfile = 'models/final_prediction.pickle'
    # model = p.load(open(modelfile, 'rb'))
    # app.run(debug=True, host='0.0.0.0')
    
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)