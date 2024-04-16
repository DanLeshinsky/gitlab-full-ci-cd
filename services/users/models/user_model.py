from pydantic import BaseModel, field_validator, EmailStr


class UserModel(BaseModel):
    email: EmailStr
    name: str
    nickname: str
    uuid:str

    @field_validator("email", "name", "nickname", "uuid")
    def fields_are_not_empty(cls, val):
        if val == "" or val is None:
            raise ValueError("The field is empty")
        else:
            return val
