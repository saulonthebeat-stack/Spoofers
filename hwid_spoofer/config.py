"""HWID Spoofer Configuration."""

import os
from dotenv import load_dotenv

load_dotenv()

# Database
DATABASE_PATH = os.getenv('DATABASE_PATH', 'hwid_spoofer.db')
EXCEL_OUTPUT_PATH = os.getenv('EXCEL_OUTPUT_PATH', 'HWID_Cambios.xlsx')
BACKUP_PATH = os.getenv('BACKUP_PATH', 'backups')

# Componentes soportados
COMPONENTS = {
    'cpu': 'Procesador (CPU)',
    'gpu': 'Tarjeta Gráfica (GPU)',
    'disk': 'Disco Duro (HDD/SSD)',
    'motherboard': 'Placa Madre',
    'memory': 'Memoria RAM',
    'nic': 'Tarjeta de Red',
    'bios': 'BIOS',
}

# Debug
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Logging
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FILE = os.getenv('LOG_FILE', 'hwid_spoofer.log')
