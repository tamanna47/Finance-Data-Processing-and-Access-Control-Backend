# Finance-Data-Processing-and-Access-Control-Backend
A FastAPI-based backend system for finance dashboard management with JWT authentication, role-based access control, financial records CRUD, and dashboard analytics.

A backend system built using **FastAPI**, **SQLite**, and **SQLAlchemy** for managing financial records, user authentication, role-based access control, and dashboard analytics.

---

## Project Overview

This project is designed as a finance backend system where users with different roles can securely access and manage financial data.

The system supports:
- User registration and login
- JWT-based authentication
- Role-Based Access Control (RBAC)
- Financial records CRUD operations
- Record filtering
- Dashboard summary APIs
- Input validation and error handling

---

## Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **Database:** SQLite
- **ORM:** SQLAlchemy
- **Authentication:** JWT (JSON Web Token)
- **Validation:** Pydantic

---

## User Roles

### Viewer
- Can access dashboard summary APIs

### Analyst
- Can access dashboard APIs
- Can view financial records

### Admin
- Can manage users
- Can create, update, and delete financial records
- Can access dashboard APIs

---

## Features Implemented

- User and role management
- Financial records CRUD
- Record filtering (type, category, date)
- Dashboard summary APIs
- Role-Based Access Control
- Input validation and error handling
- Database persistence

---

## Project Structure

``` id="djlwmr"
backend project/
│
├── main_app.py
├── database.py
├── dependencies.py
├── users.py
├── financial_record.py
├── auth_routes.py
├── user_routes.py
├── financial_routes.py
├── dashboard_routes.py
├── user_schema.py
├── auth_schemas.py
├── financial_schema.py
├── utility_auth.py
├── role_check.py
├── requirements.txt
└── README.md
