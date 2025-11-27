"""
Simple demo showing how to use the CRM system.
This is a quick example of the CRUD operations in action.
"""

from database import init_database
from crud import ContactManager


def main():
    """Run a simple demo of the CRM system."""
    print("=" * 60)
    print("CRM SYSTEM DEMO")
    print("=" * 60)

    # Initialize database if it doesn't exist
    print("\nInitializing database...")
    init_database()

    # Use the ContactManager with context manager
    with ContactManager() as cm:
        # Add some contacts
        print("\n📝 Adding contacts...")
        contact1 = cm.create_contact(
            name="Sarah Chen",
            email="sarah@acmecorp.com",
            phone="555-1234",
            company="Acme Corp",
            notes="CEO - very important client",
        )
        print(f"  ✓ Added: {contact1.name}")

        contact2 = cm.create_contact(
            name="Mike Rodriguez",
            email="mike@techstart.io",
            company="TechStart",
            notes="CTO - interested in enterprise plan",
        )
        print(f"  ✓ Added: {contact2.name}")

        contact3 = cm.create_contact(
            name="Emily Davis", phone="555-5678", company="Acme Corp"
        )
        print(f"  ✓ Added: {contact3.name}")

        # Show all contacts
        print("\n📋 All contacts in database:")
        all_contacts = cm.get_all_contacts()
        for contact in all_contacts:
            print(f"  [{contact.id}] {contact.name}")
            if contact.email:
                print(f"      📧 {contact.email}")
            if contact.phone:
                print(f"      📱 {contact.phone}")
            if contact.company:
                print(f"      🏢 {contact.company}")
            print()

        # Search example
        print("🔍 Searching for 'Acme Corp':")
        results = cm.search_contacts("Acme Corp")
        print(f"  Found {len(results)} contacts:")
        for contact in results:
            print(f"    - {contact.name}")

        # Update example
        print("\n✏️  Updating Mike's phone number...")
        cm.update_contact(contact_id=contact2.id, phone="555-9999")
        updated = cm.get_contact(contact2.id)
        print(f"  ✓ {updated.name}'s phone is now: {updated.phone}")

        # Stats
        print(f"\n📊 Total contacts: {cm.count_contacts()}")

    print("\n" + "=" * 60)
    print("Demo complete! Database saved to crm.db")
    print("=" * 60)


if __name__ == "__main__":
    main()
