from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    account_id: int

user = User(name="jack", email="jack@gmail.com", account_id=1234)
print(user)
print(user.name)