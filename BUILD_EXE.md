# Weather Dashboard - Compilador de Ejecutables

Este documento proporciona instrucciones detalladas para crear ejecutables (.exe, app, bin) para diferentes plataformas.

## 📦 Requisitos Previos

### Todos los Sistemas
- Python 3.8+
- pip (gestor de paquetes de Python)
- 500 MB espacio en disco

### Windows
- Windows 7 o superior
- Visual C++ Redistributable (opcional)

### macOS
- macOS 10.12 o superior
- Xcode Command Line Tools (opcional)

### Linux
- Ubuntu 18.04+, Debian 10+, Fedora 30+, etc.
- build-essential (gcc, make)

---

## 🪟 **Windows - Crear .EXE**

### Opción 1: Script Automático (Recomendado)

```batch
# 1. Abre cmd en la carpeta del proyecto
# 2. Ejecuta:
build-exe-windows.bat

# 3. El .exe se creará en: dist/Weather Dashboard.exe
```

### Opción 2: Instalación Manual

```batch
# 1. Instala PyInstaller
pip install pyinstaller

# 2. Navega a la carpeta del proyecto
cd Spoofers

# 3. Crea el ejecutable
pyinstaller --onefile --windowed ^^
    --name="Weather Dashboard" ^^
    --add-data "templates:templates" ^^
    --add-data "static:static" ^^
    --add-data ".env.example:." ^^
    weather_app.py

# 4. El .exe está en: dist/Weather Dashboard.exe
```

### Opción 3: Con Icono Personalizado

```batch
pyinstaller --onefile --windowed ^^
    --icon=weather_dashboard/icon.ico ^^
    --name="Weather Dashboard" ^^
    --add-data "templates:templates" ^^
    --add-data "static:static" ^^
    weather_app.py
```

---

## 🐧 **Linux - Crear Ejecutable**

### Opción 1: Script Automático (Recomendado)

```bash
# 1. Dale permisos al script
chmod +x build-exe-linux-mac.sh

# 2. Ejecuta:
./build-exe-linux-mac.sh

# 3. El ejecutable estará en: dist/Weather\ Dashboard
```

### Opción 2: Instalación Manual

```bash
# 1. Instala dependencias
sudo apt-get install python3-dev
pip install pyinstaller

# 2. Crea el ejecutable
pyinstaller --onefile \
    --name="Weather Dashboard" \
    --add-data "templates:templates" \
    --add-data "static:static" \
    weather_app.py

# 3. Ejecutable en: dist/Weather\ Dashboard
```

---

## 🍎 **macOS - Crear Ejecutable**

### Opción 1: Script Automático (Recomendado)

```bash
# 1. Dale permisos
chmod +x build-exe-linux-mac.sh

# 2. Ejecuta:
./build-exe-linux-mac.sh

# 3. Ejecutable en: dist/Weather Dashboard
```

### Opción 2: Crear App Bundle (.app)

```bash
# 1. Instala PyInstaller
pip install pyinstaller

# 2. Crea el bundle
pyinstaller --onefile --windowed \
    --name="Weather Dashboard" \
    --add-data "templates:templates" \
    --add-data "static:static" \
    --osx-bundle-identifier com.weatherdashboard.app \
    weather_app.py

# 3. App en: dist/Weather Dashboard.app
```

### Opción 3: Crear DMG (Instalador macOS)

```bash
# 1. Instala create-dmg
brew install create-dmg

# 2. Crea el ejecutable primero
pyinstaller --onefile --windowed \
    --name="Weather Dashboard" \
    --add-data "templates:templates" \
    --add-data "static:static" \
    weather_app.py

# 3. Crea el DMG
create-dmg \
    --volname "Weather Dashboard" \
    --window-pos 200 120 \
    --window-size 800 400 \
    --icon-size 100 \
    --icon "Weather Dashboard.app" 200 190 \
    "dist/Weather Dashboard.dmg" \
    "dist/Weather Dashboard.app/"
```

---

## 📦 **Compilación Avanzada**

