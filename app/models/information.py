from pydantic import BaseModel
from typing import Dict

class Information(BaseModel):
    main_text: str
    expressions_dict: Dict[str, str] 
