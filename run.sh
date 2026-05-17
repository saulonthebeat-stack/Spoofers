#!/bin/bash
# Weather Dashboard - Linux/Mac Runner
# Este script ejecuta la aplicación

echo ""
echo "========================================"
echo "  Weather Dashboard"
echo "========================================"
echo ""

# Verificar si el entorno virtual existe
if [ ! -d "venv" ]; then
    echo "[ERROR] Entorno virtual no encontrado"
    echo "Ejecuta primero: ./install-linux-mac.sh"
    exit 1
fi

echo "Activando entorno virtual..."
source venv/bin/activate

echo "[OK] Entorno virtual activado"
echo ""

# Verificar si .env existe
if [ ! -f ".env" ]; then
    echo "[ERROR] Archivo .env no encontrado"
    echo ""
    echo "Por favor:"
    echo "1. Copia .env.example a .env"
    echo "2. Edita .env y añade tu API key"
    echo ""
    exit 1
fi

echo "Iniciando Weather Dashboard..."
echo ""
echo "✓ La aplicación está disponible en: http://localhost:5000"
echo "✓ Abre tu navegador y navega a esa dirección"
echo "✓ Presiona Ctrl+C para detener la aplicación"
echo ""

python3 weather_app.py
