# app.py
import os
import socket
from flask import Flask, render_template
from dotenv import load_dotenv
import sys
import logging


load_dotenv()
app = Flask(__name__)
DEPLOYMENT_VERSION = os.environ.get('DEPLOYMENT_VERSION', 'unknown')
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
app.logger.addHandler(console_handler)
logger.setLevel(logging.DEBUG)

@app.route('/')
def index():
    logger.info("Demo app invoked")
    ip_addr = socket.gethostbyname(socket.gethostname())
    logger.warning("Warning Log demo")
    return render_template('index.html', version=DEPLOYMENT_VERSION, ip_addr=ip_addr)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
