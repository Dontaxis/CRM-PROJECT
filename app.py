"""
Flask web application for the CRM system.
Provides a web interface for managing contacts.
"""

from flask import Flask, render_template, request, redirect, url_for, flash
from crud import ContactManager
from database import init_database

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-in-production'  # For flash messages

# Initialize database on startup
init_database()


@app.route('/')
def index():
    """Homepage - show all contacts."""
    with ContactManager() as cm:
        contacts = cm.get_all_contacts()
        total_count = cm.count_contacts()
    return render_template('index.html', contacts=contacts, total_count=total_count)


@app.route('/contact/<int:contact_id>')
def view_contact(contact_id):
    """View a single contact's details."""
    with ContactManager() as cm:
        contact = cm.get_contact(contact_id)
    if not contact:
        flash('Contact not found', 'error')
        return redirect(url_for('index'))
    return render_template('view_contact.html', contact=contact)


@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    """Add a new contact."""
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        company = request.form.get('company')
        notes = request.form.get('notes')

        # Validate required fields
        if not name:
            flash('Name is required', 'error')
            return render_template('add_contact.html')

        # Create the contact
        with ContactManager() as cm:
            contact = cm.create_contact(
                name=name,
                email=email or None,
                phone=phone or None,
                company=company or None,
                notes=notes or None
            )

        flash(f'Contact "{contact.name}" added successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('add_contact.html')


@app.route('/edit/<int:contact_id>', methods=['GET', 'POST'])
def edit_contact(contact_id):
    """Edit an existing contact."""
    with ContactManager() as cm:
        contact = cm.get_contact(contact_id)

    if not contact:
        flash('Contact not found', 'error')
        return redirect(url_for('index'))

    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        company = request.form.get('company')
        notes = request.form.get('notes')

        # Validate required fields
        if not name:
            flash('Name is required', 'error')
            return render_template('edit_contact.html', contact=contact)

        # Update the contact
        with ContactManager() as cm:
            cm.update_contact(
                contact_id=contact_id,
                name=name,
                email=email or None,
                phone=phone or None,
                company=company or None,
                notes=notes or None
            )

        flash(f'Contact "{name}" updated successfully!', 'success')
        return redirect(url_for('view_contact', contact_id=contact_id))

    return render_template('edit_contact.html', contact=contact)


@app.route('/delete/<int:contact_id>', methods=['POST'])
def delete_contact(contact_id):
    """Delete a contact."""
    with ContactManager() as cm:
        contact = cm.get_contact(contact_id)
        if contact:
            contact_name = contact.name
            cm.delete_contact(contact_id)
            flash(f'Contact "{contact_name}" deleted successfully', 'success')
        else:
            flash('Contact not found', 'error')

    return redirect(url_for('index'))


@app.route('/search')
def search():
    """Search for contacts."""
    query = request.args.get('q', '')

    if not query:
        return redirect(url_for('index'))

    with ContactManager() as cm:
        results = cm.search_contacts(query)

    return render_template('search_results.html', results=results, query=query)


if __name__ == '__main__':
    # Run the Flask app
    # host='0.0.0.0' makes it accessible from outside the container (important for Codespaces)
    app.run(debug=True, host='0.0.0.0', port=5000)
