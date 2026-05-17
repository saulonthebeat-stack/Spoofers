@echo off
REM Weather Dashboard - Windows Runner
REM Este script ejecuta la aplicación

echo.
echo ========================================
echo   Weather Dashboard
echo ========================================
echo.

REM Verificar si el entorno virtual existe
if not exist "venv" (
    echo [ERROR] Entorno virtual no encontrado
    echo Ejecuta primero: install-windows.bat
    pause
    exit /b 1
)

echo Activando entorno virtual...
call venv\Scripts\activate.bat

echo [OK] Entorno virtual activado
echo.

REM Verificar si .env existe
if not exist ".env" (
    echo [ERROR] Archivo .env no encontrado
    echo.
    echo Por favor:
    echo 1. Copia .env.example a .env
    echo 2. Edita .env y añade tu API key
    echo.
    pause
    exit /b 1
)

echo Iniciando Weather Dashboard...
echo.
echo ✓ La aplicación está disponible en: http://localhost:5000
echo ✓ Abre tu navegador y navega a esa dirección
echo ✓ Presiona Ctrl+C para detener la aplicación
echo.

python weather_app.py

pause
