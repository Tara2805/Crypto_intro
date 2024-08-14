from binascii import unhexlify

# The given hex string
hex_data = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'

# Convert hex string to bytes
data = unhexlify(hex_data)

# Try all possible single-byte XOR keys
for key in range(256):
    # XOR each byte in the data with the key
    decrypted = bytes([b ^ key for b in data])
    
    # Check if the result is a readable ASCII string
    try:
        decrypted_text = decrypted.decode('utf-8')
        if decrypted_text.isprintable():
            print(f"Key: {key}, Decrypted text: {decrypted_text}")
    except UnicodeDecodeError:
        continue
