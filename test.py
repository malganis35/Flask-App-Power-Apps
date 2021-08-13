# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 10:32:06 2021

@author: VG6196
"""

#%% Importing the requests library
import requests
import json
import pandas as pd


#%% Create the dataset
lst_pays = ["France", "UK", "US"]
lst_vente = [10, 20, 30]
df_data = pd.DataFrame()
df_data["Pays"] = lst_pays
df_data["Vente"] = lst_vente


#%% API Call
# url = "http://localhost:5000/api/predict"
url = "https://flask-power-apps.herokuapp.com/api/predict"

data = df_data.to_dict(orient="records")
headers = {
            "multiplier": "-1"
            }
r = requests.post(url, json=json.dumps(data), headers = headers)

#%% API Return
json_data = json.loads(r.text)
print(json_data)