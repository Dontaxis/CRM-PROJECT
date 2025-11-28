# CRM Learning Project

A learning project to understand how Customer Relationship Management (CRM) systems work by building one from scratch.

## Purpose

This project is built to:
- Understand the core concepts behind CRM systems
- Practice Python programming and database design
- Learn about data relationships and business logic
- Build something practical that can be extended over time

## Technology Stack

- **Language**: Python 3
- **Database**: SQLite (simple, file-based database perfect for learning)
- **Web Framework**: Flask (for the web interface)
- **Architecture**: Modern web-based UI with HTML/CSS templates

## Project Structure

```
crm-project/
├── README.md           # This file
├── .gitignore         # Python and database files to exclude
├── app.py             # Flask web application (main entry point)
├── database.py        # Database setup and connection
├── models.py          # Contact data model
├── crud.py            # CRUD operations for contacts
├── seed_data.py       # Populate database with realistic sample data
├── test_database.py   # Tests to verify database operations
├── demo.py            # Simple demo of the CRM in action
├── templates/         # HTML templates for web interface
│   ├── base.html
│   ├── index.html
│   ├── add_contact.html
│   ├── edit_contact.html
│   ├── view_contact.html
│   └── search_results.html
└── static/            # CSS and static files
    └── css/
        └── style.css
```

## Core Features

- **Web Interface**: Modern, professional UI accessible in your browser
- **Contact Management**: Store and manage contact information (name, email, phone, company, notes)
- **CRUD Operations**: Create, Read, Update, Delete contacts via web forms
- **Search Functionality**: Find contacts by name or company
- **Sample Data**: Realistic seed data with 30 contacts across 6 industries
- **SQLite Database**: Simple, file-based database perfect for learning

## Getting Started

### GitHub Codespaces (Recommended)

1. Click the **Code** button on GitHub
2. Select **Codespaces** tab
3. Click **Create codespace on main** (or your branch)
4. Once it loads, install dependencies and run:
   ```bash
   pip install -r requirements.txt
   python3 seed_data.py    # Populate with sample data
   python3 app.py          # Start the web server
   ```
5. Click **"Open in Browser"** when the port notification appears
6. Your CRM will open in a new tab at `http://localhost:5000`

**Why Codespaces?** Everything is pre-configured - Python, Git, and a full development environment in your browser.

### Local Setup

```bash
# Clone the repo
git clone <your-repo-url>
cd CRM-PROJECT

# Install dependencies
pip install -r requirements.txt

# Populate database with sample data
python3 seed_data.py

# Start the web server
python3 app.py
```

Then open your browser to `http://localhost:5000`

### Testing & Development

```bash
# Run the tests to verify database operations
python3 test_database.py

# Run the demo to see CRUD operations in terminal
python3 demo.py

# Initialize an empty database
python3 database.py
```

## Database Schema

**Contacts Table:**
- `id` - Auto-incrementing primary key
- `name` - Contact's full name (required)
- `email` - Email address (optional)
- `phone` - Phone number (optional)
- `company` - Company name (optional)
- `notes` - Additional notes (optional)
- `created_at` - Timestamp of creation

## Learning Journey

This is a learning project to understand CRM systems from the ground up. The focus is on:
1. Clean, readable code
2. Proper data modeling
3. Understanding relationships between entities
4. Building something that actually works

## Status

✅ **Functional** - Web interface complete with full CRUD operations

**What's Working:**
- ✅ SQLite database with contacts table
- ✅ Full CRUD operations (Create, Read, Update, Delete)
- ✅ Professional web interface with Flask
- ✅ Search functionality
- ✅ Realistic sample data seeder
- ✅ Responsive design

**Future Enhancements:**
- Add more tables (deals, interactions, tasks)
- User authentication
- Export contacts to CSV
- Email integration
- Dashboard with analytics
