from pydantic import BaseModel


class EmailData(BaseModel):
    email: str
    subject: str
    message: str
