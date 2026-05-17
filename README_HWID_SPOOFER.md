# HWID Spoofer - Gestor de Números de Serie

> **Herramienta profesional para cambiar números de serie de componentes de tu computadora** 🖥️

---

## ✨ **Características**

### 🔧 **Soporta Todos los Componentes**
- ✅ Procesador (CPU)
- ✅ Tarjeta Gráfica (GPU)
- ✅ Disco Duro (HDD/SSD)
- ✅ Placa Madre
- ✅ Memoria RAM
- ✅ Tarjeta de Red (MAC)
- ✅ BIOS

### 📊 **Generación de Reportes**
- ✅ Exporta cambios a Excel
- ✅ Historial completo de cambios
- ✅ Resumen de modificaciones
- ✅ Timestamps automáticos

### 💾 **Base de Datos Integrada**
- ✅ Registro de todos los cambios
- ✅ Historial persistente
- ✅ Búsqueda y filtrado
- ✅ Estadísticas detalladas

### 🔒 **Seguridad**
- ✅ Backup automático de registros
- ✅ Logs detallados
- ✅ Validación de cambios
- ✅ Rastreo de modificaciones

---

## 📦 **Instalación**

### Requisitos
- Windows 7+
- Python 3.8+
- Permiso de administrador

### Pasos de Instalación

```bash
# 1. Descarga el proyecto
git clone https://github.com/saulonthebeat-stack/Spoofers.git
cd Spoofers

# 2. Instala dependencias
pip install wmi openpyxl

# 3. O usa el archivo requirements.txt
pip install -r requirements.txt
```

---

## 🚀 **Uso**

### Ejecutar el Programa

```bash
# En modo interactivo
python hwid_spoofer_app.py

# O usa el script de ejecución
run.bat  # Windows
./run.sh # Linux/Mac
```

### Menú Principal

```
[MENÚ PRINCIPAL]

1. Escanear Hardware
   - Ver información actual de todos los componentes
   - Muestra seriales actuales
   - Información detallada de hardware

2. Cambiar Serial de Componente
   - Selecciona componente a modificar
   - Ingresa serial actual
   - Ingresa nuevo serial
   - Confirma el cambio

3. Ver Cambios Realizados
   - Lista los cambios en la sesión actual
   - Muestra estado de cada cambio
   - Detalle de seriales

4. Exportar a Excel
   - Crea archivo HWID_Cambios.xlsx
   - Incluye todos los cambios
   - Resumen automático

5. Ver Historial
   - Historial de las últimas 20 modificaciones
   - Búsqueda por componente
   - Filtrado por fecha

6. Salir
   - Cierra la aplicación
```

---

## 📊 **Archivo Excel Generado**

### HWID_Cambios.xlsx

**Hoja Principal: "HWID Changes"**

| Fecha/Hora | Componente | Descripción | Serial Original | Serial Nuevo | Estado | Notas |
|---|---|---|---|---|---|---|
| 2026-05-17 10:30:45 | disk | Disco Duro (HDD/SSD) | ABC123DEF456 | XYZ789UVW012 | Exitoso | Cambio de SSD |
| 2026-05-17 10:31:12 | gpu | Tarjeta Gráfica | GPU001 | GPU002 | Exitoso | Actualización GPU |

**Hoja: "Resumen"**

```
Total de Cambios: 15
Cambios Exitosos: 14
Componentes Modificados: 6
Fecha de Generación: 2026-05-17 10:32:00
```

---

## 🎯 **Ejemplos de Uso**

### Cambiar Serial del Disco Duro

```
[MENÚ PRINCIPAL]
Selecciona una opción: 2

[CAMBIAR SERIAL DE COMPONENTE]
Componentes disponibles:
1. Procesador (CPU)
2. Tarjeta Gráfica (GPU)
3. Disco Duro (HDD/SSD)
4. Placa Madre
5. Memoria RAM
6. Tarjeta de Red
7. BIOS

Selecciona componente: 3

Serial actual: D1S4ABC123XYZ
Nuevo serial: D1S4NEWSER001

✅ Serial de Disco Duro (HDD/SSD) cambiado exitosamente
```

### Generar Reporte Excel

```
[MENÚ PRINCIPAL]
Selecciona una opción: 4

[EXPORTAR A EXCEL]
✅ Archivo exportado: HWID_Cambios.xlsx

(Abre el archivo en Excel para ver el reporte completo)
```

