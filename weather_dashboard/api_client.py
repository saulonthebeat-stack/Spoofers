"""Weather API client for OpenWeatherMap."""

import logging
import requests
from typing import Dict, Optional, List
from datetime import datetime
from .config import (
    OPENWEATHER_API_KEY,
    WEATHER_CURRENT_URL,
    WEATHER_FORECAST_URL,
    UNITS,
    LANG,
)

logger = logging.getLogger(__name__)


class WeatherAPIClient:
    """Client for OpenWeatherMap API."""

    def __init__(self, api_key: str = OPENWEATHER_API_KEY):
        """Initialize the API client."""
        self.api_key = api_key
        self.session = requests.Session()
        self.session.timeout = 10

    def get_current_weather(self, city: str) -> Optional[Dict]:
        """Fetch current weather for a city.
        
        Args:
            city: City name
            
        Returns:
            Weather data dictionary or None if request fails
        """
        try:
            params = {
                'q': city,
                'appid': self.api_key,
                'units': UNITS,
                'lang': LANG,
            }
            response = self.session.get(WEATHER_CURRENT_URL, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Error fetching weather for {city}: {e}")
            return None

    def get_forecast(self, city: str, days: int = 5) -> Optional[Dict]:
        """Fetch weather forecast for a city.
        
        Args:
            city: City name
            days: Number of days to forecast (default: 5)
            
        Returns:
            Forecast data dictionary or None if request fails
        """
        try:
            params = {
                'q': city,
                'appid': self.api_key,
                'units': UNITS,
                'lang': LANG,
                'cnt': days * 8,  # 8 forecasts per day (3-hour intervals)
            }
            response = self.session.get(WEATHER_FORECAST_URL, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Error fetching forecast for {city}: {e}")
            return None

    def get_multiple_cities(self, cities: List[str]) -> Dict[str, Dict]:
        """Fetch weather for multiple cities.
        
        Args:
            cities: List of city names
            
        Returns:
            Dictionary with city data
        """
        results = {}
        for city in cities:
            weather = self.get_current_weather(city)
            if weather:
                results[city] = weather
        return results

    def parse_weather_data(self, data: Dict) -> Dict:
        """Parse weather data into readable format.
        
        Args:
            data: Raw weather data from API
            
        Returns:
            Parsed weather data
        """
        if not data:
            return {}

        return {
            'city': data.get('name', 'Unknown'),
            'country': data.get('sys', {}).get('country', ''),
            'temperature': data.get('main', {}).get('temp'),
            'feels_like': data.get('main', {}).get('feels_like'),
            'temp_min': data.get('main', {}).get('temp_min'),
            'temp_max': data.get('main', {}).get('temp_max'),
            'pressure': data.get('main', {}).get('pressure'),
            'humidity': data.get('main', {}).get('humidity'),
            'weather': data.get('weather', [{}])[0].get('main', 'Unknown'),
            'description': data.get('weather', [{}])[0].get('description', ''),
            'icon': data.get('weather', [{}])[0].get('icon', '01d'),
            'wind_speed': data.get('wind', {}).get('speed'),
            'wind_deg': data.get('wind', {}).get('deg'),
            'clouds': data.get('clouds', {}).get('all'),
            'visibility': data.get('visibility'),
            'sunrise': datetime.fromtimestamp(data.get('sys', {}).get('sunrise', 0)),
            'sunset': datetime.fromtimestamp(data.get('sys', {}).get('sunset', 0)),
            'timestamp': datetime.fromtimestamp(data.get('dt', 0)),
        }

    def close(self):
        """Close the session."""
        self.session.close()
