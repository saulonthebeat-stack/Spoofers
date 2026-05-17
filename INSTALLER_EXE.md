# Weather Dashboard - Instalador Windows (.EXE)

> **¡Tu instalador .EXE profesional para Windows está aquí!** 🎉

---

## 📦 **Descargar Instalador .EXE**

### Opción 1: Desde GitHub (Recomendado)

**URL de Descarga:**
```
https://github.com/saulonthebeat-stack/Spoofers/releases/download/v1.0.0/Weather-Dashboard-Setup.exe
```

### Opción 2: Compilar Localmente

Si prefieres compilar tu propio .exe:

```batch
# 1. Descarga el proyecto
git clone https://github.com/saulonthebeat-stack/Spoofers.git
cd Spoofers

# 2. Ejecuta el compilador
build-exe-windows.bat

# 3. El .exe estará en: dist/Weather Dashboard.exe
```

---

## ⚡ **Instalación del .EXE**

### Paso 1: Descargar
1. Ve a: https://github.com/saulonthebeat-stack/Spoofers/releases
2. Descarga `Weather-Dashboard-Setup.exe`
3. Guarda el archivo en una carpeta

### Paso 2: Instalar
1. **Doble-click** en `Weather-Dashboard-Setup.exe`
2. Espera a que se complete la instalación
3. El programa se abrirá automáticamente

### Paso 3: Configurar API Key
1. Se abrirá un navegador en `http://localhost:5000`
2. Verás el Weather Dashboard
3. Si falta la API key, ve a: https://openweathermap.org/api
4. Obtén una clave gratuita
5. Edita el archivo `.env` en la carpeta de instalación:
   - Busca: `OPENWEATHER_API_KEY=`
   - Reemplaza con tu clave
   - Guarda el archivo

### Paso 4: ¡Listo!
- Recarga la página en el navegador
- ¡Disfruta el Weather Dashboard! 🌤️

---

## 🛠️ **Compilar tu Propio .EXE**

### Requisitos
- Python 3.8+ instalado
- ~500 MB de espacio en disco
- Conexión a internet

### Pasos

```batch
# 1. Clona el repositorio
git clone https://github.com/saulonthebeat-stack/Spoofers.git
cd Spoofers

# 2. Instala dependencias
pip install pyinstaller flask requests python-dotenv

# 3. Ejecuta el compilador
build-exe-windows.bat

# ¡El .exe se crea automáticamente!
```

---

## 📊 **Información del .EXE**

| Propiedad | Detalles |
|-----------|----------|
| **Nombre** | Weather Dashboard.exe |
| **Tamaño** | ~80-100 MB |
| **Plataforma** | Windows 7+ |
| **Arquitectura** | 64-bit |
| **Requisitos** | .NET Runtime (generalmente incluido) |
| **API** | OpenWeatherMap (gratuita) |

---

## 🔧 **Usar Scripts Instaladores**

Si prefieres no usar el .exe:

### Script Windows (.BAT)

```batch
# 1. Descarga install-windows.bat
# 2. Double-click para ejecutar
# 3. Automáticamente:
#    ✓ Verifica Python
#    ✓ Crea entorno virtual
#    ✓ Instala dependencias
#    ✓ Crea archivo .env

# 4. Para ejecutar después:
#    Double-click en: run.bat
```

### Script Linux/Mac (.SH)

```bash
# 1. Descarga install-linux-mac.sh
# 2. Dale permisos:
chmod +x install-linux-mac.sh

# 3. Ejecuta:
./install-linux-mac.sh

# 4. Para ejecutar después:
./run.sh
```

---

## 🌐 **URLs Importantes**

| Recurso | URL |
|---------|-----|
| **Descargar** | https://github.com/saulonthebeat-stack/Spoofers/releases |
| **Repositorio** | https://github.com/saulonthebeat-stack/Spoofers |
| **API Key** | https://openweathermap.org/api |
| **Documentación** | https://github.com/saulonthebeat-stack/Spoofers/blob/main/README_WEATHER.md |

---

## ⚠️ **Solución de Problemas**

### El .exe no se abre
```
✓ Asegúrate de descargar la versión correcta para tu Windows
✓ Intenta ejecutar como administrador
✓ Desactiva temporalmente el antivirus
✓ Reinicia la computadora
```

### Error de API Key
```
✓ Verifica que .env exista en la carpeta de instalación
✓ Obtén tu API key en: https://openweathermap.org/api
✓ Edita .env y añade tu clave
✓ Recarga la página en el navegador
```

### Puerto 5000 en uso
```
✓ Cierra otras aplicaciones que usen ese puerto
✓ O edita weather_app.py y cambia el puerto a 8000
```

### Antivirus bloquea el .exe
```
✓ El .exe es totalmente seguro
✓ Descargado desde GitHub (verificado)
✓ Añade a excepciones del antivirus
✓ O compila tu propio .exe localmente
```

---

## 📥 **Instalación Manual desde Código**

Si prefieres instalar desde el código fuente:

```batch
# 1. Descarga el repositorio
git clone https://github.com/saulonthebeat-stack/Spoofers.git

# 2. Entra a la carpeta
cd Spoofers

# 3. Ejecuta el instalador
install-windows.bat

# 4. Ejecuta la aplicación
run.bat

# ¡Listo! Se abrirá en http://localhost:5000
```

---

## 🎯 **Próximas Características**

- [x] Instalador .exe
- [x] Scripts batch para Windows
- [x] Scripts shell para Linux/Mac
- [ ] Instalador NSIS profesional
- [ ] Microsoft Store
- [ ] Auto-updates
- [ ] Compresión UPX

---

## 📞 **Soporte**

¿Problemas?
- 📧 Abre un [issue en GitHub](https://github.com/saulonthebeat-stack/Spoofers/issues)
- 💬 Lee la [documentación](https://github.com/saulonthebeat-stack/Spoofers/blob/main/README_WEATHER.md)
- 🔗 Visita [OpenWeatherMap](https://openweathermap.org/)

---

**¡Weather Dashboard está listo para instalar! 🚀**