---

## 📂 **Estructura del Proyecto**

```
Spoofers/
├── hwid_spoofer/
│   ├── __init__.py              # Inicializador
│   ├── config.py                # Configuración
│   ├── hardware_info.py         # Detección de hardware
│   ├── registry_spoofing.py     # Modificación de registro
│   ├── excel_generator.py       # Generador de Excel
│   └── database.py              # Base de datos SQLite
├── tests/
│   └── test_hwid_spoofer.py     # Tests unitarios
├── hwid_spoofer_app.py          # Aplicación principal
├── requirements.txt             # Dependencias
└── HWID_Cambios.xlsx            # Reporte generado
```

---

## 🔧 **Configuración**

Edita `hwid_spoofer/config.py`:

```python
# Ruta de base de datos
DATABASE_PATH = 'hwid_spoofer.db'

# Ruta del archivo Excel
EXCEL_OUTPUT_PATH = 'HWID_Cambios.xlsx'

# Ruta de respaldos
BACKUP_PATH = 'backups'

# Componentes soportados
COMPONENTS = {
    'cpu': 'Procesador (CPU)',
    'gpu': 'Tarjeta Gráfica (GPU)',
    'disk': 'Disco Duro (HDD/SSD)',
    # ...
}
```

---

## 📝 **Logging**

Todos los cambios se registran en:
- `hwid_spoofer.log` - Archivo de logs
- `hwid_spoofer.db` - Base de datos SQLite
- Consola - Salida en tiempo real

---

## 🧪 **Testing**

Ejecuta los tests:

```bash
pytest tests/test_hwid_spoofer.py -v

# Con cobertura
pytest --cov=hwid_spoofer tests/
```

---

## ⚙️ **Funciones Avanzadas**

### Obtener Historial Completo

```python
from hwid_spoofer_app import HWIDSpoofer

spoofer = HWIDSpoofer()
history = spoofer.get_change_history(limit=50)

for record in history:
    print(f"{record['timestamp']} - {record['component']}: {record['status']}")
```

### Programación de Cambios

```python
spoofer = HWIDSpoofer()

# Cambiar múltiples componentes
components_to_change = [
    ('disk', 'ABC123', 'XYZ789'),
    ('gpu', 'GPU001', 'GPU999'),
    ('cpu', 'CPU001', 'CPU888'),
]

for component, old_serial, new_serial in components_to_change:
    spoofer.spoof_component(component, new_serial, old_serial)

# Exportar todo a Excel
spoofer.export_to_excel()
```

---

## ⚠️ **Consideraciones Importantes**

### ✅ Uso Legal
- Esta herramienta es **para uso personal**
- Respeta la privacidad y leyes locales
- No la uses con intenciones maliciosas
- Ten respaldos de tus datos originales

### 🔒 Seguridad
- Ejecuta como administrador
- Haz respaldo del registro antes de cambios
- Prueba en máquina virtual primero
- Guarda el archivo Excel con los cambios

### 🛡️ Respaldo
- La aplicación crea respaldos automáticos
- Los logs registran todos los cambios
- Base de datos persistente
- Excel con historial completo

---

## 🐛 **Solución de Problemas**

### Error: "Acceso denegado"
```
✓ Ejecuta como administrador
✓ Abre cmd/PowerShell con "Ejecutar como administrador"
✓ Desactiva antivirus temporalmente
```

### Error: "WMI no disponible"
```
✓ Verifica que Windows Installer esté activo
✓ Reinstala WMI si es necesario
✓ Reinicia la computadora
```

### El cambio no se aplica
```
✓ Reinicia la computadora
✓ Algunos cambios requieren reinicio
✓ Verifica el log para errores
```

---

## 📞 **Soporte**

- 📧 GitHub Issues: https://github.com/saulonthebeat-stack/Spoofers/issues
- 📚 Documentación: README_WEATHER.md
- 🐍 Python: python.org
- 🪟 Windows: microsoft.com

---

## 📜 **Licencia**

MIT License - Ver LICENSE para detalles

---

## 👨‍💻 **Autor**

**Saul on the Beat Stack**
- GitHub: @saulonthebeat-stack
- Repo: https://github.com/saulonthebeat-stack/Spoofers

---

**¡Tu HWID Spoofer profesional está listo! 🚀**
