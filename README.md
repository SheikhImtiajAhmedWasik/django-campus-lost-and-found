# 🔎 Campus Lost & Found System

### 🎓 A Django-Based Lost & Found Management System for Campus

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![Django](https://img.shields.io/badge/Django-5.x-success?style=for-the-badge\&logo=django)
![Database](https://img.shields.io/badge/Database-SQLite-lightgrey?style=for-the-badge)
![Authentication](https://img.shields.io/badge/Authentication-Django-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Project-Assignment-purple?style=for-the-badge)

---

## 📌 Project Overview

**Campus Lost & Found System** is a real-world Django web application designed to help students and campus users report, find, and manage lost or found items.

Users can register and log in to the system, create Lost or Found reports, search and filter existing reports, and manage their own submissions.

The project is designed to practice several important Django concepts, including:

```text
Forms
  ↓
Templates
  ↓
CRUD
  ↓
Authentication
  ↓
Django ORM
  ↓
Middleware
  ↓
Messages
```

---

# 🎯 Objective

Build a real-life **Campus Lost & Found System** using Django to gain practical experience with:

* 📝 Django Forms
* 🎨 Templates
* 🔄 CRUD Operations
* 🔐 User Authentication
* ⚙️ Custom Middleware
* 🗄️ Django ORM
* 💬 Django Messages

---

# ✨ Key Features

## 🔐 1. User Authentication

Users can:

* 📝 Register
* 🔑 Login
* 🚪 Logout

Every Lost/Found report is associated with the **logged-in user who created it**.

This ensures that users can manage their own reports securely.

### User Flow

```text
Register
   ↓
Login
   ↓
Create Report
   ↓
Manage Own Reports
   ↓
Logout
```

---

# 📦 2. Lost & Found Reports

Authenticated users can create reports containing the following information:

| Field                  | Description                         |
| ---------------------- | ----------------------------------- |
| 🏷️ Item Name          | Name of the lost or found item      |
| 🔄 Type                | Lost / Found                        |
| 📂 Category            | Item category                       |
| 📝 Description         | Detailed information about the item |
| 📍 Location            | Where the item was lost/found       |
| 📅 Date                | Date related to the report          |
| 📞 Contact Information | Contact details                     |
| 🖼️ Image              | Optional item image                 |

### Example

```text
Item Name: ID Card
Type: Lost
Category: Documents
Description: Student ID card lost near the library.
Location: Central Library
Date: 2026-09-01
Contact: 01XXXXXXXXX
Image: Optional
```

---

# 🔄 3. Complete CRUD Operations

The system implements complete **CRUD** functionality.

| Operation  | Function                        |
| ---------- | ------------------------------- |
| 🆕 Create  | Create a new Lost/Found report  |
| 👁️ Read   | View reports and report details |
| ✏️ Update  | Edit your own report            |
| 🗑️ Delete | Delete your own report          |

### 🔒 Ownership Protection

Users are only allowed to:

* Edit their own reports
* Delete their own reports
* Mark their own reports as resolved

Users **cannot modify or delete another user's report**.

This provides an important layer of authorization and data protection.

---

# 🔎 4. Search & Filter

Users can search and filter reports using:

* 🔍 Item Name
* 📂 Category
* 🔄 Lost / Found
* 📊 Report Status

### Example Search

```text
Search: ID Card
Type: Lost
Category: Documents

[ Search ]
```

The system then displays reports matching the selected criteria.

---

# 📊 5. Report Status

Each report has a status:

* 🟢 **Active**
* ✅ **Resolved**

The owner of a report can mark it as **Resolved** once the lost/found item issue has been successfully handled.

### Status Flow

```text
New Report
    │
    ▼
  Active
    │
    │ Owner marks as resolved
    ▼
 Resolved
```

---

# 🧩 6. Django Templates

The project uses **Django Template Inheritance** to maintain a consistent layout throughout the website.

### Required Templates

```text
base.html
home.html
reports.html
report_detail.html
report_form.html
login.html
register.html
my_reports.html
```

### Template Structure

```text
             base.html
                 │
        ┌────────┼─────────┐
        │        │         │
        ▼        ▼         ▼
      home    reports    login
        │        │
        │        ▼
        │   report_detail
        │
        ├── register
        ├── report_form
        └── my_reports
```

`base.html` is used for the common:

* Navbar
* Page layout
* CSS/static resources
* Shared components

This avoids repeating the same HTML structure across multiple pages.

---

# ⚙️ 7. Custom Middleware

A custom Django middleware is implemented to log information about incoming requests.

The middleware records:

* 👤 User
* 🌐 Request Method
* 🔗 URL / Path
* ⏱️ Request Processing Time

### Example Terminal Output

```text
User: Rahim
Method: POST
Path: /reports/create/
Time: 0.08 seconds
```

The log can be displayed directly in the terminal while the Django development server is running.

### Middleware Flow

```text
User Request
     │
     ▼
Custom Middleware
     │
     ├── Capture User
     ├── Capture Method
     ├── Capture Path
     ├── Measure Request Time
     │
     ▼
Django View
     │
     ▼
Response
```

---

# 💬 8. Django Messages

The project uses Django's built-in **Messages Framework** to provide feedback after important actions.

### Example Messages

```text
Report created successfully!
```

```text
Report updated successfully!
```

```text
Report deleted successfully!
```

```text
Report marked as resolved!
```

These messages help users understand whether their actions were completed successfully.

---

# 🛠️ Django Concepts Practiced

| Django Concept    | Usage                                    |
| ----------------- | ---------------------------------------- |
| 🗃️ Models        | Store report and user-related data       |
| 📝 Forms          | Create and validate report/user input    |
| 👁️ Views         | Handle application logic                 |
| 🔗 URLs           | Define application routes                |
| 🎨 Templates      | Display dynamic content                  |
| 🔐 Authentication | Register, login, and logout              |
| 🗄️ Django ORM    | Interact with the database               |
| ⚙️ Middleware     | Log user requests                        |
| 💬 Messages       | Display action feedback                  |
| 🔄 CRUD           | Create, read, update, and delete reports |

---

# 📂 Suggested Project Structure

```text
django-campus-lost-and-found/
│
├── manage.py
│
├── lost_found/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── middleware.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── reports.html
│   ├── report_detail.html
│   ├── report_form.html
│   ├── login.html
│   ├── register.html
│   └── my_reports.html
│
├── static/
│   └── css/
│       └── style.css
│
├── media/
│   └── reports/
│
├── db.sqlite3
├── requirements.txt
└── README.md
```

> The exact folder structure may vary depending on how the Django project and application are organized.

---

# 🚀 Installation & Setup

Follow the steps below to run the project locally.

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/django-campus-lost-and-found.git
```

Navigate to the project directory:

```bash
cd django-campus-lost-and-found
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

If `requirements.txt` is available:

```bash
pip install -r requirements.txt
```

Otherwise, install Django:

```bash
pip install django
```

---

## 4. Apply Database Migrations

Run:

```bash
python manage.py makemigrations
```

Then:

```bash
python manage.py migrate
```

---

## 5. Create a Superuser

If the project includes Django Admin functionality, create an admin account:

```bash
python manage.py createsuperuser
```

Follow the instructions displayed in the terminal.

---

## 6. Run the Development Server

Start the Django server:

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

---

# 🧪 Example User Workflow

A typical user interaction with the application looks like this:

```text
                  ┌───────────────┐
                  │    Register   │
                  └───────┬───────┘
                          │
                          ▼
                  ┌───────────────┐
                  │     Login     │
                  └───────┬───────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Browse Reports    │
                └─────────┬─────────┘
                          │
              ┌───────────┴───────────┐
              ▼                       ▼
       Create Report            Search / Filter
              │                       │
              ▼                       ▼
       Manage Own Report        View Report
              │
       ┌──────┼───────┐
       ▼      ▼       ▼
     Edit   Delete  Resolve
```

---

# 📸 Screenshots

Add screenshots of your completed application here.

Replace the example paths below with your actual screenshots.

## 🏠 Home Page

![Home Page](screenshots/home.png)

---

## 🔐 Login Page

![Login Page](screenshots/login.png)

---

## 📋 Reports Page

![Reports Page](screenshots/reports.png)

---

## 📖 Report Details

![Report Details](screenshots/report-detail.png)

---

## 📝 Create Report

![Create Report](screenshots/create-report.png)

---

## 👤 My Reports

![My Reports](screenshots/my-reports.png)

---

# 🔒 Security & Authorization

The application ensures that users cannot modify other users' reports.

For update and delete operations:

```text
User
 │
 ▼
Is the user authenticated?
 │
 ├── No ──► Login Required
 │
 └── Yes
       │
       ▼
Is the report owned by the user?
       │
       ├── No ──► Access Denied
       │
       └── Yes
              │
              ▼
        Allow the action
```

This ownership-based authorization is an important part of the application's security.

---

# 📋 Feature Checklist

| Feature                  | Status |
| ------------------------ | :----: |
| User Registration        |    ✅   |
| User Login               |    ✅   |
| User Logout              |    ✅   |
| Create Reports           |    ✅   |
| View Reports             |    ✅   |
| Report Details           |    ✅   |
| Update Own Reports       |    ✅   |
| Delete Own Reports       |    ✅   |
| Search Reports           |    ✅   |
| Filter Reports           |    ✅   |
| Lost / Found Type        |    ✅   |
| Active / Resolved Status |    ✅   |
| Optional Image           |    ✅   |
| Template Inheritance     |    ✅   |
| Custom Middleware        |    ✅   |
| Request Logging          |    ✅   |
| Django Messages          |    ✅   |
| Django ORM               |    ✅   |

---

# 🎓 Learning Outcomes

By completing this project, you will gain practical experience with:

* Building a real-world Django application
* Creating database models
* Working with Django ORM
* Creating and validating forms
* Implementing authentication
* Protecting user-owned data
* Implementing CRUD operations
* Building dynamic templates
* Using template inheritance
* Implementing search and filtering
* Working with Django Messages
* Creating custom middleware
* Handling optional image uploads
* Organizing a Django project

---

# 🧠 Core Django Architecture

The project brings several Django concepts together:

```text
             ┌──────────────┐
             │     User     │
             └──────┬───────┘
                    │
                    ▼
             ┌──────────────┐
             │     URL      │
             └──────┬───────┘
                    │
                    ▼
             ┌──────────────┐
             │     View     │
             └──────┬───────┘
                    │
             ┌──────┴───────┐
             ▼              ▼
       ┌───────────┐  ┌────────────┐
       │   Forms   │  │    ORM     │
       └───────────┘  └─────┬──────┘
                            │
                            ▼
                       ┌─────────┐
                       │  Model  │
                       └────┬────┘
                            │
                            ▼
                       ┌─────────┐
                       │Database │
                       └─────────┘

                    View
                     │
                     ▼
                 Template
                     │
                     ▼
                Web Response
```

---

# 📌 Future Improvements

Possible future enhancements include:

* 📧 Email notifications when a matching item is reported
* 🔍 Advanced search
* 📍 Map-based location selection
* 🔔 Notification system
* ❤️ Save/bookmark reports
* 💬 User-to-user communication
* 📱 Improved mobile responsive design
* 🖼️ Multiple image uploads
* 🛡️ More advanced permission controls

---

# 👨‍💻 Author

**Your Name**

GitHub: `@your-username`

---

<div align="center">

## ⭐ Campus Lost & Found System

Built with 🐍 **Python** and 🌐 **Django**

A practical Django project demonstrating **Authentication, CRUD, ORM, Forms, Templates, Middleware, and Messages**.

</div>
