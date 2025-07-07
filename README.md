# Employee Management System (Django REST + Frontend)

This is a full-stack employee management application built with Django REST Framework (DRF) and a Bootstrap-powered frontend. It supports user authentication, city management, employee operations, and logging of critical actions.

---

##  Features

* User Registration, Login, and Logout (Token-based auth)
* Add and View Cities
* CRUD Operations on Employees
* Activate or Deactivate Employees
* Auto-clear form inputs on submission
* Logging of key events to `logs/employee.log`

---

##  Tech Stack

### Backend:

* Python 3.12+
* Django 5.2+
* Django REST Framework
* Token Authentication

### Frontend:

* HTML
* Bootstrap 5
* JavaScript (Fetch API)

---

## Project Structure

```
drf_employee_project/
├── backend/                # App with models, views, serializers
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── drf_employee_project/  # Main Django settings & URLs
│   ├── settings.py
│   ├── urls.py
│
├── frontend/
│   └── index.html          # Bootstrap + JS based frontend
│
├── logs/
│   └── employee.log        # Log file (auto-created)
│
├── manage.py
└── requirements.txt
```

---

## API Endpoints

| Endpoint                          | Method         | Description                |
| --------------------------------- | -------------- | -------------------------- |
| `/api/register/`                  | POST           | Register new user          |
| `/api/login/`                     | POST           | Login and receive token    |
| `/api/logout/`                    | POST           | Logout current user        |
| `/api/cities/`                    | GET/POST       | List or create cities      |
| `/api/employees/`                 | GET/POST       | List or create employees   |
| `/api/employees/<id>/`            | GET/PUT/DELETE | Retrieve, update or delete |
| `/api/employees/<id>/deactivate/` | PATCH          | Deactivate employee        |
| `/api/employees/<id>/activate/`   | PATCH          | Activate employee          |

---

##  Logging

* All actions (like city/employee creation, activation, deletion) are logged in `logs/employee.log`
* Log format includes timestamp, level, and action message

---

## Setup Instructions

### Clone the repo

```bash
git clone https://github.com/yourusername/employee-api-project.git
cd employee-api-project
```

### Backend Setup

```bash
python3 -m venv venv
source venv/bin/activate  # Or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend

* Open `frontend/index.html` in your browser

---

## Author

**Aloknath Tiwari**
📧 [aloknathtiwari2000@gmail.com](mailto:aloknathtiwari2000@gmail.com)
🔗 [GitHub](https://github.com/Alok3k7)

---

## License

This project is open-source and available under the MIT License.
