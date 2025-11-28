"""
Seed the CRM database with realistic sample data.
Run this to populate your database with fictional contacts that feel real.
"""

from crud import ContactManager
from database import init_database
import random


# Realistic sample data pools
FIRST_NAMES = [
    "James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda",
    "William", "Barbara", "David", "Elizabeth", "Richard", "Susan", "Joseph", "Jessica",
    "Thomas", "Sarah", "Christopher", "Karen", "Daniel", "Nancy", "Matthew", "Lisa",
    "Anthony", "Betty", "Mark", "Margaret", "Donald", "Sandra"
]

LAST_NAMES = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
    "Rodriguez", "Martinez", "Hernandez", "Lopez", "Wilson", "Anderson", "Thomas",
    "Taylor", "Moore", "Jackson", "Martin", "Lee", "Thompson", "White", "Harris",
    "Clark", "Lewis", "Robinson", "Walker", "Young", "Allen", "King"
]

# Industry-specific companies
COMPANIES = {
    "construction": [
        "BuildRight Construction", "Apex Builders", "Summit Construction Group",
        "Foundation First Inc", "Elite Contracting", "Metro Building Solutions"
    ],
    "tech": [
        "CloudScale Systems", "DataFlow Technologies", "Innovate Software",
        "TechBridge Solutions", "Quantum Analytics", "CodeCraft Inc"
    ],
    "healthcare": [
        "HealthFirst Medical Group", "CarePlus Clinic", "Wellness Partners",
        "MediCare Solutions", "Vitality Health Systems", "Community Health Alliance"
    ],
    "retail": [
        "Premier Retail Co", "MarketPlace Solutions", "Retail Dynamics",
        "ShopSmart Enterprises", "Consumer First Group", "Trading Post LLC"
    ],
    "manufacturing": [
        "Precision Manufacturing", "Industrial Fabricators Inc", "MakeTech Industries",
        "Production Systems Group", "Quality Manufacturing Co", "Assembly Line Solutions"
    ],
    "consulting": [
        "Strategic Advisors Group", "Business Insights Consulting", "Growth Partners LLC",
        "Executive Solutions", "Management Consulting Group", "Optimize Strategies"
    ]
}

ROLES = [
    "CEO", "CFO", "CTO", "VP of Sales", "Director of Operations",
    "Procurement Manager", "Project Manager", "Operations Director",
    "Business Development Manager", "Head of IT", "Purchasing Director"
]

LEAD_SOURCES = [
    "LinkedIn outreach", "Industry conference", "Referral from existing client",
    "Cold call", "Website inquiry", "Trade show", "Partner referral",
    "Email campaign", "Networking event", "Google search"
]

DEAL_VALUES = [
    "$5K-10K", "$10K-25K", "$25K-50K", "$50K-100K", "$100K-250K", "$250K+"
]

LEAD_STATUS = [
    "Hot lead - ready to close",
    "Warm - in discussions",
    "Cold - initial contact only",
    "Nurturing - follow up in 30 days",
    "Proposal sent - awaiting decision",
    "Discovery phase",
    "Evaluating competitors",
    "Budget approved - moving forward"
]


def generate_email(first_name, last_name, company):
    """Generate a realistic business email."""
    # Remove spaces and special chars from company name
    company_domain = company.lower().replace(" ", "").replace(",", "")
    # Take first word if company name is long
    if len(company_domain) > 20:
        company_domain = company_domain.split("inc")[0].split("llc")[0].split("group")[0][:15]

    first_initial = first_name[0].lower()
    last = last_name.lower()

    email_formats = [
        f"{first_initial}{last}@{company_domain}.com",
        f"{first_name.lower()}.{last}@{company_domain}.com",
        f"{last}@{company_domain}.com",
    ]

    return random.choice(email_formats)


def generate_phone():
    """Generate a realistic US phone number."""
    area_code = random.choice(["212", "415", "617", "312", "214", "713", "404", "305", "602", "503"])
    exchange = random.randint(200, 999)
    number = random.randint(1000, 9999)
    return f"{area_code}-{exchange}-{number}"


