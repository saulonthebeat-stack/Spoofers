@echo off
REM Weather Dashboard - Windows Batch Installer
REM Este script instala todas las dependencias necesarias

echo.
echo ========================================
echo   Weather Dashboard - Instalador
echo ========================================
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python no está instalado
    echo.
    echo Descarga Python desde:
    echo https://www.python.org/downloads/
    echo.
    echo IMPORTANTE: Durante la instalación marca la opción:
    echo "Add Python to PATH"
    echo.
    pause
    exit /b 1
)

echo [OK] Python encontrado
python --version
echo.

REM Verificar si pip está disponible
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] pip no está disponible
    pause
    exit /b 1
)

echo [OK] pip disponible
echo.

REM Crear entorno virtual
if not exist "venv" (
    echo Creando entorno virtual...
    python -m venv venv
    if %errorlevel% neq 0 (
        echo [ERROR] Error al crear entorno virtual
        pause
        exit /b 1
    )
    echo [OK] Entorno virtual creado
) else (
    echo [OK] Entorno virtual ya existe
)

echo.
echo Activando entorno virtual...
call venv\Scripts\activate.bat

echo [OK] Entorno virtual activado
echo.

REM Crear archivo .env si no existe
if not exist ".env" (
    echo Creando archivo .env...
    if exist ".env.example" (
        copy .env.example .env
        echo [OK] Archivo .env creado
    )
)

echo.
echo Instalando dependencias...
pip install flask requests python-dotenv pytest pytest-cov -q

if %errorlevel% neq 0 (
    echo [ERROR] Error al instalar dependencias
    pause
    exit /b 1
)

echo [OK] Dependencias instaladas
echo.

echo ========================================
echo   ¡Instalación Completa!
echo ========================================
echo.
echo Pasos siguientes:
echo.
echo 1. Edita el archivo .env con tu API key:
echo    - Abre: .env
echo    - Añade tu API key de OpenWeatherMap
echo    - Obtén la clave gratis en: https://openweathermap.org/api
echo.
echo 2. Para ejecutar la aplicación:
echo    - Ejecuta: run.bat
echo.
echo 3. Abre tu navegador en:
echo    http://localhost:5000
echo.
pause
