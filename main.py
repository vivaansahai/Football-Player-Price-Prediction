import pandas as pd
import pickle
from flask import Flask, render_template, request
# import sklearn  

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    page_views = float(request.form['page_views'])
    fpl_value = float(request.form['fpl_value'])
    fpl_sel = float(request.form['fpl_sel'])
    fpl_points = float(request.form['fpl_points'])
    big_club = int(request.form['big_club'])
    x = pd.DataFrame([[page_views, fpl_value, fpl_sel, fpl_points, big_club]], columns=['page_views', 'fpl_value', 'fpl_sel', 'fpl_points', 'big_club'])
    model = pickle.load(open('predictPrice.pkl', 'rb'))
    prediction = model.predict(x)
    return render_template('index.html', prediction_text=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)