"""Hardware information detection."""

import platform
import subprocess
import logging
from typing import Dict, Optional
import wmi
import uuid

logger = logging.getLogger(__name__)


class HardwareInfo:
    """Detects and retrieves hardware information."""

    def __init__(self):
        """Initialize hardware info detector."""
        try:
            self.wmi_client = wmi.WMI()
        except Exception as e:
            logger.error(f"Error initializing WMI: {e}")
            self.wmi_client = None

    def get_cpu_info(self) -> Dict[str, str]:
        """Get CPU information.
        
        Returns:
            Dictionary with CPU serial and model
        """
        try:
            if self.wmi_client:
                cpus = self.wmi_client.Win32_Processor()
                if cpus:
                    cpu = cpus[0]
                    return {
                        'serial': self._get_cpu_serial(),
                        'model': cpu.Name,
                        'cores': cpu.NumberOfCores,
                        'threads': cpu.NumberOfLogicalProcessors,
                    }
        except Exception as e:
            logger.error(f"Error getting CPU info: {e}")
        return {}

    def _get_cpu_serial(self) -> str:
        """Get CPU serial number."""
        try:
            result = subprocess.run(
                ['wmic', 'cpu', 'get', 'processorid'],
                capture_output=True,
                text=True
            )
            lines = result.stdout.strip().split('\n')
            if len(lines) > 1:
                return lines[1].strip()
        except Exception as e:
            logger.error(f"Error getting CPU serial: {e}")
        return "N/A"

    def get_gpu_info(self) -> Dict[str, str]:
        """Get GPU information.
        
        Returns:
            Dictionary with GPU serial and model
        """
        try:
            if self.wmi_client:
                gpus = self.wmi_client.Win32_VideoController()
                if gpus:
                    gpu = gpus[0]
                    return {
                        'serial': gpu.PNPDeviceID if hasattr(gpu, 'PNPDeviceID') else 'N/A',
                        'model': gpu.Name,
                        'memory': gpu.AdapterRAM,
                    }
        except Exception as e:
            logger.error(f"Error getting GPU info: {e}")
        return {}

    def get_disk_info(self) -> Dict[str, str]:
        """Get disk information.
        
        Returns:
            Dictionary with disk serial and model
        """
        try:
            if self.wmi_client:
                disks = self.wmi_client.Win32_DiskDrive()
                if disks:
                    disk = disks[0]
                    return {
                        'serial': disk.SerialNumber if disk.SerialNumber else 'N/A',
                        'model': disk.Model,
                        'size': disk.Size,
                    }
        except Exception as e:
            logger.error(f"Error getting disk info: {e}")
        return {}

    def get_motherboard_info(self) -> Dict[str, str]:
        """Get motherboard information.
        
        Returns:
            Dictionary with motherboard serial and model
        """
        try:
            if self.wmi_client:
                boards = self.wmi_client.Win32_BaseBoard()
                if boards:
                    board = boards[0]
                    return {
                        'serial': board.SerialNumber,
                        'model': board.Product,
                        'manufacturer': board.Manufacturer,
                    }
        except Exception as e:
            logger.error(f"Error getting motherboard info: {e}")
        return {}

    def get_memory_info(self) -> Dict[str, str]:
        """Get RAM information.
        
        Returns:
            Dictionary with memory info
        """
        try:
            if self.wmi_client:
                memory = self.wmi_client.Win32_PhysicalMemory()
                if memory:
                    mem = memory[0]
                    total_size = sum(int(m.Capacity) for m in memory) / (1024**3)
                    return {
                        'serial': mem.SerialNumber if mem.SerialNumber else 'N/A',
                        'model': mem.PartNumber,
                        'capacity': f"{total_size:.0f}GB",
                    }
        except Exception as e:
            logger.error(f"Error getting memory info: {e}")
        return {}

    def get_nic_info(self) -> Dict[str, str]:
        """Get network adapter information.
        
        Returns:
            Dictionary with NIC info
        """
        try:
            if self.wmi_client:
                nics = self.wmi_client.Win32_NetworkAdapterConfiguration()
                if nics:
                    nic = nics[0]
                    return {
                        'mac': nic.MACAddress if nic.MACAddress else 'N/A',
                        'model': nic.Description,
                    }
        except Exception as e:
            logger.error(f"Error getting NIC info: {e}")
        return {}

    def get_bios_info(self) -> Dict[str, str]:
        """Get BIOS information.
        
        Returns:
            Dictionary with BIOS info
        """
        try:
            if self.wmi_client:
                bios = self.wmi_client.Win32_BIOS()
                if bios:
                    b = bios[0]
                    return {
                        'serial': b.SerialNumber,
                        'version': b.Version,
                        'manufacturer': b.Manufacturer,
                    }
        except Exception as e:
            logger.error(f"Error getting BIOS info: {e}")
        return {}

    def get_all_hardware(self) -> Dict[str, Dict]:
        """Get all hardware information.
        
        Returns:
            Dictionary with all hardware info
        """
        return {
            'cpu': self.get_cpu_info(),
            'gpu': self.get_gpu_info(),
            'disk': self.get_disk_info(),
            'motherboard': self.get_motherboard_info(),
            'memory': self.get_memory_info(),
            'nic': self.get_nic_info(),
            'bios': self.get_bios_info(),
        }
