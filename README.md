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
- **Architecture**: Command-line interface to start, potentially web-based later

## Project Structure

```
crm-project/
├── README.md           # This file
├── .gitignore         # Python and database files to exclude
├── database.py        # Database setup and connection
├── models.py          # Contact data model
├── crud.py            # CRUD operations for contacts
├── test_database.py   # Tests to verify database operations
├── demo.py            # Simple demo of the CRM in action
└── main.py            # Entry point and CLI interface (WIP)
```

## Core Features

- **Contact Management**: Store and manage contact information (name, email, phone, company, notes)
- **CRUD Operations**: Create, Read, Update, Delete contacts
- **Search Functionality**: Find contacts by name or company
- **SQLite Database**: Simple, file-based database perfect for learning

## Getting Started

### GitHub Codespaces (Recommended)

1. Click the **Code** button on GitHub
2. Select **Codespaces** tab
3. Click **Create codespace on main** (or your branch)
4. Once it loads, run the quickstart:
   ```bash
   ./quickstart.sh
   ```

**Why Codespaces?** Everything is pre-configured - Python, Git, and a full development environment in your browser.

### Local Setup

```bash
# Clone the repo
git clone <your-repo-url>
cd CRM-PROJECT

# Run the tests to verify everything works
python3 test_database.py

# Run the demo to see CRUD operations in action
python3 demo.py

# Initialize the database manually
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

🚧 **In Development** - Currently setting up the foundation
