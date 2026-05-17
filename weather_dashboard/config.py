"""Configuration for Weather Dashboard."""

import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY', 'demo')
OPENWEATHER_BASE_URL = 'https://api.openweathermap.org/data/2.5'
WEATHER_FORECAST_URL = f'{OPENWEATHER_BASE_URL}/forecast'
WEATHER_CURRENT_URL = f'{OPENWEATHER_BASE_URL}/weather'

# App Configuration
DEBUG = os.getenv('DEBUG', 'False') == 'True'
PORT = int(os.getenv('PORT', 5000))
HOST = os.getenv('HOST', '0.0.0.0')

# Cache Configuration
CACHE_TIMEOUT = 600  # 10 minutes

# Default Cities
DEFAULT_CITIES = ['London', 'New York', 'Tokyo', 'Sydney', 'Paris']

# Units
UNITS = 'metric'  # Celsius
LANG = 'en'
