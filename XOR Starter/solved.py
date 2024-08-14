# Given string
label = "label"

# XOR each character with 13 and convert back to character
new_string = ''.join(chr(ord(char) ^ 13) for char in label)

# Format the result as required
flag = f"crypto{{{new_string}}}"

print(flag)
