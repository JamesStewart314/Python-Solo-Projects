from typing import Final, TypedDict

class Email_Dict(TypedDict):
    email: str
    password: str

MyEmail: Final[Email_Dict] = {'email': 'FakeEmail@gmail.com', 'password': 'FakePassword123'}


