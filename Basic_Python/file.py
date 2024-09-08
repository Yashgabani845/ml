# Writing to a file
f = open("file.txt", "w")  # Open file in write mode
f.write("This is the first line.\n")  # Writing to the file
f.write("This is the second line.\n")
f.close()  # Closing the file

# Appending to the file
f = open("file.txt", "a")  # Open file in append mode
f.write("This is an appended line.\n")  # Appending to the file
f.close()  # Closing the file

# Reading from the file using read()
with open("file.txt", "r") as f:
    data = f.read()  # Reading the entire file
    print("Content after writing and appending:")
    print(data)  # Printing file content

# Reading the file line by line using readline()
with open("file.txt", "r") as f:
    print("\nReading line by line:")
    line = f.readline()  # Read the first line
    while line:
        print(line, end="")  # Print the line
        line = f.readline()  # Read the next line

# Binary mode example (writing and reading in binary mode)
with open("binary_file.bin", "wb") as f:
    f.write(b"This is a binary file.\n")  # Writing bytes to a binary file

with open("binary_file.bin", "rb") as f:
    binary_data = f.read()  # Reading the binary file
    print("\n\nBinary file content:")
    print(binary_data)  # Printing binary file content
