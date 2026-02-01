import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s %(message)s',
    handlers=[
        logging.FileHandler('my_app.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

log = logging.getLogger(__name__)

def divide(a, b):
    log.info(f"Attempting to divide {a} by {b}")
    try:
        result = a / b
        log.info(f"Division successful. Result: {result}")
        return result
    except ZeroDivisionError:
        log.error("Tried to divide by zero!")
        return None

log.info("Script Started")
divide(10,2)
divide(5,0)
log.info("Script Finished")