from base64 import b64decode
from base64 import b64encode
import hashlib
import os

server_key = os.urandom(32)
salt = os.urandom(32)
encrypted_key = hashlib.pbkdf2_hmac("sha256", server_key, salt, 100_000)

current_server_key = b64encode(server_key).decode("utf-8")
print(current_server_key)


r_salt = b64decode(current_server_key.encode("utf-8"))
print(r_salt)
print(server_key)

# encrypted_key = b64decode(current_server_key.encode("utf-8"))
# print(encrypted_key)
# check_key = hashlib.pbkdf2_hmac(
#     "sha256", b64decode(current_server_key.encode("utf-8")), salt, 100_000
# )
# print(check_key)
