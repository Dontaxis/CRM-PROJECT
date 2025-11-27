"""
CRM Learning Project - Main Entry Point
A simple command-line CRM system to understand how customer management works.
"""

from database import Database, init_database
from models import Customer, Contact, Interaction
import sys


def print_menu():
    """Display the main menu."""
    print("\n" + "=" * 50)
    print("CRM LEARNING PROJECT")
    print("=" * 50)
    print("\n[1] Manage Customers")
    print("[2] Manage Contacts")
    print("[3] Log Interaction")
    print("[4] View Reports")
    print("[5] Initialize Database")
    print("[0] Exit")
    print("-" * 50)


def manage_customers():
    """Placeholder for customer management."""
    print("\n📋 Customer Management")
    print("(Feature coming soon...)")


def manage_contacts():
    """Placeholder for contact management."""
    print("\n👥 Contact Management")
    print("(Feature coming soon...)")


def log_interaction():
    """Placeholder for logging interactions."""
    print("\n📝 Log Interaction")
    print("(Feature coming soon...)")


def view_reports():
    """Placeholder for viewing reports."""
    print("\n📊 Reports")
    print("(Feature coming soon...)")


def main():
    """Main application loop."""
    print("\n🚀 Welcome to the CRM Learning Project!")
    print("This is a learning project to understand CRM systems.\n")

    while True:
        print_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            manage_customers()
        elif choice == "2":
            manage_contacts()
        elif choice == "3":
            log_interaction()
        elif choice == "4":
            view_reports()
        elif choice == "5":
            print("\n🔧 Initializing database...")
            init_database()
        elif choice == "0":
            print("\n👋 Thanks for using the CRM system. Goodbye!")
            sys.exit(0)
        else:
            print("\n❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        sys.exit(0)
