import os
from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# Initialize metrics retrievals and /metrics endpoint
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Application metadata', version='1.0.0')

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

@app.route('/frog', methods=['GET'])
def show_frog():
    return '''<img src="/static/frog.jpg" alt="Frog" width="400"><img src="/static/frog2.jpeg" alt="Frog2" width="400">'''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

