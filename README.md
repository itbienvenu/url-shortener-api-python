# FastAPI URL Shortener API

A simple URL shortener service built with FastAPI and SQLAlchemy.  
This project demonstrates how to create a secure, database-backed URL shortener with user registration and login functionality.

---

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

#API END POINT

| Method | Path          | Description                            |
| ------ | ------------- | -------------------------------------- |
| POST   | `/register`   | Register a new user                    |
| POST   | `/login`      | Login a user                           |
| POST   | `/shorten`    | Create a shortened URL (auth required) |
| GET    | `/get_all`    | List all shortened URLs                |
| GET    | `/{url_code}` | Redirect to the original URL           |

#PROJECT STRUCTURE

.
├── main.py            # FastAPI app and routes
├── models.py          # Pydantic models and SQLAlchemy models
├── db/
│   ├── database.py    # Database connection and session setup
│   └── models.py      # SQLAlchemy models
├── demo.py            # Utility functions (e.g. code generator)
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
