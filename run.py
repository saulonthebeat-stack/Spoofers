#!/usr/bin/env python
"""Simple runner for Weather Dashboard."""

import sys
import os
from pathlib import Path

# Add the current directory to the path
sys.path.insert(0, str(Path(__file__).parent))

if __name__ == "__main__":
    # Check if .env exists, if not create from .env.example
    if not Path(".env").exists():
        if Path(".env.example").exists():
            with open(".env.example", "r") as f:
                content = f.read()
            with open(".env", "w") as f:
                f.write(content)
            print("✓ Archivo .env creado desde .env.example")
            print("✓ Por favor edita .env con tu API key de OpenWeatherMap\n")
        else:
            print("⚠ Falta el archivo .env.example")
    
    # Import and run the Flask app
    from weather_app import app
    
    print("")
    print("="*50)
    print("  Weather Dashboard")
    print("="*50)
    print("")
    print("✓ Iniciando en http://localhost:5000")
    print("✓ Presiona Ctrl+C para detener")
    print("")
    
    app.run(debug=False, host="0.0.0.0", port=5000)
