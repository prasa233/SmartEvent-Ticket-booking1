from datetime import datetime
from typing import Optional
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field
from pydantic import BaseModel, ConfigDict, EmailStr
from pydantic import BaseModel, ConfigDict, EmailStr, Field
from pydantic import BaseModel, EmailStr

# =========================================================
# AUTH
# =========================================================


class RegisterRequest(BaseModel):
    username: str
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class UserRegister(BaseModel):
    name: str
    email: EmailStr
    password: str
class RegisterRequest(BaseModel):
    username: str = Field(
        min_length=3,
        max_length=50
    )

    email: EmailStr

    password: str = Field(
        min_length=6,
        max_length=100
    )


class UserCreate(BaseModel):
    username: str = Field(
        min_length=3,
        max_length=50
    )

    email: EmailStr

    password: str = Field(
        min_length=6,
        max_length=100
    )


class UserLogin(BaseModel):
    email: EmailStr

    password: str

from pydantic import BaseModel


class LoginRequest(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


# =========================================================
# EVENT
# =========================================================

class EventCreate(BaseModel):
    title: str = Field(
        min_length=2,
        max_length=200
    )

    description: str

    category: str

    location: str

    event_date: datetime

    ticket_price: float = Field(
        gt=0
    )

    banner_image: Optional[str] = None

    total_tickets: int = Field(
        gt=0
    )


class EventResponse(BaseModel):
    id: int
    title: str
    description: str
    category: str
    location: str
    event_date: datetime
    ticket_price: float
    banner_image: Optional[str]
    total_tickets: int
    available_tickets: int
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )
# =========================================================
# BOOKING
# =========================================================

class BookingCreate(BaseModel):
    event_id: int

    ticket_quantity: int = Field(
        ge=1,
        le=100
    )


class BookingResponse(BaseModel):
    id: int
    user_id: int
    event_id: int
    ticket_quantity: int
    total_price: float
    booking_status: str
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )


# =========================================================
# TICKET
# =========================================================

class TicketResponse(BaseModel):
    id: int
    booking_id: int
    ticket_code: str
    qr_code_url: str | None = None
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )


# =========================================================
# NOTIFICATION
# =========================================================

class NotificationResponse(BaseModel):
    id: int
    user_id: int
    title: str
    message: str
    type: str
    is_read: bool
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )





   