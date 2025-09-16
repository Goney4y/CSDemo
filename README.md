# CSDemo

A simple "Hello World" Python web application using Flask.

## Features

- Simple HTTP endpoint that returns "Hello World!"
- Health check endpoint for monitoring
- Lightweight Flask-based web server

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

Start the web server:
```bash
python app.py
```

The application will start on `http://localhost:5000`

### Available Endpoints

- `GET /` - Returns "Hello World!" message
- `GET /health` - Returns health status in JSON format

### Testing

Run the test suite:
```bash
python test_app.py
```

## Example Usage

```bash
# Test the main endpoint
curl http://localhost:5000/

# Test the health check
curl http://localhost:5000/health
```