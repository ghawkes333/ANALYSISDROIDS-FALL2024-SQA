import os  # Ensure os is imported
import logging
from main import giveTimeStamp, deleteRepo, dumpContentIntoFile, makeChunks, cloneRepo  # Assuming your code is in main.py

def test_logging():
    test_dir = "test_directory"
    
    # Ensure the directory exists before creating files inside it
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
        logging.info(f"Test directory '{test_dir}' created.")
    
    # Call some of the functions from main.py to see if logging works
    timestamp = giveTimeStamp()
    logging.info(f"Timestamp returned: {timestamp}")
    
    # Test deleteRepo function
    deleteRepo(test_dir, 'test_type')
    
    # Test dumpContentIntoFile function
    content = "This is a test."
    file_path = os.path.join(test_dir, 'test_file.txt')
    # Check if the directory exists before trying to write the file
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)  # Create the directory if it doesn't exist
    
    dumpContentIntoFile(content, file_path)

    # Test makeChunks function
    sample_list = [1, 2, 3, 4, 5, 6]
    chunk_size = 2
    for chunk in makeChunks(sample_list, chunk_size):
        logging.info(f"Chunk: {chunk}")
    
    # Test cloneRepo function (provide a valid repo URL if needed)
    # Example: cloneRepo("https://github.com/yourrepo.git", "clone_test_dir")
    
    # Optionally, delete the directory after the test
    deleteRepo(test_dir, 'test_type')
    logging.info(f"Test directory '{test_dir}' deleted.")

if __name__ == "__main__":
    logging.basicConfig(filename='test_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    test_logging()