### Incluir Archivos Adicionales

```bash
pyinstaller --onefile \
    --add-data "templates:templates" \
    --add-data "static:static" \
    --add-data "data:data" \
    --add-data ".env.example:." \
    weather_app.py
```

### Ocultar Ventana de Consola (Windows)

```batch
pyinstaller --onefile --windowed weather_app.py
```

### Comprimir Ejecutable

```bash
# Instala UPX
sudo apt-get install upx  # Linux
brew install upx          # macOS
choco install upx         # Windows

# Usa UPX con PyInstaller
pyinstaller --onefile --upx-dir=/path/to/upx weather_app.py
```

---

## 🔧 **Solución de Problemas**

### Error: "Python not found"
```bash
# Windows
# Asegúrate de instalar Python con "Add Python to PATH"
# O especifica la ruta completa:
C:\Users\YourName\AppData\Local\Programs\Python\Python310\python.exe -m PyInstaller --onefile weather_app.py
```

### Error: "No module named flask"
```bash
pip install flask requests python-dotenv
pyinstaller --onefile weather_app.py
```

### El ejecutable se abre pero no funciona
```bash
# Asegúrate de ejecutarlo desde la carpeta correcta
# O usa --add-data para incluir archivos necesarios
```

### Ejecutable muy grande (>100MB)
```bash
# Usa UPX para comprimir
pyinstaller --onefile --upx-dir=/path/to/upx weather_app.py

# O elimina archivos no necesarios
pyinstaller --onefile --exclude-module=numpy weather_app.py
```

---

## 📊 **Tamaño de Ejecutables Típicos**

| Sistema | Sin Comprimir | Con UPX |
|---------|---------------|----------|
| Windows | 60-100 MB | 20-30 MB |
| Linux | 50-80 MB | 15-25 MB |
| macOS | 55-90 MB | 18-28 MB |

---

## 🚀 **Distribución**

### 1. Crear Instalador Windows (.MSI)

```bash
# Instala WiX Toolset desde: https://wixtoolset.org/

# O usa NSIS:
choco install nsis

# Crear script NSIS (weather-installer.nsi)
# Y compilar con:
makensis weather-installer.nsi
```

### 2. Crear Instalador Linux (.deb, .rpm)

```bash
# Para .deb (Debian/Ubuntu)
checkinstall

# Para .rpm (Fedora/RHEL)
alien -r dist/weather-dashboard.deb
```

### 3. Crear Ejecutable para GitHub Releases

```bash
# 1. Crea el ejecutable
pyinstaller --onefile weather_app.py

# 2. Comprime
zip -r Weather-Dashboard-Windows.zip dist/weather_app.exe
zip -r Weather-Dashboard-Linux.zip dist/weather_app
zip -r Weather-Dashboard-Mac.zip dist/weather_app

# 3. Sube a GitHub Releases
```

---

## ✨ **Próximas Mejoras**

- [ ] Instalador MSI para Windows
- [ ] Instalador .deb para Linux
- [ ] App Bundle para macOS
- [ ] Firma digital de ejecutables
- [ ] Auto-update
- [ ] Icono personalizado

---

## 📝 **Comandos Útiles**

```bash
# Ver información de PyInstaller
pyinstaller --help

# Analizar dependencias
pyinstaller --collect-all=flask weather_app.py

# Crear spec file para personalización
pyi-makespec --onefile weather_app.py

# Usar spec file existente
pyinstaller weather_app.spec
```

---

## 🎯 **Checklist Antes de Distribuir**

- [ ] Prueba el ejecutable en máquina limpia
- [ ] Verifica que se incluyan todos los archivos necesarios
- [ ] Comprueba que el .env funcione correctamente
- [ ] Prueba en diferentes versiones del SO
- [ ] Verifica la API key de OpenWeatherMap
- [ ] Crea un instalador profesional
- [ ] Incluye instrucciones claras
- [ ] Sube a GitHub Releases

---

**¡Tu Weather Dashboard está listo para distribuir! 🎉**
