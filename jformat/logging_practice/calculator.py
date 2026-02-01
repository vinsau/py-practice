import logging
import sys
import shutil

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers = [
        logging.FileHandler('calc.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

log = logging.getLogger(__name__)
columns = shutil.get_terminal_size().columns

def verify_input(var_):
    while True:
        try:
            value = float(input(f"Enter value of {var_}: "))
            if value == 0:
                raise ZeroDivisionError
            else:
                break
        except ZeroDivisionError:
            print('=' * columns)
            log.exception("Division by zero is not allowed. Retry input")
            print('=' * columns)
            
    return value

def divide():
    a = verify_input('a')
    b = verify_input('b')
    log.info(f"Dividing {a} by {b}")
    return a / b

def main():
    log.info("Starting application...")
    log.info(f"Result: {divide()}")
    log.info("Stopping application")

if __name__ == '__main__':
    main()
