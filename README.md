# TodoApp with FastAPI

A simple To-Do list web app built with FastAPI backend and SQLite for storage. Manage your tasks easily with basic CRUD operations.

## Features

- Create, read, update, and delete tasks  
- Persistent storage using Postgrsql database  
- Clean RESTful API built with FastAPI  
- Modular and easy-to-extend code structure
- 
## Prerequisites

- Python 3.8 or higher  
- Required Python packages:
  - fastapi
  - uvicorn
  - sqlalchemy
  - passlib[bcrypt]
  - bcrypt==3.2.0
  - python-multipart
  - python-jose[cryptography]
  - psycopg2-binary 

## Setup

1. Clone this repository

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
