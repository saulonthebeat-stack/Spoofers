# Weather Dashboard 🌤️

A modern, real-time weather dashboard application that fetches weather data from OpenWeatherMap API.

## Features

✨ **Real-time Weather Data**
- Current weather information for multiple cities
- Temperature, humidity, wind speed, and more
- Weather icons and descriptions

📊 **Interactive Charts**
- 5-day forecast visualization
- Temperature trends
- Humidity and wind speed charts
- Interactive Chart.js integration

🔍 **Search Functionality**
- Search for any city in the world
- Quick access to weather information
- Support for multiple cities

💾 **Smart Caching**
- Reduces API calls
- Improves performance
- Configurable cache timeout
- Cache management endpoints

🎨 **Modern UI**
- Responsive design
- Beautiful gradient backgrounds
- Smooth animations
- Mobile-friendly interface

## Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/saulonthebeat-stack/Spoofers.git
   cd Spoofers
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API Key**
   - Copy `.env.example` to `.env`
   - Get your API key from [OpenWeatherMap](https://openweathermap.org/api)
   - Add your API key to `.env`:
   ```
   OPENWEATHER_API_KEY=your_api_key_here
   ```

5. **Run the application**
   ```bash
   python weather_app.py
   ```
   
   The dashboard will be available at `http://localhost:5000`

## Usage

### Web Dashboard

1. **View Weather**: The dashboard loads weather for default cities on startup
2. **Search**: Use the search bar to find weather for any city
3. **Forecast**: Click on a city card to view its 5-day forecast
4. **Refresh**: Click the refresh button to update all data
5. **Cache**: Manage cache with the cache management buttons

### API Endpoints

#### Get Current Weather
```bash
GET /api/weather/<city>
```

Example:
```bash
curl http://localhost:5000/api/weather/London
```

Response:
```json
{
  "city": "London",
  "country": "GB",
  "temperature": 20,
  "humidity": 60,
  "weather": "Cloudy",
  "wind_speed": 5
}
```

#### Get Forecast
```bash
GET /api/forecast/<city>
```

#### Get Multiple Cities
```bash
GET /api/weather?cities=London,Paris,New York
```

#### Cache Information
```bash
GET /api/cache/info
```

#### Clear Cache
```bash
POST /api/cache/clear
```

## Project Structure

```
Spoofers/
├── weather_dashboard/
│   ├── __init__.py
│   ├── config.py              # Configuration settings
│   ├── api_client.py          # OpenWeatherMap API client
│   └── weather_service.py     # Weather service with caching
├── templates/
│   ├── index.html             # Main dashboard
│   └── error.html             # Error page
├── static/
│   ├── style.css              # Styling
│   └── app.js                 # Frontend JavaScript
├── tests/
│   └── test_weather_service.py# Unit tests
├── weather_app.py             # Flask application
├── .env.example               # Environment variables template
└── requirements.txt           # Python dependencies
```

## Configuration

Edit `.env` file to customize:

```
# OpenWeatherMap API Configuration
OPENWEATHER_API_KEY=your_api_key_here

# Application Configuration
DEBUG=False
PORT=5000
HOST=0.0.0.0
```

## Testing

Run tests with pytest:

```bash
pytest

# With coverage
pytest --cov=weather_dashboard

# Verbose output
pytest -v
```

## Code Quality

Format and lint code:

```bash
# Format with black
black .

# Lint with flake8
flake8 .

# Sort imports with isort
isort .
```

## Technologies Used

- **Backend**: Flask, Python
- **Frontend**: HTML, CSS, JavaScript
- **Charts**: Chart.js
- **API**: OpenWeatherMap
- **Testing**: pytest
- **Code Quality**: black, flake8, isort

## API Key

Get your free API key from [OpenWeatherMap](https://openweathermap.org/api):

1. Visit https://openweathermap.org/api
2. Sign up for a free account
3. Go to API Keys section
4. Copy your API key
5. Add it to your `.env` file

## Troubleshooting

### "API key not found"
- Ensure you have created `.env` file from `.env.example`
- Add your OpenWeatherMap API key to `.env`

### "City not found"
- Make sure the city name is spelled correctly
- Try searching with country code (e.g., "London, GB")

### "Connection error"
- Check your internet connection
- Verify OpenWeatherMap API is accessible
- Check API rate limits

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](../CONTRIBUTING.md)

## License

MIT License - See [LICENSE](../LICENSE) for details

## Support

For issues and questions:
- Open an [issue](https://github.com/saulonthebeat-stack/Spoofers/issues)
- Check [documentation](https://openweathermap.org/api)

---

**Made with ❤️ for weather enthusiasts**
