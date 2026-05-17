"""Main HWID Spoofer Application."""

import logging
import sys
from datetime import datetime
from typing import Dict
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('hwid_spoofer.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

from hwid_spoofer.config import COMPONENTS, EXCEL_OUTPUT_PATH, DATABASE_PATH
from hwid_spoofer.hardware_info import HardwareInfo
from hwid_spoofer.registry_spoofing import RegistrySpoofing
from hwid_spoofer.excel_generator import ExcelReportGenerator
from hwid_spoofer.database import HWIDDatabase


class HWIDSpoofer:
    """Main HWID Spoofer application."""

    def __init__(self):
        """Initialize the spoofer."""
        self.hardware = HardwareInfo()
        self.database = HWIDDatabase(DATABASE_PATH)
        self.changes = []
        logger.info("HWID Spoofer initialized")

    def scan_hardware(self) -> Dict:
        """Scan current hardware.
        
        Returns:
            Dictionary with hardware information
        """
        logger.info("Scanning hardware...")
        hardware_info = self.hardware.get_all_hardware()
        
        for component, info in hardware_info.items():
            logger.info(f"{component}: {info}")
        
        return hardware_info

    def spoof_component(self, component: str, new_serial: str, 
                       old_serial: str, description: str = "") -> bool:
        """Spoof a specific component.
        
        Args:
            component: Component type
            new_serial: New serial number
            old_serial: Original serial number
            description: Component description
            
        Returns:
            True if successful
        """
        try:
            logger.info(f"Spoofing {component}: {old_serial} -> {new_serial}")
            
            # Choose spoofing method based on component
            success = False
            if component == 'disk':
                success = RegistrySpoofing.spoof_disk_serial(old_serial, new_serial)
            elif component == 'nic':
                success = RegistrySpoofing.spoof_mac_address(old_serial, new_serial, 'Ethernet')
            else:
                success = RegistrySpoofing.modify_wmi_serial(component, new_serial)
            
            # Record the change
            status = "success" if success else "failed"
            self.database.add_change(
                component=component,
                description=description or COMPONENTS.get(component, component),
                old_serial=old_serial,
                new_serial=new_serial,
                status=status
            )
            
            # Track the change
            self.changes.append({
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'component': component,
                'description': description or COMPONENTS.get(component, component),
                'old_serial': old_serial,
                'new_serial': new_serial,
                'status': 'Exitoso' if success else 'Fallido',
                'notes': ''
            })
            
            return success
        except Exception as e:
            logger.error(f"Error spoofing {component}: {e}")
            return False

    def export_to_excel(self) -> bool:
        """Export changes to Excel.
        
        Returns:
            True if successful
        """
        try:
            if not self.changes:
                logger.warning("No changes to export")
                return False
            
            generator = ExcelReportGenerator(EXCEL_OUTPUT_PATH)
            success = generator.generate_report(self.changes)
            
            # Add summary
            summary = self.database.get_summary()
            summary['generated'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            generator.add_summary_sheet(summary)
            
            if success:
                logger.info(f"Excel report exported: {EXCEL_OUTPUT_PATH}")
            
            return success
        except Exception as e:
            logger.error(f"Error exporting to Excel: {e}")
            return False

    def get_change_history(self, limit: int = 50) -> list:
        """Get change history from database.
        
        Args:
            limit: Number of records to retrieve
            
        Returns:
            List of change records
        """
        return self.database.get_changes(limit)

    def interactive_mode(self):
        """Run in interactive mode."""
        print("\n" + "="*60)
        print("  HWID SPOOFER - Gestor de Números de Serie")
        print("="*60 + "\n")
        
        while True:
            print("\n[MENÚ PRINCIPAL]\n")
            print("1. Escanear Hardware")
            print("2. Cambiar Serial de Componente")
            print("3. Ver Cambios Realizados")
            print("4. Exportar a Excel")
            print("5. Ver Historial")
            print("6. Salir\n")
            
            choice = input("Selecciona una opción (1-6): ").strip()
            
            if choice == '1':
                self._scan_menu()
            elif choice == '2':
                self._spoof_menu()
            elif choice == '3':
                self._show_changes()
            elif choice == '4':
                self._export_menu()
            elif choice == '5':
                self._show_history()
            elif choice == '6':
                print("\n¡Hasta luego!")
                break
            else:
                print("\n❌ Opción inválida")

    def _scan_menu(self):
        """Scan hardware menu."""
        print("\n[ESCANEO DE HARDWARE]\n")
        hardware = self.scan_hardware()
        
        for component, info in hardware.items():
            if info:
                print(f"\n{COMPONENTS.get(component, component)}:")
                for key, value in info.items():
                    print(f"  {key}: {value}")

    def _spoof_menu(self):
        """Spoof component menu."""
        print("\n[CAMBIAR SERIAL DE COMPONENTE]\n")
        print("Componentes disponibles:")
        for idx, (key, name) in enumerate(COMPONENTS.items(), 1):
            print(f"{idx}. {name}")
        
        choice = input("\nSelecciona componente (1-7): ").strip()
        components_list = list(COMPONENTS.keys())
        
        if 1 <= int(choice) <= len(components_list):
            component = components_list[int(choice) - 1]
            old_serial = input(f"\nSerial actual: ").strip()
            new_serial = input(f"Nuevo serial: ").strip()
            
            if self.spoof_component(component, new_serial, old_serial):
                print(f"\n✅ Serial de {COMPONENTS[component]} cambiado exitosamente")
            else:
                print(f"\n❌ Error al cambiar serial")
        else:
            print("\n❌ Opción inválida")

    def _show_changes(self):
        """Show current changes."""
        print("\n[CAMBIOS REALIZADOS]\n")
        if not self.changes:
            print("No hay cambios realizados aún.")
            return
        
        for change in self.changes:
            print(f"\n{change['timestamp']} - {change['component']}")
            print(f"  {change['old_serial']} → {change['new_serial']}")
            print(f"  Estado: {change['status']}")

    def _export_menu(self):
        """Export menu."""
        print("\n[EXPORTAR A EXCEL]\n")
        if self.export_to_excel():
            print(f"✅ Archivo exportado: {EXCEL_OUTPUT_PATH}")
        else:
            print("❌ Error al exportar")

    def _show_history(self):
        """Show change history."""
        print("\n[HISTORIAL DE CAMBIOS]\n")
        history = self.get_change_history(20)
        
        if not history:
            print("No hay historial.")
            return
        
        for record in history:
            print(f"\n{record.get('timestamp')} - {record.get('component')}")
            print(f"  {record.get('old_serial')} → {record.get('new_serial')}")
            print(f"  Estado: {record.get('status')}")


if __name__ == '__main__':
    try:
        spoofer = HWIDSpoofer()
        spoofer.interactive_mode()
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        sys.exit(1)
