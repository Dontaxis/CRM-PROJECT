"""
Test file to verify database and CRUD operations work correctly.
Run this to make sure everything is set up properly.
"""

from database import init_database
from crud import ContactManager
import os


def test_crud_operations():
    """Test all CRUD operations."""
    # Use a test database so we don't mess with real data
    test_db = "test_crm.db"

    # Clean up any existing test database
    if os.path.exists(test_db):
        os.remove(test_db)
        print(f"Removed existing {test_db}")

    # Initialize the database
    print("\n1. INITIALIZING DATABASE")
    print("-" * 50)
    from database import Database

    db = Database(test_db)
    db.connect()
    db.create_tables()
    db.close()

    # Test CRUD operations using context manager
    print("\n2. TESTING CREATE (Adding contacts)")
    print("-" * 50)
    with ContactManager(test_db) as cm:
        # Create some test contacts
        contact1 = cm.create_contact(
            name="Alice Johnson",
            email="alice@techcorp.com",
            phone="555-0101",
            company="TechCorp",
            notes="Lead developer",
        )
        print(f"Created: {contact1}")

        contact2 = cm.create_contact(
            name="Bob Smith",
            email="bob@startup.io",
            phone="555-0102",
            company="StartupIO",
        )
        print(f"Created: {contact2}")

        contact3 = cm.create_contact(
            name="Carol Williams", company="TechCorp", notes="Project manager"
        )
        print(f"Created: {contact3}")

    print("\n3. TESTING READ (Getting all contacts)")
    print("-" * 50)
    with ContactManager(test_db) as cm:
        all_contacts = cm.get_all_contacts()
        print(f"Total contacts: {len(all_contacts)}")
        for contact in all_contacts:
            print(f"  - {contact}")

    print("\n4. TESTING READ (Getting single contact)")
    print("-" * 50)
    with ContactManager(test_db) as cm:
        contact = cm.get_contact(1)
        if contact:
            print(f"Found contact ID 1: {contact}")
            print(f"  Email: {contact.email}")
            print(f"  Phone: {contact.phone}")
            print(f"  Notes: {contact.notes}")

    print("\n5. TESTING SEARCH")
    print("-" * 50)
    with ContactManager(test_db) as cm:
        results = cm.search_contacts("TechCorp")
        print(f"Searching for 'TechCorp': {len(results)} results")
        for contact in results:
            print(f"  - {contact}")

    print("\n6. TESTING UPDATE")
    print("-" * 50)
    with ContactManager(test_db) as cm:
        print("Before update:")
        contact = cm.get_contact(2)
        print(f"  {contact}")

        # Update Bob's phone and notes
        cm.update_contact(
            contact_id=2, phone="555-9999", notes="Updated phone number"
        )

        print("After update:")
        contact = cm.get_contact(2)
        print(f"  {contact}")
        print(f"  New phone: {contact.phone}")
        print(f"  New notes: {contact.notes}")

    print("\n7. TESTING DELETE")
    print("-" * 50)
    with ContactManager(test_db) as cm:
        print(f"Contacts before delete: {cm.count_contacts()}")

        deleted = cm.delete_contact(3)
        print(f"Deleted contact ID 3: {deleted}")

        print(f"Contacts after delete: {cm.count_contacts()}")

        remaining = cm.get_all_contacts()
        print("Remaining contacts:")
        for contact in remaining:
            print(f"  - {contact}")

    print("\n8. TESTING COUNT")
    print("-" * 50)
    with ContactManager(test_db) as cm:
        count = cm.count_contacts()
        print(f"Total contacts in database: {count}")

    print("\n" + "=" * 50)
    print("ALL TESTS COMPLETED SUCCESSFULLY!")
    print("=" * 50)
    print(f"\nTest database created: {test_db}")
    print("You can delete it with: rm test_crm.db")


if __name__ == "__main__":
    test_crud_operations()
