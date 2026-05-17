"""Weather service with caching."""

import logging
from typing import Dict, List, Optional
from datetime import datetime, timedelta
from .api_client import WeatherAPIClient

logger = logging.getLogger(__name__)


class WeatherService:
    """Service for weather data management with caching."""

    def __init__(self, api_key: str = None, cache_timeout: int = 600):
        """Initialize the weather service.
        
        Args:
            api_key: OpenWeatherMap API key
            cache_timeout: Cache timeout in seconds
        """
        self.client = WeatherAPIClient(api_key)
        self.cache = {}
        self.cache_timeout = cache_timeout

    def get_current_weather(self, city: str) -> Optional[Dict]:
        """Get current weather for a city with caching.
        
        Args:
            city: City name
            
        Returns:
            Parsed weather data
        """
        # Check cache
        if city in self.cache:
            cached_data, timestamp = self.cache[city]
            if datetime.now() - timestamp < timedelta(seconds=self.cache_timeout):
                logger.info(f"Cache hit for {city}")
                return cached_data

        # Fetch from API
        raw_data = self.client.get_current_weather(city)
        if raw_data:
            parsed_data = self.client.parse_weather_data(raw_data)
            # Cache the result
            self.cache[city] = (parsed_data, datetime.now())
            return parsed_data

        return None

    def get_forecast(self, city: str) -> Optional[Dict]:
        """Get weather forecast for a city.
        
        Args:
            city: City name
            
        Returns:
            Forecast data
        """
        forecast_data = self.client.get_forecast(city)
        if forecast_data:
            return self._parse_forecast(forecast_data)
        return None

    def _parse_forecast(self, data: Dict) -> Dict:
        """Parse forecast data.
        
        Args:
            data: Raw forecast data
            
        Returns:
            Parsed forecast data
        """
        forecasts = []
        for item in data.get('list', []):
            forecasts.append({
                'dt': datetime.fromtimestamp(item.get('dt')),
                'temp': item.get('main', {}).get('temp'),
                'weather': item.get('weather', [{}])[0].get('main'),
                'humidity': item.get('main', {}).get('humidity'),
                'wind_speed': item.get('wind', {}).get('speed'),
                'clouds': item.get('clouds', {}).get('all'),
                'rain': item.get('rain', {}).get('3h', 0),
            })
        return {
            'city': data.get('city', {}).get('name'),
            'country': data.get('city', {}).get('country'),
            'forecasts': forecasts,
        }

    def get_multiple_cities(self, cities: List[str]) -> Dict[str, Dict]:
        """Get weather for multiple cities.
        
        Args:
            cities: List of city names
            
        Returns:
            Dictionary with weather data for each city
        """
        results = {}
        for city in cities:
            weather = self.get_current_weather(city)
            if weather:
                results[city] = weather
        return results

    def clear_cache(self):
        """Clear the cache."""
        self.cache.clear()
        logger.info("Cache cleared")

    def get_cache_info(self) -> Dict:
        """Get cache information.
        
        Returns:
            Cache info dictionary
        """
        return {
            'size': len(self.cache),
            'cities': list(self.cache.keys()),
        }
