"""
Data models for the CRM system.
Starting simple with just a Contact model.
"""

from datetime import datetime
from typing import Optional


class Contact:
    """Represents a contact in the CRM system."""

    def __init__(
        self,
        name: str,
        email: Optional[str] = None,
        phone: Optional[str] = None,
        company: Optional[str] = None,
        notes: Optional[str] = None,
        contact_id: Optional[int] = None,
        created_at: Optional[datetime] = None,
    ):
        self.id = contact_id
        self.name = name
        self.email = email
        self.phone = phone
        self.company = company
        self.notes = notes
        self.created_at = created_at or datetime.now()

    def __repr__(self):
        return f"Contact(id={self.id}, name='{self.name}', company='{self.company}')"

    def __str__(self):
        """Human-readable string representation."""
        return f"{self.name} ({self.company or 'No company'})"
