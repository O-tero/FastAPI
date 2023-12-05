from typing import List, Optional

class Todo(BaseModel):
    id: Optional[int]
    item: str
    
    @classmethod
    def as_form(
        cls,
        item: str = Form(...)
    ):
        return cls(item=item)
