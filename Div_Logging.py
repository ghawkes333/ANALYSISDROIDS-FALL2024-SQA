import logging

# Configure logging to include timestamps and log level
logging.basicConfig(filename='FileFour.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def divide(a, b):
    try:
        if b == 0:
            logging.warning("Attempted to divide by zero. Division by zero is not allowed.")
            return None
        # Perform the division
        result = a / b
        # Log the operation with a clear comment
        logging.info(f"Divide operation performed: {a} / {b} = {result}. This logs the result of dividing two numbers.")
        return result
    except Exception as e:
        # Log the exception with a clear context
        logging.exception("Error in divide method: An exception occurred while attempting to divide values.")
        return None

# Example call to the divide function
if __name__ == "__main__":
    divide(10, 2)  # This should generate a log entry
    divide(10, 0)  # This will trigger the warning for division by zero
