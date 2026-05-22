# Bus Punching Management System - Full Documentation

## 1. Introduction
The **Bus Punching Management System** is a web-based application designed to modernize how students use college/school buses. Instead of carrying physical paper passes, students are issued digital passes with QR codes. Students can scan their QR code to "punch in" when they board the bus and "punch out" when they leave. Administrators can track all buses, students, and attendance in real-time.

---

## 2. Technologies Used
- **Frontend (What the user sees)**: React.js, Vite, HTML, CSS, JavaScript.
- **Backend (The brain of the system)**: Python, Flask.
- **Database (Where data is stored)**: MySQL.
- **Security**: Passwords are encrypted, and logins are secured using JWT (JSON Web Tokens).

---

## 3. User Roles

### A. Administrator (Admin)
The Admin manages the entire system.
- **Manage Students**: Add new students or view registered students.
- **Manage Buses**: Add new buses, update routes, and assign drivers.
- **Issue Passes**: Assign a bus pass to a student (e.g., Monthly, Yearly).
- **Monitor Attendance**: See who traveled on which bus and at what time.
- **View Dashboard**: See total buses, total active passes, and daily punch statistics.

### B. Student
The Student uses the system to travel on the bus.
- **Register/Login**: Create an account or log in with their email.
- **View Pass**: Check their active digital bus pass and expiry date.
- **Generate QR Code**: Show their unique QR code to scan on the bus.
- **Punch In / Punch Out**: Scan their pass to mark attendance.
- **View History**: Check their past travel history (dates, times, and routes).

---

## 4. Step-by-Step User Guide

### How to use the system as a Student:
1. **Sign Up**: Go to the Registration page, enter your details (Name, Email, Student ID, Password), and sign up.
2. **Wait for Pass**: The Admin will verify your details and issue a bus pass to your account.
3. **Login**: Go to the Login page and enter your Email and Password.
4. **Get QR Code**: Click on "My Pass". You will see a button to "Show QR Code". This is your digital ticket.
5. **Punch In**: Go to the "Scan & Punch" section. Point the camera at the bus's QR scanner (or scan your code). The system will record that you have boarded the bus (IN).
6. **Punch Out**: When getting off, scan again. The system records that you have left the bus (OUT).

### How to use the system as an Admin:
1. **Login**: Use the admin email and password.
2. **Add a Bus**: Go to the "Buses" tab. Click "Add Bus". Enter the bus number, route, and driver details.
3. **Issue a Pass**: Go to the "Bus Passes" tab. Select a student, select a bus, choose the duration (Monthly/Yearly), and click "Issue Pass".
4. **Check Reports**: Go to the Dashboard or "Reports" tab to see daily attendance and punch logs.

---

## 5. System Features Explained Simply

- **Digital QR Passes**: No more lost paper cards. Every pass generates a unique QR code on the student's phone.
- **Real-Time Tracking**: The moment a student punches in, the admin can see it on the dashboard.
- **Role-Based Login**: Students cannot access admin pages, and admins have full control over the data.
- **Secure Data**: Passwords are never stored as plain text. The system uses strict security (bcrypt) to keep accounts safe.

---

## 6. How to Start the Project (For Developers)

If you want to run this code on your computer, follow these simple steps:

### Step 1: Set up the Database
1. Open MySQL on your computer.
2. Run the `backend/db/schema.sql` file. This creates all the necessary tables (users, buses, passes, etc.).
3. Open the `backend/config.py` file and update `MYSQL_PASSWORD` with your actual MySQL password.

### Step 2: Start the Backend (Python)
1. Open your terminal or command prompt.
2. Go to the backend folder: `cd backend`
3. Install the required Python packages: `pip install -r requirements.txt`
4. Run the server: `python app.py`
*(The backend will now be running in the background).*

### Step 3: Start the Frontend (React)
1. Open a **new** terminal.
2. Go to the frontend folder: `cd frontend`
3. Install the required Node packages: `npm install`
4. Start the website: `npm run dev`
5. Open your web browser and go to the link shown in the terminal (usually `http://localhost:5173`).

---

## 7. Default Admin Login Details
If you just installed the database, an admin account is automatically created for you:
- **Email**: admin@busmanagement.com
- **Password**: Admin@123

*Note: You can use this to log in immediately and start adding buses and issuing passes!*
