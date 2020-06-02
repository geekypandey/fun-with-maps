import csv
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    with open('data.csv') as f:
        reader = csv.reader(f)
        next(reader)
        data = list(enumerate(reader, start=1))
    print(data[0])
    return render_template('index.html', data=data)

