age: int = 25
def greeting(name: str) -> str:
    return f"Hello, {name}!"
print(greeting("Alice"))           
from typing import List, Tuple, Dict, Union
numbers: List[int] = [1, 2, 3, 4, 5]
person: Tuple[str, int] = ("Alice", 30)
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}
identifier: Union[int, str] = "ID123"
identifier = 12345 
def http_status(status): #work as switch
    match status:
        case 200:
            return "OK"
        case 404:
           return "Not Found"
        case 500:   
            return "Internal Server Error"
        case _:
            return "Unknown status"
# Usage
print(http_status(200)) # Output: OK
print(http_status(404)) # Output: Not Found
print(http_status(500)) # Output: Internal Server Error
print(http_status(403)) # Output: Unknown status

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = dict1 | dict2
print(merged) # Output: {'a': 1, 'b': 3, 'c': 4}


# with (
#     open('file1.txt') as f1,
#     open('file2.txt') as f2
# ):
#using this kind of syntax we can use multiple file descriptor
fruits = ["apple", "banana", "cherry", "date"]

# Using enumerate to get index and value
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# You can also specify a start index
for index, fruit in enumerate(fruits, start=1):
    print(f"Index {index}: {fruit}")

# Creating a list of squares from 0 to 9
squares = [x**2 for x in range(10)]
print(squares)