def generate_notes(industry, lead_source, deal_value, status):
    """Generate realistic business notes."""
    pain_points = {
        "construction": "Looking to streamline project management",
        "tech": "Scaling infrastructure challenges",
        "healthcare": "Improving patient data management",
        "retail": "Optimizing inventory and supply chain",
        "manufacturing": "Reducing production costs",
        "consulting": "Need better client reporting tools"
    }

    notes = f"Lead source: {lead_source}\n"
    notes += f"Industry: {industry.capitalize()}\n"
    notes += f"Potential deal value: {deal_value}\n"
    notes += f"Status: {status}\n"
    notes += f"Pain point: {pain_points[industry]}"

    return notes


def seed_database(num_contacts=30):
    """Populate database with realistic sample contacts."""
    print("=" * 70)
    print("SEEDING CRM DATABASE WITH SAMPLE DATA")
    print("=" * 70)

    # Initialize database if needed
    print("\n📊 Initializing database...")
    init_database()

    with ContactManager() as cm:
        # Check if database already has data
        existing_count = cm.count_contacts()
        if existing_count > 0:
            print(f"\n⚠️  Database already contains {existing_count} contacts.")
            response = input("Clear existing data and reseed? (y/n): ").lower()
            if response == 'y':
                # Delete all existing contacts
                all_contacts = cm.get_all_contacts()
                for contact in all_contacts:
                    cm.delete_contact(contact.id)
                print(f"✓ Cleared {existing_count} existing contacts")
            else:
                print("Keeping existing data and adding new contacts...")

        print(f"\n📝 Creating {num_contacts} sample contacts...\n")

        created_contacts = []

        for i in range(num_contacts):
            # Pick random data
            first_name = random.choice(FIRST_NAMES)
            last_name = random.choice(LAST_NAMES)
            industry = random.choice(list(COMPANIES.keys()))
            company = random.choice(COMPANIES[industry])
            role = random.choice(ROLES)

            # Generate contact details
            name = f"{first_name} {last_name}"
            email = generate_email(first_name, last_name, company)
            phone = generate_phone()

            # Generate business context
            lead_source = random.choice(LEAD_SOURCES)
            deal_value = random.choice(DEAL_VALUES)
            status = random.choice(LEAD_STATUS)

            notes = generate_notes(industry, lead_source, deal_value, status)

            # Create the contact
            contact = cm.create_contact(
                name=name,
                email=email,
                phone=phone,
                company=f"{company} - {role}",
                notes=notes
            )

            created_contacts.append(contact)

            # Show progress every 5 contacts
            if (i + 1) % 5 == 0:
                print(f"  ✓ Created {i + 1}/{num_contacts} contacts...")

        print(f"\n✅ Successfully created {len(created_contacts)} contacts!")

        # Show some statistics
        print("\n" + "=" * 70)
        print("DATABASE STATISTICS")
        print("=" * 70)

        print(f"\nTotal contacts: {cm.count_contacts()}")

        # Count by industry
        print("\nContacts by industry:")
        for industry in COMPANIES.keys():
            results = cm.search_contacts(industry)
            print(f"  {industry.capitalize()}: {len(results)} contacts")

        # Show a few sample contacts
        print("\n" + "=" * 70)
        print("SAMPLE CONTACTS (First 3)")
        print("=" * 70)

        for i, contact in enumerate(created_contacts[:3], 1):
            print(f"\n[{i}] {contact.name}")
            print(f"    📧 {contact.email}")
            print(f"    📱 {contact.phone}")
            print(f"    🏢 {contact.company}")
            print(f"    📝 Notes:")
            for line in contact.notes.split('\n'):
                print(f"       {line}")

        print("\n" + "=" * 70)
        print("SEEDING COMPLETE!")
        print("=" * 70)
        print("\nTry these commands to explore the data:")
        print("  python3 -c 'from crud import ContactManager; cm = ContactManager(); cm.db.connect(); print(cm.search_contacts(\"tech\"))'")
        print("  sqlite3 crm.db 'SELECT name, company FROM contacts LIMIT 10;'")
        print("\n")


if __name__ == "__main__":
    seed_database(30)
