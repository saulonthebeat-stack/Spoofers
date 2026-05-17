"""Weather Dashboard Package."""

__version__ = "1.0.0"
__author__ = "Saul on the Beat Stack"

from .api_client import WeatherAPIClient
from .weather_service import WeatherService

__all__ = ["WeatherAPIClient", "WeatherService"]
