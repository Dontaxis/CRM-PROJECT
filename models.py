"""
Data models for the CRM system.
These classes represent the core entities: Customers, Contacts, and Interactions.
"""

from datetime import datetime
from typing import Optional, List


class Customer:
    """Represents a customer/company in the CRM system."""

    def __init__(
        self,
        company_name: str,
        industry: Optional[str] = None,
        notes: Optional[str] = None,
        customer_id: Optional[int] = None,
        created_at: Optional[datetime] = None,
    ):
        self.id = customer_id
        self.company_name = company_name
        self.industry = industry
        self.notes = notes
        self.created_at = created_at or datetime.now()

    def __repr__(self):
        return f"Customer(id={self.id}, company='{self.company_name}', industry='{self.industry}')"


class Contact:
    """Represents a contact person associated with a customer."""

    def __init__(
        self,
        customer_id: int,
        first_name: str,
        last_name: str,
        email: Optional[str] = None,
        phone: Optional[str] = None,
        role: Optional[str] = None,
        contact_id: Optional[int] = None,
        created_at: Optional[datetime] = None,
    ):
        self.id = contact_id
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.role = role
        self.created_at = created_at or datetime.now()

    @property
    def full_name(self):
        """Return the contact's full name."""
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"Contact(id={self.id}, name='{self.full_name}', role='{self.role}')"


class Interaction:
    """Represents an interaction with a customer."""

    def __init__(
        self,
        customer_id: int,
        interaction_type: str,
        subject: Optional[str] = None,
        notes: Optional[str] = None,
        contact_id: Optional[int] = None,
        interaction_id: Optional[int] = None,
        interaction_date: Optional[datetime] = None,
    ):
        self.id = interaction_id
        self.customer_id = customer_id
        self.contact_id = contact_id
        self.interaction_type = interaction_type  # e.g., 'email', 'call', 'meeting'
        self.subject = subject
        self.notes = notes
        self.interaction_date = interaction_date or datetime.now()

    def __repr__(self):
        return f"Interaction(id={self.id}, type='{self.interaction_type}', subject='{self.subject}')"
