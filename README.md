# TodoApp with FastAPI

A simple To-Do list web app built with **FastAPI**, **PostgreSQL**, and **Jinja2 templates**.
It lets you manage your daily tasks with authentication and full CRUD functionality.

---

## Features

- 🔑 User authentication (register, login, logout)
- 📝 Create, read, update, and delete todos
- ✅ Mark todos as complete or undo them
- 🎨 Responsive UI with Bootstrap
- 🗄️ Persistent storage using PostgreSQL
- ⚡ RESTful API powered by FastAPI

---

## Tech Stack

- **Backend:** FastAPI, SQLAlchemy  
- **Frontend:** Jinja2 Templates, Bootstrap  
- **Database:** PostgreSQL (default, configurable via SQLAlchemy URL)  
- **Static Files:** CSS, JS, Bootstrap  

---

## Installation

**Clone the repository**

git clone https://github.com/yourusername/todo-app.git  
cd todo-app

**Create a virtual environment**

python -m venv venv  
source venv/bin/activate   # Linux/Mac  
venv\Scripts\activate      # Windows

**Install dependencies**

pip install -r requirements.txt

**Set up the database**

SQLALCHEMY_DATABASE_URL = "postgresql://username:password@localhost/TodoApplicationDatabase"

**Run the app**

uvicorn main:app --reload

**Open in browser**

http://127.0.0.1:8000
