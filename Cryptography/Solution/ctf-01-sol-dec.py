import base64

def xor_encrypt(text, key):
    return bytes([b ^ ord(key[i % len(key)]) for i, b in enumerate(text)])

def math_reverse(data):
    return bytes([(b - 17) % 256 for b in data])

hex_ciphertext = "5669316f59785a5a455278624c47776350424e754a796b33566c5a2f4b43705a4b436f544b30556c4a68647154526b684653746c4969633d"

# Step 2: Decode from hex then from base64
b64_decoded = bytes.fromhex(hex_ciphertext)
transformed = base64.b64decode(b64_decoded)

# Step 3: Reverse the math transformation
xored = math_reverse(transformed)

# Step 4: Try to deduce the key using the known flag prefix
known_prefix = b"1nf1n1ty{"
recovered_key = bytes([xored[i] ^ known_prefix[i] for i in range(len(known_prefix))])
print("[+] Recovered key (partial or full):", recovered_key.decode())

# Step 5: Decrypt the full flag using the recovered key
full_flag = xor_encrypt(xored, "tr1cky")
print("[*] Decrypted flag:", full_flag.decode())
