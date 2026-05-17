"""HWID Spoofer - Registry manipulation."""

import logging
import subprocess
from typing import Dict, Optional
import winreg

logger = logging.getLogger(__name__)


class RegistrySpoofing:
    """Handles registry modifications for HWID spoofing."""

    # Registry paths for different components
    REGISTRY_PATHS = {
        'disk': [
            r'HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\disk\\Enum',
        ],
        'motherboard': [
            r'HKEY_LOCAL_MACHINE\\HARDWARE\\DESCRIPTION\\System\\MultifunctionAdapter',
        ],
        'network': [
            r'HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces',
        ],
    }

    @staticmethod
    def backup_registry(component: str) -> bool:
        """Backup registry before modification.
        
        Args:
            component: Component type
            
        Returns:
            True if backup successful
        """
        try:
            backup_file = f"registry_backup_{component}.reg"
            cmd = f'reg export "HKEY_LOCAL_MACHINE\\SYSTEM" "{backup_file}" /y'
            subprocess.run(cmd, shell=True, check=True)
            logger.info(f"Registry backed up to {backup_file}")
            return True
        except Exception as e:
            logger.error(f"Error backing up registry: {e}")
            return False

    @staticmethod
    def spoof_disk_serial(old_serial: str, new_serial: str) -> bool:
        """Spoof disk serial number.
        
        Args:
            old_serial: Original serial
            new_serial: New serial
            
        Returns:
            True if successful
        """
        try:
            # Backup first
            RegistrySpoofing.backup_registry('disk')
            
            # Modify registry
            key_path = r'HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\disk\\Enum'
            cmd = f'reg add "{key_path}" /v "0" /d "{new_serial}" /f'
            subprocess.run(cmd, shell=True, check=True, capture_output=True)
            logger.info(f"Disk serial spoofed: {old_serial} -> {new_serial}")
            return True
        except Exception as e:
            logger.error(f"Error spoofing disk serial: {e}")
            return False

    @staticmethod
    def spoof_mac_address(old_mac: str, new_mac: str, interface: str) -> bool:
        """Spoof MAC address.
        
        Args:
            old_mac: Original MAC
            new_mac: New MAC
            interface: Network interface name
            
        Returns:
            True if successful
        """
        try:
            RegistrySpoofing.backup_registry('network')
            
            key_path = rf'HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Class\\{{4D36E972-E325-11CE-BFC1-08002BE10318}}'
            
            # Find the correct subkey
            cmd = f'reg add "{key_path}" /v "NetworkAddress" /d "{new_mac}" /f'
            subprocess.run(cmd, shell=True, check=True, capture_output=True)
            logger.info(f"MAC address spoofed: {old_mac} -> {new_mac}")
            return True
        except Exception as e:
            logger.error(f"Error spoofing MAC address: {e}")
            return False

    @staticmethod
    def modify_wmi_serial(component: str, new_serial: str) -> bool:
        """Modify WMI serial number.
        
        Args:
            component: Component type
            new_serial: New serial number
            
        Returns:
            True if successful
        """
        try:
            # Use WMI to modify
            if component == 'disk':
                cmd = f'wmic logicaldisk where name="C:" set SerialNumber="{new_serial}"'
            elif component == 'motherboard':
                cmd = f'wmic baseboard set SerialNumber="{new_serial}"'
            else:
                return False
            
            subprocess.run(cmd, shell=True, check=True, capture_output=True)
            logger.info(f"WMI {component} serial modified: {new_serial}")
            return True
        except Exception as e:
            logger.error(f"Error modifying WMI: {e}")
            return False
