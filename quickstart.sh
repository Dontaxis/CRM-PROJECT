#!/bin/bash
# Quickstart script for CRM Learning Project
# Run this after opening in Codespaces or cloning the repo

echo "🚀 CRM Learning Project - Quickstart"
echo "===================================="
echo ""

# Check Python version
echo "✓ Checking Python..."
python3 --version

echo ""
echo "📦 No external dependencies needed (uses Python stdlib only)"
echo ""

# Run tests
echo "🧪 Running tests..."
python3 test_database.py

echo ""
echo "✅ Setup complete! Try these commands:"
echo ""
echo "  python3 demo.py           # Run demo with sample data"
echo "  python3 database.py       # Initialize empty database"
echo "  python3 main.py           # Start CLI interface (coming soon)"
echo ""
