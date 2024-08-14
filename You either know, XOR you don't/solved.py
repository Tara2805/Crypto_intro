from binascii import unhexlify

# The given encrypted hex string
hex_data = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'

# Convert hex string to bytes
encrypted_data = unhexlify(hex_data)

key = b'myXORkey'

# Repeat the key to match the length of the encrypted message
full_key = (key * (len(encrypted_data) // len(key) + 1))[:len(encrypted_data)]

# Decrypt the full message using the derived full key
decrypted_message = bytes([a ^ b for a, b in zip(encrypted_data, full_key)])

# Print the decrypted message
print(decrypted_message.decode('utf-8'))
