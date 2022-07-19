import random

from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()


def generated_person():
    dep = ['IT', 'HR', 'SALES', 'MARKETING', 'ASSISTIVE', 'MANAGEMENT']
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.middle_name() + " " + faker_ru.last_name(),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        age=random.randint(18, 70),
        salary=random.randint(20, 150) * 1000,
        department=dep[random.randint(0, 5)]
    )
