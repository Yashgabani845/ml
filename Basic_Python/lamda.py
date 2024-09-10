from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using lambda and map to get squares of numbers
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"Squared numbers: {squared_numbers}")

# Using lambda and filter to get only even squares
even_squares = list(filter(lambda x: x % 2 == 0, squared_numbers))
print(f"Even squares: {even_squares}")

# Using reduce to get the product of even squares
product_of_even_squares = reduce(lambda x, y: x * y, even_squares)
print(f"Product of even squares: {product_of_even_squares}")

# Using join and format to create a formatted string
result_str = "Even squares: {} | Product of even squares: {}".format(
    ", ".join(map(str, even_squares)), product_of_even_squares
)

print(result_str)
