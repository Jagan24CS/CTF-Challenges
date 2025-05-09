import base64

def xor_encrypt(text, key):
    return bytes([b ^ ord(key[i % len(key)]) for i, b in enumerate(text)])

def math_transform(data):
    return bytes([(b + 17) % 256 for b in data])

flag = b"1nf1n1ty{x0r_plus_17_tr1ck3y_math_cipher}"
key = "tr1cky"  # This is the key to be found

# Step 1: XOR the flag with the key
xored = xor_encrypt(flag, key)

# Step 2: Apply math transformation
transformed = math_transform(xored)

# Step 3: Encode to base64 then to hex
b64_encoded = base64.b64encode(transformed)
final_ciphertext = b64_encoded.hex()

print(final_ciphertext)
