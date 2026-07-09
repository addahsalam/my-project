# Setup Guide

## Prerequisites
- Python 3.11
- MySQL 8.0+
- Django 5.0
- Ubuntu 20.04+

## Installation

1. Clone repository:
```bash
git clone https://github.com/addahsalam/my-project.git
cd my-project && git checkout qr-attendance-system
```

2. Create virtual environment:
```bash
python3.11 -m venv venv && source venv/bin/activate
```

3. Install dependencies:
```bash
cd backend && pip install -r requirements.txt
```

4. Configure environment:
```bash
cp .env.example .env
```

5. Run migrations:
```bash
python manage.py migrate
python manage.py createsuperuser
```

6. Start server:
```bash
python manage.py runserver
```

## Testing
```bash
python manage.py test
```
