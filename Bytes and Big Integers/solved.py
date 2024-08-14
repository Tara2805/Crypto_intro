#pip install pycryptodome

from Crypto.Util.number import long_to_bytes

# The given integer
large_integer = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

# Convert the integer to bytes
byte_data = long_to_bytes(large_integer)

# Decode the bytes to a message
message = byte_data.decode('ascii')

print(message)

