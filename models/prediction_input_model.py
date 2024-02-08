from pydantic import BaseModel

class PredictionInput(BaseModel):
    tickets_out: int
    capacity: int
    month: int
    day: int
