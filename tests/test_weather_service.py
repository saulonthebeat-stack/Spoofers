"""Tests for the weather service."""

import pytest
from datetime import datetime
from weather_dashboard.weather_service import WeatherService
from weather_dashboard.api_client import WeatherAPIClient


class TestWeatherService:
    """Test cases for WeatherService."""

    @pytest.fixture
    def service(self):
        """Provide a WeatherService instance for testing."""
        return WeatherService(api_key='demo')

    def test_service_initialization(self, service):
        """Test that WeatherService initializes correctly."""
        assert service is not None
        assert service.cache is not None
        assert service.cache_timeout == 600

    def test_clear_cache(self, service):
        """Test cache clearing."""
        service.cache['London'] = ({'temp': 20}, datetime.now())
        assert len(service.cache) == 1
        
        service.clear_cache()
        assert len(service.cache) == 0

    def test_cache_info(self, service):
        """Test getting cache information."""
        service.cache['London'] = ({'temp': 20}, datetime.now())
        service.cache['Paris'] = ({'temp': 18}, datetime.now())
        
        info = service.get_cache_info()
        assert info['size'] == 2
        assert 'London' in info['cities']
        assert 'Paris' in info['cities']


class TestWeatherAPIClient:
    """Test cases for WeatherAPIClient."""

    @pytest.fixture
    def client(self):
        """Provide a WeatherAPIClient instance for testing."""
        return WeatherAPIClient(api_key='demo')

    def test_client_initialization(self, client):
        """Test that WeatherAPIClient initializes correctly."""
        assert client is not None
        assert client.api_key == 'demo'
        assert client.session is not None

    def test_parse_weather_data(self, client):
        """Test parsing weather data."""
        raw_data = {
            'name': 'London',
            'sys': {'country': 'GB', 'sunrise': 1234567890, 'sunset': 1234567900},
            'main': {
                'temp': 20,
                'feels_like': 18,
                'temp_min': 15,
                'temp_max': 25,
                'pressure': 1013,
                'humidity': 60,
            },
            'weather': [{'main': 'Cloudy', 'description': 'partly cloudy', 'icon': '02d'}],
            'wind': {'speed': 5, 'deg': 180},
            'clouds': {'all': 50},
            'visibility': 10000,
            'dt': 1234567890,
        }
        
        parsed = client.parse_weather_data(raw_data)
        
        assert parsed['city'] == 'London'
        assert parsed['country'] == 'GB'
        assert parsed['temperature'] == 20
        assert parsed['humidity'] == 60
        assert parsed['weather'] == 'Cloudy'

    def test_parse_weather_data_empty(self, client):
        """Test parsing empty weather data."""
        parsed = client.parse_weather_data(None)
        assert parsed == {}
        
        parsed = client.parse_weather_data({})
        assert len(parsed) > 0  # Should have default values
