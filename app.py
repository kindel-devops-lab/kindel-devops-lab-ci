import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    """Root endpoint returning basic service status."""
    return jsonify({
        "message": "Welcome !",
        "status": "running"
    })

@app.route('/health', methods=['GET'])
def health_check():
    """Healthcheck endpoint"""
    return jsonify({
        "status": "UP",
        "service": "flask-app"
    }), 200

@app.route('/description', methods=['GET'])
def message():
    return "<h1>Description Page</h1><p>The purpose of this website is to help me practice developing and optimizing an entire project using a DevSecOps approach.</p> <p>Specifically: Develop a web microservice, containerize it properly, automate testing, build an automated CI/CD pipeline</p>"

@app.route('/frog', methods=['GET'])
def show_frog():
    return '''<img src="/static/frog.jpg" alt="Frog" width="400"><img src="/static/frog2.jpeg" alt="Frog2" width="400">'''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

