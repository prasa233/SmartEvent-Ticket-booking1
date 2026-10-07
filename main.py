from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .database import Base, engine
from .routers import (
    auth,
    users,
    events,
    bookings,
    tickets,
    notifications,
)

# --------------------------------------------------
# Paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / "static"

STATIC_DIR.mkdir(exist_ok=True)

# --------------------------------------------------
# Database
# --------------------------------------------------

Base.metadata.create_all(bind=engine)

# --------------------------------------------------
# FastAPI application
# --------------------------------------------------

app = FastAPI(
    title="SmartEvent - Event Discovery & Ticket Booking ",
    description="Backend API for SmartEvent",
    version="2.0.0",
)

# --------------------------------------------------
# Static files
# --------------------------------------------------

app.mount(
    "/static",
    StaticFiles(directory=str(STATIC_DIR)),
    name="static",
)

# --------------------------------------------------
# Routers
# --------------------------------------------------

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(events.router)
app.include_router(bookings.router)
app.include_router(tickets.router)
app.include_router(notifications.router)

# --------------------------------------------------
# Root
# --------------------------------------------------

@app.get("/")
def root():
    return {
        "message": "SmartEvent API is running"
    }


# --------------------------------------------------
# Health check
# --------------------------------------------------

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }