from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..dependencies import get_current_user
from ..models import User, Booking, Ticket
from ..schemas import TicketResponse


router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)


@router.post(
    "/booking/{booking_id}",
    response_model=TicketResponse,
    status_code=201
)
def generate_ticket(
    booking_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # 1. Find booking
    booking = (
        db.query(Booking)
        .filter(
            Booking.id == booking_id,
            Booking.user_id == current_user.id
        )
        .first()
    )

    # 2. Check booking
    if booking is None:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    # 3. Check whether ticket already exists
    existing_ticket = (
        db.query(Ticket)
        .filter(Ticket.booking_id == booking.id)
        .first()
    )

    if existing_ticket is not None:
        return existing_ticket

    # 4. Generate unique ticket code
    ticket_code = f"TKT-{uuid4().hex[:10].upper()}"

    # 5. Create ticket
    ticket = Ticket(
        booking_id=booking.id,
        ticket_code=ticket_code,
        qr_code_url=None
    )

    # 6. Save ticket
    db.add(ticket)
    db.commit()
    db.refresh(ticket)

    # 7. Return ticket
    return ticket