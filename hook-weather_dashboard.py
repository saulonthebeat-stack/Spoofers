"""PyInstaller hook for weather_dashboard package."""

from PyInstaller.utils.hooks import collect_data_files

# Collect all data files from the weather_dashboard package
datas = collect_data_files('weather_dashboard')
