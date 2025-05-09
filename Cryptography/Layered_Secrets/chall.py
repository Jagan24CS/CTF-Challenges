import base64

def xor_encrypt(text, key):
    return bytes([b ^ ord(key[i % len(key)]) for i, b in enumerate(text)])

def math_transform(data):
    return bytes([(b + 17) % 256 for b in data])

flag = b"1nf1n1ty{fake_flag}"
key = "fake_key"  # This is the key to be found

xored = xor_encrypt(flag, key)

transformed = math_transform(xored)

b64_encoded = base64.b64encode(transformed)
final_ciphertext = b64_encoded.hex()

print(final_ciphertext)
