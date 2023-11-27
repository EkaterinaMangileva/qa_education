from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')


def generated_person():
    yield Person(
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        email=faker_ru.email(),
        phone=faker_ru.phone_number(),
        birthday_day=faker_ru.date_of_birth(),
        password=faker_ru.password(),
    )

