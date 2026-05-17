#!/bin/bash
# Weather Dashboard macOS/Linux Executable Builder
# Este script crea un ejecutable para Linux y macOS

echo ""
echo "========================================"
echo "  Weather Dashboard - Compilador EXE"
echo "========================================"
echo ""

# Verificar si Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python3 no está instalado"
    echo "Instala Python desde: https://www.python.org/downloads/"
    exit 1
fi

echo "[OK] Python3 encontrado"
echo ""

# Crear entorno virtual
if [ ! -d "venv" ]; then
    echo "Creando entorno virtual..."
    python3 -m venv venv
fi

echo "Activando entorno virtual..."
source venv/bin/activate

echo "[OK] Entorno virtual activado"
echo ""

# Instalar dependencias
echo "Instalando dependencias..."
pip install pyinstaller flask requests python-dotenv -q

if [ $? -ne 0 ]; then
    echo "[ERROR] Error al instalar dependencias"
    exit 1
fi

echo "[OK] Dependencias instaladas"
echo ""

# Crear carpeta de distribución
mkdir -p dist build

echo "Creando ejecutable..."
echo ""

# Ejecutar PyInstaller
pyinstaller --onefile \
    --windowed \
    --name="Weather Dashboard" \
    --add-data "templates:templates" \
    --add-data "static:static" \
    --add-data ".env.example:." \
    --distpath="dist" \
    --buildpath="build" \
    weather_app.py

if [ $? -ne 0 ]; then
    echo "[ERROR] Error al crear el ejecutable"
    exit 1
fi

echo ""
echo "[OK] ¡Ejecutable creado exitosamente!"
echo ""
echo "Ubicación: dist/Weather Dashboard"
echo ""
echo "Para ejecutar:"
echo "  ./dist/Weather\ Dashboard"
echo ""

deactivate
