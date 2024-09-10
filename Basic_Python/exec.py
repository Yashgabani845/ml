class CustomError(Exception):
    """Custom exception class for specific errors."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class NegativeNumberError(CustomError):
    """Custom exception for handling negative number inputs."""
    def __init__(self, message="Number cannot be negative"):
        self.message = message
        super().__init__(self.message)

class ZeroNumberError(CustomError):
    """Custom exception for handling zero inputs."""
    def __init__(self, message="Number cannot be zero"):
        self.message = message
        super().__init__(self.message)

def process_number(num):
    """Process the number and raise exceptions based on the value."""
    if num < 0:
        raise NegativeNumberError()
    elif num == 0:
        raise ZeroNumberError()
    return f"Processing number: {num}"

def main():
    try:
        num = int(input("Enter a number: "))
        result = process_number(num)
        print(result)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
    except NegativeNumberError as nne:
        print(f"Error: {nne}")
    except ZeroNumberError as zne:
        print(f"Error: {zne}")
    except CustomError as ce:
        print(f"Custom error occurred: {ce}")
    finally:
        print("Execution finished, whether or not an exception occurred.")

if __name__ == "__main__":
    main()
