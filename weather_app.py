#!/usr/bin/env python
"""Weather Dashboard Flask Application."""

import logging
from flask import Flask, render_template, jsonify, request
from weather_dashboard.weather_service import WeatherService
from weather_dashboard.config import DEFAULT_CITIES, HOST, PORT, DEBUG

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
app.config['DEBUG'] = DEBUG

# Initialize weather service
weather_service = WeatherService()


@app.route('/')
def index():
    """Render the main dashboard."""
    try:
        weather_data = weather_service.get_multiple_cities(DEFAULT_CITIES)
        return render_template('index.html', weather_data=weather_data)
    except Exception as e:
        logger.error(f"Error in index route: {e}")
        return render_template('error.html', error=str(e)), 500


@app.route('/api/weather/<city>')
def get_weather(city):
    """API endpoint to get weather for a specific city."""
    try:
        weather = weather_service.get_current_weather(city)
        if weather:
            return jsonify(weather)
        return jsonify({'error': f'Weather data not found for {city}'}), 404
    except Exception as e:
        logger.error(f"Error fetching weather: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/forecast/<city>')
def get_forecast(city):
    """API endpoint to get forecast for a specific city."""
    try:
        forecast = weather_service.get_forecast(city)
        if forecast:
            return jsonify(forecast)
        return jsonify({'error': f'Forecast not found for {city}'}), 404
    except Exception as e:
        logger.error(f"Error fetching forecast: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/weather')
def get_multiple_weather():
    """API endpoint to get weather for multiple cities."""
    try:
        cities = request.args.get('cities', ','.join(DEFAULT_CITIES)).split(',')
        weather_data = weather_service.get_multiple_cities(cities)
        return jsonify(weather_data)
    except Exception as e:
        logger.error(f"Error fetching multiple weather: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/cache/info')
def cache_info():
    """Get cache information."""
    try:
        return jsonify(weather_service.get_cache_info())
    except Exception as e:
        logger.error(f"Error getting cache info: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/cache/clear', methods=['POST'])
def clear_cache():
    """Clear the cache."""
    try:
        weather_service.clear_cache()
        return jsonify({'message': 'Cache cleared successfully'})
    except Exception as e:
        logger.error(f"Error clearing cache: {e}")
        return jsonify({'error': str(e)}), 500


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    logger.info(f"Starting Weather Dashboard on {HOST}:{PORT}")
    app.run(host=HOST, port=PORT, debug=DEBUG)
