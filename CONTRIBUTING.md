# Guía de Contribución

Gracias por tu interés en contribuir a Spoofers. Este documento proporciona directrices para contribuir al proyecto.

## 📋 Antes de empezar

- Asegúrate de tener Python 3.8 o superior instalado
- Familiarízate con el proyecto leyendo el README.md
- Revisa los problemas abiertos antes de crear uno nuevo

## 🔧 Configuración del desarrollo

```bash
# Clona el repositorio
git clone https://github.com/saulonthebeat-stack/Spoofers.git
cd Spoofers

# Crea un entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instala las dependencias
pip install -r requirements.txt
```

## 📝 Proceso de contribución

1. **Fork el proyecto**
   - Haz clic en el botón "Fork" en GitHub

2. **Crea una rama**
   ```bash
   git checkout -b feature/tu-feature
   # o
   git checkout -b fix/tu-fix
   ```

3. **Haz tus cambios**
   - Asegúrate de que tu código siga el estilo del proyecto
   - Escribe o actualiza tests según sea necesario

4. **Formato de código**
   ```bash
   # Formatea con black
   black .
   
   # Verifica con flake8
   flake8 .
   ```

5. **Prueba tu código**
   ```bash
   pytest
   ```

6. **Commit y Push**
   ```bash
   git commit -m "Descripción clara de los cambios"
   git push origin feature/tu-feature
   ```

7. **Abre un Pull Request**
   - Describe claramente tus cambios
   - Referencia cualquier issue relacionado

## 📝 Commits

Usa mensajes de commit descriptivos:

- `feat: add new feature`
- `fix: fix bug in module`
- `docs: update documentation`
- `test: add unit tests`
- `refactor: refactor code`

## 🐛 Reporte de bugs

Al reportar bugs, incluye:

- Descripción clara del problema
- Pasos para reproducir
- Comportamiento esperado vs. actual
- Tu entorno (Python version, OS, etc.)

## ✨ Sugerencias de features

- Describe claramente la feature
- Explica el caso de uso
- Proporciona ejemplos si es posible

## 📞 Contacto

Si tienes preguntas, abre un issue o contacta al mantedor del proyecto.

¡Gracias por contribuir! 🎉