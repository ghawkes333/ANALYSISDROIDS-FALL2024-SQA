import logging

# Configure logging to include timestamps and log level
logging.basicConfig(filename='FileTwo.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def subtract(a, b):
    try:
        # Perform the subtraction
        result = a - b
        # Log the operation with a clear comment
        logging.info(f"Subtract operation performed: {a} - {b} = {result}. This logs the result of subtracting two numbers.")
        return result
    except Exception as e:
        # Log the exception with a clear context
        logging.exception("Error in subtract method: An exception occurred while attempting to subtract values.")
        return None

# Example call to the subtract function
if __name__ == "__main__":
    subtract(10, 5)  # This should generate a log entry
