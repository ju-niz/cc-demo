# app.py
import os
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
DEPLOYMENT_VERSION = os.environ.get('DEPLOYMENT_VERSION', 'unknown')

@app.route('/')
def index():
    return render_template('index.html', version=DEPLOYMENT_VERSION)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
