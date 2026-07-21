# QIS Virtual Campus Guide

## Project Description

**QIS Virtual Campus Guide** is a simple college website built with Django. It allows students to explore college information, browse courses, view the campus gallery, watch a virtual campus tour, and submit admission enquiries.

This project is designed for **freshers learning Django basics** — the code is clean, simple, and easy to explain in interviews.

## Features

- **Home Page** — Hero banner, about section, why choose QIS, courses preview, placement highlights
- **About Page** — College introduction, vision, mission, and facilities
- **Courses Page** — Bootstrap cards showing all courses with details
- **Gallery Page** — Image gallery managed from admin panel
- **Campus Tour Page** — Embedded YouTube video and facility cards
- **Enquiry Page** — ModelForm for admission enquiry submission
- **Contact Page** — Address, phone, email, and Google Map
- **Admin Panel** — Manage courses, view enquiries, upload gallery images

## Technologies Used

- Python 3
- Django 4.2
- SQLite
- HTML, CSS, JavaScript
- Bootstrap 5
- Bootstrap Icons

## Installation Steps

### 1. Clone or download the project

```bash
cd qis-virtual-campus-guide
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run database migrations

```bash
python manage.py migrate
```

### 5. Load sample courses

```bash
python manage.py load_courses
```

### 6. Create admin user

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Open **http://127.0.0.1:8000/** in your browser.

Admin panel: **http://127.0.0.1:8000/admin/**

## Folder Structure

```
qis-virtual-campus-guide/
├── manage.py
├── requirements.txt
├── README.md
├── qis_campus/          # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                # Home, About, Gallery, Campus Tour, Contact
│   ├── models.py        # Gallery model
│   ├── views.py
│   └── urls.py
├── courses/             # Course listing and details
│   ├── models.py        # Course model
│   ├── views.py
│   └── urls.py
├── enquiry/             # Admission enquiry form
│   ├── models.py        # Enquiry model
│   ├── forms.py         # EnquiryForm (ModelForm)
│   ├── views.py
│   └── urls.py
├── templates/           # HTML templates
├── static/              # CSS, JS, images
└── media/               # Uploaded files (courses, gallery)
```

## Django Concepts Used

- Models and Django ORM
- Function-Based Views
- URL Routing
- Templates and Template Inheritance
- ModelForms
- Django Admin
- Messages Framework
- Static Files and Media Files

## Future Improvements

- User authentication for students
- Online application form with document upload
- Email notification on enquiry submission
- Course search and filter
- Blog/News section for college updates
- Faculty profile pages
- Placement statistics dashboard

## Author

Built as a fresher portfolio project to demonstrate Django fundamentals.
