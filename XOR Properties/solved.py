# Import the required module
from binascii import unhexlify
import itertools

# Convert hex strings to bytes
KEY1 = unhexlify('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
KEY2_XOR_KEY1 = unhexlify('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e')
KEY2_XOR_KEY3 = unhexlify('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
FLAG_XOR_KEYS = unhexlify('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')

# Calculate KEY2
KEY2 = bytes(a ^ b for a, b in zip(KEY1, KEY2_XOR_KEY1))

# Calculate KEY3
KEY3 = bytes(a ^ b for a, b in zip(KEY2, KEY2_XOR_KEY3))

# Calculate FLAG
FLAG = bytes(a ^ b ^ c ^ d for a, b, c, d in zip(FLAG_XOR_KEYS, KEY1, KEY2, KEY3))

# Print the flag
print(f"{{{FLAG.decode()}}}")
