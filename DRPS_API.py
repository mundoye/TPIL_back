from flask import Flask, jsonify
from flask import render_template
import pandas as pd
from flask import request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

data_moy7 = pd.read_pickle('./Avg7.pkl')
data_moy21 = pd.read_pickle('./Avg21.pkl')
data_max = pd.read_pickle('./Max.pkl')

@app.route('/get_data', methods=["POST", "GET"])
def get_data():
    cellule = request.json['cellule']
    dat7 = data_moy7[data_moy7.Cellule == cellule].values.tolist()[0][1:]
    dat21 = data_moy21[data_moy21.Cellule == cellule].values.tolist()[0][1:]
    dat_max = data_max[data_max.Cellule == cellule].values.tolist()[0][1:]
    mois = data_moy7.columns.tolist()[0:][1:]

    return jsonify({
        'moy7' : dat7,
        'moy21' : dat21,
        'max' : dat_max,
        'mois' : mois
    })


if __name__ == "__main__":
    app.run(debug=True)
