import logging

# Configure logging to also output to the console
logging.basicConfig(filename='FileOne.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def add(a, b):
    try:
        # Perform the addition
        result = a + b
        # Log the operation
        logging.info(f"Add operation performed: {a} + {b} = {result}. This logs the result of adding two numbers.")
        return result
    except Exception as e:
        # Log the exception
        logging.exception("Error in add method: An exception occurred while attempting to add values.")
        return None

# Example call to the add function
if __name__ == "__main__":
    add(5, 7)  # This should generate a log entry
