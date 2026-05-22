# Bus Punching Management System - Documentation Summary

This document serves as a high-level summary and structural guide. You can use this as an outline to write your comprehensive, original project documentation.

## 1. Project Overview
- **Name**: Bus Punching Management System
- **Purpose**: A full-stack web application for managing student bus passes and tracking real-time bus attendance via QR code scanning.
- **Key Users**: 
  - **Students**: Register, view their bus passes, generate QR codes, and punch in/out.
  - **Administrators**: Manage buses, users (students), issue bus passes, and view system analytics/reports.

## 2. Technology Stack
- **Frontend**: React.js (Vite), Node.js (v18+)
- **Backend**: Python (3.9+), Flask framework
- **Database**: MySQL (8.0+)
- **Security**: JWT for API authentication, bcrypt for password hashing

## 3. Core Features
- **Authentication & Authorization**: Role-based access control (Student vs. Admin).
- **Bus Management**: Admins can add, update, and manage bus routes, capacities, and driver details.
- **Bus Pass Issuance**: Admins issue unique digital passes (monthly, quarterly, yearly) linked to a specific bus and student.
- **QR Code Generation**: Digital passes feature unique, scanable QR tokens.
- **Punch In/Out System**: Students can scan their pass QR code to log their entry/exit on buses in real-time.
- **Analytics & Reporting**: Admin dashboard providing statistics, user management, and punch history logs.

## 4. Database Schema Structure
The application relies on 5 primary tables:
1. **`users`**: Stores all accounts (id, name, email, role [student/admin], password_hash, student_id).
2. **`buses`**: Details of fleet (id, bus_number, route_name, driver_name, capacity, status).
3. **`bus_passes`**: Issued passes linking a user and a bus (id, user_id, bus_id, pass_type, dates, qr_token).
4. **`punch_records`**: Event logs of every scan (id, user_id, bus_id, punch_type [IN/OUT], timestamp).
5. **`attendance_summary`**: Denormalized table for fast attendance query reporting.

## 5. API Endpoints (Quick Reference)

### Authentication
- `POST /api/auth/login`: Login for all users
- `POST /api/auth/register`: Student self-registration
- `GET /api/auth/me`: Get current authenticated user profile

### Bus & Pass Operations
- `GET/POST /api/buses`: List all buses or create new ones (Admin)
- `GET/POST /api/passes`: List or issue passes (Admin)
- `GET /api/passes/my`: Fetch student's own pass
- `GET /api/passes/<id>/qr`: Retrieve QR image for a pass

### Punch Tracking
- `POST /api/punch/scan`: Record a new punch using QR scan
- `GET /api/punch/history`: Fetch user's punch log
- `GET /api/punch/status`: Get the current punch status (IN/OUT)

### Admin Operations
- `GET /api/admin/stats`: Get high-level statistics for dashboard
- `GET /api/admin/users`: List all registered users
- `GET /api/admin/reports`: Generate analytics reports

## 6. How to Run Locally
1. **Database**: Execute `backend/db/schema.sql` in MySQL and configure `backend/config.py` with the correct password.
2. **Backend**: Navigate to `backend/`, create a virtual environment, install `requirements.txt`, and run `python app.py` (Defaults to `localhost:5000`).
3. **Frontend**: Navigate to `frontend/`, run `npm install`, then `npm run dev` (Defaults to `localhost:5173`).

---

**Next Steps for Original Documentation**: 
- Expand on each API endpoint with sample JSON request/response payloads.
- Detail the UI/UX flow for the frontend application, including screenshots.
- Add deployment instructions for a production environment.
- Document any third-party libraries or packages used (e.g., QR scanning library).
