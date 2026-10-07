# SmartEvent – Event Discovery & Ticket Booking System

SmartEvent is a full-stack event discovery and ticket booking application that allows users to discover events, book tickets, view digital QR tickets, and receive event and booking notifications.

The application is developed using **FastAPI for the backend** and **React + Vite for the frontend**.


#  Backend Setup

## 1. Navigate to Backend

```bash
cd backend
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

## 3. Activate Virtual Environment

### Windows PowerShell

```powershell
venv\Scripts\Activate.ps1
```

### Windows CMD

```cmd
venv\Scripts\activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 5. Configure Environment Variables

Create a `.env` file inside the `backend` folder.

Example:

```env
DATABASE_URL=sqlite:///./smartevent.db
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Do not commit the `.env` file to GitHub.

## 6. Run FastAPI

From the `backend` directory:

```bash
python -m uvicorn app.main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger API documentation:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

# ⚛️ Frontend Setup

## 1. Navigate to Frontend

```bash
cd frontend
```

## 2. Install Dependencies

```bash
npm install
```

## 3. Start React Development Server

```bash
npm run dev
```

Frontend will normally be available at:

```text
http://localhost:5173
```

---

# 🔗 API Integration

The React frontend communicates with FastAPI using Axios.

Example API structure:

```text
POST   /auth/register
POST   /auth/login
GET    /users/me

GET    /events
GET    /events/{event_id}
GET    /events/category/{category}

POST   /bookings
GET    /bookings
GET    /bookings/{booking_id}

GET    /tickets
GET    /tickets/{ticket_id}

GET    /notifications
PATCH  /notifications/{notification_id}/read
```

Authenticated requests use:

```text
Authorization: Bearer <JWT_TOKEN>
```

---

# 📋 Booking Workflow

The expected booking workflow is:

```text
User
  │
  ▼
Login
  │
  ▼
Browse Events
  │
  ▼
Select Event
  │
  ▼
Choose Ticket Quantity
  │
  ▼
Check Availability
  │
  ▼
Calculate Total Price
  │
  ▼
Create Booking
  │
  ▼
Confirm Booking
  │
  ▼
Generate Ticket
  │
  ▼
Generate QR Code
  │
  ▼
Show Digital Ticket
  │
  ▼
Send Notification
```

---

# 🧪 Testing

Backend APIs should be tested using:

* Swagger UI
* Pytest
* FastAPI TestClient

Example:

```bash
pytest
```

Important scenarios to test:

* User registration
* Duplicate email registration
* User login
* Invalid credentials
* Protected endpoints
* Event listing
* Event search
* Category filtering
* Successful booking
* Invalid ticket quantity
* Sold-out event
* Booking ownership
* QR ticket generation
* Notifications

---

# 📦 GitHub Setup

Initialize Git:

```bash
git init
```

Add files:

```bash
git add .
```

Commit:

```bash
git commit -m "Initial SmartEvent project"
```

Connect your GitHub repository:

```bash
git remote add origin YOUR_GITHUB_REPOSITORY_URL
```

Push the project:

```bash
git branch -M main
git push -u origin main
```

---

# 🚫 .gitignore

The project should not upload sensitive or unnecessary files.

Example:

```gitignore
# Python
venv/
__pycache__/
*.pyc

# Environment
.env

# Database
*.db
*.sqlite3

# React
node_modules/
dist/

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
```

---

# 🎯 Extended Deliverables

The completed project should provide:

* ✅ User authentication
* ✅ JWT security
* ✅ Event discovery
* ✅ Event search
* ✅ Category filtering
* ✅ Ticket booking
* ✅ Ticket availability validation
* ✅ Booking history
* ✅ QR-based digital tickets
* ✅ Unique ticket codes
* ✅ Event reminders
* ✅ Notifications
* ✅ React frontend
* ✅ FastAPI backend
* ✅ Database relationships
* ✅ API integration
* ✅ Responsive interface
* ✅ Proper loading and error handling
* ✅ Secure environment configuration

---

# 🏁 Final Objective

SmartEvent is designed to simulate a real-world event discovery and ticket booking platform.

The final application enables users to:

**Discover → Select → Book → Confirm → Receive QR Ticket → Manage Bookings → Receive Notifications**

The project demonstrates practical skills in:

* FastAPI development
* REST API design
* JWT authentication
* Database relationships
* React development
* Frontend-backend integration
* Ticket booking workflows
* QR code generation
* Notification systems
* Application security

---

## 👨‍💻 Project Status

**Project:** SmartEvent – Event Discovery & Ticket Booking System

**Backend:** FastAPI

**Frontend:** React + Vite

**Database:** SQLite / PostgreSQL / MySQL

**Status:** In Development
