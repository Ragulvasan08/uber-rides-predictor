import numpy as np
from flask import Flask, render_template, request, jsonify, flash
import math
import pickle
import logging
import os
from werkzeug.exceptions import HTTPException
import traceback

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-change-this-in-production')

# Global variable for model
model = None

def load_model():
    """Load the ML model safely"""
    global model
    try:
        model_path = 'model.pkl'
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found: {model_path}")
        
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        logger.info("Model loaded successfully")
        return True
    except Exception as e:
        logger.error(f"Error loading model: {str(e)}")
        return False

def validate_input(data):
    """Validate input data"""
    required_fields = ['Priceperweek', 'Population', 'Monthlyincome', 'Averageparkingpermonth']
    errors = []
    
    for field in required_fields:
        if field not in data or not data[field]:
            errors.append(f"{field} is required")
            continue
            
        try:
            value = float(data[field])
            if value < 0:
                errors.append(f"{field} must be positive")
        except ValueError:
            errors.append(f"{field} must be a valid number")
    
    return errors

@app.route('/')
def home():
    """Home page route"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Prediction endpoint with improved error handling"""
    try:
        # Validate model is loaded
        if model is None:
            if not load_model():
                return render_template('index.html', 
                                     error="Model not available. Please try again later.")
        
        # Get form data
        form_data = request.form.to_dict()
        
        # Validate input
        validation_errors = validate_input(form_data)
        if validation_errors:
            return render_template('index.html', 
                                 error="Please fix the following errors: " + ", ".join(validation_errors))
        
        # Convert inputs to float
        try:
            int_features = [float(form_data['Priceperweek']),
                          float(form_data['Population']),
                          float(form_data['Monthlyincome']),
                          float(form_data['Averageparkingpermonth'])]
        except ValueError as e:
            return render_template('index.html', 
                                 error="Invalid input values. Please check your inputs.")
        
        # Make prediction
        final_features = np.array([int_features]).reshape(1, -1)
        prediction = model.predict(final_features)
        output = round(prediction[0], 2)
        
        # Format the result
        result = f"Number of weekly rides will be {math.floor(output)}"
        
        logger.info(f"Prediction successful: {result}")
        return render_template('index.html', prediction_text=result)
        
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        logger.error(traceback.format_exc())
        return render_template('index.html', 
                             error="An error occurred during prediction. Please try again.")

@app.route('/api/predict', methods=['POST'])
def api_predict():
    """API endpoint for predictions"""
    try:
        if model is None:
            if not load_model():
                return jsonify({'error': 'Model not available'}), 503
        
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        validation_errors = validate_input(data)
        if validation_errors:
            return jsonify({'error': validation_errors}), 400
        
        int_features = [float(data['Priceperweek']),
                       float(data['Population']),
                       float(data['Monthlyincome']),
                       float(data['Averageparkingpermonth'])]
        
        final_features = np.array([int_features]).reshape(1, -1)
        prediction = model.predict(final_features)
        output = round(prediction[0], 2)
        
        return jsonify({
            'prediction': math.floor(output),
            'weekly_rides': math.floor(output)
        })
        
    except Exception as e:
        logger.error(f"API prediction error: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('error.html', error="Page not found"), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return render_template('error.html', error="Internal server error"), 500

@app.errorhandler(Exception)
def handle_exception(e):
    """Handle all other exceptions"""
    if isinstance(e, HTTPException):
        return e
    
    logger.error(f"Unhandled exception: {str(e)}")
    return render_template('error.html', error="Something went wrong"), 500

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None
    })

if __name__ == "__main__":
    # Load model on startup
    if load_model():
        logger.info("Application started successfully")
    else:
        logger.error("Failed to load model on startup")
    
    app.run(debug=True, host='0.0.0.0', port=5000)

     