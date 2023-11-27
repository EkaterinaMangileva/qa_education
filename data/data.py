from dataclasses import dataclass


@dataclass
class Person:
    first_name: str = None
    last_name: str = None
    email: str = None
    phone: int = None
    birthday_day: int = None
    password: str = None