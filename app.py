#!/usr/bin/env python3
"""
A simple "Hello World" Python web application using Flask.
"""

from flask import Flask

# Create Flask application instance
app = Flask(__name__)


@app.route('/')
def hello_world():
    """Return a simple Hello World message."""
    return 'Hello World!'


@app.route('/health')
def health_check():
    """Simple health check endpoint."""
    return {'status': 'healthy', 'message': 'Hello World App is running'}


if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True, host='0.0.0.0', port=5000)