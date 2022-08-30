import threading
from random import randint
from typing import Any


def get_random_temperature() -> float:
    """
    Function to generate a random temperature from 30º to 40º C.
    """
    return randint(30, 40)


def get_sensor_1_value() -> None:
    """
    Function to get the value of a "sensor_1" IoT device.
    """
    temperature = get_random_temperature()
    print(f'SENSOR 1: {temperature}')
    insert_into_database(temperature)


def get_sensor_2_value() -> None:
    """
    Function to get the value of a "sensor_2" IoT device.
    """
    temperature = get_random_temperature()
    print(f'SENSOR 2: {temperature}')
    insert_into_database(temperature)


def get_sensor_3_value() -> None:
    """
    Function to get the value of a "sensor_3" IoT device.
    """
    temperature = get_random_temperature()
    print(f'SENSOR 3: {temperature}')
    insert_into_database(temperature)


def insert_into_database(data: Any) -> None:
    """
    Function to insert the data received as argument in the database.

    Parameters
    -----------
    data : Any
        The data to be stored in the database.
    """
