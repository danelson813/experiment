from log_helper import *


def decorator2(func):
    print("Inside decorator")

    def wrapper(*args, **kwargs):
        print("Inside wrapper.")
        logger.info("Do something before the function.")
        value = func(*args, **kwargs)
        print("Inside wrapper")
        logger.info("Do something after the function")
        return value
    return wrapper
