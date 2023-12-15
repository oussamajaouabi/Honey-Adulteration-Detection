from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def man():
    default_data = None
    return render_template('home.html', data=default_data)

@app.route('/home', methods=['GET', 'POST'])
def home():
    data = None

    if request.method == 'POST':
        csv_file = request.files['csv_file']

        if csv_file:
            df = pd.read_csv(csv_file)
            c = df.shape[1]
            arr = df.values[:,:c-1]
            data = model.predict(arr)

    return render_template('home.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
