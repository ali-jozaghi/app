from dataclasses import dataclass

@dataclass
class User:
    user_id: int
    email: str
    fullname: str
