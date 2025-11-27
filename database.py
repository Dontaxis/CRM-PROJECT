"""
Database setup and connection management for the CRM system.
Uses SQLite for simplicity and portability.
"""

import sqlite3
from pathlib import Path


class Database:
    """Manages database connection and table creation."""

    def __init__(self, db_name="crm.db"):
        """Initialize database connection."""
        self.db_path = Path(db_name)
        self.connection = None

    def connect(self):
        """Establish connection to the database."""
        self.connection = sqlite3.connect(self.db_path)
        self.connection.row_factory = sqlite3.Row  # Access columns by name
        return self.connection

    def close(self):
        """Close database connection."""
        if self.connection:
            self.connection.close()

    def create_tables(self):
        """Create all necessary tables for the CRM system."""
        cursor = self.connection.cursor()

        # Customers table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                company_name TEXT NOT NULL,
                industry TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                notes TEXT
            )
        """)

        # Contacts table (many contacts can belong to one customer)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER NOT NULL,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT,
                phone TEXT,
                role TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (customer_id) REFERENCES customers(id)
            )
        """)

        # Interactions table (track all customer interactions)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS interactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER NOT NULL,
                contact_id INTEGER,
                interaction_type TEXT NOT NULL,
                subject TEXT,
                notes TEXT,
                interaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (customer_id) REFERENCES customers(id),
                FOREIGN KEY (contact_id) REFERENCES contacts(id)
            )
        """)

        self.connection.commit()
        print("Database tables created successfully!")


def init_database():
    """Initialize the database with all tables."""
    db = Database()
    db.connect()
    db.create_tables()
    db.close()


if __name__ == "__main__":
    # Run this file directly to initialize the database
    init_database()
