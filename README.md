# QR Attendance System

A comprehensive attendance management system using QR codes with Django backend and Android mobile app.

## Features

- **Backend**: Django 5.0 with Python 3.11
- **Frontend**: HTML, CSS, JavaScript with Bootstrap
- **Database**: MySQL (Production), SQLite (Testing)
- **QR Code Generation**: Python qrcode library
- **Authentication**: Django built-in user system with role-based access (Lecturer, Student, Admin)
- **Mobile App**: Android Studio for QR scanning and student registration
- **Deployment**: Ubuntu VM with Gunicorn and Nginx

## Tech Stack

- **Backend Framework**: Django 5.0
- **Language**: Python 3.11
- **Database**: MySQL 8.0+, SQLite 3 (testing)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Mobile**: Android Studio, Java/Kotlin
- **Server**: Ubuntu, Nginx, Gunicorn
- **QR Code**: qrcode library

## Installation & Setup

### Backend Setup

1. Create virtual environment:
```bash
python3.11 -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
cd backend
pip install -r requirements.txt
```

3. Database setup:
```bash
python manage.py migrate
python manage.py createsuperuser
```

4. Run development server:
```bash
python manage.py runserver
```

## User Roles

- **Admin**: System administrator, manage users and courses
- **Lecturer**: Create courses, generate QR codes, view attendance reports
- **Student**: Scan QR codes to mark attendance

## License

MIT License
