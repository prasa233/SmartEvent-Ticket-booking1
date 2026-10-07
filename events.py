from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Event
from ..schemas import EventCreate, EventResponse


router = APIRouter(
    prefix="/events",
    tags=["Events"]
)


# --------------------------------------------------
# Create Event
# --------------------------------------------------

@router.post(
    "/",
    response_model=EventResponse,
    status_code=201
)
def create_event(
    event_data: EventCreate,
    db: Session = Depends(get_db)
):
    event = Event(
        title=event_data.title,
        description=event_data.description,
        category=event_data.category,
        location=event_data.location,
        event_date=event_data.event_date,
        ticket_price=event_data.ticket_price,
        banner_image=event_data.banner_image,
        total_tickets=event_data.total_tickets,
        available_tickets=event_data.total_tickets
    )

    db.add(event)
    db.commit()
    db.refresh(event)

    return event


# --------------------------------------------------
# Get All Events
# --------------------------------------------------

@router.get(
    "/",
    response_model=list[EventResponse]
)
def get_events(
    category: Optional[str] = None,
    search: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Event)

    if category:
        query = query.filter(
            Event.category == category
        )

    if search:
        query = query.filter(
            Event.title.ilike(f"%{search}%")
        )

    return query.order_by(
        Event.event_date.asc()
    ).all()


# --------------------------------------------------
# Get Event By ID
# --------------------------------------------------

@router.get(
    "/{event_id}",
    response_model=EventResponse
)
def get_event(
    event_id: int,
    db: Session = Depends(get_db)
):
    event = db.query(Event).filter(
        Event.id == event_id
    ).first()

    if not event:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    return event
