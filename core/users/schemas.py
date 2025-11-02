from pydantic import BaseModel, Field, model_validator


class UserLoginSchema(BaseModel):
    username: str = Field(...)
    password: str = Field(..., description="User's password")


class UserRegisterSchema(BaseModel):
    username: str = Field(...)
    password: str = Field(..., description="User's password")
    password_confirm: str = Field(..., description="Confirm user password")

    @model_validator(mode="after")
    def check_passwords_match(self):
        if self.password != self.password_confirm:
            raise ValueError("Passwords don't match!")
        return self
