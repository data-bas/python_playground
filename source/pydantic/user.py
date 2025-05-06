from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class User(BaseModel):
    username: str
    email: EmailStr
    age: Optional[int] = Field(None, gt=0, lt=106, description="Age must be greater than 0 and less then 106")
    active: bool = True

    def save_to_db(self, cursor):
        cursor.execute(
            "INSERT INTO users (username, email, age, active) VALUES (%s, %s, %s, %s)",
            (self.username, self.email, self.age, self.active)
        )
