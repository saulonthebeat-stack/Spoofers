#!/bin/bash
# Weather Dashboard - Linux/Mac Installer
# Este script instala todas las dependencias necesarias

echo ""
echo "========================================"
echo "  Weather Dashboard - Instalador"
echo "========================================"
echo ""

# Verificar si Python3 está instalado
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python3 no está instalado"
    echo ""
    echo "Para instalar Python3:"
    echo "  Ubuntu/Debian: sudo apt-get install python3 python3-pip"
    echo "  macOS: brew install python3"
    echo "  Fedora: sudo dnf install python3"
    echo ""
    exit 1
fi

echo "[OK] Python3 encontrado"
python3 --version
echo ""

# Verificar si pip3 está disponible
if ! command -v pip3 &> /dev/null; then
    echo "[ERROR] pip3 no está disponible"
    echo ""
    echo "Para instalar pip3:"
    echo "  Ubuntu/Debian: sudo apt-get install python3-pip"
    echo "  macOS: brew install python3"
    echo "  Fedora: sudo dnf install python3-pip"
    echo ""
    exit 1
fi

echo "[OK] pip3 disponible"
echo ""

# Crear entorno virtual
if [ ! -d "venv" ]; then
    echo "Creando entorno virtual..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "[ERROR] Error al crear entorno virtual"
        exit 1
    fi
    echo "[OK] Entorno virtual creado"
else
    echo "[OK] Entorno virtual ya existe"
fi

echo ""
echo "Activando entorno virtual..."
source venv/bin/activate

echo "[OK] Entorno virtual activado"
echo ""

# Crear archivo .env si no existe
if [ ! -f ".env" ]; then
    echo "Creando archivo .env..."
    if [ -f ".env.example" ]; then
        cp .env.example .env
        echo "[OK] Archivo .env creado"
    fi
fi

echo ""
echo "Instalando dependencias..."
pip install flask requests python-dotenv pytest pytest-cov -q

if [ $? -ne 0 ]; then
    echo "[ERROR] Error al instalar dependencias"
    deactivate
    exit 1
fi

echo "[OK] Dependencias instaladas"
echo ""

echo "========================================"
echo "  ¡Instalación Completa!"
echo "========================================"
echo ""
echo "Pasos siguientes:"
echo ""
echo "1. Edita el archivo .env con tu API key:"
echo "   - Abre: .env"
echo "   - Añade tu API key de OpenWeatherMap"
echo "   - Obtén la clave gratis en: https://openweathermap.org/api"
echo ""
echo "2. Para ejecutar la aplicación:"
echo "   - Ejecuta: ./run.sh"
echo ""
echo "3. Abre tu navegador en:"
echo "   http://localhost:5000"
echo ""
