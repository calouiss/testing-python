import logging
logging.basicConfig(level=logging.INFO)
logging.debug("This is debug")
logging.info("This is info")
logging.warning("This is warning")
logging.error("This is error")
logging.critical("This is critical")
def divide(a,b):
    logging.info("This is for division")
    try:
        result=a / b
        logging.debug(f"{a} is dividing {b}")
        return result
    except ZeroDivisionError:
        logging.error("Cannot divide by 0")
        return None
print(divide(10,2))
divide(10,0)


