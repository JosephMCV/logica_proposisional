from pydantic import BaseModel
from typing import Dict

class Information(BaseModel):
    main_text: str
    restrictions: Dict[str, str] 
