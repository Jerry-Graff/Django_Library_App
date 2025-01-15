# Django Library App

Welcome to the **Django Library App**! You can visit the site by going to:  
**[www.djangolibapp.xzy](http://www.djangolibapp.xzy/)**

This application is a basic library system allowing users to:
- View and loan books.
- Reserve books if they are on loan.
- Extend loan due dates.
- For admins: manage (CRUD) books and view readers.

---

## Table of Contents
1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation and Local Setup](#installation-and-local-setup)
---

## Features

1. **User Authentication**  
   - Readers can log in, loan, and reserve books.  
   - Admins can log in with superuser/staff privileges.

2. **Book Management (CRUD)**  
   - Admins can create, read, update, and delete books from the library.

3. **Loan and Reservation**  
   - Users can loan available books (loan due date auto-set to 2 weeks).  
   - Readers can reserve books on loan, blocking loan extensions for current borrowers.


---

## Requirements

- **Python 3.9+**  
- **Django 5.1+**  
- **SQLite** (default for development)
- **Docker** (for containerization)
- **AWS Lightsail** (for hosting)

---

## Installation and Local Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Jerry-Graff/django-library-app.git
   cd django-library-app