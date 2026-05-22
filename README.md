# Bus Punching Management System — Quick Start Guide

## Prerequisites
- Python 3.9+ with pip
- Node.js 18+ with npm
- MySQL 8.0+

---

## Step 1: Set Up MySQL Database

Open MySQL shell (or MySQL Workbench) and run:

```sql
mysql -u root -p < backend/db/schema.sql
```

Or open the file `backend/db/schema.sql` in MySQL Workbench and execute it.

---

## Step 2: Configure Database Password

Open `backend/config.py` and set your MySQL password:

```python
MYSQL_PASSWORD = 'your_mysql_password_here'
```

---

## Step 3: Start the Flask Backend

```bash
cd backend

# Create virtual environment (first time)
python -m venv venv
venv\Scripts\activate       # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Start server
python app.py
```

Backend runs at: http://localhost:5000

---

## Step 4: Start the React Frontend

Open a **new terminal**:

```bash
cd frontend
npm install    # if not done already
npm run dev
```

Frontend runs at: http://localhost:5173

---

## Demo Login Credentials

| Role  | Email                        | Password   |
|-------|------------------------------|------------|
| Admin | admin@busmanagement.com      | Admin@123  |

Register a student account via `/register`.

---

## Admin Workflow

1. Login as Admin
2. Go to **Buses** → Add buses
3. Go to **Users** → Add students (or students can self-register)
4. Go to **Bus Passes** → Issue a pass to a student (select bus + dates)
5. Pass is created with a unique QR token

## Student Workflow

1. Register / Login as student
2. Go to **My Pass** → View pass + click "Show QR Code"
3. Go to **Scan & Punch** → Start camera → Scan QR code
4. Punch IN/OUT is recorded automatically
5. View history in **My History**

---

## API Endpoints Reference

| Endpoint                      | Method | Auth  | Description               |
|-------------------------------|--------|-------|---------------------------|
| `/api/auth/login`             | POST   | None  | Login                     |
| `/api/auth/register`          | POST   | None  | Register student          |
| `/api/auth/me`                | GET    | JWT   | Current user info         |
| `/api/buses`                  | GET    | JWT   | List all buses            |
| `/api/buses`                  | POST   | Admin | Create bus                |
| `/api/passes`                 | GET    | JWT   | List passes               |
| `/api/passes`                 | POST   | Admin | Issue new pass            |
| `/api/passes/my`              | GET    | JWT   | Student's own pass        |
| `/api/passes/<id>/qr`         | GET    | JWT   | Get QR image              |
| `/api/punch/scan`             | POST   | JWT   | Scan QR → record punch    |
| `/api/punch/history`          | GET    | JWT   | Punch history             |
| `/api/punch/status`           | GET    | JWT   | Last punch status         |
| `/api/admin/stats`            | GET    | Admin | Dashboard statistics      |
| `/api/admin/users`            | GET    | Admin | All users                 |
| `/api/admin/punches`          | GET    | Admin | All punch records         |
| `/api/admin/reports`          | GET    | Admin | Filtered analytics data   |
