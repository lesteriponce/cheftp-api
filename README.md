# cheftp-api

A Django REST Framework API for managing contact form submissions on the cheftp. Provides a customer inquiries, and an admin for request management.

## Requirements

- Python 3.8+
- pip
- virtualenv 

## Installation

1. **Clone the repository and navigate into the project directory**
   
   git clone https://github.com/lesteriponce/cheftp-api.git
   cd cheftp-api
   

2. **Create and activate a virtual environment**
   
   python3 -m venv venv
   source venv/bin/activate        # macOS/Linux
   venv\Scripts\activate           # Windows
   

3. **Install dependencies**
   
   pip install -r requirements.txt
   

4. **Set up environment variables**
   
   cp .env.example .env
   

5. **Apply database migrations**
   
   python manage.py migrate
   

6. **Create a superuser account**
   
   python manage.py createsuperuser
   

## Configuration

`SECRET_KEY`  - your-secret-key-here
`DEBUG`  - must be `False` in production
`ALLOWED_HOSTS`  -`localhost,127.0.0.1` 

## Running the Server

python manage.py runserver 


The API will be available at `http://localhost:8000/api/`.

## API Reference

### Public Endpoints

#### POST /api/contact/
Submit a new contact request. No authentication required.

**Request body:**
```json
{
  "full_name": "Lester Ponce",
  "email": "lesteriponc@example.com",
  "phone_number": "+1-555-1234",
  "address": "024 Main Street, Manila",
  "date_requested": "2025-06-01T10:00:00Z",
  "message": "I would like more information about your services."
}
```

### Authenticated Endpoints

- **GET /api/contact/list/**
  Returns a list of all contact submissions.

- **GET /api/contact/{id}/**
  Returns the details of a single contact submission.

- **PUT /api/contact/{id}/**
  Updates a contact submission by ID.

- **DELETE /api/contact/{id}/**
  Deletes a contact submission by ID.

## Authentication

Protected endpoints use token-based authentication. Include the token in the request header:

Authorization: Token <your-auth-token>


To generate a token for a user:

python manage.py drf_create_token <username>


## Data Model

 `id` | Auto-generated, read-only 
 `full_name` | Required. Max 255 characters 
 `email` | Required. Must be a valid email address 
 `phone_number` | Required. Max 20 characters 
 `address` | Required. Max 500 characters 
 `date_requested` | DateTime | Required 
 `message` | Text | Required 
 `status` | Auto-managed. Values: `new`, `read`, `replied`. Defaults to `new` 
 `created_at` | Auto-generated on creation 

## Admin Interface

The Django admin panel is available at `http://localhost:8000/admin/`.

**Supported operations:**

- View all contact submissions
- Update submission status (new, read, replied)
- Search submissions by name or email
- Filter submissions by status

## CORS Configuration

- `http://localhost:3000` — local development
- `https://www.cheftp.com` — production


## Tech Stack

Django - 6.0.3 Web framework 
Django REST Framework - 3.16.1  API toolkit and token authentication 
django-cors-headers - 4.9.0  Cross-origin request handling 
djangorestframework-authtoken - 1.2.0  Token-based auth support 
python-dotenv - 1.2.2  Environment variable management 
SQLite - Development database 