"""Tests for HWID Spoofer."""

import pytest
from hwid_spoofer.hardware_info import HardwareInfo
from hwid_spoofer.database import HWIDDatabase
from hwid_spoofer.excel_generator import ExcelReportGenerator
import tempfile
import os


class TestHardwareInfo:
    """Test hardware information detection."""

    def test_hardware_info_initialization(self):
        """Test HardwareInfo initializes without error."""
        hardware = HardwareInfo()
        assert hardware is not None
        assert hardware.wmi_client is not None

    def test_get_all_hardware(self):
        """Test getting all hardware info."""
        hardware = HardwareInfo()
        all_hw = hardware.get_all_hardware()
        
        # Should have entries for each component type
        assert 'cpu' in all_hw
        assert 'gpu' in all_hw
        assert 'disk' in all_hw


class TestHWIDDatabase:
    """Test HWID database."""

    @pytest.fixture
    def temp_db(self):
        """Create temporary database for testing."""
        fd, path = tempfile.mkstemp(suffix='.db')
        os.close(fd)
        db = HWIDDatabase(path)
        yield db
        os.unlink(path)

    def test_database_initialization(self, temp_db):
        """Test database initializes correctly."""
        assert temp_db is not None

    def test_add_change(self, temp_db):
        """Test adding a change record."""
        result = temp_db.add_change(
            component='disk',
            description='Test Disk',
            old_serial='ABC123',
            new_serial='XYZ789',
            status='success'
        )
        assert result is True

    def test_get_changes(self, temp_db):
        """Test retrieving changes."""
        temp_db.add_change(
            component='cpu',
            description='Test CPU',
            old_serial='CPU001',
            new_serial='CPU002',
            status='success'
        )
        
        changes = temp_db.get_changes()
        assert len(changes) > 0

    def test_get_summary(self, temp_db):
        """Test getting database summary."""
        temp_db.add_change(
            component='disk',
            description='Test',
            old_serial='A',
            new_serial='B',
            status='success'
        )
        
        summary = temp_db.get_summary()
        assert summary['total_changes'] > 0


class TestExcelGenerator:
    """Test Excel report generator."""

    def test_excel_generation(self):
        """Test generating Excel report."""
        with tempfile.TemporaryDirectory() as tmpdir:
            filename = os.path.join(tmpdir, 'test.xlsx')
            generator = ExcelReportGenerator(filename)
            
            changes = [
                {
                    'timestamp': '2026-05-17 10:00:00',
                    'component': 'disk',
                    'description': 'Test Disk',
                    'old_serial': 'ABC123',
                    'new_serial': 'XYZ789',
                    'status': 'Exitoso',
                    'notes': 'Test'
                }
            ]
            
            result = generator.generate_report(changes)
            assert result is True
            assert os.path.exists(filename)
