# app.py
import os
import socket
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
DEPLOYMENT_VERSION = os.environ.get('DEPLOYMENT_VERSION', 'unknown')

@app.route('/')
def index():
    ip_addr = socket.gethostbyname(socket.gethostname())
    return render_template('index.html', version=DEPLOYMENT_VERSION, ip_addr=ip_addr)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
