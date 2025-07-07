# Employee_api_with_drf
# Employee Management System (Django REST + Frontend)

This is a simple employee management web application built using **Django REST Framework** (DRF) for the backend and **HTML + Bootstrap + JavaScript** for the frontend. It supports user registration, login, city management, employee CRUD operations, and activation/deactivation of employees.

## Features

* 🔐 User Registration & Login with Token Authentication
* 🌆 Add and list cities
* 👥 Add, Update, Delete, and List Employees
* ✅ Activate / ❌ Deactivate Employees
* 🔄 Auto-clear input forms after submission

## Technologies Used

### Backend

* Python 3.x
* Django
* Django REST Framework
* Token Authentication

### Frontend

* HTML5
* Bootstrap 5
* JavaScript (Fetch API)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/employee-management.git
cd employee-management
```

### 2. Backend Setup

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Migrate database
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

### 3. Frontend Setup

The frontend is available in the `templates/frontend.html` file. You can view it by navigating to the API base URL or open it directly in your browser.

## API Endpoints

| Endpoint                          | Method         | Description                         |
| --------------------------------- | -------------- | ----------------------------------- |
| `/api/register/`                  | POST           | Register a new user                 |
| `/api/login/`                     | POST           | Login and get auth token            |
| `/api/logout/`                    | POST           | Logout and revoke token             |
| `/api/cities/`                    | GET/POST       | List or create cities               |
| `/api/employees/`                 | GET/POST       | List or create employees            |
| `/api/employees/<id>/`            | GET/PUT/DELETE | Retrieve, update or delete employee |
| `/api/employees/<id>/deactivate/` | PATCH          | Deactivate employee                 |
| `/api/employees/<id>/activate/`   | PATCH          | Activate employee                   |

## Screenshots

Add screenshots here if desired.

## Author

* **Aloknath Tiwari**
  [GitHub](https://github.com/Alok3k7)
  Email: [aloknathtiwari2000@gmail.com](mailto:aloknathtiwari2000@gmail.com)

## License

This project is licensed under the MIT License.
