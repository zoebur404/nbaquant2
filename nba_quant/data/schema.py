from pydantic import BaseModel
from typing import List, Optional

class Market(BaseModel):
    player: str
    team: str
    market: str
    line: float
    over: float
    under: float
    book: str
