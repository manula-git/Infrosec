import hashlib
import sys
import os

value=sys.argv[1].encode('utf-8')
salt=os.urandom(32)
key = hashlib.sha512(str(value + salt).encode('utf-8')).hexdigest()
print(key)
