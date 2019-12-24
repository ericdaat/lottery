import random
import logging

from application.model import Number, session


def draw_number(issued_numbers):
    choices = set(range(1, 100))

    for issued_number in issued_numbers:
        if issued_number in choices:
            choices.remove(issued_number)

    logging.debug("picking from {0} choices".format(len(choices)))

    number = random.choice(list(choices))
    logging.info("number {0} is drawn".format(number))

    insert_number_in_db(number)

    return number


def get_issued_numbers():
    issued_numbers = Number.query.all()
    numbers = [n.value for n in issued_numbers]

    return set(numbers)


def get_last_number_issued():
    number = Number.query.order_by(Number.created_at.desc()).first()

    return number


def insert_number_in_db(number):
    number_to_insert = Number(value=number)
    session.add(number_to_insert)
    session.commit()

    return number_to_insert


def reset_numbers():
    Number.query.delete()
    session.commit()
