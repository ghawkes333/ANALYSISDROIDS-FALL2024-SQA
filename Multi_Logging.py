import logging

# Configure logging to include timestamps and log level
logging.basicConfig(filename='FileThree.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def multiply(a, b):
    try:
        # Perform the multiplication
        result = a * b
        # Log the operation with a clear comment
        logging.info(f"Multiply operation performed: {a} * {b} = {result}. This logs the result of multiplying two numbers.")
        return result
    except Exception as e:
        # Log the exception with a clear context
        logging.exception("Error in multiply method: An exception occurred while attempting to multiply values.")
        return None

# Example call to the multiply function
if __name__ == "__main__":
    multiply(6, 7)  # This should generate a log entry
