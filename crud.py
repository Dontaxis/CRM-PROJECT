"""
CRUD operations for the CRM system.
Handles Create, Read, Update, Delete operations for contacts.
"""

from database import Database
from models import Contact
from typing import Optional, List


class ContactManager:
    """Manages all CRUD operations for contacts."""

    def __init__(self, db_name="crm.db"):
        """Initialize with database connection."""
        self.db = Database(db_name)

    def __enter__(self):
        """Context manager entry - connect to database."""
        self.db.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - close database connection."""
        self.db.close()

    # CREATE
    def create_contact(
        self,
        name: str,
        email: Optional[str] = None,
        phone: Optional[str] = None,
        company: Optional[str] = None,
        notes: Optional[str] = None,
    ) -> Contact:
        """
        Create a new contact in the database.

        Args:
            name: Contact's full name (required)
            email: Email address (optional)
            phone: Phone number (optional)
            company: Company name (optional)
            notes: Additional notes (optional)

        Returns:
            Contact object with assigned ID
        """
        cursor = self.db.connection.cursor()
        cursor.execute(
            """
            INSERT INTO contacts (name, email, phone, company, notes)
            VALUES (?, ?, ?, ?, ?)
            """,
            (name, email, phone, company, notes),
        )
        self.db.connection.commit()

        contact_id = cursor.lastrowid
        return Contact(
            name=name,
            email=email,
            phone=phone,
            company=company,
            notes=notes,
            contact_id=contact_id,
        )

    # READ - Single contact
    def get_contact(self, contact_id: int) -> Optional[Contact]:
        """
        Retrieve a single contact by ID.

        Args:
            contact_id: ID of the contact to retrieve

        Returns:
            Contact object if found, None otherwise
        """
        cursor = self.db.connection.cursor()
        cursor.execute(
            "SELECT * FROM contacts WHERE id = ?",
            (contact_id,),
        )
        row = cursor.fetchone()

        if row:
            return Contact(
                contact_id=row["id"],
                name=row["name"],
                email=row["email"],
                phone=row["phone"],
                company=row["company"],
                notes=row["notes"],
            )
        return None

    # READ - All contacts
    def get_all_contacts(self) -> List[Contact]:
        """
        Retrieve all contacts from the database.

        Returns:
            List of Contact objects
        """
        cursor = self.db.connection.cursor()
        cursor.execute("SELECT * FROM contacts ORDER BY name")
        rows = cursor.fetchall()

        contacts = []
        for row in rows:
            contacts.append(
                Contact(
                    contact_id=row["id"],
                    name=row["name"],
                    email=row["email"],
                    phone=row["phone"],
                    company=row["company"],
                    notes=row["notes"],
                )
            )
        return contacts

    # READ - Search contacts
    def search_contacts(self, search_term: str) -> List[Contact]:
        """
        Search for contacts by name or company.

        Args:
            search_term: Term to search for (case-insensitive)

        Returns:
            List of matching Contact objects
        """
        cursor = self.db.connection.cursor()
        search_pattern = f"%{search_term}%"
        cursor.execute(
            """
            SELECT * FROM contacts
            WHERE name LIKE ? OR company LIKE ?
            ORDER BY name
            """,
            (search_pattern, search_pattern),
        )
        rows = cursor.fetchall()

        contacts = []
        for row in rows:
            contacts.append(
                Contact(
                    contact_id=row["id"],
                    name=row["name"],
                    email=row["email"],
                    phone=row["phone"],
                    company=row["company"],
                    notes=row["notes"],
                )
            )
        return contacts

    # UPDATE
    def update_contact(
        self,
        contact_id: int,
        name: Optional[str] = None,
        email: Optional[str] = None,
        phone: Optional[str] = None,
        company: Optional[str] = None,
        notes: Optional[str] = None,
    ) -> bool:
        """
        Update an existing contact.
        Only updates fields that are provided (not None).

        Args:
            contact_id: ID of contact to update
            name: New name (optional)
            email: New email (optional)
            phone: New phone (optional)
            company: New company (optional)
            notes: New notes (optional)

        Returns:
            True if contact was updated, False if not found
        """
        # First check if contact exists
        if not self.get_contact(contact_id):
            return False

        # Build dynamic update query
        updates = []
        values = []

        if name is not None:
            updates.append("name = ?")
            values.append(name)
        if email is not None:
            updates.append("email = ?")
            values.append(email)
        if phone is not None:
            updates.append("phone = ?")
            values.append(phone)
        if company is not None:
            updates.append("company = ?")
            values.append(company)
        if notes is not None:
            updates.append("notes = ?")
            values.append(notes)

        if not updates:
            return True  # Nothing to update

        values.append(contact_id)
        query = f"UPDATE contacts SET {', '.join(updates)} WHERE id = ?"

        cursor = self.db.connection.cursor()
        cursor.execute(query, values)
        self.db.connection.commit()

        return True

    # DELETE
    def delete_contact(self, contact_id: int) -> bool:
        """
        Delete a contact from the database.

        Args:
            contact_id: ID of contact to delete

        Returns:
            True if contact was deleted, False if not found
        """
        cursor = self.db.connection.cursor()
        cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
        self.db.connection.commit()

        # Check if a row was actually deleted
        return cursor.rowcount > 0

    # UTILITY
    def count_contacts(self) -> int:
        """
        Count total number of contacts.

        Returns:
            Number of contacts in database
        """
        cursor = self.db.connection.cursor()
        cursor.execute("SELECT COUNT(*) as count FROM contacts")
        row = cursor.fetchone()
        return row["count"]
