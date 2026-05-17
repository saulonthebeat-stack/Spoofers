@echo off
REM Weather Dashboard Windows Installer
REM Este script crea un ejecutable (.exe) para Windows

echo.
echo ========================================
echo   Weather Dashboard - Instalador .EXE
echo ========================================
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python no está instalado o no está en PATH
    echo Descarga Python desde: https://www.python.org/downloads/
    echo Asegúrate de marcar "Add Python to PATH" durante la instalación
    pause
    exit /b 1
)

echo [OK] Python encontrado
echo.

REM Verificar si pip está instalado
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] pip no está instalado
    pause
    exit /b 1
)

echo [OK] pip encontrado
echo.

REM Instalar dependencias
echo Instalando dependencias...
pip install pyinstaller flask requests python-dotenv -q

if %errorlevel% neq 0 (
    echo [ERROR] Error al instalar dependencias
    pause
    exit /b 1
)

echo [OK] Dependencias instaladas
echo.

REM Crear carpeta de distribución
if not exist "dist" mkdir dist
if not exist "build" mkdir build

echo Creando ejecutable...
echo.

REM Ejecutar PyInstaller
pyinstaller --onefile ^^
    --windowed ^^
    --icon=weather_dashboard/icon.ico ^^
    --name="Weather Dashboard" ^^
    --add-data "templates:templates" ^^
    --add-data "static:static" ^^
    --add-data ".env.example:." ^^
    --distpath="dist" ^^
    --buildpath="build" ^^
    weather_app.py

if %errorlevel% neq 0 (
    echo [ERROR] Error al crear el ejecutable
    pause
    exit /b 1
)

echo.
echo [OK] ¡Ejecutable creado exitosamente!
echo.
echo Ubicación: dist/Weather Dashboard.exe
echo.
echo El instalador se encuentra en la carpeta 'dist'
echo.
pause
