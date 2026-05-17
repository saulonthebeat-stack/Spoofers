"""HWID Spoofer Database."""

import sqlite3
import logging
from datetime import datetime
from typing import List, Dict, Optional

logger = logging.getLogger(__name__)


class HWIDDatabase:
    """SQLite database for HWID tracking."""

    def __init__(self, db_path: str = "hwid_spoofer.db"):
        """Initialize database.
        
        Args:
            db_path: Path to database file
        """
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        """Initialize database tables."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Create changes table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS hwid_changes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                        component TEXT NOT NULL,
                        description TEXT,
                        old_serial TEXT,
                        new_serial TEXT,
                        status TEXT,
                        notes TEXT,
                        revert_needed BOOLEAN DEFAULT 0
                    )
                ''')
                
                # Create components table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS components (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        component_type TEXT UNIQUE,
                        description TEXT,
                        current_serial TEXT,
                        original_serial TEXT,
                        modified BOOLEAN DEFAULT 0,
                        last_modified DATETIME
                    )
                ''')
                
                conn.commit()
                logger.info("Database initialized successfully")
        except Exception as e:
            logger.error(f"Error initializing database: {e}")

    def add_change(self, component: str, description: str, old_serial: str, 
                   new_serial: str, status: str = "success", notes: str = "") -> bool:
        """Add a change record.
        
        Args:
            component: Component type
            description: Component description
            old_serial: Original serial
            new_serial: New serial
            status: Operation status
            notes: Additional notes
            
        Returns:
            True if successful
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO hwid_changes 
                    (component, description, old_serial, new_serial, status, notes)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (component, description, old_serial, new_serial, status, notes))
                conn.commit()
                logger.info(f"Change recorded: {component} - {status}")
                return True
        except Exception as e:
            logger.error(f"Error adding change: {e}")
            return False

    def get_changes(self, limit: int = 100) -> List[Dict]:
        """Get recent changes.
        
        Args:
            limit: Number of records to retrieve
            
        Returns:
            List of change records
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT * FROM hwid_changes 
                    ORDER BY timestamp DESC 
                    LIMIT ?
                ''', (limit,))
                
                records = [dict(row) for row in cursor.fetchall()]
                return records
        except Exception as e:
            logger.error(f"Error retrieving changes: {e}")
            return []

    def update_component(self, component_type: str, current_serial: str, 
                        original_serial: str = "") -> bool:
        """Update component information.
        
        Args:
            component_type: Type of component
            current_serial: Current serial
            original_serial: Original serial (for tracking)
            
        Returns:
            True if successful
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT OR REPLACE INTO components 
                    (component_type, current_serial, original_serial, modified, last_modified)
                    VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
                ''', (component_type, current_serial, original_serial or current_serial, 1))
                conn.commit()
                return True
        except Exception as e:
            logger.error(f"Error updating component: {e}")
            return False

    def get_all_components(self) -> List[Dict]:
        """Get all components.
        
        Returns:
            List of component records
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM components')
                records = [dict(row) for row in cursor.fetchall()]
                return records
        except Exception as e:
            logger.error(f"Error retrieving components: {e}")
            return []

    def get_summary(self) -> Dict:
        """Get database summary.
        
        Returns:
            Summary statistics
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                cursor.execute('SELECT COUNT(*) FROM hwid_changes')
                total_changes = cursor.fetchone()[0]
                
                cursor.execute('SELECT COUNT(*) FROM hwid_changes WHERE status = "success"')
                successful_changes = cursor.fetchone()[0]
                
                cursor.execute('SELECT COUNT(*) FROM components WHERE modified = 1')
                modified_components = cursor.fetchone()[0]
                
                return {
                    'total_changes': total_changes,
                    'successful_changes': successful_changes,
                    'modified_components': modified_components,
                }
        except Exception as e:
            logger.error(f"Error getting summary: {e}")
            return {}
