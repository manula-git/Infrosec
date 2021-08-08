import hashlib
import sys
import os

value=sys.argv[1].encode('utf-8')
salt=os.urandom(32)
key = hashlib.pbkdf2_hmac('sha512',value,salt,200000)
print(key.hex())
