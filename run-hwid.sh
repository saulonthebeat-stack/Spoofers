#!/bin/bash
# HWID Spoofer - Linux/Mac Runner
# Este script ejecuta la aplicación HWID Spoofer

echo ""
echo "========================================"
echo "  HWID Spoofer - Gestor de Series"
echo "========================================"
echo ""

# Verificar si el entorno virtual existe
if [ ! -d "venv" ]; then
    echo "[ADVERTENCIA] Entorno virtual no encontrado"
    echo "Creando entorno virtual..."
    python3 -m venv venv
fi

echo "Activando entorno virtual..."
source venv/bin/activate

echo "[OK] Entorno virtual activado"
echo ""

echo "Instalando dependencias..."
pip install openpyxl -q

echo "[OK] Dependencias instaladas"
echo ""

echo "========================================"
echo "  Iniciando HWID Spoofer"
echo "========================================"
echo ""
echo "✓ La aplicación se abrirá en modo interactivo"
echo "✓ Selecciona una opción del menú"
echo "✓ Presiona Ctrl+C para salir"
echo ""

python3 hwid_spoofer_app.py
