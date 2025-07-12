from pydantic import BaseModel,Field
from typing import Annotated

#Output validation
class ResponseModel(BaseModel):
    response:Annotated[int,Field("1 indicate Presence and 0 indicate Absence")]
