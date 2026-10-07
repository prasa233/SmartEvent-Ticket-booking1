
from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    Boolean,
    ForeignKey,
    Float,
)

from sqlalchemy.orm import relationship

from .database import Base


# ==================================================
# USER
# ==================================================

class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    username = Column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    email = Column(
        String(255),
        unique=True,
        nullable=False,
        index=True,
    )

    hashed_password = Column(
        String(255),
        nullable=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )

    bookings = relationship(
        "Booking",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    notifications = relationship(
        "Notification",
        back_populates="user",
        cascade="all, delete-orphan",
    )


# ==================================================
# EVENT
# ==================================================

class Event(Base):
    __tablename__ = "events"
 
    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    title = Column(
        String(200),
        nullable=False,
    )

    description = Column(
        Text,
        nullable=True,
    )

    category = Column(
        String(100),
        nullable=False,
    )

    location = Column(
        String(200),
        nullable=False,
    )

    event_date = Column(
        DateTime,
        nullable=False,
    )

    ticket_price = Column(
        Float,
        nullable=False,
    )

    banner_image = Column(
        String(500),
        nullable=True,
    )

    total_tickets = Column(
        Integer,
        nullable=False,
    )

    available_tickets = Column(
        Integer,
        nullable=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )

    bookings = relationship(
        "Booking",
        back_populates="event",
        cascade="all, delete-orphan",
    )


# ==================================================
# BOOKING
# ==================================================

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    event_id = Column(
    Integer,
    ForeignKey("events.id"),
    nullable=False
)

    ticket_quantity = Column(
        Integer,
        nullable=False,
    )

    total_price = Column(
        Float,
        nullable=False,
    )

    booking_status = Column(
        String(50),
        default="CONFIRMED",
        nullable=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )

    user = relationship(
        "User",
        back_populates="bookings",
    )

    event = relationship(
        "Event",
        back_populates="bookings",
    )

    ticket = relationship(
        "Ticket",
        back_populates="booking",
        uselist=False,
        cascade="all, delete-orphan",
    )


# ==================================================
# TICKET
# ==================================================

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    booking_id = Column(
        Integer,
        ForeignKey("bookings.id"),
        nullable=False,
        unique=True,
    )

    ticket_code = Column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    qr_code_url = Column(
        String(500),
        nullable=True,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )

    booking = relationship(
        "Booking",
        back_populates="ticket",
    )


# ==================================================
# NOTIFICATION
# ==================================================

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    title = Column(
        String(200),
        nullable=False,
    )

    message = Column(
        Text,
        nullable=False,
    )

    type = Column(
        String(50),
        nullable=True,
    )

    is_read = Column(
        Boolean,
        default=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )

    user = relationship(
        "User",
        back_populates="notifications",
    )

