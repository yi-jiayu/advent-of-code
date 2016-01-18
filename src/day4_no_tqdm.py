import sys
from hashlib import md5

TARGET = '00000'
SECRET_KEY = 'yzbqklnj'
nonce = 0
hash_ = ''

print('Hashing... ', end='')
sys.stdout.flush()

while hash_[0:len(TARGET)] != TARGET:
    nonce += 1
    attempt = SECRET_KEY + str(nonce)
    m = md5()
    m.update(str.encode(attempt))
    hash_ = m.hexdigest()

print('Done!')
print('Answer: {}'.format(nonce))
