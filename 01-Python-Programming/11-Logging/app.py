import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArithmeticApp")

def add(a, b):
    result =  a + b
    logger.debug(f"Adding {a} + {b} = {result}")
    return result

def divide(a, b):
    try:
        result =  a / b
        logger.debug(f"Adding {a} + {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by Zero Error")
        return None
    
add(4, 15)
divide(4, 5)
