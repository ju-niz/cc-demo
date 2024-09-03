# app.py
import os
from flask import Flask, render_template

app = Flask(__name__)
DEPLOYMENT_VERSION = os.environ.get('DEPLOYMENT_VERSION', 'unknown')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
