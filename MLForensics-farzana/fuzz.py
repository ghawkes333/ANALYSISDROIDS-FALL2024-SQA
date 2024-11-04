import json
import datetime
import re
import math
import random
import string

def fuzz_json_loads():
    try:
        # Randomly generate a JSON-like string
        random_string = ''.join(random.choices(string.printable, k=20))
        json.loads(random_string)
    except json.JSONDecodeError:
        pass  # Expected for malformed JSON
    except Exception as e:
        print("Unexpected error in json.loads:", e)

def fuzz_datetime_strptime():
    try:
        # Randomly generate a date string
        random_date_str = ''.join(random.choices(string.printable, k=10))
        datetime.datetime.strptime(random_date_str, "%Y-%m-%d")
    except ValueError:
        pass  # Expected for malformed dates
    except Exception as e:
        print("Unexpected error in datetime.strptime:", e)

def fuzz_re_match():
    try:
        # Randomly generate a regex pattern and a string to match
        random_pattern = ''.join(random.choices(string.printable, k=5))
        random_string = ''.join(random.choices(string.printable, k=10))
        re.match(random_pattern, random_string)
    except re.error:
        pass  # Expected for malformed regex
    except Exception as e:
        print("Unexpected error in re.match:", e)

def fuzz_math_sqrt():
    try:
        # Randomly choose a number, which might be negative
        random_number = random.uniform(-100, 100)
        math.sqrt(random_number)
    except ValueError:
        pass  # Expected for negative numbers
    except Exception as e:
        print("Unexpected error in math.sqrt:", e)

def fuzz_random_choice():
    try:
        # Randomly generate a list with varying lengths (including empty)
        random_list = [random.choice(string.printable) for _ in range(random.randint(0, 10))]
        random.choice(random_list)
    except IndexError:
        pass  # Expected for empty list
    except Exception as e:
        print("Unexpected error in random.choice:", e)

def main():
    for _ in range(100):  # Fuzz each method 100 times
        fuzz_json_loads()
        fuzz_datetime_strptime()
        fuzz_re_match()
        fuzz_math_sqrt()
        fuzz_random_choice()

if __name__ == "__main__":
    main()
