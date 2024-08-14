# Define the integer array
ascii_values = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

# Convert each integer to its corresponding ASCII character
flag_characters = [chr(value) for value in ascii_values]

# Join the list of characters into a single string
flag = ''.join(flag_characters)

# Print the resulting flag
print(flag)