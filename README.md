# FastAPI URL Shortener API

A simple URL shortener service built with FastAPI and SQLAlchemy.  
This project demonstrates how to create a secure, database-backed URL shortener with user registration and login functionality.

---

-Live Url: https://urlapi-r5yr.onrender.com/

-Documentation Link: https://urlapi-r5yr.onrender.com/docs

## Features

- User registration and login  
- JWT-based authentication (optional to add)  
- Create shortened URLs with unique codes  
- Redirect from short URL to original URL  
- Track number of clicks on each shortened URL  
- SQLite database integration using SQLAlchemy ORM  
- CORS middleware enabled for frontend interaction

---

## Tech Stack

- **FastAPI** - Web framework  
- **SQLAlchemy** - ORM for database operations  
- **SQLite** - Lightweight database (can be swapped for MySQL/PostgreSQL)  
- **Pydantic** - Data validation and serialization  
- **Python 3.9+**

---

## Getting Started

### Prerequisites

- Python 3.9 or newer installed  
- `pip` package manager  

### Installation

1. Clone the repository  
```bash
git clone https://github.com/your-username/fastapi-url-shortener.git
cd fastapi-url-shortener 
```

2. Create and Activate Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the application

```bash 
uvicorn main:app --reload
```

## 🌐 Frontend Interface
A basic frontend is provided inside the frontend/ folder to interact with the API:

### 📂 frontend/index.html
Login and register forms

Stores JWT access token in sessionStorage

### 📂 frontend/shorten.html
Allows authenticated users to shorten URLs

Displays shortened URL

Preserves last shortened result using sessionStorage

Redirects to login page if user is not authenticated

To test the frontend:

Open frontend/index.html in your browser to register or login

Once logged in, navigate to frontend/shorten.html to shorten URLs

``💡 Make sure your backend is running at http://127.0.0.1:8000``
``Use Live Server extension in VSCode for better local dev``

## API END POINT

| Method | Endpoint      | Description                        | Auth |
| ------ | ------------- | ---------------------------------- | ---- |
| POST   | `/register`   | Register a new user                | ❌    |
| POST   | `/login`      | Login a user                       | ❌    |
| POST   | `/shorten`    | Create a shortened URL             | ✅    |
| GET    | `/get_all`    | Get all shortened URLs (for debug) | ❌    |
| GET    | `/{url_code}` | Redirect to original URL           | ❌    |



## 🔐 Register a new user
### POST /register
```
{
  "names": "John Doe",
  "email": "john@example.com",
  "password": "StrongPassword123"
}
```

## 🔑 Login user
### POST /login

```
{
  "email": "john@example.com",
  "password": "StrongPassword123"
}

```

Returns:

```
{
    "status": 200,
    "message": "User logged in",
    "access_token":"................"
}

```
## 🔗 Shorten a URL
### POST /shorten

```
{
  "valid": "https://www.example.com"
}

```

Return:
```
{
    "message": "URL shortened well",
    "shorten_url": "http://127.0.0.1:8000/RprNAa68",
    "data": {
        "valid": "https://github.com",
        "code": "RprNAa68",
        "created_at": "2000-00-12T13:17:55.436658",
        "clicks": 0,
        "id": "70d8c8ab-6d5c-4b07-b2c2-e79a7668e2ab",
        "expires_at": null
    }
}
```

## ↪️ Redirect using short code
### GET /{url_code}

Example:
`GET /abc123xy`
Redirects to original URL.

## PROJECT STRUCTURE
<pre>
.
├── main.py              # FastAPI app and routes
├── models.py            # Pydantic & SQLAlchemy models
├── demo.py              # Code generator and utility functions
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
├── db/
│   ├── database.py      # SQLAlchemy DB setup
│   └── models.py        # SQLAlchemy models
├── frontend/
│   ├── index.html       # Login & Register page
│   └── shorten.html     # URL shortening interface

</pre>
