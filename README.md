# cheftp-api

A Django REST API that powers the contact form for the cheftp. Built to handle customer inquiries cleanly and efficiently.

- Handles contact form submissions through a REST API
- Validates incoming data and provides clear error messages
- Includes an admin panel to manage contact requests
- Ready for frontend integration with CORS support
- Token-based authentication available
- Full CRUD operations for contact management

### What you'll need
- Python 3.8 or newer
- pip (comes with Python)
- virtualenv (optional but recommended)

### Setting it up

1. **Grab the code**
   
   cd cheftp-api
   

2. **Set up a virtual environment**
   
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   

3. **Install the dependencies**
   
   pip install -r requirements.txt
   

4. **Configure your environment**
   
   cp .env.example .env
   # Open .env and add your settings
   

5. **Set up the database**
   
   python manage.py migrate
   

6. **Create an admin account**
   
   python manage.py createsuperuser
   

7. **Run the server**
   
   python manage.py runserver 0.0.0.0:8000
   

Your API is now running at `http://localhost:8000/api/`

## API Endpoints

### POST /api/contact/
Create a new contact request.


### GET /api/contact/list/
List all contact requests (requires authentication).

### GET /api/contact/{id}/
Get details of a specific contact request (requires authentication).

### PUT /api/contact/{id}/
Update a contact request (requires authentication).

### DELETE /api/contact/{id}/
Delete a contact request (requires authentication).

## Connecting Your Frontend
The API accepts requests from:
- `http://localhost:3000` (when developing)
- `https://www.cheftp.com` (when it's live)


## Admin Panel

Head to `http://localhost:8000/admin/` to:
- View all customer requests
- Mark requests as read or replied to
- Search through messages by name or email
- Filter by status
- Manage contact data


## Configuration

### Environment Variables (.env)
```
SECRET_KEY=your-secret-key-here-change-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```


## The Data Model

Each contact request stores:
- **id** (auto-generated, read-only)
- **full_name** (required, max 255 chars)
- **email** (required, validated email format)
- **phone_number** (required, max 20 chars)
- **address** (required, max 500 chars)
- **date_requested** (required, datetime)
- **message** (required, text field)
- **status** (auto-managed: new/read/replied, defaults to 'new')
- **created_at** (auto-generated timestamp)

## Tech Stack

- **Django 6.0.3** - The web framework
- **Django REST Framework 3.16.1** - API toolkit with token authentication
- **django-cors-headers 4.9.0** - Handles cross-origin requests
- **djangorestframework-authtoken 1.2.0** - Token-based authentication
- **SQLite** - Database for development
- **python-dotenv 1.2.2** - Environment variable management
- **locust 2.17.0** - Load testing tool

## Authentication

The API uses token-based authentication for protected endpoints:
- `/api/contact/list/` - Requires authentication
- `/api/contact/{id}/` - Requires authentication for GET, PUT, DELETE
- `/api/contact/` - Public endpoint for creating new requests

To use authenticated endpoints, include an Authorization header:
```
Authorization: Token your-auth-token-here
```