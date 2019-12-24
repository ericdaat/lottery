import random

from application.model import Number, session


def draw_number():
    choices = list(range(1, 100))
    number = random.choice(choices)

    return number

def get_issued_numbers():
    issued_numbers = Number.query.all()
    numbers = [n.value for n in issued_numbers]

    return numbers


def insert_number_in_db(number):
    number_to_insert = Number(value=number)
    session.add(number_to_insert)
    session.commit()

    return number_to_insert
