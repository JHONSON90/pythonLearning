from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[str] = None ## le estamos diciendo que puede recibirlo o no
    username: str
    email: str
