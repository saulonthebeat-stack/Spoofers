@echo off
REM HWID Spoofer - Windows Batch Runner
REM Este script ejecuta la aplicación HWID Spoofer

echo.
echo ========================================
echo   HWID Spoofer - Gestor de Series
echo ========================================
echo.

REM Verificar si el entorno virtual existe
if not exist "venv" (
    echo [ADVERTENCIA] Entorno virtual no encontrado
    echo Creando entorno virtual...
    python -m venv venv
)

echo Activando entorno virtual...
call venv\Scripts\activate.bat

echo [OK] Entorno virtual activado
echo.

echo Instalando dependencias...
pip install wmi openpyxl -q

echo [OK] Dependencias instaladas
echo.

echo ========================================
echo   Iniciando HWID Spoofer
echo ========================================
echo.
echo ✓ La aplicación se abrirá en modo interactivo
echo ✓ Selecciona una opción del menú
echo ✓ Presiona Ctrl+C para salir
echo.

python hwid_spoofer_app.py

pause
