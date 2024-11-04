import logging

# Configure logging to include timestamps and log level
logging.basicConfig(filename='FileFive.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def add_to_file(file_path, content):
    try:
        # Open the file in append mode and write the content
        with open(file_path, 'a') as file:
            file.write(content + '\n')
            # Log the successful addition of content
            logging.info(f"Added content to {file_path}: {content}. This logs the successful write operation.")
    except Exception as e:
        # Log the exception with a clear context
        logging.exception(f"Error adding to file {file_path}: An exception occurred while writing to the file.")

# Example call to the add_to_file function
if __name__ == "__main__":
    add_to_file('example.txt', 'This is a test line.')  # This should generate a log entry
