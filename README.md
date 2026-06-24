# 📝 Django Task Manager

[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)

#### A clean, full-stack task management web application built with **Django**. Supports creating, viewing, updating, and deleting tasks through a template-driven interface backed by Django's ORM and SQLite database.

---

## 🌟 Key Features

- **Task CRUD Operations** – Create, read, update, and delete tasks through a clean web interface
- **Django ORM Integration** – Persistent task storage using Django's built-in database layer with SQLite
- **Template-Driven UI** – Server-rendered HTML pages using Django's templating engine
- **Django Admin Panel** – Out-of-the-box admin interface for managing tasks directly
- **URL Routing** – Clean URL patterns for navigating between task views
- **Form Handling** – Django forms for validated task input and submission

---

## 🛠️ Tech Stack

- **Backend** – Python, Django
- **Database** – SQLite (Django default)
- **Frontend** – HTML5, Django Templates
- **Admin** – Django Admin

---

## 📂 Project Structure

```
Django-Task-Manager/
├── tasks/                  # Core Django app
│   ├── models.py           # Task data model
│   ├── views.py            # View logic for CRUD operations
│   ├── urls.py             # App-level URL routing
│   ├── forms.py            # Django forms for task input
│   ├── admin.py            # Admin panel registration
│   └── templates/          # HTML templates for task views
├── todoapp/                # Django project configuration
│   ├── settings.py         # Project settings
│   ├── urls.py             # Project-level URL configuration
│   └── wsgi.py             # WSGI entry point
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── .gitignore
```

---

## 🚀 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip

### Clone Repository

```bash
git clone https://github.com/MuhammadUsman-Khan/Django-Task-Manager.git
cd Django-Task-Manager
```

### Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser (Optional — for Admin Panel)

```bash
python manage.py createsuperuser
```

### Run the Development Server

```bash
python manage.py runserver
```

Access the app at: `http://127.0.0.1:8000`

Admin panel at: `http://127.0.0.1:8000/admin`

---

## 🎮 Usage

- **View Tasks** – Navigate to the home page to see all existing tasks
- **Create Task** – Use the task form to add a new task with a title and description
- **Update Task** – Edit any existing task through its detail or edit view
- **Delete Task** – Remove a task permanently from the list
- **Admin Panel** – Log in as a superuser to manage tasks directly via Django Admin

---

## 📈 Future Enhancements

- **User Authentication** – Register and login to manage personal task lists
- **Task Status Tracking** – Mark tasks as pending, in-progress, or completed
- **Due Dates & Priorities** – Add deadline and priority fields to tasks
- **Search & Filtering** – Filter tasks by status, date, or keyword
- **REST API** – Expose task data via Django REST Framework endpoints
- **Deployment** – Host on Railway, Render, or Heroku with PostgreSQL

---

## 🧠 Learning Outcomes

- Structuring a Django project with apps, models, views, and templates
- Implementing full CRUD functionality using Django's ORM and form system
- Working with Django's URL dispatcher and template inheritance
- Using the Django Admin interface for rapid data management
- Managing database migrations with `makemigrations` and `migrate`

---

## 👨‍💻 Developer

**Muhammad Usman Khan**

- GitHub: [@MuhammadUsman-Khan](https://github.com/MuhammadUsman-Khan)
- LinkedIn: [muhammad-usman-khan00](https://www.linkedin.com/in/muhammad-usman-khan00)
- Email: m.usman.khan.stu@gmail.com
