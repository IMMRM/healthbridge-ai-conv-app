from typing import Optional
from pydantic import BaseModel

class MemberQueryParams(BaseModel):
    email: Optional[str] = None
    phone: Optional[str] = None
    memberId: Optional[str] = None