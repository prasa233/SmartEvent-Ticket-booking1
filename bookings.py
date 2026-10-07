from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..dependencies import get_current_user
from ..models import User, Event, Booking, Ticket
from ..schemas import BookingCreate, BookingResponse


router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)


@router.post("/", response_model=BookingResponse, status_code=201)
def create_booking(
    booking_data: BookingCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # 1. Find event
    event = (
        db.query(Event)
        .filter(Event.id == booking_data.event_id)
        .first()
    )

    if event is None:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    # 2. Validate ticket quantity
    if booking_data.ticket_quantity <= 0:
        raise HTTPException(
            status_code=400,
            detail="Ticket quantity must be greater than 0"
        )

    # 3. Check available tickets
    if event.available_tickets < booking_data.ticket_quantity:
        raise HTTPException(
            status_code=400,
            detail="Not enough tickets available"
        )

    # 4. Calculate total price
    total_price = (
        event.ticket_price * booking_data.ticket_quantity
    )

    # 5. Create booking
    booking = Booking(
        user_id=current_user.id,
        event_id=event.id,
        ticket_quantity=booking_data.ticket_quantity,
        total_price=total_price,
        booking_status="CONFIRMED"
    )

    # 6. Reduce available tickets
    event.available_tickets -= booking_data.ticket_quanti
    # 7. Save booking
    db.add(booking)
    db.commit()
    db.refresh(booking)

    # 8. Create ticket
    ticket_code = f"TKT-{uuid4().hex[:10].upper()}"

    ticket = Ticket(
        booking_id=booking.id,
        ticket_code=ticket_code,
        qr_code_url=None
    )

    db.add(ticket)
    db.commit()
    db.refresh(ticket)

    return booking


@router.get("/my", response_model=list[BookingResponse])
def get_my_bookings(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    bookings = (
        db.query(Booking)
        .filter(Booking.user_id == current_user.id)
        .order_by(Booking.created_at.desc())
        .all()
    )

    return bookings


@router.get("/{booking_id}", response_model=BookingResponse)
def get_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    booking = (
        db.query(Booking)
        .filter(
            Booking.id == booking_id,
            Booking.user_id == current_user.id
        )
        .first()
    )

    if booking is None:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    return booking

   