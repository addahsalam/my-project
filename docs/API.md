# QR Attendance System - API Documentation

## Base URL
http://localhost:8000/api

## Authentication
All endpoints require session authentication.

## Endpoints

### Users
- GET /users/users/ - List all users
- GET /users/users/{id}/ - Get user details
- GET /users/users/me/ - Get current user profile
- POST /users/profiles/ - Create user profile

### Courses
- GET /courses/courses/ - List all courses
- POST /courses/courses/ - Create course
- GET /courses/courses/{id}/ - Get course details
- PUT /courses/courses/{id}/ - Update course
- DELETE /courses/courses/{id}/ - Delete course

### Attendance
- GET /attendance/sessions/ - List sessions
- POST /attendance/sessions/ - Create session
- POST /attendance/sessions/{id}/mark_attendance/ - Mark attendance
- GET /attendance/records/ - List records

### QR Codes
- GET /qrcode/qrcodes/ - List QR codes
- POST /qrcode/qrcodes/generate/ - Generate QR code
