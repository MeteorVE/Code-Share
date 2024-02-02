# !pip install pycryptodome
import json
from base64 import b64encode
from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes

plaintext = b'Hello, ChaCha20 !'

# generate key & nonce
key = get_random_bytes(32)
nonce = get_random_bytes(12)
key = b'abcdefgh'+ b'\x00' * (32 - len(b'abcdefgh'))
nonce = b'00000000'

# create ChaCha20 cipher
cipher = ChaCha20.new(key=key, nonce=nonce)

# encrypt
ciphertext = cipher.encrypt(plaintext) # (cipher state will be changed, can't be used again.)

# turn nonce & ciphertext to Base64 string
encoded_nonce = b64encode(nonce).decode('utf-8')
encoded_ciphertext = b64encode(ciphertext).decode('utf-8')

result = json.dumps({'nonce': encoded_nonce, 'ciphertext': encoded_ciphertext})
print("First Result: ", result)

# create second ChaCha20 cipher (cipher state will be changed, can't be used again.)
cipher2 = ChaCha20.new(key=key, nonce=nonce)
decrypted_data = cipher2.decrypt(ciphertext)
decrypted_text = decrypted_data.decode('utf-8')

print("Second Result: ", decrypted_text)

# Compare
if plaintext == decrypted_text.encode('utf-8'):
    print("Compare result: Same !")
else:
    print("Compare result: Difference !")