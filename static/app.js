/**
 * Weather Dashboard Frontend Application
 */

const API_BASE = '/api';
let forecastChart = null;

/**
 * Initialize the dashboard
 */
async function init() {
    await refreshAll();
    updateCacheInfo();
}

/**
 * Refresh all weather data
 */
async function refreshAll() {
    const grid = document.getElementById('weatherGrid');
    grid.innerHTML = '<div class="loading">Loading weather data</div>';
    
    try {
        const response = await fetch(`${API_BASE}/weather`);
        const data = await response.json();
        
        grid.innerHTML = '';
        for (const [city, weather] of Object.entries(data)) {
            const card = createWeatherCard(weather);
            grid.appendChild(card);
            
            // Load forecast for the first city
            if (city === Object.keys(data)[0]) {
                await loadForecast(city);
            }
        }
    } catch (error) {
        grid.innerHTML = `<div class="error-message">Error loading weather data: ${error.message}</div>`;
        console.error('Error:', error);
    }
}

/**
 * Create a weather card element
 */
function createWeatherCard(weather) {
    const card = document.createElement('div');
    card.className = 'weather-card';
    card.onclick = () => loadForecast(weather.city);
    
    const iconUrl = `https://openweathermap.org/img/wn/${weather.icon}@4x.png`;
    const tempC = Math.round(weather.temperature);
    const feelsLikeC = Math.round(weather.feels_like);
    
    card.innerHTML = `
        <div class="city-name">${weather.city}, ${weather.country}</div>
        <img src="${iconUrl}" alt="${weather.description}" class="weather-icon" style="width: 120px; height: 120px;">
        <div class="temperature">${tempC}°C</div>
        <div class="weather-description">${weather.description}</div>
        
        <div class="weather-details">
            <div class="detail-item">
                <span class="detail-label">Feels Like</span>
                <span class="detail-value">${feelsLikeC}°C</span>
            </div>
            <div class="detail-item">
                <span class="detail-label">Humidity</span>
                <span class="detail-value">${weather.humidity}%</span>
            </div>
            <div class="detail-item">
                <span class="detail-label">Wind Speed</span>
                <span class="detail-value">${weather.wind_speed} m/s</span>
            </div>
            <div class="detail-item">
                <span class="detail-label">Pressure</span>
                <span class="detail-value">${weather.pressure} hPa</span>
            </div>
            <div class="detail-item">
                <span class="detail-label">Visibility</span>
                <span class="detail-value">${(weather.visibility / 1000).toFixed(1)} km</span>
            </div>
            <div class="detail-item">
                <span class="detail-label">Clouds</span>
                <span class="detail-value">${weather.clouds}%</span>
            </div>
        </div>
    `;
    
    return card;
}

/**
 * Load and display forecast for a city
 */
async function loadForecast(city) {
    try {
        const response = await fetch(`${API_BASE}/forecast/${city}`);
        const data = await response.json();
        
        if (data.forecasts) {
            displayForecastChart(data.forecasts);
        }
    } catch (error) {
        console.error('Error loading forecast:', error);
    }
}

/**
 * Display forecast data in a chart
 */
function displayForecastChart(forecasts) {
    const ctx = document.getElementById('forecastChart');
    
    if (!ctx) return;
    
    // Prepare data
    const labels = forecasts.map(f => new Date(f.dt).toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' }));
    const temps = forecasts.map(f => f.temp);
    const humidity = forecasts.map(f => f.humidity);
    const windSpeed = forecasts.map(f => f.wind_speed);
    
    // Destroy existing chart if it exists
    if (forecastChart) {
        forecastChart.destroy();
    }
    
    // Create new chart
    forecastChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [
                {
                    label: 'Temperature (°C)',
                    data: temps,
                    borderColor: '#ff6600',
                    backgroundColor: 'rgba(255, 102, 0, 0.1)',
                    tension: 0.4,
                    yAxisID: 'y',
                },
                {
                    label: 'Humidity (%)',
                    data: humidity,
                    borderColor: '#0066cc',
                    backgroundColor: 'rgba(0, 102, 204, 0.1)',
                    tension: 0.4,
                    yAxisID: 'y1',
                },
                {
                    label: 'Wind Speed (m/s)',
                    data: windSpeed,
                    borderColor: '#00cc66',
                    backgroundColor: 'rgba(0, 204, 102, 0.1)',
                    tension: 0.4,
                    yAxisID: 'y2',
                },
            ],
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            interaction: {
                mode: 'index',
                intersect: false,
            },
            scales: {
                y: {
                    type: 'linear',
                    display: true,
                    position: 'left',
                    title: {
                        display: true,
                        text: 'Temperature (°C)',
                    },
                },
                y1: {
                    type: 'linear',
                    display: true,
                    position: 'center',
                    title: {
                        display: true,
                        text: 'Humidity (%)',
                    },
                },
                y2: {
                    type: 'linear',
                    display: true,
                    position: 'right',
                    title: {
                        display: true,
                        text: 'Wind Speed (m/s)',
                    },
                    grid: {
                        drawOnChartArea: false,
                    },
                },
            },
        },
    });
}

/**
 * Search for a specific city
 */
async function searchCity() {
    const input = document.getElementById('cityInput');
    const city = input.value.trim();
    
    if (!city) {
        alert('Please enter a city name');
        return;
    }
    
    const grid = document.getElementById('weatherGrid');
    grid.innerHTML = '<div class="loading">Searching</div>';
    
    try {
        const response = await fetch(`${API_BASE}/weather/${city}`);
        const data = await response.json();
        
        if (data.error) {
            grid.innerHTML = `<div class="error-message">Error: ${data.error}</div>`;
            return;
        }
        
        grid.innerHTML = '';
        const card = createWeatherCard(data);
        grid.appendChild(card);
        
        // Load forecast
        await loadForecast(city);
        
        // Update cache info
        updateCacheInfo();
        
        // Clear input
        input.value = '';
    } catch (error) {
        grid.innerHTML = `<div class="error-message">Error: ${error.message}</div>`;
        console.error('Error:', error);
    }
}

/**
 * Clear the cache
 */
async function clearCache() {
    if (!confirm('Are you sure you want to clear the cache?')) {
        return;
    }
    
    try {
        const response = await fetch(`${API_BASE}/cache/clear`, { method: 'POST' });
        const data = await response.json();
        
        alert(data.message || 'Cache cleared');
        await refreshAll();
    } catch (error) {
        alert(`Error clearing cache: ${error.message}`);
        console.error('Error:', error);
    }
}

/**
 * Update cache information
 */
async function updateCacheInfo() {
    try {
        const response = await fetch(`${API_BASE}/cache/info`);
        const data = await response.json();
        
        const cacheInfo = document.getElementById('cacheInfo');
        if (cacheInfo) {
            cacheInfo.textContent = `Cache: ${data.size} cities`;
        }
    } catch (error) {
        console.error('Error updating cache info:', error);
    }
}

/**
 * Allow searching by pressing Enter
 */
document.addEventListener('DOMContentLoaded', () => {
    const cityInput = document.getElementById('cityInput');
    if (cityInput) {
        cityInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                searchCity();
            }
        });
    }
    
    // Initialize the dashboard
    init();
});
