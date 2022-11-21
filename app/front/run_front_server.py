from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from requests.exceptions import ConnectionError
from requests import Session
from wtforms import StringField
from wtforms.validators import DataRequired

import json

class ClientDataForm(FlaskForm):
    sepal_length = StringField('sepal length (cm)', validators=[DataRequired()])
    sepal_width = StringField('sepal width (cm)', validators=[DataRequired()])
    petal_length = StringField('petal length (cm)', validators=[DataRequired()])
    petal_width = StringField('petal width (cm)', validators=[DataRequired()])


app = Flask(__name__)
app.config.update(
    CSRF_ENABLED=True,
    SECRET_KEY='you-will-never-guess',
)

def get_prediction(sepal_length, sepal_width, petal_length, petal_width):
    body = {
        'sepal_length': sepal_length,
        'sepal_width': sepal_width,
        'petal_length': petal_length,
        'petal_width': petal_width
    }
    result = {}

    myurl = "http://0.0.0.0:9180/predict"
    with Session() as s:
        s.headers.update({'Content-Type': 'application/json; charset=utf-8'})
        with s.post(myurl, json=body) as r:
            if r.status_code == 200:
                result = r.text

    return result


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/predicted/<response>')
def predicted(response):

    return render_template('predicted.html', response=response)


@app.route('/predict_form', methods=['GET', 'POST'])
def predict_form():
    form = ClientDataForm()
    data = dict()
    if request.method == 'POST':
        data['sepal_length'] = request.form.get('sepal_length')
        data['sepal_width'] = request.form.get('sepal_width')
        data['petal_length'] = request.form.get('petal_length')
        data['petal_width'] = request.form.get('petal_width')


        try:
            response = str(
                get_prediction(
                    data['sepal_length'],
                    data['sepal_width'],
                    data['petal_length'],
                    data['petal_width']
                )
            )
        except ConnectionError:
            response = json.dumps({"error": "ConnectionError"})
        return redirect(url_for('predicted', response=response))
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9181, debug=True)
